
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Strings and Lists

## Table of Contents

1. [The Common Foundation: Arrays Under the Hood](#1-the-common-foundation-arrays-under-the-hood)
2. [Strings](#2-strings)
3. [Python Lists](#3-python-lists)
4. [Indexing and Slicing](#4-indexing-and-slicing)
5. [Reference vs. Copy (Lists)](#5-reference-vs-copy-lists)
6. [Concatenation](#6-concatenation)
7. [Search with `in`](#7-search-with-in)
8. [String Methods: `split()`](#8-string-methods-split)
9. [String Methods: `join()`](#9-string-methods-join)
10. [Strings vs. Lists — Side-by-Side Comparison](#10-strings-vs-lists--side-by-side-comparison)

---

## 1. The Common Foundation: Arrays Under the Hood

Both strings and lists are built on top of the array concept. Before looking at either one, remember what an array is: a **fixed-size block of consecutive memory cells**, accessed by index (offset from the start).

```
Memory:  [ 'h' ][ 'e' ][ 'l' ][ 'l' ][ 'o' ]
Index:      0     1     2     3     4
           ↑
         s  (reference to start)
```

A string is an array of **characters**. A list is an array of **any values**. Python wraps both in objects that add useful features on top — but the underlying structure is the same.

---

## 2. Strings

### What is a string?

A string is an **array of characters**. Each character occupies one position, accessible by index.

```python
s = "hello"
print(s[0])   # 'h'
print(s[4])   # 'o'
print(len(s)) # 5
```

Python stores extra metadata alongside the characters (like the length), so `len(s)` is instant — it just reads a stored value rather than counting.

### Immutability — the critical rule

Strings in Python are **immutable**: you can read any character by index, but you **cannot change** a character in place.

```python
s = "hello"
print(s[2])    # 'l'  — reading is fine

s[0] = 'H'    # ERROR: TypeError — strings do not support item assignment
```

Any operation that appears to "modify" a string actually creates a **brand new string** and returns it. The original is untouched.

```python
s = "hello"
s = 'H' + s[1:]   # creates a new string "Hello", reassigns s to it
print(s)           # "Hello"
```

> **Why immutable?** Python made this design choice deliberately. Because strings are so commonly shared between parts of a program, making them immutable prevents accidental modification and enables internal optimizations.

### Built-in String Operations

| Operation | Syntax | What it does |
|-----------|--------|--------------|
| Length | `len(s)` | Number of characters |
| Index | `s[i]` | Character at position i |
| Concatenate | `s + s2` | Join two strings → new string |
| Repeat | `s * n` | Repeat n times → new string |
| Find substring | `s.find(sub)` | Returns first index, or **-1** if not found |
| Find substring | `s.index(sub)` | Returns first index, or **raises error** if not found |
| Count | `s.count(sub)` | Count non-overlapping occurrences |
| Replace | `s.replace(old, new)` | Replace occurrences → new string |
| Split | `s.split(sep)` | Split into list of strings |
| Join | `sep.join(lst)` | Join list of strings into one |
| Strip whitespace | `s.strip()` | Remove leading/trailing whitespace → new string |
| Lowercase | `s.lower()` | Convert to lowercase → new string |
| Uppercase | `s.upper()` | Convert to uppercase → new string |
| Starts with | `s.startswith(x)` | Returns True/False |
| Ends with | `s.endswith(x)` | Returns True/False |
| Search (bool) | `sub in s` | Returns True if substring exists |

Every method that "changes" a string returns a **new string**. Always capture the result.

```python
s = "hello"
s.upper()        # does nothing useful — result is discarded
s = s.upper()    # correct: reassign s to the new uppercase string
print(s)         # "HELLO"
```

---

## 3. Python Lists

### What is a list?

A Python list is a **dynamic array** — an array that manages its own size for you. Under the hood, it performs the same memory operations described in the arrays notes: allocating space, copying on resize, shifting on insert/delete. Python just hides all of that.

```python
a = []             # empty list
a.append(42)       # push: [42]
a.append(17)       # push: [42, 17]
a.append(8)        # push: [42, 17, 8]
a.pop()            # pop:  [42, 17]   (returns 8)
```

> **Naming note:** What array notes call "push" is called **`append`** in Python. Same operation — adds one element to the end.

Because Python does the bookkeeping for you, you never need to track size manually — `len(a)` always gives you the current count.

### Mutability

Unlike strings, lists are **mutable**: you can change any element by index at any time.

```python
a = [1, 2, 3]
a[1] = 99          # OK — lists support item assignment
print(a)           # [1, 99, 3]
```

### Creating lists

Three common ways to create a list:

```python
# 1. Empty list — start with nothing, build up with append
a = []

# 2. Pre-populated list — write the values directly
a = [10, 20, 30, 40, 50]

# 3. Repeat-initialized list — same value repeated N times
a = [0] * 10       # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = [None] * 5     # [None, None, None, None, None]
```

The `[value] * n` syntax is extremely useful when you want to pre-allocate a list of a known size — for example, simulating a raw fixed-size array or filling a grid with zeros. This is the same multiplication operation that works on strings (`"ha" * 3` → `"hahaha"`), applied to a one-element list.

### Lists can hold mixed types

In a traditional array, every element has the same type. Python lists are flexible — you can mix types. (This is possible because each cell technically holds a reference to an object, not the object itself.)

```python
mixed = [42, "hello", 3.14, True]   # valid in Python
```

### Built-in List Operations

| Operation | Syntax | Array Equivalent |
|-----------|--------|-----------------|
| Push to end | `lst.append(x)` | push |
| Remove last | `lst.pop()` | pop |
| Remove at index | `lst.pop(i)` | delete |
| Insert at index | `lst.insert(i, x)` | insert (shifts right) |
| Delete at index | `del lst[i]` | delete |
| Access by index | `lst[i]` | indexing |
| Get size | `len(lst)` | (manual tracking in raw arrays) |
| Concatenate | `lst + lst2` | merge (creates new list) |
| Sort in place | `lst.sort()` | sort |
| Sort (new list) | `sorted(lst)` | sort + duplicate |
| Reverse in place | `lst.reverse()` | reverse |
| Search (bool) | `x in lst` | linear search |
| Search (index) | `lst.index(x)` | linear search |
| Count occurrences | `lst.count(x)` | iterate + count |
| Duplicate | `lst.copy()` | duplicate |
| Extend in place | `lst.extend(lst2)` | concatenate in place |
| Compare | `lst == lst2` | comparison |

---

## 4. Indexing and Slicing

Both strings and lists support slicing — a powerful way to extract pieces of a sequence.

### Zero-based indexing (recap)

Index 0 is the first element (an offset of 0 from the start). This applies to both strings and lists.

```python
s = "I like apples"
#    0123456789...

print(s[0])   # 'I'
print(s[7])   # 'a'
```

### Negative indexing

Negative indices count backward from the **end** of the sequence.

```python
s = "I like apples"

print(s[-1])   # 's'   (last character)
print(s[-2])   # 'e'   (second to last)
print(s[-6])   # 'a'   (6th from the end)
```

Negative indices are a convenience. `s[-n]` is equivalent to `s[len(s) - n]`.

**When is this useful?** When you care about the *tail* of a sequence. For example, every email address ends with a domain like `.com` or `.net`. The tail is predictable even when the beginning is variable:

```python
email = "alice@gmail.com"
print(email[-3:])    # "com"

email2 = "bob@someplace.net"
print(email2[-3:])   # "net"
```

> **Critical: single index vs. slice with negative numbers**
>
> This is a very common mistake. `s[-3]` and `s[-3:]` look similar but do completely different things:
>
> | Syntax | What you get | Example on `"gmail.com"` |
> |--------|--------------|--------------------------|
> | `s[-3]` | **One character** — the 3rd from the end | `'c'` |
> | `s[-3:]` | **Substring** — everything from the 3rd-from-end to the finish | `'com'` |
>
> ```python
> s = "gmail.com"
> print(s[-3])    # 'c'     ← just one character
> print(s[-3:])   # 'com'   ← the last 3 characters
> ```
>
> Always ask yourself: do I want one character, or a substring? If you want a substring from the tail, you need the colon.

### Slicing syntax

The general form is `sequence[start : stop : step]`. All three parts are optional.

| Slice | Meaning | Array equivalent |
|-------|---------|-----------------|
| `s[a:b]` | Elements from index a up to (not including) b | subarray |
| `s[:b]` | From the beginning up to b | subarray from start |
| `s[a:]` | From index a to the end | subarray to end |
| `s[:]` | Entire sequence | duplicate |
| `s[::2]` | Every other element (step 2) | — |
| `s[::-1]` | Entire sequence, reversed | reverse |
| `s[a:b:step]` | From a to b, every step-th element | — |

The **stop index is always exclusive** — it acts as a "stop before here" sign, not "include this."

```python
s = "I like apples"

print(s[2:6])    # "like"         (indices 2, 3, 4, 5)
print(s[:6])     # "I like"       (from start to index 5)
print(s[7:])     # "apples"       (from index 7 to end)
print(s[:])      # "I like apples"  (full copy)
print(s[::2])    # "Ilk pls"      (every other character)
print(s[::-1])   # "selppa ekil I" (reversed)
```

The same syntax works identically on lists:

```python
lst = [10, 20, 30, 40, 50]

print(lst[1:4])    # [20, 30, 40]
print(lst[:3])     # [10, 20, 30]
print(lst[2:])     # [30, 40, 50]
print(lst[:])      # [10, 20, 30, 40, 50]  (independent copy)
print(lst[::-1])   # [50, 40, 30, 20, 10]  (reversed)
```

Slicing always creates a **new** string or list — it does not modify the original.

### Connecting slicing back to array operations

Slices map directly to the array operations from the arrays note:

- `s[a:b]` is a **subarray** (consecutive block)
- `s[:]` is a **duplicate** (full copy)
- `s[::-1]` is a **reverse**
- Step slicing like `s[::2]` is a **filter** by position

---

## 5. Reference vs. Copy (Lists)

This is one of Python's most surprising behaviors, and understanding it requires understanding how Python stores values.

### How Python stores values

In Python, a variable does not hold a value directly — it holds a **reference**: a pointer to wherever the value lives in memory.

A list is a container of references. Each slot in the list holds a reference to some object, not the object itself.

```
a = [1, 2, 3]

List container:   [ slot 0 ][ slot 1 ][ slot 2 ]
                       ↓         ↓         ↓
Actual objects:   [int: 1]  [int: 2]  [int: 3]
```

### `b = a` — creating an alias

When you write `b = a`, you copy the reference to the **list itself** — not the list's contents. Both `a` and `b` now refer to the **same object** in memory. `b` is an **alias** for `a`: two different names pointing at one single list.

```
a ──→  [ slot 0 ][ slot 1 ][ slot 2 ]
b ──→  (same object — b is an alias for a)
```

Changing anything through `b` is the same as changing it through `a`:

```python
a = [1, 2, 3]
b = a             # b is an alias — it refers to the exact same list object

b[1] = 99
print(a)          # [1, 99, 3]  ← a was changed through b!
print(b)          # [1, 99, 3]
```

### `b = a[:]` — creating an independent copy

`b = a[:]` creates a **new, independent list**. Changing `b` does not affect `a`, and vice versa.

```python
a = [1, 2, 3]
b = a[:]          # new container, slots point to same integer objects

b[1] = 99         # replaces b's slot 1 — does not touch a
print(a)          # [1, 2, 3]   ← unchanged
print(b)          # [1, 99, 3]
```

You can also use `a.copy()` — it does the same thing:

```python
b = a.copy()      # equivalent to a[:]
```

### When the list contains other lists

If a list's elements are themselves lists, `[:]` only copies the outer list — the inner lists are not copied. `a[0]` and `b[0]` become **aliases for the same inner list**, so modifying that inner list affects both `a` and `b`:

```python
a = [[1, 2], [3, 4]]   # a list of lists
b = a[:]               # b is a new list, but a[0] and b[0] are aliases for the same inner list

b[0][0] = 99           # changes the inner list — a[0] and b[0] are the same object
print(a)               # [[99, 2], [3, 4]]  ← a was affected!
print(b)               # [[99, 2], [3, 4]]
```

To copy the inner lists as well, use `copy.deepcopy()`:

```python
import copy
b = copy.deepcopy(a)

b[0][0] = 99
print(a)    # [[1, 2], [3, 4]]   ← completely unaffected
print(b)    # [[99, 2], [3, 4]]
```

> **For this course:** you will mostly work with flat lists of integers and strings (immutable values). `b = a[:]` and `b = a.copy()` will behave as fully independent copies in those cases. Just be aware the deeper mechanism exists.

> **Strings do not have this issue.** Since strings are immutable, there is nothing to accidentally share or corrupt. Every string operation that "changes" a string already returns a new one.

---

## 6. Concatenation

Concatenation means joining two sequences end-to-end into a new one. The `+` operator does this for both strings and lists.

### Strings

```python
s1 = "hello"
s2 = " world"
s3 = s1 + s2
print(s3)    # "hello world"

print(s1)    # "hello"  ← unchanged; + always creates a new string
print(s2)    # " world" ← unchanged
```

Because strings are immutable, `+` can never modify either operand — it always produces a brand-new string.

### Lists

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)    # [1, 2, 3, 4, 5, 6]

print(a)    # [1, 2, 3]  ← unchanged
print(b)    # [4, 5, 6]  ← unchanged
```

Same rule: `+` creates a new list and leaves both originals untouched.

### The `+=` shorthand

`+=` is short for "concatenate and reassign". It works on both strings and lists:

```python
s = "foo"
s += "bar"      # same as: s = s + "bar"
print(s)        # "foobar"

lst = [1, 2, 3]
lst += [4, 5]   # same as: lst = lst + [4, 5]
print(lst)      # [1, 2, 3, 4, 5]
```

> **Strings vs. lists with `+=`:** For strings, `+=` always creates a new string (because strings are immutable). For lists, Python is smarter — `lst += [...]` actually extends the list **in place** rather than creating a new one. The end result looks the same, but internally no copy is made. This is equivalent to calling `lst.extend([...])`.

### Concatenation is not insertion

`+` always appends the entire second sequence at the end. If you need to insert in the middle, that is `lst.insert(i, x)`, not concatenation.

---

## 7. Search with `in`

The `in` operator tests whether something exists inside a sequence. It returns `True` or `False`.

```python
result = value in sequence
```

`not in` is the negation:

```python
result = value not in sequence
```

### Strings: substring search

For strings, `in` checks whether one string appears **anywhere inside** another — it is a substring match, not a single-character match.

```python
s = "hello world"

print("hello" in s)     # True   ← "hello" is a substring
print("ell" in s)       # True   ← multi-character substring
print("xyz" in s)       # False  ← not present
print("o w" in s)       # True   ← spaces count, it's just a substring

print("xyz" not in s)   # True
```

The substring can be any length — one character, several characters, or even the full string.

### Lists: exact element search

For lists, `in` checks whether a value is **exactly one of the elements**. It does not look inside elements.

```python
lst = ["hello", "world", "foo"]

print("hello" in lst)   # True   ← exact match with an element
print("he" in lst)      # False  ← "he" is not an element (even though it's inside "hello")
print("xyz" in lst)     # False

print("xyz" not in lst) # True
```

### The critical difference

This is one of the most common beginner mistakes:

```python
s   = "hello"
lst = ["hello"]

print("he" in s)     # True   ← string: "he" is a substring of "hello"
print("he" in lst)   # False  ← list: "he" is not an element of the list
```

**String `in`** = "does this text appear anywhere inside?"
**List `in`** = "is this value one of the items in the list?"

### Using `in` in conditions

`in` is most useful inside `if` statements:

```python
# Check if a word appears in a sentence
sentence = "the quick brown fox"
if "fox" in sentence:
    print("fox found")

# Check if a value is in a list of valid options
valid_commands = ["start", "stop", "restart"]
cmd = input("Enter command: ")
if cmd not in valid_commands:
    print("Unknown command")
```

---

## 8. String Methods: `split()`

`split()` is one of the most important tools for working with real-world text data. It takes a string and **chops it up** into a list of smaller strings based on a separator.

### Default behavior: split on whitespace

```python
s = "hello world foo"
parts = s.split()
print(parts)    # ['hello', 'world', 'foo']
```

`split()` without arguments:
- Splits on any whitespace (spaces, tabs, newlines)
- Automatically removes leading/trailing whitespace
- Consecutive spaces are treated as one separator
- Returns a **list of strings**

### Split on a specific delimiter

Pass any string as the separator:

```python
ip = "192.168.1.23"
parts = ip.split('.')
print(parts)    # ['192', '168', '1', '23']

line = "Alice,30,Engineer"
fields = line.split(',')
print(fields)   # ['Alice', '30', 'Engineer']
```

### Practical use: parsing input

If your program receives three numbers on one line separated by spaces:

```python
line = input()        # user types: "3 4 5"
parts = line.split()  # ['3', '4', '5']

# convert to integers
numbers = []
for x in parts:
    numbers.append(int(x))

print(numbers)   # [3, 4, 5]
```

### Practical use: parsing log files and IP addresses

Log files are designed to be parsed. They usually follow a predictable format — fields separated by spaces, commas, or tabs. `split()` handles this directly:

```python
log_entry = "192.168.1.10 GET /index.html 200"
fields = log_entry.split()
ip       = fields[0]   # "192.168.1.10"
method   = fields[1]   # "GET"
path     = fields[2]   # "/index.html"
status   = fields[3]   # "200"
```

For IP addresses, split on `'.'` to get individual octets:

```python
ip = "192.168.1.23"
octets = ip.split('.')
last_two = octets[-2:]   # ['1', '23']
```

### Combining split() with strip()

Sometimes parsed pieces still have surrounding whitespace. `strip()` removes it:

```python
s = "  hello  "
print(s.strip())    # "hello"

# Common pattern: split then strip each piece
line = " Alice , 30 , Engineer "
fields = [f.strip() for f in line.split(',')]
print(fields)    # ['Alice', '30', 'Engineer']
```

---

## 9. String Methods: `join()`

`join()` is the **inverse of `split()`**: given a list of strings, it glues them together into a single string.

### Syntax

```python
separator.join(list_of_strings)
```

The separator string is what gets inserted **between** each element.

```python
words = ['hello', 'I', 'like', 'apples']

result = ' '.join(words)     # join with a space
print(result)                # "hello I like apples"

result = '_'.join(words)     # join with underscore
print(result)                # "hello_I_like_apples"

result = ', '.join(words)    # join with comma-space
print(result)                # "hello, I, like, apples"

result = ''.join(words)      # join with nothing
print(result)                # "helloIlikeapples"
```

### The syntax looks backwards

The call is made on the **separator** (a string), not on the list. This is unintuitive. The way to read it:

> *"Use this separator to join these items."*

```python
"-".join(['a', 'b', 'c'])   →   "a-b-c"
```

### Typical use: round-trip with split()

```python
s = "hello world foo"
parts = s.split()            # ['hello', 'world', 'foo']
rejoined = ' '.join(parts)   # "hello world foo"
print(rejoined == s)         # True
```

### Practical use: building output from parts

```python
ip_parts = ['192', '168', '1', '23']
ip = '.'.join(ip_parts)
print(ip)    # "192.168.1.23"
```

> `join()` only works with lists of **strings**. If your list contains integers or other types, convert them first:
>
> ```python
> nums = [1, 2, 3]
> result = ','.join(str(n) for n in nums)   # "1,2,3"
> ```

---

## 10. Strings vs. Lists — Side-by-Side Comparison

| Feature | String | List |
|---------|--------|------|
| What it stores | Characters only | Any values |
| Mutable? | **No** — read only | **Yes** — read and write |
| Index access | `s[i]` ✓ | `lst[i]` ✓ |
| Change element | `s[i] = x` ✗ ERROR | `lst[i] = x` ✓ |
| Slicing | `s[a:b:step]` ✓ | `lst[a:b:step]` ✓ |
| Concatenate with `+` | ✓ (new string) | ✓ (new list) |
| `len()` | ✓ | ✓ |
| Iterate with `for` | ✓ (yields chars) | ✓ (yields elements) |
| `in` search | ✓ (substring match) | ✓ (element match) |
| Append/pop | ✗ not supported | ✓ |
| Sort in place (`lst.sort()` modifies the list directly) | ✗ | ✓ |

### Code example: similarities

Both support indexing, `len()`, iteration, and `in`:

```python
s = "hello"
lst = ['h', 'e', 'l', 'l', 'o']

# Indexing
print(s[1])      # 'e'
print(lst[1])    # 'e'

# Length
print(len(s))    # 5
print(len(lst))  # 5

# Membership test
print('e' in s)       # True
print('e' in lst)     # True

# Iteration (covered in the for-loops note)
for ch in s:   print(ch)    # h e l l o
for x in lst:  print(x)     # h e l l o
```

### Code example: key difference (mutability)

```python
s = "hello"
lst = ['h', 'e', 'l', 'l', 'o']

# Strings — cannot modify in place
s[0] = 'H'        # TypeError!
s = 'H' + s[1:]   # must create a new string: "Hello"

# Lists — can modify in place
lst[0] = 'H'      # OK: ['H', 'e', 'l', 'l', 'o']

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
```
