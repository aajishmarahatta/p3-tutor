"""The answer-key guard (tutor/.claude/hooks/keys_guard.py): it blocks the main conversation,
and any subagent that is not allowed, from reaching keys/, and it lets the allowed subagents
and every other read through. Each test runs the script as Claude Code does, with the tool call
as JSON on stdin, and checks the exit code (2 blocks, 0 allows). Nothing here calls Claude."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests import REPO

SCRIPT = REPO / "tutor" / ".claude" / "hooks" / "keys_guard.py"
SETTINGS = REPO / "tutor" / ".claude" / "settings.json"


class GuardTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = str(Path(cls.tmp.name).resolve())
        (Path(cls.root) / "keys").mkdir()
        (Path(cls.root) / "keys" / "0001.json").write_text("{}")
        (Path(cls.root) / "lessons").mkdir()

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def run_guard(self, tool, agent=None, raw=None, **args):
        data = {"tool_name": tool, "tool_input": args, "cwd": self.root}
        if agent:
            data["agent_type"] = agent
            data["agent_id"] = "a1"
        stdin = raw if raw is not None else json.dumps(data)
        return subprocess.run(
            [sys.executable, str(SCRIPT)], input=stdin, capture_output=True, text=True, timeout=30
        )

    def blocked(self, tool, agent=None, **args):
        done = self.run_guard(tool, agent, **args)
        self.assertEqual(done.returncode, 2, f"{tool} {args} should be blocked: {done.stderr}")
        self.assertIn("keys/", done.stderr)

    def allowed(self, tool, agent=None, **args):
        done = self.run_guard(tool, agent, **args)
        self.assertEqual(done.returncode, 0, f"{tool} {args} should be allowed: {done.stderr}")


class MainConversationBlocked(GuardTestCase):
    def test_read(self):
        self.blocked("Read", file_path="keys/0001.json")

    def test_read_path_variations(self):
        for path in (
            "./keys/0001.json",
            self.root + "/keys/0001.json",
            "keys\\0001.json",
            ".\\keys\\0001.json",
            "lessons/../keys/0001.json",
            "KEYS/0001.json",
            "Keys/0001.json",
            "/somewhere/else/keys/0001.json",
            "k*/0001.json",
            "ke?s/0001.json",
            "[k]eys/0001.json",
            "keys",
            "keys/",
        ):
            with self.subTest(path=path):
                self.blocked("Read", file_path=path)

    def test_read_through_a_symlink(self):
        link = Path(self.root) / "shortcut"
        if not link.exists():
            try:
                link.symlink_to(Path(self.root) / "keys")
            except OSError:
                self.skipTest("symlinks are not available here")
        self.blocked("Read", file_path="shortcut/0001.json")

    def test_grep(self):
        self.blocked("Grep", pattern="answer", path="keys")
        self.blocked("Grep", pattern="answer", path=self.root + "/keys")
        self.blocked("Grep", pattern="answer", glob="keys/*.json")
        self.blocked("Grep", pattern="answer", glob="**/keys/**")

    def test_grep_from_the_root_reaches_the_keys(self):
        self.blocked("Grep", pattern="answer")
        self.blocked("Grep", pattern="answer", path=".")
        self.blocked("Grep", pattern="answer", path=self.root)
        self.blocked("Grep", pattern="answer", path=str(Path(self.root).parent))

    def test_glob(self):
        self.blocked("Glob", pattern="keys/*.json")
        self.blocked("Glob", pattern="**/keys/*")
        self.blocked("Glob", pattern="*.json", path="keys")
        self.blocked("Glob", pattern="k*/*.json")
        self.blocked("Glob", pattern="./keys/**")

    def test_bash(self):
        for command in (
            "cat keys/0001.json",
            "cat ./keys/0001.json",
            "cat " + self.root + "/keys/0001.json",
            "head -n 5 KEYS/0001.json",
            "cd keys && cat 0001.json",
            "cat keys\\0001.json",
            "cat 'keys'/0001.json",
            'cat "ke""ys"/0001.json',
            "cat ke\\ys/0001.json",
            "cat k*/0001.json",
            "cat ke?s/*",
            "cat [k]eys/0001.json",
            "cat * ",
            "ls keys",
            "python3 -c \"print(open('keys/0001.json').read())\"",
            "cat $(ls keys/*)",
            "grep -r answer .",
            "grep -rn answer lessons keys",
            "rg answer",
            "find . -name '*.json' -exec cat {} +",
            "ls | xargs cat",
        ):
            with self.subTest(command=command):
                self.blocked("Bash", command=command)

    def test_powershell(self):
        for command in (
            "Get-Content keys\\0001.json",
            "Get-Content .\\keys\\0001.json",
            "gc keys/0001.json",
            "type keys\\0001.json",
            "Get-ChildItem -Recurse | Get-Content",
            "Select-String answer k*\\*.json",
            "Get-Content ('ke' + 'ys\\0001.json')".replace("'ke' + 'ys", "'keys"),
        ):
            with self.subTest(command=command):
                self.blocked("PowerShell", command=command)

    def test_a_subagent_that_is_not_allowed(self):
        for agent in ("lesson-writer", "lesson-planner", "lesson-reviewer", "someone-else"):
            with self.subTest(agent=agent):
                self.blocked("Read", agent, file_path="keys/0001.json")
                self.blocked("Bash", agent, command="cat keys/0001.json")


class AllowedReads(GuardTestCase):
    def test_the_authorized_subagents_read_keys(self):
        for agent in ("grader", "grade-reviewer", "quiz-reviewer"):
            with self.subTest(agent=agent):
                self.allowed("Read", agent, file_path="keys/0001.json")
                self.allowed("Read", agent, file_path=self.root + "/keys/0001.json")
                self.allowed("Grep", agent, pattern="answer", path="keys")
                self.allowed("Glob", agent, pattern="keys/*.json")

    def test_the_main_conversation_reads_everything_else(self):
        self.allowed("Read", file_path="quizzes/0001.json")
        self.allowed("Read", file_path="MISSION.md")
        self.allowed("Read", file_path="NOTES.md")
        self.allowed("Read", file_path="drafts/0002-key.json")
        self.allowed("Read", file_path="grades/0001-s1.json")
        self.allowed("Read", file_path="learning-records/0001-first-session.md")
        self.allowed("Read", file_path=self.root + "/submissions/s1.json")
        self.allowed("Read", file_path="monkeys/keystone.md")

    def test_searches_and_listings_that_do_not_reach_keys(self):
        self.allowed("Glob", pattern="lessons/*.html")
        self.allowed("Glob", pattern="quizzes/*.json")
        self.allowed("Glob", pattern="**/*.md")
        self.allowed("Grep", pattern="O3", path="learning-records")
        self.allowed("Grep", pattern="O3", path="lessons", glob="*.html")

    def test_shell_commands_that_do_not_reach_keys(self):
        for command in ("ls lessons", "ls -la", "cat NOTES.md", "cat quizzes/0001.json", "pwd", "wc -w lessons/*.html"):
            with self.subTest(command=command):
                self.allowed("Bash", command=command)
        self.allowed("PowerShell", command="Get-Content quizzes\\0001.json")
        self.allowed("PowerShell", command="Get-ChildItem lessons")


class FailsClosed(GuardTestCase):
    def test_input_it_cannot_read_blocks(self):
        for raw in ("", "not json", "[]", "null", '{"tool_name": "Read"}', '{"tool_input": {}}'):
            with self.subTest(raw=raw):
                done = self.run_guard("Read", raw=raw)
                self.assertEqual(done.returncode, 2, done.stderr)

    def test_a_read_with_no_path_blocks(self):
        self.blocked("Read")

    def test_a_shell_call_with_no_command_blocks(self):
        self.blocked("Bash")


class Registered(unittest.TestCase):
    def test_the_hook_is_registered_for_the_five_tools_and_fails_closed(self):
        settings = json.loads(SETTINGS.read_text())
        entries = settings["hooks"]["PreToolUse"]
        matcher = entries[0]["matcher"]
        for tool in ("Read", "Grep", "Glob", "Bash", "PowerShell"):
            self.assertIn(tool, matcher.split("|"))
        hook = entries[0]["hooks"][0]
        self.assertEqual(hook["type"], "command")
        self.assertEqual(hook["onFailure"], "block")
        self.assertIn("$CLAUDE_PROJECT_DIR/.claude/hooks/keys_guard.py", hook["command"])
        self.assertTrue(SCRIPT.is_file())

    def test_the_existing_permissions_are_kept(self):
        settings = json.loads(SETTINGS.read_text())
        self.assertIn("WebSearch", settings["permissions"]["allow"])
        self.assertIn("Agent(p3-guide)", settings["permissions"]["deny"])


if __name__ == "__main__":
    unittest.main()
