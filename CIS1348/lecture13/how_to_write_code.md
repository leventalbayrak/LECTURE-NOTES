
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

# How to Write Code

## Table of Contents

### Part I: Mindset
- [The Right Attitude](#the-right-attitude)
  - [1. Understand the Problem](#1-understand-the-problem)
  - [2. Solve the Problem You Have, Not a Hypothetical One](#2-solve-the-problem-you-have-not-a-hypothetical-one)
  - [3. Always Check Your Work](#3-always-check-your-work)
  - [4. The Platform Is Part of the Problem](#4-the-platform-is-part-of-the-problem)
- [Programming with Common Sense: Practical Rules](#programming-with-common-sense-practical-rules)
  - [1. Only build what was asked.](#1-only-build-what-was-asked)
  - [2. Do not handle scenarios that cannot happen.](#2-do-not-handle-scenarios-that-cannot-happen)
  - [3. Do not abstract prematurely.](#3-do-not-abstract-prematurely)
  - [4. Implement first, then observe.](#4-implement-first-then-observe)
  - [5. Crash loudly rather than fail silently.](#5-crash-loudly-rather-than-fail-silently)
### Part II: Development Process
1. [How to Approach a Program](#1-how-to-approach-a-program)
2. [Comments: Only Write What Earns Its Place](#2-comments-only-write-what-earns-its-place)
3. [Why You Verify Every Step](#3-why-you-verify-every-step)
4. [How to Verify Correctness by Random Sampling](#4-how-to-verify-correctness-by-random-sampling)

### Part III: Coding Patterns
1. [Lookup Tables vs. Appending](#1-lookup-tables-vs-appending)
2. [Separate File I/O from Logic](#2-separate-file-io-from-logic)
3. [Command-Line Arguments](#3-command-line-arguments)
4. [Parsing: Choose the Right Delimiter](#4-parsing-choose-the-right-delimiter)
5. [Counting with Dictionaries](#5-counting-with-dictionaries)
6. [Sorting a List of Tuples](#6-sorting-a-list-of-tuples)

### Part IV: Code Walkthroughs
1. [Code Walkthrough: Project 1 Solution](#1-code-walkthrough-project-1-solution)
2. [Code Walkthrough: Exam 1 Solution](#2-code-walkthrough-exam-1-solution)

---

## Part I: Mindset

---

## The Right Attitude

Understand the problem fully, solve exactly that problem, and do it correctly.

---

## 1. Understand the Problem

Before you write a single line of code — before you think about data structures, algorithms, or approach — understand the problem you are being asked to solve.

Read the spec. Read it again. What exactly is being asked? What are the inputs and outputs? What are the boundaries — what data is valid, what isn't? What are the constraints: size, format, performance? What is explicitly out of scope?

These are not optional questions. If you cannot answer them, do not start coding. Every line written on a misunderstood problem is waste — and waste that compounds the longer you keep going. An hour spent clarifying requirements costs less than a day spent building the wrong thing.

You do not need to know every detail before starting. You need to understand the actual problem well enough to recognize when you are solving the right one.

---

## 2. Solve the Problem You Have, Not a Hypothetical One

One of the most common mistakes new programmers make is solving a problem that was never asked. You are given a specification. That specification defines the problem. Your job is to write code that solves that specific problem — not a more general version of it, not a future version of it, not a version that handles scenarios nobody mentioned.

When you add flexibility and generality beyond what was asked, you are not being a better programmer — you are creating work for yourself. Every extra line has to be written, debugged, read, and maintained. Code that accommodates hypothetical futures is pure cost with no current benefit. The spec is the boundary. Stay inside it.

For example: suppose the spec says there are always 100 files in a directory, and that number is fixed and will never change. A misguided instinct is to write code that automatically scans the directory and counts the files rather than simply using 100. That is a different problem — one nobody asked you to solve. Do not invent problems for yourself.

If the requirements change later — say, now you need to handle a variable number of files — then *that* becomes the problem, and you solve it then.

Write the simplest correct solution. Complexity is a cost you pay — only pay it when you must.
When you feel the urge to make something more general or flexible than what was asked, that is the signal to stop — not to build.

---

## 3. Always Check Your Work

Never assume your code is correct. Always verify. No matter how experienced you are, check every step.

- **Never assume** something works because it looks right. Check it.
- **Read the error message.** The moment you get an error, it tells you exactly what went wrong. Don't ignore it and keep typing.

---

## 4. The Platform Is Part of the Problem

The problem you are solving is not just the algorithm or the logic — it includes the environment in which your code will run. Platform is part of the problem definition.

If your code is written to run on a server and the requirement changes to run on a mobile phone, that is not a minor adjustment — that is a different problem. Memory limits, processing power, available libraries, operating system behavior — all of these are constraints defined by the platform. When the platform changes, the constraints change, and your solution must change with them.

This matters for how you scope your work. Do not write code for a platform you do not have. Write for the actual target. If the target changes later, revisit and revise — but do not try to anticipate every possible environment in advance. That is speculative work with no current benefit.

---

## Programming with Common Sense: Practical Rules

The principles below apply whenever you have the freedom to design and make decisions. When working under a lead or following project rules that conflict with these, defer to those rules — those represent the real constraints you are operating under.

### 1. Only build what was asked.

Do not invent flexibility, configurability, or generality that nobody requested. Complexity is a cost — only pay it when you must. When the spec defines the bounds of the problem, write code for those bounds. A right-click menu realistically holds 5–20 items — there is no need to add functionality for 50 million items, or to introduce a complex sort or data structure just in case it "becomes 10,000 items someday." Every line that wasn't asked for adds complexity, bloat, and dependencies — all of which must be read, understood, and maintained by everyone who touches the code after you. You also end up maintaining code paths that are never visited and never tested by real-world usage.

### 2. Do not handle scenarios that cannot happen.

When you write a program, you know things about it that an outsider does not — certain values are always in a valid range, certain functions are only called in a specific order, certain data always has a specific format because your own code produced it. Do not add defensive checks for cases your own design makes impossible. Error handling and validation belong at system boundaries: user input, external files, network calls. Inside your own logic, trust your own design. If your code uses an internal constant, there is no need to guard against someone passing a different value — that situation cannot arise by construction. Similarly, when parsing a log or any structured input, you do not need to accommodate every possible malformed line — unless the spec explicitly requires it. If you encounter a format you did not expect, stop and throw an error. That is a cleaner, more appropriate response than silently misreading data.

### 3. Do not abstract prematurely.

Only introduce a helper, a class, or a shared function when you have a concrete, proven reason that it simplifies things. Three similar lines of code are better than an abstraction invented to handle a case that may never come.

### 4. Implement first, then observe.

Do not spend time designing the "right" structure before you have written anything. You cannot know what the right structure is until you have real, working code in front of you. The instinct to design everything up front leads to over-engineering: you end up building abstractions for complexity that never materializes. Instead, write the simplest, most direct version that does the job. Run it. Then look at what you actually have — not what you imagined — and decide what, if anything, genuinely needs to change.

### 5. Crash loudly rather than fail silently.

When something is wrong — unexpected input, a format you did not anticipate, a value that should not exist — it is perfectly fine for your program to stop immediately and throw an error. You do not need to gracefully recover from every situation. In fact, a program that crashes with a clear error is more honest and more debuggable than one that quietly mishandles bad data and produces wrong results with no warning. Trying to accommodate every possible scenario often produces fragile, bloated code that fails in subtle ways. Refusing to run when something is not right is not a weakness — it is a design decision.

These are not restrictions — they are the natural result of solving the problem in front of you instead of a hypothetical one. The simplest correct solution is always the goal.

---

## Part II: Development Process

---

## 1. How to Approach a Program

Before you start coding, get a rough idea of the tasks involved. You do not need to know every step in advance. You need a general direction — enough to start. As you complete each small task, you will understand the problem better, and you can adjust your plan as you go.

Start by identifying the tasks you can think of. Write these tasks down as comments in your file. They become your working roadmap — not a rigid contract, but a guideline that you revise as you learn more.

Before writing any code, you should also be able to figure out how to solve the problem manually. Browse the files, click through the data, dump things into Excel if you have to. If you cannot solve the problem by hand, you cannot code it. This manual exploration builds understanding of the data and the problem structure that no amount of code can replace.

Write code correctly, one small step at a time, rather than writing a lot of code and then hunting for bugs. The goal is correctness at every step.

**Do one task. Run the code. Verify it worked. Move to the next task.**

When you work this way — one small piece at a time — you are free from the pressure of getting everything right all at once. If something fails, you know exactly where the failure is, because you only changed one thing.

This is not a slow way to work. It is a very reliable way to work. Writing 300 lines and hunting bugs at the end is not efficient/effective programming.

---

## 2. Comments: Only Write What Earns Its Place

A comment exists for one reason: to add something the code itself cannot say. If a comment does not do that, it should not be there.

The practical test: does this comment help someone read and reason about this code, or does it slow them down? A comment that merely restates what the code obviously does forces the reader to process two things where one was enough. When the code later changes and the comment is not updated, that comment becomes actively misleading.

**A comment is justified when it does one of two things:**
- Marks a named phase or task in your program, giving the reader a map
- Explains something the code genuinely cannot express on its own — a non-obvious reason, a constraint, a known edge case

The most common legitimate use is task labels, which connect directly to how you approach a program: the tasks you write down at the start become your comments.

```python
# LOAD DATA
...
# PROCESS
...
# WRITE OUTPUT
```

These labels give structure to a longer program. They help you navigate while writing and help the reader understand what each block is doing at a high level.

What comments are **not** for:

```python
i = i + 1                # increment i by 1       ← restates the obvious
names[i] = line.strip()  # strip and assign        ← same
```

These add nothing. They are noise. If you feel the need to comment on what a line does, that is usually a signal to rename a variable or restructure the code — not to write the comment.

Good code is readable on its own. Every comment is also a maintenance obligation: it must stay accurate as the code evolves. Write fewer, better comments.

---

## 3. Verify Every Step

There are simply too many ways things can go wrong.

Suppose you write all your code at once and it fails. If you made mistakes in 2 places out of 9 steps, the number of ways those 2 mistakes could combine is:

```
9 × 8 / 2 = 36 possible failure combinations
```

If you made 3 mistakes out of 9 steps:

```
9 × 8 × 7 / 6 = 84 possible combinations
```

When you verify each step as you go, you catch bugs at the moment they are introduced. You never face a pile of interacting failures. Your search space stays small.

There is another benefit: each time you check a step and it works, you build a **mental map** of the code. If something breaks later, you already know which parts are solid. You can narrow the problem immediately.

The time you spend verifying as you go is far less than the time you would spend debugging a pile of interacting failures at the end.

---

## 4. How to Verify Correctness by Random Sampling

When you print or inspect output, **do not check in a predictable pattern**. Do not look at the first few entries. Do not look at the last ones. Do not look at the middle. Pick entries **at random**.

Here is why: some bugs only reveal themselves in certain positions. Structured errors can hide at the beginning, the end, or in specific patterns. If you always check the same spots, you can miss them entirely. Random sampling breaks this — the more random entries you check, the lower the chance that they all happen to look correct while the code is actually buggy.

**Practical technique:**
- Run the code, see the full output
- Pick an entry at random
- Go manually verify that entry against your raw data

> "The probability that you randomly check multiple entries and they all appear correct by chance — while the code is actually buggy — is very, very low."

This is a chain probability argument: each random check you do is an independent chance to catch a bug. The more entries you check, the more the combined probability of missing a bug drops. If there is a bug and each random check has even a modest chance of revealing it, doing several checks makes it almost certain you will find it.

Also: **form an expectation before you look**. Before checking output, make a rough mental prediction. If you expect the boss to have received about $30,000 and you see $31,000, that is reassuring. If you see $300, something is wrong. Always predict first, then observe.

---

## Part III: Coding Patterns

---

## 1. Lookup Tables vs. Appending

A **lookup table** is a pre-allocated list where the *index is meaningful* — it corresponds to an ID, a person, a position.

```python
NUM_MEMBERS = 100           # named constant — self-documenting, not generalization
names = [""] * NUM_MEMBERS  # pre-allocate slots
names[i] = "some name"      # store at the exact index
```

> **Named constants/globals vs. premature generalization.** `NUM_MEMBERS = 100` can be a global variable or a named constant: the value is set to 100. The name makes the intent explicit and removes a magic number (a naked `100`) scattered across the code base (though that is also acceptable in simple cases!). Names are documentation — they make it easier to reason about your code and intention.
>
> What you *should not* do is invent a function parameter, a config file, or a class hierarchy to make the number "flexible" — that is premature generalization. The principle is: do not abstract your logic before you have a reason to.

**Do not use `.append()` on a lookup table.** A lookup table works because you assign values to specific, meaningful indices. Using `.append()` on a lookup table is using the wrong tool for the job — `.append()` is meant for situations where you are accumulating items and the index doesn't carry meaning (like collecting transactions into a list, as we do later in the code).

```python
names.append("some name")  # WRONG — this is not how you use a lookup table
```

Compare this to a regular list where you are just accumulating items:

```python
transactions = []
transactions.append(some_value)  # fine — we are just collecting items here
```

These are two different use cases. Decide upfront: do I need to look things up by position (where the index *means* something, like an ID)? If yes, pre-allocate and assign by index. Am I just collecting items? Then append.

---

## 2. Separate File I/O from Logic

When you are loading data from a file and also doing computation, keep them in separate loops.

```python
NUM_MEMBERS = 100

# STEP 1: Load names (file I/O)
names = [""] * NUM_MEMBERS
for i in range(NUM_MEMBERS):
    f = open(f"members/member_ID{i}.txt", "r")
    names[i] = f.readline().strip()
    f.close()

# STEP 2: Find the collector (logic)
collector_id = -1
for i in range(NUM_MEMBERS):
    if names[i] == collector_name:
        collector_id = i
        break
```

Why separate loops? Because:
- They are conceptually different tasks
- You can verify each independently
- The logic step could later be parallelized independently of the file reads
- It is easier to reason about one thing at a time

This is a small program, but the habit matters. In larger programs, mixing I/O and computation in the same loop creates hard-to-test, hard-to-modify code.

---

## 3. Command-Line Arguments

Hard-coding a filename in your script means you must edit the source every time you want to run on different data. That is the wrong approach.

Instead, pass filenames as **command-line arguments**:

```bash
python solution.py apache_logs.txt result.txt
```

In Python, read these with `sys.argv`:

```python
import sys

input_file = sys.argv[1]   # first argument after the script name
output_file = sys.argv[2]  # second argument
```

`sys.argv[0]` is the name of your script — specifically, whatever path was used to invoke it. If you run `python ./scripts/solution.py`, then `sys.argv[0]` will be `./scripts/solution.py`, not just `solution.py`. Your actual data arguments start at index 1.

This is how real tools work. You write the tool once; you feed it different data every time you run it.

---

## 4. Parsing: Choose the Right Delimiter

When parsing structured text (logs, CSV, custom formats), the choice of delimiter matters.

**Spaces are fragile.** Fields like `"Mozilla/5.0 (Macintosh; Intel Mac OS X)"` contain spaces. Splitting on space will shatter this into many pieces unpredictably.

**Quotes (and other structural characters) are reliable.** The Apache log format wraps variable-length fields in quotes:

```
"GET /page HTTP/1.1" 200 1234 "https://referrer.com" "Mozilla/..."
```

If you split on `"`, each quoted section becomes a clean element. The spaces inside don't matter.

```python
parts = line.strip().split('"')
# parts[1] = "GET /page HTTP/1.1"
# parts[2] = " 200 1234 "  <- status code and bytes, space-separated
# parts[3] = "https://referrer.com"
```

**How to figure out the right delimiter:** a lot of this is trial and error, and that is normal. You do not need to be clever about it. Just try a delimiter, print the parts, and see if the split makes sense. If it does, you found a good delimiter. If not, try another one.

Remember: **log files are made to be parsed by others.** That is their entire purpose — they exist so that someone (or some program) can read them later and extract information. Whatever system produces the log follows a consistent rule set for formatting. Your job is just to figure out what that rule set is.

---

## 5. Counting with Dictionaries

When you need to count occurrences of strings (or any hashable value), use a dictionary.

```python
uniquereferrers = {}

if referrer in uniquereferrers:
    uniquereferrers[referrer] += 1
else:
    uniquereferrers[referrer] = 1
```

The first time you see a referrer, you create an entry with count 1. Every subsequent time, you increment it.

A more compact alternative using `.get()`:

```python
uniquereferrers[referrer] = uniquereferrers.get(referrer, 0) + 1
```

Both work. The first version is more explicit and easier to read when you're learning.

---

## 6. Sorting a List of Tuples

Python's `sort()` (and `sorted()`) compares tuples element by element, left to right. You can exploit this to sort by any field by putting it first in the tuple.

To sort a list of referrers by frequency (highest first):

```python
result = []
for referrer in uniquereferrers:
    result.append((uniquereferrers[referrer], referrer))  # count first!

result.sort(reverse=True)  # sorts by count descending
```

When you write out the results, swap the order back:

```python
for r in result:
    f.write(f"{r[1]}\t{r[0]}\n")  # referrer, count
```

This technique — putting the sort key first in a tuple — is a general, clean way to sort by any criterion without needing a custom comparator.

---

## Part IV: Code Walkthroughs

---

## 1. Code Walkthrough: Project 1 Solution

The full solution is 76 lines. It is read top to bottom as a sequence of clearly labeled steps.

### Step 1 — Get Collector Name
```python
spotifyfile = open("SPOTIFY_PRIVATE_PLAYLIST_BEST_OF_BEETLES_SONGS.txt", "r")
collectorname = spotifyfile.readline().strip()
spotifyfile.close()
```
Read one line, strip whitespace. Don't paste the name in — read it from the file so the code works for any dataset.

**Verify:** `print(collectorname)` — confirm you see the right name before continuing.

---

### Step 2 — Load All Member Names into a Lookup Table
```python
names = [""] * 100
for i in range(100):
    memberfile = open(f"members/member_ID{i}.txt", "r")
    names[i] = memberfile.readline().strip()
    memberfile.close()
```
Pre-allocate 100 slots. Assign each name at its corresponding index `i`. The index is the ID — this is what makes it a lookup table.

**Verify:** `print(i, names[i])` inside the loop. Spot-check a few random entries against the actual files.

---

### Step 3 — Find Collector ID
```python
collectorid = -1
for i in range(100):
    if names[i] == collectorname:
        collectorid = i
        break
```
Scan the lookup table for the collector's name. When found, record the index and stop. Starting with `-1` is intentional: if the name is never found, `collectorid` stays `-1`, which is an obviously wrong value that signals a problem.

**Verify:** `print(collectorid)` — confirm it matches the file you expect.

---

### Step 4 — Load and Parse All Transactions
```python
transactionsfile = open("transactions.txt", "r")
transactionlines = transactionsfile.readlines()
transactionsfile.close()

fromlist = []
tolist = []
amountlist = []
for line in transactionlines:
    line = line.strip()
    parts = line.split("|")
    fromid = int(parts[0].split(":")[1])
    toid = int(parts[1].split(":")[1])
    amount = int(parts[2].split(":")[1])
    fromlist.append(fromid)
    tolist.append(toid)
    amountlist.append(amount)

numberoftransactions = len(fromlist)
```
Three parallel lists: `fromlist[i]`, `tolist[i]`, `amountlist[i]` all refer to the same transaction at index `i`.

The format of each transaction line is `from:ID|to:ID|amount:N`. Split by `|` to get the three fields; split each field by `:` and take index `[1]` to get the value; convert to `int`.

**Verify:** Print a few parsed transactions and cross-check them visually against `transactions.txt`.

---

### Step 5 — Calculate Total Received from Collector
```python
total_amount_received_from_the_collector = [0] * 100

for i in range(numberoftransactions):
    if fromlist[i] == collectorid:
        total_amount_received_from_the_collector[tolist[i]] += amountlist[i]
```
For every transaction where the sender is the collector, add the amount to the receiver's running total.

**Verify:** Print non-zero entries. You should see a small number of people who received money from the collector.

---

### Step 6 — Find the Boss
```python
bossid = -1
maxreceived = 0
for i in range(100):
    if total_amount_received_from_the_collector[i] > maxreceived:
        maxreceived = total_amount_received_from_the_collector[i]
        bossid = i
```
Scan all totals. Keep track of the maximum seen so far and the person who achieved it. At the end, `bossid` holds the winner.

**Verify:** `print(bossid)` — then manually search the transactions file for transactions from the collector to this ID to sanity-check the total.

---

### Step 7 — Mark Criminals
```python
iscriminal = [False] * 100
iscriminal[bossid] = True
for i in range(numberoftransactions):
    if tolist[i] == bossid:
        iscriminal[fromlist[i]] = True
```
Everyone who sent money to the boss is a criminal. The boss is also marked — explicitly, because the boss did not send money to himself.

**Verify:** Print IDs and names of all criminals. Confirm the boss is in the list.

---

### Step 8 — Calculate Balances
```python
balance = [0] * 100
for i in range(numberoftransactions):
    balance[tolist[i]] += amountlist[i]
    balance[fromlist[i]] -= amountlist[i]
```
For every transaction: add to the receiver's balance, subtract from the sender's balance. This is done for everyone — no need to filter by criminal status here.

---

### Step 9 — Write the Report
```python
report = open("analysis.txt", "w")
report.write("id\tname\tbalance\n")
for i in range(100):
    if iscriminal[i] == True:
        report.write(f"{i}\t{names[i]}\t{balance[i]}\n")
report.close()
```
Loop from 0 to 99. Print only criminals. Because we loop in index order, the output is naturally sorted by ID — no sort function needed.

---

## 2. Code Walkthrough: Exam 1 Solution

The task: parse an Apache web server log, find all 404 errors, count how often each referrer URL caused them, and output the results sorted by frequency.

The full solution is 32 lines.

### Step 1 — Accept Arguments
```python
import sys

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]
```
The script is called as `python solution.py apache_logs.txt result.txt`. Never hard-code filenames — the grader runs the script with different filenames.

---

### Step 2 — Read the Log
```python
lines = open(inputfilename, "r").readlines()
```
One line of code. All log lines are now in a list.

---

### Step 3 — Parse Each Line
```python
uniquereferrers = {}

for line in lines:
    parts = line.strip().split('"')
    returncode = parts[2].strip().split()[0]
    referrer = parts[3]
```
Apache log lines look like this:
```
1.2.3.4 - - [01/Jan/2024] "GET /page HTTP/1.1" 200 1234 "https://referrer.com" "Mozilla/..."
```
Splitting on `"` (the quote character) separates the variable-length string fields cleanly:
- `parts[1]` = the request (`GET /page HTTP/1.1`)
- `parts[2]` = ` 200 1234 ` (status code and byte count, space-separated)
- `parts[3]` = the referrer URL
- `parts[5]` = the user agent string

Take `parts[2]`, strip it, split on space, take index `[0]` to get just the status code (`"200"`, `"404"`, etc.).

**Why not split on spaces directly?** The user-agent and referrer fields contain spaces. Space-splitting would break them into many fragments. Quotes are a safe boundary.

---

### Step 4 — Filter
```python
    if returncode != "404":
        continue
    if referrer == "-":
        continue
```
Skip lines that are not 404 errors. Skip entries with no referrer (a `-` means the request came directly, not from another site).

---

### Step 5 — Count Referrers
```python
    if referrer in uniquereferrers:
        uniquereferrers[referrer] += 1
    else:
        uniquereferrers[referrer] = 1
```
Dictionary accumulates a count per referrer URL.

---

### Step 6 — Build Sortable List
```python
result = []
for referrer in uniquereferrers:
    r = (uniquereferrers[referrer], referrer)
    result.append(r)

result.sort(reverse=True)
```
Each element is `(count, referrer)`. Sorting puts the highest count first.

---

### Step 7 — Write Output
```python
f = open(outputfilename, "w")
f.write("referrer\tcount\n")
for r in result:
    f.write(f"{r[1]}\t{r[0]}\n")
f.close()
```
Output: header row, then one line per referrer in descending frequency order.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
