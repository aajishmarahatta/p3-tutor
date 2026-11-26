#!/usr/bin/env python3
"""PreToolUse guard: keeps the answer keys in keys/ away from the tutor's main conversation.

Claude Code runs this before every Read, Grep, Glob, Bash and PowerShell call (see
.claude/settings.json), with the call as JSON on stdin. Exit 2 blocks the call and the model
sees the message written to stderr; exit 0 lets it go ahead. Inside a subagent the input carries
agent_type, the subagent's name; in the main conversation it does not.

Who may read the keys, and why (each one is one more place a key could leak from):
  grader          grades a submission against its key; it cannot do the job without it.
  grade-reviewer  regrades the draft grades from the quiz, key and submission, to find a wrong
                  verdict or misconception id.
  quiz-reviewer   solves the draft quiz blind, then checks its key and the misconception ids
                  against the keys of earlier quizzes.
Every other subagent (the lesson planner, writer and reviewer) and the main conversation are
blocked. The quiz and grade skills never need a key themselves: they hand that work to the
subagents above, and /quiz writes its key once, from a draft in drafts/.

What it does not stop (accepted gaps): a name built from pieces at run time (for example a
shell variable or Python string concatenation that spells the folder), a command that copies
the key before reading it from an allowed place, and a Glob that lists key file names without
reading them. In the bench the shell is not allowed at all, so these matter in live sessions.

Every unreadable or unexpected input blocks, on purpose: a broken guard must not look like no guard.
"""

import fnmatch
import json
import os
import re
import sys

ALLOWED_AGENTS = {"grader", "grade-reviewer", "quiz-reviewer"}
FOLDER = "keys"
GLOB_CHARS = "*?["

MESSAGE = (
    "Blocked: the answer keys in keys/ are not available to the main conversation. "
    "Quiz items are in quizzes/. Grading and key checks are done by the grader subagent "
    "(the grade skill starts it), and the quiz skill writes its key once from a draft in drafts/."
)


def block(reason=""):
    sys.stderr.write(MESSAGE + (" (" + reason + ")" if reason else "") + "\n")
    sys.exit(2)


def parts_of(path):
    """The components of a path, with Windows separators, quotes and ./ and ../ resolved."""
    text = path.strip().strip("\"'`").replace("\\", "/")
    return [p for p in os.path.normpath(text).split("/") if p not in ("", ".")]


def is_glob(part):
    return any(c in part for c in GLOB_CHARS)


def could_be_folder(part, strict):
    """True when a path component is the keys folder, or a glob that can match it."""
    low = part.lower()
    if low == FOLDER:
        return True
    if is_glob(low) and fnmatch.fnmatchcase(FOLDER, low):
        # a bare * or ** lists every folder; only a strict check (a file read, a shell command)
        # treats it as reaching keys, a pattern with a letter in it always does
        return strict or bool(re.search(r"[a-z]", low))
    return False


def inside_keys(path, root, strict):
    """True when the path is in keys/, by its components or after resolving it from the root."""
    if any(could_be_folder(p, strict) for p in parts_of(path)):
        return True
    text = path.strip().strip("\"'`").replace("\\", "/")
    target = os.path.realpath(os.path.join(root, text)).lower()
    keys = os.path.realpath(os.path.join(root, FOLDER)).lower()
    return target == keys or target.startswith(keys + os.sep)


def covers_keys(path, root):
    """True when a recursive search from this path would reach keys/ (the root or above)."""
    text = (path or ".").strip().strip("\"'`").replace("\\", "/")
    target = os.path.realpath(os.path.join(root, text)).lower()
    keys = os.path.realpath(os.path.join(root, FOLDER)).lower()
    return target == keys or keys.startswith(target.rstrip(os.sep) + os.sep)


RECURSIVE = [
    r"\b(rg|ag|ack|findstr)\b",
    r"\b(grep|egrep|fgrep|zgrep)\b[^;&|]*\s(-[a-z]*r[a-z]*|--recursive|--include|-d\s*recurse)\b",
    r"\bfind\b[^;&|]*(-exec|-execdir|-ok|-print0)",
    r"\bxargs\b",
    r"-recurse\b",
]


def shell_blocked(command, root):
    original = command.replace("\r", "\n")
    # drop quoting and escapes that split a name, such as ke""ys or k\eys
    flat = re.sub(r"[\"'`^]", "", original)
    for text in (flat, flat.replace("\\", "/"), re.sub(r"[\\]", "", flat)):
        if re.search(r"(?<![A-Za-z0-9_])keys(?![A-Za-z_])", text, re.I):
            return "the command names keys/"
    for token in re.split(r"[\s/;|&<>(),=:]+", flat.replace("\\", "/")):
        if token and is_glob(token) and fnmatch.fnmatchcase(FOLDER, token.lower()):
            return "a wildcard in the command can match keys/"
    for pattern in RECURSIVE:
        if re.search(pattern, flat, re.I):
            return "a recursive search or xargs can reach keys/"
    return ""


def decide(data):
    if data.get("agent_type") in ALLOWED_AGENTS:
        return ""
    tool = data.get("tool_name")
    args = data.get("tool_input")
    if not isinstance(tool, str) or not isinstance(args, dict):
        return "unreadable tool call"
    root = os.path.realpath(data.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())

    def text(key):
        value = args.get(key)
        return value if isinstance(value, str) else ""

    if tool == "Read":
        path = text("file_path") or text("path")
        if not path or inside_keys(path, root, strict=True):
            return "reads keys/ or names no file"
    elif tool == "Glob":
        for value in (text("pattern"), text("path")):
            if value and inside_keys(value, root, strict=False):
                return "lists keys/"
    elif tool == "Grep":
        path = text("path")
        if inside_keys(path, root, strict=True) if path else False:
            return "searches keys/"
        if covers_keys(path, root):
            return "a search from the workspace root reaches keys/: name a folder such as lessons/"
        for value in (text("glob"), text("pattern")):
            if value and any(could_be_folder(p, False) for p in parts_of(value)):
                return "the glob or pattern names keys/"
    elif tool in ("Bash", "PowerShell"):
        command = text("command")
        if not command:
            return "no command"
        reason = shell_blocked(command, root)
        if reason:
            return reason
    return ""


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        block("the hook input could not be read")
    if not isinstance(data, dict):
        block("the hook input is not an object")
    reason = decide(data)
    if reason:
        block(reason)
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as error:  # decide on purpose: an unexpected failure blocks
        block("guard error: " + type(error).__name__)
