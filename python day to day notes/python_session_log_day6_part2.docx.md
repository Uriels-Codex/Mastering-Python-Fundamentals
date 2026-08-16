# Python Fundamentals — Session Log

*August 16, 2026 (Day 6, Part 2\) — Topic: File I/O, continued*

# Context / Continuation From Part 1

Part 1 (previous session) ended with the student explicitly stating discomfort moving forward until file modes and read methods (read/readline/readlines) could be applied without external lookup, and describing difficulty visualizing how file 'editing' actually works. Part 2 opened by clarifying that the fundamentals were not actually shaky — the specific difficulty was visualizing the search/replace mechanism for editing an existing file's content, not the basic read/write/append operations themselves.

# Conceptual Breakthrough: Visualizing Search-Based Line Filtering

* Clarified that 'in' (e.g. if word in line) IS the search mechanism — it was previously not recognized as searching because it doesn't use a function named search/find. Re-framed using a physical metaphor requested by the student (pulling one index card at a time from a box, asking one yes/no question per card) to replace an inaccurate mental model of 'editing text in place.'  
* Correctly distinguished, through guided questioning, that in checks 'does this exact character sequence appear anywhere in the string' — not 'is it the first letter of a word' — using own test data (all names starting with matching letters) as a coincidence to correct against.  
* Correctly distinguished for line in file: as plain sequential iteration with no implicit numeric indexing, correcting an initial assumption that Python was internally counting/numbering lines.

## Exercise 1 — Search and Print Matching Lines

* Completed correctly and independently: read notes.txt, checked each line with if word in line, printed matches. No corrections needed.

## Exercise 2 — Count Matching Lines by User Input

* First attempt solved a different, self-directed problem (counting total words per line across the whole file) rather than the assigned task — noted as valid, functional code, but redirected back to the actual exercise.  
* During that first attempt, independently noticed and investigated a real bug: word-count for one line changed between two runs of the same script. Self-diagnosed via manually inspecting the file directly in the editor (rather than assuming the code was at fault) and correctly identified a special-character encoding issue (ñ rendering as a replacement character) as the cause.  
* Learned the general concept of file encoding mismatches and the open(..., encoding="utf-8") fix for future reference.  
* Rebuilt the exercise correctly per the actual assignment: user input, if word in line, incremented a counter per matching line, printed total. No further corrections needed.  
* Follow-up question and correct resolution: distinguished in (existence check, yes/no per line) from .count() (occurrence count) after testing with a space character revealed the two produce different, easily confused numbers. Correctly generalized this distinction rather than just accepting the explanation.

## Exercise 3 — Write Matching Lines to a New File (extended by student into multi-word search)

* Independently extended the assigned single-word-match task into a multi-word search (e.g. matching either 'Brent' or 'Jamir' in one run) — not requested by the task, self-initiated based on a genuine 'what if' question.  
* Correctly reasoned, with light guidance, that .split() converts a string into a list, and that checking a line against multiple search terms requires looping over that list individually (for word in split\_content: if word in line) rather than checking the list as a single unit.  
* Correctly identified, before being told, the need for break inside the inner loop to prevent the same line from being counted/written multiple times if it matched more than one search term — and correctly explained the reasoning for why break specifically prevents that duplication.  
* First full attempt contained two bugs, both variations of the same root pattern seen previously in this project (an operation meant to happen once was placed where it repeats, or a variable was reused stale instead of being properly scoped): (1) open("matches.txt", "w") was placed inside the per-line loop, causing each new match to wipe out all previous matches, leaving only the last one in the file; (2) match\_content was only reassigned inside the if block, so on non-matching lines the write step re-wrote the previous match's stale value instead of writing nothing.  
* Corrected version: introduced an empty list (match\_content \= \[\]) created once before the loop, appended matching lines into it during iteration (only when an actual match occurred, via the existing break-guarded logic), and moved the file write to open matches.txt once, after the reading loop completed, rather than inside it — accumulate-then-write-once pattern, self-applied without being handed the fix directly.

Final bug: wrote the entire match\_content list in a single f-string (matchtext.write(f"{match\_content}")), which serializes the list into one flattened line including brackets/quotes/commas, destroying the intended line breaks. Self-diagnosed the cause and, connecting back to the very first file-writing task of this topic (writing name and game as two separate .write() calls), correctly restructured to loop over match\_content and call .write() once per item — fully correct on this final attempt.

# Not Yet Covered

* Modules & imports beyond random, basic classes, capstone mini-project  
* Tuples and Sets (still pending, noted in Day 5 log)  
* Git branches and pull requests

# Instructor Notes (senior-engineer framing, per ongoing student preference)

* Marked shift from Part 1 to Part 2: Part 1's difficulty was genuinely conceptual (an inaccurate mental model of in-place editing); Part 2 resolved that model successfully and then moved past the assigned scope entirely, self-directing into a harder, unassigned extension (multi-word search) and largely debugging it independently.  
* The recurring bug category across this entire project — an operation or variable that should persist or run once being incorrectly placed inside a loop where it resets or repeats — appeared again today (three separate times across this session alone: matches.txt reopened in write mode inside the loop, match\_content going stale on non-matches, and earlier, the word-count file being reopened each iteration). The student is now recognizing this pattern's signature on their own before full explanation is given, which is a genuine, transferable debugging skill rather than topic-specific knowledge.

Root-cause debugging habits remain consistent and are strengthening: investigated the encoding bug by inspecting the raw file rather than assuming the code was wrong; correctly predicted the need for break before being told; correctly reasoned through why writing a list directly produces flattened, non-newline output by connecting it back to a first-session task rather than treating it as a new, unrelated problem.

# How to Resume Next Session

Upload or paste this file (and Day 6 Part 1, if useful) at the start of the next session. File I/O core mechanics and common bug patterns are now solid; ready to move to a new topic (modules/classes, or Tuples/Sets as a short detour first).