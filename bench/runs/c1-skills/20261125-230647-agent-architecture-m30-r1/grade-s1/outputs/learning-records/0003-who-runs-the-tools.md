# Misconception to work on: the model runs the tools itself (M4)

On quiz 0001 (submission s1), Riley chose the agent loop as the defining feature and the step limit as the safeguard, but believed the model opens the booking system itself and runs all three tools inside one call. Riley also assumed the model remembers its tool choices across sessions (M3).

**Evidence:** quiz 0001, submission s1, items q2 and q4 (M4), q6 (M3); q5 gave the result going back to the model without saying why.

**Implications:** Before context and memory, rework the loop trace so the program's actions and each separate model call are marked. Later memory lessons should show that nothing carries over between sessions unless the program saves it and puts it back in the input.
