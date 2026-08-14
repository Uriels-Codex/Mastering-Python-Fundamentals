# Python Fundamentals — Session Log

*Updated: August 14, 2026 (Day 5\)*

# Goal & Context

Learning Python fundamentals toward a backend (Python/Flask/FastAPI) → cloud engineering path. Session began after 2 skipped days and low motivation; student explicitly requested going forward to be evaluated with senior-engineer-level directness rather than encouragement-first framing.

# Days 1–4 Summary (previously logged)

* Day 1: variables/data types, input/output, conditionals — completed correctly, first GitHub push done  
* Day 2: loops (while/for), nested loops, FizzBuzz — completed cleanly, debugged real git issues independently  
* Day 3: Lists — indexing, .append()/.remove()/.pop(), sorting, filtering, off-by-one index math; learned selective git staging, git restore, git log \--oneline  
* Day 4: Dictionaries (core ops, .items() looping, self-diagnosed loop-reset bug) and Functions (return values, multi-value returns, default arguments, \*args, self-caught dead-code bug)

# Day 5 Summary (today) — Topic: Error Handling (try/except)

## Core Mechanics

* Covered try/except structure, specific error types (ValueError, ZeroDivisionError, IndexError, KeyError, TypeError, FileNotFoundError, and others) vs. bare except/Exception, and why catching specific types is preferred in real code  
* Correctly diagnosed own conceptual error: testing num / 100 instead of 100 / num and expecting ZeroDivisionError — correctly self-corrected upon realizing denominator position determines the error, not the presence of a variable  
* Asked and correctly resolved a genuine question about control flow: whether a nested try inside an except block is actually reachable after the outer exception fires (confirmed: yes, except does not halt the program, only redirects flow within that block)  
* Correctly reasoned through what pass does and when to use it vs. print() inside except — landed on the right heuristic independently (print when the user needs to act on the failure, pass when it's an expected, non-actionable outcome)

## Type Conversion & Fallback Chains

* Identified real bugs in an initial dictionary-builder attempt: type(val) \== int check on input() values (always False, since input() always returns strings) and a misplaced try/except that wrapped input() instead of the actual risky conversion line  
* Learned and implemented a nested try/except fallback chain (attempt int(), fall back to float(), otherwise leave as string) after initial version was corrected by request rather than self-built  
* Independently proposed and helped design a cleaner alternative: looping over a list of candidate conversion functions (for convert in \[int, float\]) instead of manually nesting try blocks, recognizing this scales better if more types were added later  
* Correctly reasoned why tuple() and range() would not work as drop-in additions to that conversion list (tuple() splits strings character-by-character rather than converting; range() raises TypeError, not ValueError, and requires a numeric argument) — chose to defer studying those separately rather than force-fit them

## Applied Practice: Inventory Builder Task

* First attempt contained four issues: missing dictionary initialization, incorrect conversion order (\[float, int\] instead of \[int, float\]) causing whole numbers to be stored as floats, missing break causing double-conversion after success, and a stale-variable bug printing type(item\_stocks) instead of the current loop's quantity  
* Intentionally re-introduced the \[float, int\] ordering bug on a later attempt specifically to test and confirm understanding of why float() silently accepts whole-number strings, correctly explaining the float/int permissiveness relationship afterward  
* Self-diagnosed a separate, subtler bug in a related dictionary-printing loop: a print statement referencing leftover variables from an entirely different, earlier for loop, rather than the current loop's unpacked variables — correctly identified and explained the 'stale variable' mechanism unprompted before it was explained  
* Final inventory-builder version, combining int/float fallback ordering with correct break placement and correct type() usage, was fully correct

## Retry-Loop Challenge (Closing Task)

* First solution used three separate, duplicated while/try/except blocks (one per entry) — functionally correct, correctly isolated retry logic per-entry, but repetitive  
* After a conceptual nudge (not a handed solution), independently restructured into a single nested loop: an outer for loop controlling which entry is being collected, wrapping an inner while True/try/except handling retry-until-valid for that specific entry, accumulating results into a list created before the outer loop — fully correct on first restructured attempt

# Git

* Committed and pushed today's error-handling work: commit message "Day 5: error handling \- try/except, specific error types, nested fallback chains, retry loops"

# Career Planning Discussion (this session)

Clarified realistic sequencing: near-term goal is a backend/software dev internship in 3rd–4th year of college; cloud engineering reframed as the follow-up role after initial dev experience, not a direct entry point. Discussed local (PH) vs. remote/foreign job market differences for Python specifically (smaller local pool, higher pay premium; stronger fit for remote/AI-adjacent work). Also discussed and deferred LeetCode/NeetCode until after fundamentals are complete, and browsing project-based GitHub repos (e.g. 30-days-of-python) as a low-effort reference/checklist activity, not a replacement for current pacing.

# Not Yet Covered

* File I/O (next planned topic — moderate scope, estimated 3-5 tasks, naturally reinforces try/except in a new context such as FileNotFoundError)  
* Tuples and Sets (identified via reference repo comparison as small, quick topics not yet covered; candidate for a short future session)  
* Modules, basic classes, capstone mini-project  
* Git branches and pull requests

# Instructor Notes (assessment, senior-engineer framing per student request)

* Strengths: root-cause debugging rather than symptom-patching (stale-variable bug, dead-code bug in prior sessions); tests hypotheses directly against running code rather than accepting explanations on authority (deliberately reintroduced the float/int ordering bug to verify understanding); asks precise, falsifiable questions rather than vague ones; independently proposed a structurally better solution (list-of-converters loop) rather than only accepting the given nested-try pattern  
* Real gaps: has not yet worked without a pre-defined task spec — problem definition, not just problem-solving, is untested; error handling instinct is currently reactive to flagged risks rather than proactively anticipated before writing risky code; no exposure yet to reading or modifying pre-existing/unfamiliar code, or to ambiguous, non-technical requirements; naming/structure consistency across functions is still uneven (noted in Day 4 log, unresolved)  
* Overall calibration given directly to student this session: foundation-layer fundamentals (syntax, control flow, debugging instinct) are progressing solidly and are not the limiting factor; the larger, expected gaps are framework/backend-specific skills and professional/team-context skills, neither of which have been attempted yet — this is normal sequencing at this stage, not evidence of being behind

Student explicitly requested consistently direct, senior-engineer-style evaluation going forward rather than encouragement-first framing; this preference should be maintained in future sessions and logs

# How to Resume Next Session

Upload or paste this file back at the start of the next session. Next topic: File I/O.