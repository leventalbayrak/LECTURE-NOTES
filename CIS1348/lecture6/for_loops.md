
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# For Loops

## Table of Contents

1. [The Problem: While Loops Are Verbose](#1-the-problem-while-loops-are-verbose)
2. [The For Loop as a Shortcut](#2-the-for-loop-as-a-shortcut)
3. [How It Works: The Iterator Concept](#3-how-it-works-the-iterator-concept)
4. [Form 1 — Iterate Over Elements](#4-form-1--iterate-over-elements)
5. [Form 2 — Iterate Over Indices with `range()`](#5-form-2--iterate-over-indices-with-range)
6. [When to Use Each Form](#6-when-to-use-each-form)
7. [Examples on Lists](#7-examples-on-lists)
8. [Examples on Strings](#8-examples-on-strings)

---

## 1. The Problem: While Loops Are Verbose

You already know that to process every element of a list, you can use a `while` loop:

```python
lst = [10, 20, 30, 40, 50]

i = 0
while i < len(lst):
    print(lst[i])
    i += 1
```

This works — but every time you write it, you have to do three things manually:
1. **Initialize** the counter (`i = 0`)
2. **Write the condition** (`i < len(lst)`)
3. **Increment** the counter (`i += 1`)

Forget the increment and you get an infinite loop. Start at 1 instead of 0 and you skip the first element. Use `<=` instead of `<` and you get an index error.

Most of the time, you don't actually care about the counter `i` at all — you just want each element. There should be a shorter way.

---

## 2. The For Loop as a Shortcut

Python's `for` loop handles the counter, the condition, and the increment automatically. You only write what you actually care about.

```python
lst = [10, 20, 30, 40, 50]

for x in lst:
    print(x)
```

These two loops produce identical output. The `for` loop is not a different concept — it is a shortcut for writing the `while` loop pattern. Python expands it into the same indexing logic under the hood.

```python
# for loop                        # equivalent while loop
for x in lst:                     i = 0
    print(x)                      while i < len(lst):
                                      print(lst[i])
                                      i += 1
```

---

## 3. How It Works: The Iterator Concept

The `for` loop formula is always:

```python
for <variable> in <iterable>:
    ...
```

An **iterable** is anything that can give you one item at a time when asked. Think of it as an object you can *poke* — each poke gives you the next item, until there are no more items left.

Two common kinds of iterables:

| Kind | Example | How it works |
|------|---------|--------------|
| **Container** | A list or string | Stores values; yields them one by one |
| **Iterator object** | `range(5)` | Does not store values; calculates the next one on demand |

The `for` loop keeps poking the iterable on each pass through the loop body. When the iterable is exhausted, the loop ends.

> **`range()`** is a classic iterator: it does not create a list of numbers in memory. It just remembers where it is and calculates the next number each time it is poked. This makes `range(1000000)` just as efficient as `range(5)`.

---

## 4. Form 1 — Iterate Over Elements

Use this form when you need to **read** each element and you do not need its index.

```python
for <element_variable> in <list_or_string>:
    # use element_variable
```

The variable you name (the part before `in`) receives a *copy* of each element, one at a time.

### On a list:

```python
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry
```

### On a string:

```python
word = "hello"

for ch in word:
    print(ch)
# h
# e
# l
# l
# o
```

### Naming convention

Name the variable after what it represents — not `i`. If you are iterating over a list of fruits, call it `fruit`. If you are iterating over characters, call it `ch` or `char`. Reserve `i` exclusively for index variables.

When you do need index variables (Form 2), use `i` for the outermost loop and `j` for the inner loop in **nested loops**. If you need more variables, options include `k`, `ii`, `jj`, and so on.

```python
# Nested loop example — printing a multiplication table
for i in range(1, 4):        # outer loop: rows
    for j in range(1, 4):    # inner loop: columns
        print(i * j, end="  ")
    print()
# 1  2  3
# 2  4  6
# 3  6  9
```

### Important: the element variable is a copy

Assigning to the loop variable does **not** modify the original list:

```python
numbers = [1, 2, 3, 4, 5]

for n in numbers:
    n = n * 2       # this only changes the local copy 'n'

print(numbers)      # [1, 2, 3, 4, 5] — unchanged
```

If you want to modify the list, you need Form 2.

---

## 5. Form 2 — Iterate Over Indices with `range()`

Use this form when you need the **index** — either to modify the list in place, or when working with two lists simultaneously.

```python
for i in range(len(lst)):
    # use i as the index
    # lst[i] gives the element
```

### `range()` reference

`range()` generates a sequence of integers. It comes in three forms:

| Syntax | Generates | Example output |
|--------|-----------|---------------|
| `range(n)` | 0, 1, 2, …, n-1 | `range(5)` → 0 1 2 3 4 |
| `range(a, b)` | a, a+1, …, b-1 | `range(2, 6)` → 2 3 4 5 |
| `range(a, b, step)` | a, a+step, …, < b | `range(1, 10, 3)` → 1 4 7 |

`range(n)` maps perfectly to array indices because indices always run from `0` to `n-1`.

### On a list (modifying elements):

```python
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2   # modifies the actual list

print(numbers)   # [2, 4, 6, 8, 10]
```

### On a string (reading with index):

```python
word = "hello"

for i in range(len(word)):
    print(i, word[i])
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o
```

### Working with two lists simultaneously:

```python
names  = ['Alice', 'Bob', 'Carol']
scores = [92, 85, 78]

for i in range(len(names)):
    print(names[i], "scored", scores[i])
# Alice scored 92
# Bob scored 85
# Carol scored 78
```

---

## 6. When to Use Each Form

| I need to… | Use |
|------------|-----|
| Read each element | `for x in lst` |
| Modify elements in place | `for i in range(len(lst))` |
| Work with two lists at the same time | `for i in range(len(lst))` |
| Generate numbers (e.g., repeat N times) | `for i in range(n)` |
| Iterate over characters in a string | `for ch in s` |
| Find position of something in a string | `for i in range(len(s))` |

---

## 7. Examples on Lists

### Sum all elements

```python
numbers = [10, 20, 30, 40, 50]
total = 0

for n in numbers:
    total += n

print(total)   # 150
```

### Find the maximum value

```python
numbers = [3, 7, 1, 9, 4]
max_val = numbers[0]

for n in numbers:
    if n > max_val:
        max_val = n

print(max_val)   # 9
```

### Collect elements that meet a condition (filter)

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)

print(evens)   # [2, 4, 6, 8]
```

### Double every element in place

```python
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    numbers[i] *= 2

print(numbers)   # [2, 4, 6, 8, 10]
```

### Search for a value (linear search)

```python
values = [15, 32, 7, 48, 12, 3]
target = 48

for i in range(len(values)):
    if values[i] == target:
        print("Found at index", i)
        break
```

---

## 8. Examples on Strings

### Count vowels

```python
s = "I like apples"
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print(count)   # 5
```

### Check if a string is a palindrome

```python
s = "racecar"
is_palindrome = True

for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
        is_palindrome = False
        break

print(is_palindrome)   # True
```

### Find the index of the first uppercase letter

```python
s = "hello World"

for i in range(len(s)):
    if s[i].isupper():
        print("First uppercase at index", i)
        break
# First uppercase at index 6
```

### Build a new string (replace lowercase with uppercase)

Remember: strings are immutable. You cannot modify in place. Build a new one.

```python
s = "hello"
result = ""

for ch in s:
    result += ch.upper()

print(result)   # "HELLO"
```

### Parse split output with a for loop

A very common pattern: `split()` a line, then loop over the pieces.

```python
line = "3 14 7 2 9"
numbers = []

for token in line.split():
    numbers.append(int(token))

print(numbers)        # [3, 14, 7, 2, 9]
print(sum(numbers))   # 35
```

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
