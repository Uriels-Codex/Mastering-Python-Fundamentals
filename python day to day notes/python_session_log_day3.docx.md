# Python Fundamentals — Session Log

*Updated: August 8, 2026 (Day 3\)*

# Goal & Context

Learning Python fundamentals as the first step toward a backend (Python/Flask/FastAPI) → cloud engineering path. Practicing in VS Code, pushing progress to public GitHub repo: Uriels-Codex/Mastering-Python-Fundamentals.

# Days 1 & 2 Summary (previously logged)

* Day 1: variables/data types, input/output, conditionals — all completed correctly, first GitHub push done  
* Day 2: loops (while and for), nested loops, FizzBuzz, pattern printing — completed cleanly; also debugged real git issues independently (.gitignore typo, commit \-m typo)

# Day 3 Summary (today) — Topic: Lists

## Loops Review

* Reviewed while (sentinel pattern) and for (list looping) after a skipped day — retention held up well  
* Added extra polish beyond the ask: empty-input handling and case-insensitive stop matching in a while loop review task  
* Caught and fixed a formatting bug independently (missing space in a nested-loop number pattern, end="" vs end=" ")

## Lists: Core Concepts

* Covered indexing (positive and negative), .append(), .remove(), len(), and membership checks with in  
* Asked and correctly reasoned through conceptual questions: lists as dynamic (vector-like) vs static arrays; index shifting after removal; difference between .remove() (by value) and .pop() (by position, LIFO/FIFO behavior)  
* Completed a full list-manipulation task (favorite shows list) correctly, including catching own bug: an unprinted bare expression (missing print() around an 'in' check) that produced no output — a REPL vs script execution distinction

## Lists: Sorting & Searching

* Identified and self-diagnosed a real bug: calling .sort() inside a for loop caused unstable/unexpected output due to mutating a list while iterating over it  
* Correctly reasoned through the root cause after explanation: loop position tracking breaks when the underlying list is reordered mid-iteration  
* Fixed independently by moving .sort() outside the loop, called once per sort operation  
* Explored built-in vs manual sorting (bubble sort) conceptually — correctly concluded that built-ins like .sort()/std::sort() are optimized, hidden-loop implementations, not fundamentally 'loop-free'  
* Understood that .sort() mutates a list permanently in place, and that later index-based or order-dependent operations must account for whatever the last sort left behind  
* Completed max(), min(), and membership check tasks correctly

## Lists: Filtering

* Correctly built a new filtered list (numbers \> 20\) from an original list using a for loop and .append() — no errors, first attempt

## Git: New Concepts

* Learned selective staging: git add \<specific-file\> instead of git add . — used correctly to avoid committing an accidental cross-day file mix-up  
* Learned and used git restore \<file\> to discard unwanted uncommitted changes (reverted an accidental edit in day2\_fundamentals.py before committing day3\_fundamentals.py separately)  
* Learned git restore \--staged \<file\> to unstage without discarding changes (concept covered, not needed in practice today)  
* Learned git log \--oneline to view commit history, and correctly interpreted HEAD \-\> main vs (origin/main) markers to understand the local/remote sync gap before and after pushing  
* Successfully committed and pushed Day 3 work in isolation, fully synced (verified via clean git status and matching HEAD/origin/main)

# Not Yet Covered

* Dictionaries (queued as Day 4 — key-value pairs, .items()/.keys()/.values(), common lookup-table patterns)  
* Functions, error handling (try/except), file I/O, modules, basic classes  
* Git branches and pull requests

# Instructor Notes (assessment)

* Self-awareness is strong: correctly recognized reduced focus today and chose a lighter task (git review/push) instead of pushing into a brand-new topic while tired — good long-term learning habit, not a setback  
* Debugging instinct continues to grow: identified the sort-while-iterating bug as 'weird' before being told what was wrong, and asked the right follow-up questions to understand the actual mechanism rather than just accepting the fix  
* Git comprehension has moved beyond copy-pasting commands: independently reasoned through selective staging and restore to solve a real, self-identified problem (wanting a clean Day 3-only commit)

Still working from guided task lists for new topics; the open-ended, no-bullet-steps milestone is not yet given — but git troubleshooting today was handled with minimal guidance, which is a positive independence signal in a different domain

# How to Resume Next Session

Upload or paste this file back at the start of the next session so progress carries over. Next topic: Dictionaries.