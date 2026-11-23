# Quiz 0001, second attempt: the loop is solid, three gaps remain

On the spaced retake, Riley correctly identified what makes an agent, what the model outputs when it calls a tool (a request, not the tool's code), and that a tool result goes back as the next input so the model can decide what to do.
Still open: M4 (the model runs the tools itself; Riley's q4 reasoning said so, though the count was right), M6 (a stuck agent will eventually succeed, so no stop rule is needed; regressed from the first attempt), and tool choice resting on the name alone instead of the full description.

**Evidence:** quiz 0001, submission s2 (compared with s1): q2 improved to correct, q3 regressed to wrong, q4 right count with wrong reason, q6 partial.

**Implications:** Revisit that the program runs tools and every step is a separate model call, and why loops need a stopping condition, before building on them. Tool descriptions are the natural bridge to the mission goal of writing a clear tool description.
