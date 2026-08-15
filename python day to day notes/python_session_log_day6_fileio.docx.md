# Python Fundamentals — Session Log

*Updated: August 15, 2026 (Day 6\) — Topic: File I/O*

# Goal & Context

Learning Python fundamentals toward a backend (Python/Flask/FastAPI) → cloud engineering path. Student explicitly requested not to move to the next topic until File I/O concepts (especially file modes and read methods) are understood well enough to apply without external notes or lookup. This session ended without full confidence reached — planned to continue File I/O next session before moving forward.

# REFERENCE SHEET — File I/O Core Concepts

*This section is meant to be reviewed and memorized before continuing. Distinguishing these correctly was the main source of bugs this session.*

## File Modes (the second argument to open())

* "w" (write) — creates the file if it doesn't exist. If it DOES exist, immediately erases all existing content before writing. Use when you want to start completely fresh.  
* "a" (append) — creates the file if it doesn't exist. If it exists, adds new content to the END, without touching what's already there. Use when adding new entries without losing old ones.  
* "r" (read) — opens an EXISTING file to read from. Does not create or modify anything. Raises FileNotFoundError if the file doesn't exist yet.  
* Mode must always be a quoted string: "w", "a", "r" — NOT bare letters w, a, r (bare letters are read as undefined variable names and cause a NameError).

## Reading Methods — the part that caused today's core confusion

* file.read() — reads the ENTIRE file as ONE single string (no line separation). Good for "just show me everything at once," bad when you need to process entries individually.  
* file.readline() — SINGULAR. Reads ONLY THE FIRST LINE of the file, returned as one string. Easy to confuse with readlines() — this was today's actual bug.  
* file.readlines() — PLURAL. Reads the ENTIRE file and returns a LIST, where each element is one line. This is what's needed whenever you want to loop through, filter, or process individual entries/lines.  
* for line in file: (looping directly over the file object) — an alternative to readlines(); iterates one line at a time without loading a full list into memory first. Used in this session for the verification/print-back step.  
* MEMORY AID: readline (no s) \= one line. readlines (with s) \= list of all lines. The 's' is the entire difference and is easy to miss visually — double-check this specifically when writing file code.

## Why .replace() Is the Wrong Tool for Removing an Entry/Record

* contents.replace(name, "") deletes ONLY the matched text itself, wherever it appears in the whole string — it has no concept of "lines" or "records." It will leave the rest of that line intact but broken (e.g. "Name: , favorite game: Dota2"), and can also accidentally match the same text if it appears elsewhere in the file, unrelated to the intended entry.  
* Correct approach for removing a whole entry: read the file as a LIST of lines (readlines()), loop through and KEEP only lines that do NOT contain the target (if name not in line), then write the surviving lines back with "w" mode — this is a filtering pattern, structurally identical to the Day 3 "build a new list with only numbers \> 20" exercise, just applied to lines of text instead of numbers.

## The General File-Editing Pattern (files cannot be edited in place)

* This is a fundamental limitation of files at the operating-system level, not specific to Python. There is no way to directly "find and change" content inside an existing file without rewriting it.  
* The real pattern, used in every language: (1) READ the entire current contents into memory (usually as a list of lines), (2) MODIFY that in-memory version as needed (add/remove/change), (3) WRITE the full updated version back using "w" mode, which overwrites the old file completely with the corrected version.

This limitation is also the concrete, practical reason real applications move to databases once data needs frequent, precise updates — databases solve the "find and update just one record" problem properly; plain text files cannot do this efficiently at scale. Directly relevant to the later roadmap step of learning PostgreSQL.

## with open(...) as f: vs. manual open()/close()

* with open(...) as f: automatically closes the file when the indented block ends — even if an error occurs partway through. This is the standard, recommended approach in real code.  
* Manual f \= open(...) / f.close() requires the developer to remember to call .close() themselves; forgetting it, or an error occurring before the manual close() line, can leave the file improperly closed (unsaved data, file left locked). with removes this risk entirely.

open() is a built-in function — no import statement is required to use it, unlike modules such as random.

# File Location Behavior

open("filename.txt", ...) with no path looks in the current working directory — the same folder the .py script is being run from — NOT the whole computer. To reference a file elsewhere, a full or relative path must be given explicitly.

# Session Walkthrough — Bugs Encountered & Resolved

## Task 1 — Basic Write/Read

* Correctly wrote name and favorite game to profile.txt using "w" mode, then read it back with "r" mode wrapped in try/except for FileNotFoundError. Minor syntax slip along the way (mode written as bare r instead of "r"; wrong exception name FileExistsError instead of FileNotFoundError) — both self-corrected quickly once flagged.

## Task 2 — Append Mode \+ Line-by-Line Reading

* Correctly switched to "a" mode to add new entries without erasing existing ones. Initial version omitted new input() calls (relied on stale variables from a prior code block) — caught and fixed by request. Correctly diagnosed (with guidance) why looping with print(line) produced doubled blank lines: each line already contains its own trailing newline character, and print() adds another on top of it. Chose line.strip() over end="" as the fix — a valid, commonly used alternative; both approaches and their difference (strip modifies the string's whitespace entirely, end="" only suppresses print()'s own newline) were discussed.

## Task 3 — Read, Modify, Write Back (Removing an Entry)

* First attempt used contents.replace(remove\_name, "") on the full file text — this was identified as fundamentally the wrong approach, not just a minor bug: it deletes only the matched name text, leaving a broken remnant of the line behind, and does not remove the record as a whole. Root cause and mechanism were walked through in detail on request before moving to a fix.

Second attempt correctly restructured to a read-filter-write pattern, but used file.readline() (singular) instead of file.readlines() (plural) — this caused lines to hold only the first line of the file as a single string, meaning the subsequent for line in lines: loop iterated character-by-character instead of line-by-line. Root cause explained in detail; corrected on the next attempt to file.readlines(), producing a fully correct final version: read all lines, filter out lines containing the target name, write the remainder back, then verify by reading again.

# Student's Stated Concern (end of session)

Explicitly stated discomfort moving to a new topic until able to distinguish and apply file modes and reading methods (read/readline/readlines, w/a/r) without needing to look up notes or tips externally. This is a reasonable, well-founded checkpoint given that the core bugs this session were specifically confusions between similarly-named methods (readline vs. readlines) and mode letters, not deeper logic errors — the surrounding logic (try/except usage, filtering pattern, write-back pattern) was consistently correct throughout.

# Not Yet Covered

* Solidify File I/O distinctions above to the point of independent recall (planned for next session, before moving forward)  
* Modules & imports beyond random, basic classes, capstone mini-project  
* Tuples and Sets (still pending from Day 5 notes)  
* Git branches and pull requests

# Instructor Notes (senior-engineer framing, per ongoing student preference)

* The pattern of bugs this session differs meaningfully from prior sessions: earlier bugs (loop-reset, stale variables, dead-code returns) were logic/reasoning errors, generally understood quickly once traced through. Today's bugs (readline vs. readlines, bare mode letters, wrong exception name) were closer to naming/recall friction — knowing the concept but reaching for the wrong specific tool. This is a normal and expected stage when a topic introduces several similarly-shaped, easily confused built-ins at once, not a sign of weaker reasoning ability.  
* The correct instinct to slow down and consolidate before moving forward, rather than pushing ahead on shaky recall, is itself a good engineering habit — going into File I/O usage in a real project (e.g. config loading, log files) with an unclear read()/readline()/readlines() distinction would produce exactly this class of subtle, hard-to-spot bug in practice.

Underlying structural skills (try/except placement, filtering patterns, write-back logic, using error messages to self-diagnose) remained consistently solid throughout this session even while the specific method names were shaky — this distinction is worth the student keeping in mind: the reasoning is not the weak point, the vocabulary/recall is.

# How to Resume Next Session

Upload or paste this file back at the start of the next session. Plan: brief self-quiz against the Reference Sheet above (recall file modes and read/readline/readlines from memory before checking), then a few more small File I/O tasks reusing these specifically to build fluency, before moving to the next new topic.