# Python Fundamentals — Session Log

*Session Date: August 6, 2026*

# Goal & Context

Learning Python fundamentals as the first step toward a backend (Python/Flask/FastAPI) → cloud engineering path. Working through tasks live, in real time, rather than a fixed day-by-day schedule. Practicing in VS Code, with plans to push progress to a public GitHub repo.

# Environment Setup Completed

* Python 3.14.6 installed and verified  
* VS Code installed, Python extension added  
* Practice folder created: "UrieL-- pyhthon" on Desktop  
* Learned to use the built-in Terminal (not the Output panel) for input()-based programs  
* Enabled "Code-runner: Run In Terminal" setting so Run button behaves like Java/C++ IDEs  
* Decided against PyCharm long-term in favor of VS Code (lighter, multi-purpose for future Docker/Terraform/YAML work)

# Tasks Completed

## Task 1: Variables & Data Types

* Created string, int, float, and boolean variables (name, age, height, is\_student)  
* Printed variables individually and combined into a sentence using an f-string  
* Learned multi-line f-strings: triple quotes vs. adjacent string literals inside parentheses vs. backslash continuation  
* Note: used camelCase (isStudent) instead of Python convention snake\_case (is\_student) — flagged as a style habit to unlearn from JS/Java  
* Result: correct on first real attempt

## Task 2: Input/Output

* Used input() to collect name and age  
* Correctly type-cast age input to int() (with a self-written comment explaining why)  
* Fixed on first correction: printed age \+ 10 instead of current age

## Task 3: Conditionals (if / elif / else)

* Built an even/odd checker using modulo (%) — correct on first try  
* Built a grade calculator (A–F) using chained if/elif/else with correct descending order of comparisons  
* Used float() input and round() — asked a sharp question about rounding behavior  
* Learned Python's round() uses "round half to even" (banker's rounding), not "round half up"  
* Fixed two small bugs independently after they were flagged (D branch printing "A", F branch printing "E")

# Not Yet Covered

* Loops (for, while) — multiplication table \+ running sum with while loop (next task queued)  
* Lists, dictionaries, functions, error handling, file I/O, modules, basic classes

Git/GitHub push — account creation discussed, not yet executed

# Instructor Notes (assessment)

* Genuinely engaging with "why," not just copying code (asked about rounding behavior, camelCase vs snake\_case, range() as function vs. plain-English "range")  
* Good habits forming: writing explanatory comments, saving old code instead of deleting, fixing bugs correctly after being told (not just told the answer)  
* Currently working from guided step-by-step checklists for each task  
* Next milestone: an open-ended task with no bullet steps, to test whether structure/logic is retained independently — timing left to instructor's judgment based on progress

# How to Resume Next Session

Upload or paste this file back at the start of the next session so progress carries over, since this isn't stored automatically.