
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Hash Tables (Dictionaries)

## Table of Contents
1. [Why Hash Tables?](#1-why-hash-tables)
2. [The Hash Function](#2-the-hash-function)
3. [Collisions](#3-collisions)
4. [Collision Resolution — Chaining](#4-collision-resolution--chaining)
5. [Python Dictionaries](#5-python-dictionaries)
6. [Dictionaries as Records](#6-dictionaries-as-records)
7. [Working with Dictionaries](#7-working-with-dictionaries)
8. [Counting with a Dictionary](#8-counting-with-a-dictionary)
9. [Nested Dictionaries — A Mini Database](#9-nested-dictionaries--a-mini-database)
10. [Performance: `in` on a Dict vs. a List](#10-performance-in-on-a-dict-vs-a-list)
11. [Summary](#11-summary)

---

## 1. Why Hash Tables?

In the previous lecture we used arrays as **lookup tables** — data is stored at a numbered slot and retrieved instantly by its index. This is extremely fast, but it has real limitations:

| Restriction | Why it matters |
|---|---|
| Index must be an integer | You can't look up a student by name |
| Index must fit within the array size | You can't use arbitrary large numbers |
| You must memorize the index | Nobody remembers "student 48291" — they remember "Joe" |

The goal of a hash table is to **keep the speed of array lookup while letting you use any data as a key** — a name, a product ID, even an image.

---

## 2. The Hash Function

The central idea: write a function that takes any data and **deterministically** converts it into an integer index — given the same input, it always produces the same output.

```
data  →  hash function  →  integer  →  modulus  →  index
```

**Example with the string `"joe"`:**

| Character | ASCII value |
|---|---|
| j | 106 |
| o | 111 |
| e | 101 |
| **Sum** | **318** |

Array size is 7:

```
318 % 7 = 3
```

So `"joe"` maps to index 3. Every time — this is *deterministic*. The same input always produces the same index.

### Why the sum-of-characters approach is not good enough

This simple function is only used here to illustrate the concept. It breaks down quickly:

- `"joe"` and `"oje"` both sum to 318 → same hash value, same index.
- `"l"` has ASCII value 108 → 108 % 7 = 3 → same index as joe, even though the hash value is different.

Real hash functions such as **djb2** are designed to spread values out much more evenly:

```python
def djb2(s):
    hash_value = 5381
    for ch in s:
        hash_value = hash_value * 33 + ord(ch)
    return hash_value

index = djb2(string) % array_size
```

Cryptographic functions like **SHA-256** go further — collisions are so rare they are considered practically impossible. These are used for security (encryption, data integrity), not typically for hash tables, but they share the same core idea.

---

## 3. Collisions

A **collision** happens when two different keys are assigned the same index. There are two ways this can occur:

**Type 1 — Hash value collision:** The hash function produces the same integer for two different inputs.
- `"joe"` → 318
- `"oje"` → 318 (same letters, different order)

**Type 2 — Index collision:** Two different hash values map to the same index after the modulus step.
- `"joe"` → 318 → 318 % 7 = **3**
- `"l"` → 108 → 108 % 7 = **3**

Collisions are unavoidable — any array of finite size will eventually have them. A good hash function minimizes Type 1; a larger array (relative to the number of stored entries) reduces the probability of Type 2.

---

## 4. Collision Resolution — Chaining

The most straightforward strategy is called **chaining**: instead of storing a single value at each index, store a *list* of all entries that collide there.

**Example:** `"joe"`, `"oje"`, and `"l"` all collide at index 3. `"alice"` does not collide.

```
Index 0: [ ]
Index 1: [ ]
Index 2: [ ]
Index 3: [ ("joe", data_joe), ("oje", data_oje), ("l", data_l) ]
Index 4: [ ("alice", data_alice) ]
Index 5: [ ]
Index 6: [ ]
```

**Lookup for `"joe"`:**
1. Run `"joe"` through the hash function → index 3. *(one step — O(1))*
2. Go to index 3 and search the short list for `"joe"`. *(small linear search)*

The list at each index stays short — either because the array is large enough that collisions are rare, or because each slot accumulates only a small number of entries. Either way, the linear search within the chain is negligible.

Lookup is **O(1) — constant time**: the cost does not grow with the number of entries in the table.

---

## 5. Python Dictionaries

Python implements a hash table for you — it is called a **dictionary** (`dict`). You never manage the array, hash function, or collision resolution yourself.

### Creating a dictionary

**Empty dictionary, then populate:**

```python
phone_book = {}
phone_book["alice"] = "555-1234"
phone_book["bob"]   = "555-5678"
phone_book["carol"] = "555-9012"
```

**Pre-populated literal:**

```python
phone_book = {
    "alice": "555-1234",
    "bob":   "555-5678",
    "carol": "555-9012"
}
```

Both are equivalent. Choose whichever fits your situation.

### Reading a value

```python
print(phone_book["alice"])   # "555-1234"
print(phone_book["bob"])     # "555-5678"
```

Behind the scenes, Python runs `"alice"` through a hash function, finds the index, and returns the value instantly.

### Overwriting a value

```python
phone_book["alice"] = "555-9999"   # alice changed her number
```

Using the same key always points to the same slot — the old value is replaced. This is different from a list's `.append()`, which adds a new entry.

---

## 6. Dictionaries as Records

A dictionary can also compound multiple attributes of a single entity into one structure. Each key is a field name; the value is that field's data.

```python
student = {
    "name":   "joe",
    "ssn":    "123-45-6789",
    "grades": [88, 92, 75]
}

print(student["name"])     # "joe"
print(student["grades"])   # [88, 92, 75]
```

> **Note:** This is a different use pattern from a lookup table — here the keys are field names, not identifiers you search by. You are grouping the components of a single object rather than mapping many keys to values.

---

## 7. Working with Dictionaries

### Checking if a key exists — the `in` operator

Before reading a key, you may need to confirm it exists:

```python
if "alice" in phone_book:
    print(phone_book["alice"])
```

> **Important:** Trying to read a key that was never assigned raises a `KeyError`. Always check first, or use `.get()`.

### Safe access with `.get(key, default)`

```python
value = phone_book.get("dave", "N/A")   # returns "N/A" if "dave" is not in the dict
```

This is a clean alternative to the `if key in dict` pattern when you just want a fallback value.

### Deleting a key

```python
del phone_book["carol"]
```

---

## 8. Counting with a Dictionary

One of the most common uses of dictionaries is **counting occurrences** of items.

```python
cart = ["apple", "orange", "apple", "tv", "apple", "tv"]
```

**Goal:** count how many of each item appear in the cart.

### Approach 1 — explicit check

```python
counter = {}

for item in cart:
    if item in counter:         # already seen before — increment
        counter[item] += 1
    else:                       # first time seeing this item
        counter[item] = 1

print(counter)
# {"apple": 3, "orange": 1, "tv": 2}
```

**Why the check is necessary:** If `"apple"` has never been added to `counter`, then `counter["apple"]` raises a `KeyError`. You must initialize the entry before you can increment it.

### Approach 2 — `.get()` shortcut

```python
counter = {}

for item in cart:
    counter[item] = counter.get(item, 0) + 1
```

`counter.get(item, 0)` returns the current count if the key exists, or `0` if it does not. Adding 1 and storing it back handles both the first occurrence and all subsequent ones in one line.

Both approaches produce identical results. The `.get()` version is more concise.

---

## 9. Nested Dictionaries — A Mini Database

Dictionaries can hold any value — including other dictionaries or lists. This lets you build structured records:

```python
student_db = {
    "joe": {
        "address": "123 Main St",
        "ssn": "123-45-6789",
        "grades": [88, 92, 75, 100]
    },
    "alice": {
        "address": "456 Elm St",
        "ssn": "987-65-4321",
        "grades": [95, 87, 91, 78]
    }
}
```

**Accessing nested data:**

```python
student_db["joe"]["ssn"]          # "123-45-6789"
student_db["alice"]["grades"][2]  # 91  (Alice's 3rd grade, 0-indexed)
```

> This format is also the **JSON format** — Python dict syntax and JSON are essentially identical. When you read a JSON file in Python, you get a Python dictionary directly.

---

## 10. Performance: `in` on a Dict vs. a List

| Structure | `"alice" in x` | Why |
|---|---|---|
| `list` | **O(n)** — slow | Must check every element one by one |
| `dict` | **O(1)** — instant | Runs a hash function → jumps directly to the slot |

This difference matters a lot with large datasets. If you are checking membership frequently, always prefer a dictionary (or set) over a list.

---

## 11. Summary

| Concept | Key point |
|---|---|
| Hash function | Converts any data to an integer, then `% array_size` gives an index |
| Deterministic | Same key always produces the same index |
| Collision | Two keys land on the same index — unavoidable but manageable |
| Chaining | Store a small list at each slot; search within it to resolve collisions |
| Python `dict` | Built-in hash table — use string (or other) keys, O(1) access |
| `in` operator | O(1) for dicts; O(n) for lists — use dicts for membership tests |
| `.get(k, default)` | Safe read — returns default if key is absent instead of raising an error |
| Overwrite | Assigning to an existing key replaces the value |
| Nested dicts | Dicts can contain other dicts or lists — use for structured records |
| Dict as record | Keys are field names, values are attributes of a single entity |

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
