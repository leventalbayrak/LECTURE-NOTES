
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Arrays as Lookup Tables
## The Core Idea

An array can be used as a **lookup table**: you store data at specific positions, then retrieve it instantly using the position number (the index).

**What is a lookup table?** A lookup table is any structure where you can access data immediately using a unique key or locator — no searching required. Think of it like a home address: if you need to find someone, you go directly to their house. You don't knock on every door in the city until you find them. The address *is* the locator. In the same way, an array index *is* the locator — give the array a number, and it takes you straight to the data.

This is the original and most fundamental method for locating data inside a collection. Before hash maps, databases, or search algorithms, there were arrays indexed by integers.

Arrays as lookup tables are used in four major patterns — each covered in detail in this document:

1. **Data storage and retrieval** — store records (names, scores, salaries) at an index and access them instantly by ID
2. **Presence / absence** — use a boolean array to record whether a value has been seen
3. **Counting** — use an integer array to count how many times each value appears
4. **Flags / settings** — use an array to store a configuration value per resource (e.g. which ports are open, how many connections each port allows)

---

> **Note on terminology:** This lecture uses the generic term *array* — the fundamental indexed data structure found in every programming language. Python calls its version a *list*, but the concept is identical. All code examples are in Python.

## 1. Mapping Integer Indices to Values

The simplest form: store data in an array, and use the integer index as the key to retrieve it.

```python
# What's the name of the nth day of the week?
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_number = 3
print(day_names[day_number])   # "Thursday"
```

The array maps numbers → values. If you know the number, you know the value instantly.

**This is O(1) — constant time (meaning the runtime is not affected by the number of elements in the array).** The reason is simple: the array doesn't scan. It computes the memory address directly from the index (`base_address + index * element_size`) and jumps there in a single step. It doesn't matter if the array has 7 entries or 7 million — the time is always the same.

A real-world IT example: a firewall uses a table indexed by port number to decide whether to allow or block traffic. Port 80 → allow HTTP. Port 22 → allow SSH. Port 12345 → block. The table has 65,536 entries (one per port), but checking any port is a single array lookup — O(1) — regardless of how many rules exist.

### Parallel Arrays

Once you have a unique index as an identifier, you are not limited to storing a single piece of data per entity. You can maintain **multiple arrays in parallel**, where the same index refers to the same entity across all of them.

This is known as the **Struct-of-Arrays (SoA)** pattern. Instead of grouping all data about one entity into a single record (Array-of-Structs / AoS), you keep each *field* in its own array and use a shared index to link them. One index gives you instant access to every field of that entity.

```python
names   = ["alice", "bob", "carol", "dave"]
scores  = [85,      92,    78,      95    ]
grades  = ["B",     "A",   "C",     "A"   ]

# index 1 = bob across all arrays
print(names[1])    # "bob"
print(scores[1])   # 92
print(grades[1])   # "A"
```

> **The index is the identity.**
>
> All information about entity #N lives at position N in every parallel array. Normally, to find a student's score you would have to search through a list of names until you found the right one — then look up their score. But if you **store and remember the index**, every future access is O(1). The index replaces the search entirely.
>
> Note: the student's ID number (or any other identifier) can still be *stored* at that index. The index is just where you look; what you store there is up to you.

Updating one entity's data — no searching required:

```python
# bob's score changes
scores[1] = 99
grades[1] = "A+"
```

---

## 2. Using Index as an ID — The ID System

To make direct lookup work, you need a **unique identifier** for each entity. The index is the best possible ID because:

- It is **guaranteed unique** — no two entries share a position
- It is **incremental** (0, 1, 2, 3...) — easy to generate, easy to iterate
- It is **an integer** — directly usable as an array index

The pattern: assign entity #0 to index 0, entity #1 to index 1, and so on. Agree on this scheme, and every lookup is O(1).

```python
# Agreed scheme: employee ID = their index
names    = [""]  * 1000   # 1000 employees, pre-allocated
salaries = [0]   * 1000

# Load data (index = ID)
names[0]    = "alice"
salaries[0] = 75000

names[42]   = "bob"
salaries[42] = 82000

# Later: instant lookup by ID
employee_id = 42
print(names[employee_id])      # "bob"
print(salaries[employee_id])   # 82000
```

---

## 3. Converting Characters to Integers for Index Lookup

Sometimes your data is a character, not an integer. Python's `ord()` function converts any character to its integer code, so you can use it as an index.

```python
print(ord('A'))   # 65
print(ord('a'))   # 97
print(ord('0'))   # 48
```

This lets you build lookup tables indexed by character. Example — count how many times each letter appears:

```python
counts = [0] * 128   # one slot per ASCII code

text = "hello"
for ch in text:
    counts[ord(ch)] += 1

print(counts[ord('l')])   # 2  (letter 'l' appeared twice)
print(counts[ord('h')])   # 1
```

**Connection to hexadecimal:** Character codes are often shown in hex in ASCII tables (e.g., 'A' = 0x41). Hex is just another way to write the same integer — the index is the same number regardless of base. Knowing this helps you read character tables.

**Connection to dictionaries:** `ord()` is a simple version of what a dictionary does internally — it converts a non-integer key (a character, or a string) into an integer index. Dictionaries generalize this idea to arbitrary keys.

---

## 4. Searching for Indices (Linear Search)

Direct lookup is only possible when you **already know the index**. But the index is not always known in advance. If data was loaded without a pre-agreed ID scheme, or if you only have a value (like a name) and need to find its position, you must search the array to discover the index first.

### Pattern A: Does it exist? (flag)

```python
names = ["alice", "bob", "carol", "dave"]
target = "carol"
found = False

for name in names:
    if name == target:
        found = True
        break

if found:
    print(f"{target} is in the list")
else:
    print(f"{target} not found")
```

### Pattern B: Where is it? (find the index)

```python
names = ["alice", "bob", "carol", "dave"]
target = "carol"
index = -1   # -1 = "not found" sentinel

for i in range(len(names)):
    if names[i] == target:
        index = i
        break

if index != -1:
    print(f"{target} is at index {index}")
```

Use `range(len(names))` (not `for name in names`) because you need `i`, not just the value.

### Pattern C: Use the found index across parallel arrays

```python
names   = ["alice", "bob", "carol", "dave"]
scores  = [85, 92, 78, 95]

target = "carol"
target_index = -1

for i in range(len(names)):
    if names[i] == target:
        target_index = i
        break

if target_index != -1:
    scores[target_index] += 10   # update Carol's score
    print(f"{names[target_index]}: {scores[target_index]}")
```

The search is used **once** to find the index — then all subsequent access is O(1).

---

## 5. Direct Lookup vs Linear Search

| | Direct Index Lookup | Linear Search |
|---|---|---|
| **Speed** | O(1) — constant, always one step | O(n) — grows with array size |
| **Requirement** | Must already know the index | Only need the value |
| **When to use** | Data was stored with an ID scheme | Searching by name, value, or attribute |
| **Limitation** | Index system is rigid; hard for humans to remember | Slow on large arrays |

**The typical pattern in practice:** use linear search *once* to find an entity's ID, then use that ID for all future direct lookups. The cost of the one-time search is paid once; every subsequent access is O(1).

---

## 6. The Four Lookup Patterns

Every use of an array as a lookup table falls into one of four patterns. Understanding which pattern you need tells you how to set up the array and what to store in it.

### Pattern 1 — Data Storage and Retrieval

**The idea:** store records at a known index; retrieve any field instantly by that index.

**When to use:** you have entities with multiple attributes (students, employees, products) and a pre-assigned integer ID.

```python
# Student records: index = student ID
student_names  = [""] * 500
student_grades = [0]  * 500

# Store
student_names[101]  = "alice"
student_grades[101] = 92

student_names[204]  = "bob"
student_grades[204] = 78

# Retrieve instantly — no search
sid = 204
print(student_names[sid])   # "bob"
print(student_grades[sid])  # 78
```

The array is the database. The index is the primary key.

---

### Pattern 2 — Presence / Absence (Boolean Lookup)

**The idea:** use a boolean array where `True` at position `i` means "value `i` has been seen."

**When to use:** you need to answer "have I seen this before?" — duplicate detection, membership testing, visited-node tracking.

```python
# Has this character appeared in the text?
seen = [False] * 128   # one slot per ASCII code

text = "hello world"
for ch in text:
    seen[ord(ch)] = True

# Query — O(1) per check
print(seen[ord('h')])   # True  — 'h' appeared
print(seen[ord('z')])   # False — 'z' did not appear
print(seen[ord(' ')])   # True  — space appeared
```

This is far faster than searching a list of "seen characters" every time. Once the array is built, every membership query is a single array access.

**Cybersec example:** a packet filter can mark which source IPs have already been seen in a time window using a boolean array indexed by the last octet of the IP. Any repeat sender is flagged instantly — no search through a list of prior IPs.

**Integer example — finding missing numbers:**

```python
# Given a list of integers, find which numbers from 0 to 9 are missing
a = [1, 2, 3, 3, 2, 4, 2, 6, 8]

# Mark which numbers are present
present = [False] * 10   # one slot for each digit 0-9

for x in a:
    present[x] = True

# Find missing numbers
missing = []
for i in range(10):
    if not present[i]:
        missing.append(i)

print("Missing numbers:", missing)   # [0, 5, 7, 9]
```

After a single pass through the input list, we can instantly check any number 0-9 to see if it appeared. Then we iterate 0-9 (constant — only 10 steps) to report which are missing.

---

### Pattern 3 — Counting (Frequency Table)

**The idea:** use an integer array initialized to zero; increment the slot at index `i` every time value `i` appears.

**When to use:** you need to count occurrences — character frequencies, vote tallies, histogram bins, byte distribution analysis.

```python
# How many times does each character appear?
counts = [0] * 128   # one slot per ASCII code

text = "mississippi"
for ch in text:
    counts[ord(ch)] += 1

# Query
print(counts[ord('s')])   # 4
print(counts[ord('i')])   # 4
print(counts[ord('p')])   # 2
print(counts[ord('m')])   # 1
```

After a single O(n) pass through the data, any frequency query is O(1).

**Cybersec example:** analyzing a network capture, count how many packets use each protocol number (stored as a byte). `protocol_counts[6]` gives you the TCP count, `protocol_counts[17]` gives UDP — all from a single pass through the capture file.

**Integer example — counting how many times each number appears:**

```python
# Given a list of integers, count how many times each number (0-9) appears
a = [1, 2, 3, 3, 2, 4, 2, 6, 8]

# Count frequencies
counts = [0] * 10   # one slot for each digit 0-9

for x in a:
    counts[x] += 1

# Query any number's frequency in O(1)
print(counts[2])   # 3 — number 2 appeared 3 times
print(counts[3])   # 2 — number 3 appeared 2 times
print(counts[0])   # 0 — number 0 never appeared
print(counts[8])   # 1 — number 8 appeared 1 time
```

After a single O(n) pass to build the frequency table, any frequency query is O(1).

---

### Pattern 4 — Flags / Settings (Configuration Table)

**The idea:** use an array where each index represents a resource (a port, a socket, a device slot), and the value at that index stores a setting or limit for that resource.

**When to use:** you have a fixed set of numbered resources and need to store a policy or configuration value for each one — open/closed, allowed/denied, capacity limits.

```python
# Which ports are open on this server?
# Index = port number, value = True (open) or False (closed)
port_open = [False] * 65536   # 65,536 possible ports

port_open[80]   = True    # HTTP
port_open[443]  = True    # HTTPS
port_open[22]   = True    # SSH
# all others remain False (closed)

# Check any port instantly — O(1)
print(port_open[80])      # True  — open
print(port_open[8080])    # False — closed
print(port_open[443])     # True  — open
```

You can also store a numeric limit per resource instead of a boolean:

```python
# How many simultaneous connections does each port allow?
# Index = port number, value = max connections (0 = not allowed)
port_limit = [0] * 65536

port_limit[80]  = 1000   # HTTP — up to 1000 connections
port_limit[443] = 1000   # HTTPS — up to 1000 connections
port_limit[22]  =    5   # SSH — max 5 connections (restrict brute force)

# Check any port's limit instantly
incoming_port = 22
if port_limit[incoming_port] > 0:
    print(f"Port {incoming_port} allows up to {port_limit[incoming_port]} connections")
else:
    print(f"Port {incoming_port} is not allowed")
```

The difference from Pattern 2 (presence/absence) is intent: here the array stores a *policy* or *limit*, not just "have I seen this." The value carries meaning beyond True/False.

---

### Summary of the Four Patterns

| Pattern | Array stores | Initialized to | Updated by | Query answers |
|---|---|---|---|---|
| Data retrieval | records / values | empty / zero | assignment | "What is entity #N?" |
| Presence/absence | booleans | `False` | `arr[key] = True` | "Have I seen key?" |
| Counting | integers | `0` | `arr[key] += 1` | "How many times did key appear?" |
| Flags / settings | policy values | default setting | configuration | "What is the rule for resource #N?" |

All four patterns share the same foundation: convert your key to an integer index, then access the array in O(1).

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
