
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Arrays, Strings, Lists & Practical Patterns

## Table of Contents

1. [String Indexing & Slicing](#1-string-indexing--slicing)
2. [String Immutability — You Can't Change It, You Can Only Rebuild It](#2-string-immutability--you-cant-change-it-you-can-only-rebuild-it)
3. [List Indexing & Nested Lists](#3-list-indexing--nested-lists)
4. [String Reversal — Three Ways](#4-string-reversal--three-ways)
5. [Common List Patterns: Filter, Replace, Count, `in`](#5-common-list-patterns-filter-replace-count-in)
6. [Log Parsing with `split()`](#6-log-parsing-with-split)
7. [Sorting: `sort()` vs `sorted()`](#7-sorting-sort-vs-sorted)
8. [List Methods: `append`, `pop`, `insert`](#8-list-methods-append-pop-insert)
9. [Reversing a List](#9-reversing-a-list)
10. [Alias vs. Deep Copy](#10-alias-vs-deep-copy)
11. [String Methods: `upper`, `lower`, `replace`, `strip`, `split`, `join`](#11-string-methods-upper-lower-replace-strip-split-join)

---

## 1. String Indexing & Slicing

### Basic Indexing and Slicing

```python
s = "i like apples"
print(s[0])      # 'i'
print(s[-1])     # 's'
print(s[1:5])    # 'like'
print(s[-5:-2])  # 'ppl'
print(s[:])      # 'i like apples'
```

- Positive indices count from the left starting at 0.
- Negative indices count from the right: `-1` is the last character, `-2` is second-to-last, and so on.
- `s[start:stop]` extracts from `start` up to but **not including** `stop`.
- `s[:]` is a full copy.

### Step Slicing `[start:stop:step]`

```python
s = "ABCDEFG"
print(s[::2])    # 'ACEG'    — every other character
print(s[::-1])   # 'GFEDCBA' — full reversal
```

`[::-1]` is the standard Pythonic way to reverse a string or list.

### Practical Examples

```python
# File extension
s = "cool@gmail.com"
print(s[-3:])    # 'com'

# Last 4 digits of a phone number
phone = "713-555-1234"
print(phone[-4:])   # '1234'
```

---

## 2. String Immutability — You Can't Change It, You Can Only Rebuild It

Strings cannot be changed in place. Every "modification" creates a brand new string.

```python
s = "apple"
# i want Apple
# s[0] = 'A'              # not allowed — strings are immutable
newstr = "A" + s[1:]      # build a new string: "Apple"
print(newstr)              # 'Apple'
```

When you don't want to hardcode the replacement character, use `.upper()` on just the first character:

```python
s = "heeelloooook"
newstr = s[0].upper() + s[1:]   # 'Heeelloooook'
print(newstr)
```

`s[0]` is a one-character string. Calling `.upper()` on it returns its uppercase version. Then you concatenate the rest of the original string unchanged.

Always capture the result of string methods — they return a new string and never modify the original:

```python
s = "hello"
s.upper()        # result thrown away — s is still 'hello'
s = s.upper()    # correct — capture the new string
```

---

## 3. List Indexing & Nested Lists

### Basic List Indexing

```python
mylist = ["apple", "orange", "pineapple"]
print(mylist[0])     # 'apple'
print(mylist[1][0])  # 'o'  — index the list, then index the string element
```

`mylist[i][j]` first picks element `i` from the outer list, then picks character `j` from it.

### Iterating a List of Lists — Two Styles

Given a player database where each inner list is `[name, gamertag]`:

```python
playerdatabase = [
    ["john",  "JOHNKILYU"],
    ["alice", "INWONDERLAND"],
    ["kevin", "SUPERSNIPERSECRETSCROPTIOONINTELLECT5NSACIA(SPECIALAGENT)P"]
]
```

**For-each (iterator) style** — gives you the whole row each time:
```python
for player in playerdatabase:
    print(player)
```

**Index style** — gives you a position you can use to reach any column:
```python
for i in range(len(playerdatabase)):
    print(playerdatabase[i][1])   # print just the gamertag
```

Use the index style when you need the position `i`, or when you want to access a specific column. Use for-each when you just need to process each row.

### Lookup by Name (Exact Match)

```python
name = ""  # input("enter name:")
for player in playerdatabase:
    if name == player[0]:
        print(player[1])
```

### Filter by First Letter of Name

```python
playerdatabase = [
    ["john",  "xxsupersniperx400xx"],
    ["alex",  "super1337h4k3r"],
    ["sarah", "idanceonyourgrace"],
    ["jack",  "inthebox"],
    ["jacob", "SCORPIONINJAWARRIORSECRETSPYxDAGGER"]
]

userquery = "j"  # input("ENTER FIRST LETTER:")
userquery = userquery.lower()

for player in playerdatabase:
    firstletter = player[0][0]
    if firstletter == userquery:
        print(f"realid: {player[0]} nickname:{player[1]}")
```

`player[0][0]` — `player[0]` is the name string, `[0]` on that string is its first character.

### Filter by First Letter of Gamertag

You can filter on any column the same way. Here, filter by the first letter of the *gamertag* (column index 1):

```python
playerdatabase = [
    ["john",  "JOHNKILYU"],
    ["alice", "INWONDERLAND"],
    ["kevin", "SUPERSNIPERSECRETSCROPTIOONINTELLECT5NSACIA(SPECIALAGENT)P"]
]

letter = ""  # input("enter first letter of gamertag:")
for player in playerdatabase:
    if letter == player[1][0]:
        print(player[0] + " : " + player[1])
```

### Case-Insensitive Filter

To make the comparison case-insensitive, normalize both sides to lowercase before comparing:

```python
letter = ""  # input("enter first letter:")
letter = letter.lower()
for player in playerdatabase:
    if letter == player[1][0].lower():
        print(player)
```

`player[1][0]` is the first character of the gamertag. `.lower()` on that single character lets you match regardless of how the gamertag is capitalized.

### Iterating a String Character by Character

A string is iterable — you can loop over it directly:

```python
s = "ABCDEFG"
for char in s:
    print(char)
```

This prints each character on its own line: A, B, C, D, E, F, G. This is the for-each style applied to a string instead of a list.

---

## 4. String Reversal — Three Ways

```python
s = "ABCDEFG"
```

**Way 1 — Arithmetic index, print each character:**
```python
for i in range(len(s)):
    print(s[len(s)-1-i])
```
When `i=0` you get the last character (`s[6]`). When `i=1`, the second-to-last (`s[5]`). And so on.

**Way 2 — Backward range, print each character:**
```python
for i in range(len(s)-1, -1, -1):
    print(s[i])
```
`range(6, -1, -1)` counts 6, 5, 4, 3, 2, 1, 0.

**Way 3 — Slice reversal:**
```python
newstr = s[::-1]
print(newstr)   # 'GFEDCBA'
```

The `[::-1]` slice is the standard Pythonic way. The loop versions show exactly what is happening underneath.

---

## 5. Common List Patterns: Filter, Replace, Count, `in`

### Filter — Copy Only What You Want

```python
a = [1, -2, 3, -4, -5, 6]
b = []
for x in a:
    if x >= 0:
        b.append(x)
print(b)   # [1, 3, 6]
```

`b` is a new list. `a` is untouched.

### In-place Replace — Modify the Original

```python
a = [1, -2, 3, -4, -5, 6]
# replace negative numbers with 0s, in-place
for i in range(len(a)):
    if a[i] < 0:
        a[i] = 0
print(a)   # [1, 0, 3, 0, 0, 6]
```

Use `range(len(a))` for in-place modification — you need the index `i` to write back with `a[i] = ...`. A `for x in a` loop gives you a copy of each value; assigning to `x` does not change the list.

### Count — Tally Matches

```python
a = [1, 2, 3, 3, 3, 2, 1, 5, 3]
count = 0
for x in a:
    if x == 3:
        count += 1
print(count)   # 4
```

### `in` — Membership Check

```python
if 3 in a:
    print("yes")

s = "i like apples"
if "app" in s:
    print("yes")
```

- On a **list**: `in` checks for an exact element match.
- On a **string**: `in` checks whether the left side appears as a substring anywhere in the right side.

---

## 6. Log Parsing with `split()`

Each log entry has three tab-separated fields: datetime, IP address, and error message.

```python
log = [
    "2026-03-03 10:01:12\t192.168.1.10\tConnection timeout while contacting auth service",
    "2026-03-03 10:03:44\t10.0.0.25\tDatabase lock wait timeout exceeded",
    "2026-03-03 10:05:09\t172.16.5.90\tPermission denied writing to /var/app/cache",
    "2026-03-03 10:07:31\t203.0.113.7\tAPI returned 500 internal server error",
    "2026-03-03 10:09:18\t198.51.100.23\tDNS resolution failed for upstream host",
    "2026-03-03 10:12:55\t192.168.1.77\tFile not found: /etc/app/config.yaml",
    "2026-03-03 10:15:42\t8.8.8.8\tTLS handshake failed due to certificate mismatch",
    "2026-03-03 10:18:06\t10.10.10.3\tConnection reset by peer during upload",
    "2026-03-03 10:20:27\t172.31.9.14\tService unavailable on port 5432",
    "2026-03-03 10:22:50\t203.45.67.89\tRequest timeout after 30 seconds"
]
```

`split('\t')` breaks each entry on the tab character:
- `parts[0]` = datetime (`"2026-03-03 10:01:12"`)
- `parts[1]` = IP address (`"192.168.1.10"`)
- `parts[2]` = error message (`"Connection timeout while contacting auth service"`)

### Print Error Message with IP

```python
for entry in log:
    parts = entry.split('\t')
    print(parts[2] + '(' + parts[1] + ')')
```

Output: `Connection timeout while contacting auth service(192.168.1.10)`

### Grab Only the First Word of the Error — Split Twice

```python
for entry in log:
    parts = entry.split('\t')
    print(parts[2].split()[0] + " (" + parts[1] + ")")
```

Output: `Connection (192.168.1.10)`

How the double split works:
1. `parts[2]` is the full error string: `"Connection timeout while contacting auth service"`
2. `.split()` with no argument splits on spaces: `["Connection", "timeout", "while", "contacting", "auth", "service"]`
3. `[0]` takes the first word: `"Connection"`

`split()` with no argument splits on any whitespace. With an argument it splits on that specific character or string.

---

## 7. Sorting: `sort()` vs `sorted()`

Two versions — know the difference:

| | `a.sort()` | `sorted(a)` |
|---|---|---|
| Modifies original | **Yes** — in place | No — original untouched |
| Return value | `None` | New sorted list |

**In-place sort:**
```python
a = [2, 7, 1, 3, 5]
a.sort()   # in-place sort
print(a)   # [1, 2, 3, 5, 7]
```

**Non-in-place sort — original preserved:**
```python
a = [2, 7, 1, 3, 5]
b = sorted(a)
print(a)   # [2, 7, 1, 3, 5]  — unchanged
print(b)   # [1, 2, 3, 5, 7]
```

**Strings sort alphabetically:**
```python
a = ["orange", "apple", "pineapple"]
b = sorted(a)
print(a)   # ['orange', 'apple', 'pineapple']  — unchanged
print(b)   # ['apple', 'orange', 'pineapple']
```

**Nested lists sort by first element by default:**
```python
a = [["orange", 7], ["apple", 4], ["pineapple", 2], ["orange", 1]]
a.sort()
print(a)   # [['apple', 4], ['orange', 1], ['orange', 7], ['pineapple', 2]]
```

When the first elements are equal, Python compares the second elements, and so on.

**Common mistake:** `result = a.sort()` — `result` will be `None`. Use `sorted()` when you need to keep the original.

### Sorting by a Non-First Column

By default, sort compares the first element. What if you want to sort by a different column — for example, by GPA (index 2)?

The trick: build a temporary list where the sort key comes first, sort it, done.

```python
studentdb = [
    [1234, "levent", 1.2],
    [8324, "john",   6.2],
    [9294, "alice",  2.2],
    [8212, "dave",   5.2],
]

# To sort by GPA, put GPA first in each row
tmpdb = []
for student in studentdb:
    tmpdb.append([student[2], student[0], student[1]])

tmpdb.sort()
print(tmpdb)
# [[1.2, 1234, 'levent'], [2.2, 9294, 'alice'], [5.2, 8212, 'dave'], [6.2, 8324, 'john']]
```

`student[2]` is GPA, `student[0]` is ID, `student[1]` is name. By putting GPA first in `tmpdb`, `sort()` naturally uses it as the key.

**Note:** A cleaner approach using `key=` with a lambda function exists and will be covered in a later lecture.

**Note:** Both `sort()` and `sorted()` accept a `key=` argument that lets you specify which part of each element to sort by.

---

## 8. List Methods: `append`, `pop`, `insert`

### `append` and `pop`

`append` adds an element to the end of the list. `pop()` with no argument removes and returns the last element. Both work at the end — no shifting required.

```python
lst = []
lst.append(10)
lst.append(20)
lst.append(30)
print(lst)           # [10, 20, 30]
val = lst.pop()      # removes from end, O(1)
print(val, lst)      # 30  [10, 20]
```

`append` and `pop()` (no argument) work at the end of the list. They are O(1) — no shifting required.

### `pop(i)` and `insert(i, value)`

When you give `pop` or `insert` an index, Python has to shift every element after that position — that's what makes them expensive compared to working at the end.

```python
lst = [10, 20, 30, 40, 50]
lst.pop(0)           # removes first element — everything shifts left, O(n)
print(lst)           # [20, 30, 40, 50]
lst.insert(0, 99)    # inserts at front — everything shifts right, O(n)
print(lst)           # [99, 20, 30, 40, 50]
```

`pop(i)` and `insert(i, x)` at arbitrary positions are O(n) — every element after position `i` shifts.

### Practical Patterns

Here are common real-world uses of `append`, `pop`, and `insert` — notice how each one builds or processes a list step by step.

```python
# Collect only passing scores
results = [72, 45, 88, 91, 38, 60, 77]
passing = []
for score in results:
    if score >= 60:
        passing.append(score)
print(passing)    # [72, 88, 91, 60, 77]

# Simple undo history
history = []
history.append("open file")
history.append("edit line 5")
history.append("save")
last = history.pop()   # undo last action
print("Undone:", last)
print("State:", history)

# Insert urgent task at the front of a queue
queue = ["task_a", "task_b", "task_c"]
queue.insert(0, "urgent_task")
next_task = queue.pop(0)
print("Processing:", next_task)
```

Lists also have `.index(value)` (returns the position of the first match) and `.count(value)` (counts how many times a value appears). Look both up in the Python docs and try them out yourself.

### Practical: Find Top Student

```python
names  = ["Alice", "Bob", "Carol", "Dave"]
scores = [88, 72, 95, 61]
best_score = max(scores)
best_idx   = scores.index(best_score)
print("Top student:", names[best_idx], "with", best_score)
# Top student: Carol with 95
```

---

## 9. Reversing a List

### DIY — Swap from Both Ends

To reverse a list in place, swap the first element with the last, the second with the second-to-last, and so on — stopping at the middle. Each iteration `i` pairs index `i` from the front with index `n-1-i` from the back.

```python
lst = [1, 2, 3, 4, 5]
n = len(lst)
for i in range(n // 2):
    temp           = lst[i]
    lst[i]         = lst[n - 1 - i]
    lst[n - 1 - i] = temp

print(lst)   # [5, 4, 3, 2, 1]
```

### Python Built-ins

Python gives you two shortcuts. `.reverse()` flips the list in place (like the loop above). `[::-1]` creates a new reversed list without touching the original — same idea as the step-slice you saw with strings.

```python
# reverse() — modifies in place, returns None
lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst)   # [5, 4, 3, 2, 1]

# Slice reversal — creates a new list, original untouched
lst = [1, 2, 3, 4, 5]
rev = lst[::-1]
print(rev)   # [5, 4, 3, 2, 1]
print(lst)   # [1, 2, 3, 4, 5]  — unchanged
```

**Strings have no `.reverse()` method** — they are immutable. Use `[::-1]`:

```python
s = "hello"
print(s[::-1])   # 'olleh'
```

---

## 10. Alias vs. Deep Copy

A variable holds a **reference** to an object, not the object itself. Assigning one list variable to another copies the reference — not the data.

```python
a = [1, 2, 3]
b = a           # b and a point to the SAME list
b[0] = 99
print(a)        # [99, 2, 3]  ← a was changed through b
print(b)        # [99, 2, 3]
```

This is the **alias trap** — you think you have two lists, but you have one list with two names.

**How to make an independent copy:**

```python
a = [1, 2, 3]
b = a[:]        # slice with empty start/stop — new list with same values
b[0] = 99
print(a)        # [1, 2, 3]  ← untouched
print(b)        # [99, 2, 3]

c = a.copy()    # same result as a[:]
```

Strings never have this problem — any "modification" already produces a new string, so aliasing is always safe.

```python
x = "hello"
y = x
y = y.upper()   # creates a new string — x unaffected
print(x)        # 'hello'
print(y)        # 'HELLO'
```

---

## 11. String Methods: `upper`, `lower`, `replace`, `strip`, `split`, `join`

Every string method returns a **new** string. The original is never modified. Always capture the result.

### `upper()` and `lower()`

```python
s = "Hello, World!"
print(s.upper())   # 'HELLO, WORLD!'
print(s.lower())   # 'hello, world!'

# Common mistake
s2 = "hello"
s2.upper()         # result thrown away — s2 is still 'hello'
s2 = s2.upper()    # correct — capture the result
print(s2)          # 'HELLO'
```

### `strip()`

Removes whitespace from both ends of a string (not from the middle):

```python
"  hello  ".strip()          # 'hello'
"  START  ".strip().lower()  # 'start'
```

### `replace()`

Replaces every occurrence of a substring with another string:

```python
s = "i like cats and cats like me"
print(s.replace("cats", "dogs"))   # 'i like dogs and dogs like me'

# Remove a character by replacing it with an empty string
print("hello!".replace("!", ""))   # 'hello'
```

`replace(old, new)` returns a new string with **all** occurrences of `old` swapped for `new`. The original string is untouched.

### Chaining Methods

String methods return strings, so you can chain them:

```python
raw = "  Hello, World!  "
clean = raw.strip().lower().replace(",", "").replace("!", "")
print(clean)   # 'hello world'
```

Practical pattern — normalize user input before comparing:
```python
raw_cmd = "  RESTART  "
cmd = raw_cmd.strip().lower()
valid = ['start', 'stop', 'restart']
if cmd in valid:
    print("Executing:", cmd)
```

### `split()`

`split()` breaks a string into a list of substrings. With no argument it splits on any whitespace; pass a character like `','` or `'.'` to split on that specific delimiter.

```python
# Default: split on whitespace
"hello world foo".split()         # ['hello', 'world', 'foo']

# Split on a specific character
"192.168.1.23".split('.')         # ['192', '168', '1', '23']
"Alice,30,Engineer".split(',')    # ['Alice', '30', 'Engineer']
```

`split()` always returns **strings**. Convert to `int` if you need numbers:

```python
line = "3 14 7 2 9"
numbers = []
for token in line.split():
    numbers.append(int(token))
print(numbers)      # [3, 14, 7, 2, 9]
print(sum(numbers)) # 35
```

### `join()`

The inverse of `split()` — glues a list of strings into one string using a separator:

```python
words = ['hello', 'I', 'like', 'apples']
' '.join(words)    # 'hello I like apples'
'_'.join(words)    # 'hello_I_like_apples'
''.join(words)     # 'helloIlikeapples'

# Reassemble IP address
octets = ['192', '168', '1', '23']
'.'.join(octets)   # '192.168.1.23'

# Reverse words in a sentence
sentence = "the quick brown fox"
' '.join(sentence.split()[::-1])   # 'fox brown quick the'
```

`join` only works with a list of strings. Convert other types first.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---
