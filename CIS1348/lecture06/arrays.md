
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Arrays

## Table of Contents

1. [What Is an Array?](#1-what-is-an-array)
2. [Indexing: Accessing Elements by Offset](#2-indexing-accessing-elements-by-offset)
3. [Array Operations](#3-array-operations)
   - [Initialize](#initialize)
   - [Duplicate](#duplicate)
   - [Sub-array and Subsequence](#sub-array-and-subsequence)
   - [Filter](#filter)
   - [Merge / Combine](#merge--combine)
   - [Resize](#resize)
   - [Search (Linear Search)](#search-linear-search)
   - [Swap](#swap)
   - [Sort](#sort)
   - [Comparison](#comparison)
   - [Reverse](#reverse)
   - [Push and Pop](#push-and-pop)
   - [Insert and Delete](#insert-and-delete)
4. [The Stack](#4-the-stack)
5. [Queue and Linked List (Conceptual Overview)](#5-queue-and-linked-list-conceptual-overview)
6. [Why Array Internals Matter](#6-why-array-internals-matter)
7. [Low-Level Code Examples](#7-low-level-code-examples)

---

## 1. What Is an Array?

An array is the most fundamental data structure in computing. Everything else is built on top of it.

**Definition:** An array is a **fixed-size block of memory** made up of **fixed-size cells**, all laid out **consecutively** — one right after another — in memory.

```
Memory:  [ 42 ][ 17 ][ 8  ][ x ][ x ]
Index:      0     1    2     3     4
```

Three things define an array:

| Property | What it means |
|----------|---------------|
| **Fixed size** | Once created, the number of cells cannot change |
| **Consecutive layout** | Cells are side-by-side in memory, no gaps |
| **Single reference** | A variable like `a` points only to the *start* of the block |
| **Same size and type** | Every cell holds the same kind of data and occupies the same amount of memory |

> **Important:** No one automatically tracks the array's size or manages its contents — that responsibility falls on you, the programmer. You must remember how large the array is and how many cells you are actually using.

### Why is consecutive layout significant?

Because the cells are guaranteed to be side-by-side, the computer can jump to any element in one step using math. This makes arrays extremely fast.

### Why do we use arrays? A real-world example

Think of a game where 100,000 bullets are flying on screen at once. Each bullet has a position, a velocity, a mass. All those values are stored in arrays — one array for positions, one for velocities, and so on.

Why? Because you need to process all of them every frame. With arrays, you don't have to go hunting for each bullet individually. You just walk through the array from start to end and process them all in one sweep. You put things in a bag so you can go process them all at once. That is the fundamental reason arrays exist.

### What about arrays that can't fit consecutively in memory?

If there is no large enough consecutive block available, you simply cannot create that array. Memory fragmentation is a real concern in systems programming. You could design a different data structure that stores chunks in separate places and links them together — but at that point you are no longer talking about a simple array.

---

## 2. Indexing: Accessing Elements by Offset

An array is created by allocating a fixed block of memory. The variable `a` holds a reference to the start of that block:

```c
// C language — in most contexts, 'a' behaves as the address of the first cell
int a[5] = {4,2,3,1,5};
```

```
a == 0x1A3F  (some address in memory)
              ↓
          [4][2][3][1][5]
         0x1A3F ...
```

`a` is just a number — a memory address. It tells the computer where the block begins. In C and most lower-level languages, this is explicit: `a` holds an address, and `a[2]` means "go to address `a`, jump 2 cells forward." There is no object, no wrapper — just a location in memory.

The only reference you have to an array is the variable that points to its **beginning**. So how do you reach element 3, or element 100?

You use an **offset** — you tell the computer: *start at the beginning of the array and jump forward by this many cells*.

```
a[0]   # jump 0 cells → first element
a[1]   # jump 1 cell  → second element
a[3]   # jump 3 cells → fourth element
```

This is why **array indexing starts at 0**, not 1. Index `0` means "zero hops from the start." It is a literal offset, not a count.

```
a[3] = 7  →  go to 'a', jump 3 cells forward, write 7 there
```

### Out-of-bounds access

An array has no built-in protection. If your array has 5 elements and you access `a[10]`, you are reading (or writing) memory that does not belong to your array.

- **Reading** out-of-bounds: returns unpredictable garbage data.
- **Writing** out-of-bounds: this is called a **buffer overflow**. It can crash your program, corrupt other data, or — intentionally — be used to hack a system. Buffer overflows are one of the most common and dangerous security vulnerabilities in software.

> "Buffer" is another name for a chunk of memory used for storing data. The term "buffer overflow" comes directly from overflowing the bounds of such a buffer.

---

## 3. Array Operations

Everything in this section can be implemented using a while loop. Understanding how these operations work at the array level is essential — even if a higher-level language hides the details from you.

### Initialize

Set every cell in the array to a known starting value. You loop through each position and assign a default (usually `0`).

---

### Duplicate

Create a new array and copy every element into it.

You loop from `0` to `size - 1` (not `size`), because the last valid index is always one less than the count.

---

### Sub-array and Subsequence

These are two different ways to extract elements from an array.

**Sub-array** — a *consecutive, unbroken block* of elements.

```
arr:      [ 1 ][ 2 ][ 3 ][ 4 ][ 5 ]
subarray:          [ 3 ][ 4 ]          ← indices 2 and 3 — contiguous
```

**Subsequence** — selected elements that do *not* have to be consecutive.

```
arr:          [ 1 ][ 2 ][ 3 ][ 4 ][ 5 ]
subsequence:  [ 1 ]       [ 3 ]       [ 5 ]   ← indices 0, 2, 4 — not contiguous
```

Practical example: if you know the position of the `@` in `levant@gmail.com`, you can use a sub-array copy to extract just the name `levant`.

---

### Filter

```
Original:  [ 1 ][ 2 ][ 3 ][ 4 ][ 5 ][ 6 ][ x ][ x ]    ← capacity=8, N=6
Keep only even numbers:
Result:    [ 2 ][ 4 ][ 6 ][ x ][ x ][ x ][ x ][ x ]    ← capacity=8, N=3  (pre-allocated worst-case)
```

Walk through the array and copy only the elements that satisfy a condition into a new array. The result is a subsequence.

Practical use: scan a log file for all HTTP 404 responses. For each line, check the status code — if it matches, push it into your result array.

---

### Merge / Combine

```
arr1:   [ 1 ][ 2 ][ 3 ][ x ][ x ]         ← capacity=5, N=3
arr2:   [ 4 ][ 5 ][ x ][ x ]              ← capacity=4, N=2
result: [ 1 ][ 2 ][ 3 ][ 4 ][ 5 ]        ← capacity=5, N=5  (allocated exactly N1+N2)
```

You cannot extend an existing array (its size is fixed). To combine two arrays, allocate a new array large enough to hold both, then copy each one in.

---

### Resize

```
Before:  [ 42 ][ 17 ][  8 ][ x ][ x ]                              ← capacity=5, N=3
After:   [ 42 ][ 17 ][  8 ][ x ][ x ][ x ][ x ][ x ][ x ][ x ]   ← capacity=10, N=3
N stays 3 — no data was lost or changed
```

An array's size cannot change after creation. But you can *simulate* resizing:

1. Allocate a new, larger array.
2. Copy all elements from the old array into the new one.
3. Move your variable (reference) to point at the new array.

From your perspective, it looks like the array grew. Under the hood, it was replaced.

---

### Search (Linear Search)

```
arr:  [  7 ][ 14 ][  3 ][  9 ][ 21 ]    ← N=5
Search for 9:
  i=0:  7 ≠ 9
  i=1: 14 ≠ 9
  i=2:  3 ≠ 9
  i=3:  9 = 9  ← found at index 3
```

**Two distinct situations:** If you already know the *index*, you can jump straight to it — `arr[i]` — in O(1), no loop needed. Search is only necessary when you have a *value* and need to find *where* it lives. Never search when you already have the index.

To find a value in an unsorted array, there is only one option: visit every element one by one and check.

This is called **linear search** because it runs through the array in a straight line. It is O(n) — in the worst case, you check every element.

> **The `i` naming convention:** The variable `i` has a special meaning in programming. It stands for *index*. You should only name a variable `i` when it genuinely represents the index of an array. Do not use `i` as a generic counter for unrelated counting.

---

### Swap

Exchange two elements by their indices. This is a fundamental building block for sorting, shuffling, and partitioning algorithms.

---

### Sort

```
[ 3 ][ 1 ][ 2 ]   ← unsorted
swap(0,1) → [ 1 ][ 3 ][ 2 ]
swap(1,2) → [ 1 ][ 2 ][ 3 ]   ← sorted
```

A sort is just a sequence of targeted swaps until all elements are in order.

Sorting rearranges the elements of the array into order. The implementation is out of scope for this course, but understanding that sorting *is possible* — and that it unlocks many other algorithms — is essential.

Once an array is sorted, operations like search can be done much faster (e.g., binary search). Spending the "electricity bill" to sort once pays off repeatedly.

---

### Comparison

Check whether two arrays contain identical elements.

You can extend this idea: searching for a sub-array *inside* a larger array is how **substring matching** works. For example, checking if the word "today" appears inside a sentence is exactly the same operation — you are looking for a small array of characters inside a larger array of characters.

```
Haystack:  [ h ][ e ][ l ][ l ][ o ][ w ][ o ][ r ][ l ][ d ]    N=10
Needle:    [ w ][ o ][ r ]                                         N=3

Check at index 0: [ h ][ e ][ l ] ≠ [ w ][ o ][ r ]
Check at index 1: [ e ][ l ][ l ] ≠ [ w ][ o ][ r ]
...
Check at index 5: [ w ][ o ][ r ] = [ w ][ o ][ r ]  ← match found at index 5
```

You can take this even further with **subsequence matching**: checking whether a pattern appears *in order but not necessarily consecutively* within a larger sequence.

```
Array:    [ a ][ b ][ c ][ d ][ e ]    N=5
Pattern:  [ a ][ c ][ e ]             N=3

Walk the array, match pattern characters in order (gaps are fine):
  index 0: a = a ✓  (advance pattern pointer)
  index 1: b ≠ c    (skip)
  index 2: c = c ✓  (advance pattern pointer)
  index 3: d ≠ e    (skip)
  index 4: e = e ✓  (advance pattern pointer)
  → all pattern characters matched in order: "ace" IS a subsequence of "abcde"
```

A subsequence allows gaps — the characters must appear in the same order, but they do not have to be adjacent.

---

### Reverse

Reverse the array in place by swapping elements from both ends, working inward.

---

### Push and Pop

When you create an array, it has empty (garbage-filled or zero) cells. You need a way to add things to it in an orderly way.

The natural approach: start from the beginning, fill cells from left to right, and track how many cells you have actually filled using a variable `N`.

```
Capacity = 5:   [ x ][ x ][ x ][ x ][ x ]    ← N = 0 (nothing yet)
After push 42:  [ 42 ][ x ][ x ][ x ][ x ]    ← N = 1
After push 17:  [ 42 ][ 17 ][ x ][ x ][ x ]    ← N = 2
After push 8:   [ 42 ][ 17 ][  8 ][ x ][ x ]    ← N = 3
```

**Push** — add an element to the end of the used portion. Place it at index `N`, then increment `N`. This is O(1) — the time it takes does not depend on how many elements are already in the array.

**Pop** — remove the last element. Decrement `N`. The data at the old position is still physically in memory, but it is now *outside* the valid range and will be overwritten the next time you push.

```
Before pop:  [ 42 ][ 17 ][  8 ][ x ][ x ]    ← N = 3
After pop:   [ 42 ][ 17 ][ x ][ x ][ x ]    ← N = 2  (8 still in memory at index 2, but ignored)
```

> **Key insight:** Nothing is ever truly deleted from memory. "Deleting" in computing means marking something as "I don't care about this anymore." The data stays until something new overwrites it. This is why a data-recovery service can sometimes retrieve files you thought you deleted — the bytes are still there, just without a label.

---

### Insert and Delete

These are **not natural** operations for arrays. They work, but they are expensive.

**Insert at position k** — to make room, every element from position k onward must shift one step to the right.

```
Before:  [ 1 ][ 3 ][ 4 ][ 6 ][ x ]    N = 4
Insert 5 at index 2:
After:   [ 1 ][ 3 ][ 5 ][ 4 ][ 6 ]    N = 5
```

**Delete at position k** — to close the gap, every element after k must shift one step to the left.

```
Before:  [ 1 ][ 3 ][ 4 ][ 6 ]    N = 4
Delete index 2 (the 4):
After:   [ 1 ][ 3 ][ 6 ][ x ]    N = 3   (last cell still holds 6 in memory, but ignored)
```

> After deletion, the last cell still holds the old value in memory. But `N` is decremented, so that cell is no longer considered part of the array. It will be overwritten naturally the next time something is pushed.

**Why this is expensive:** If you have 1,000,000 elements and insert at index 0, you must shift every single one of them. For large arrays, use a different data structure.

#### O(1) Delete: Last-Element Replacement

When the *order of elements does not matter*, you can delete in O(1):

1. Copy the last element into the slot being deleted.
2. Decrement N.

```
Before:  [ 1 ][ 3 ][ 4 ][ 6 ][ 9 ]    capacity=5, N=5
Delete index 1 (value 3) — copy last element (9) to index 1:
After:   [ 1 ][ 9 ][ 4 ][ 6 ][ x ]    capacity=5, N=4
```

> The value `9` is still physically sitting in memory at the last position — it was not erased. It just falls outside `N` now and will be overwritten the next time something is pushed there.

**Important caveat:** This changes the order of the remaining elements. Only use this when order is not significant.

**Real-world example:** A game renders 1,000,000 bullets on screen. When a bullet hits a wall, you need to remove it from the array. Using the O(n) shift-delete, removing bullets every frame across a million-element array would grind the game to a halt. Since bullets have no required order, copying the last element to the deleted slot and decrementing N removes any bullet in O(1) — no matter how many bullets are active.

---

## 4. The Stack

**Push** and **pop** together define a specific access pattern: you always add to the end and remove from the end. This pattern is so common and useful that it has its own name: the **stack**.

Think of it as a stack of plates in your kitchen:
- **Push** = place a plate on top of the stack
- **Pop** = take the top plate off

The rule is: **last in, first out (LIFO)**.

```
Push 1  →  [ 1 ]
Push 2  →  [ 1 ][ 2 ]
Push 3  →  [ 1 ][ 2 ][ 3 ]
Pop     →  [ 1 ][ 2 ]        (3 was removed)
Pop     →  [ 1 ]             (2 was removed)
```

### Why the stack is useful: a real example

Imagine you are a mouse navigating a maze. You want to explore every path without getting lost. Every time you move, you push your direction onto a stack. When you hit a dead end, you pop moves off the stack — retracing your steps — until you find a new path to explore.

This idea (explore, push moves; backtrack, pop moves) is the basis of **depth-first search**, used in countless real algorithms: file system traversal, game AI, circuit routing, and more.

### Stack overflow

Every stack has a limit. If you try to push more than the underlying array can hold, that is a **stack overflow**.

This is not just a theoretical concept — your computer uses a stack internally every time your code runs. Every time you call a function, a new frame is pushed onto the call stack (local variables, return address, etc.). When the function returns, the frame is popped. If you call functions recursively without a base case, the stack keeps growing until it reaches the array bounds and overflows.

---

## 5. Queue and Linked List (Conceptual Overview)

All data structures can be built from arrays. This section briefly covers two more — just enough to understand what they are and how they differ from the stack.

### Queue

A stack is **LIFO** (last in, first out). A queue is the opposite: **FIFO** (first in, first out).

Think of a line of people waiting at a desk. The first person to arrive is the first to be served. The last person to arrive waits until everyone ahead of them is done. That is a queue.

| | Stack | Queue |
|--|-------|-------|
| Add item | push to end | append to end |
| Remove item | pop from end | remove from **front** |
| Order | Last in, first out (LIFO) | First in, first out (FIFO) |

**How to implement a queue with an array:**

You still append new items to the end — same as always. The difference is in removal. Instead of popping from the end, you track where the *front* of the queue is using a separate index (the "head"). When you process the next item, you read from the head position and advance the head forward by one.

```
Array:  [ Alice ][ Bob ][ Carol ][      ]
Head ──→ 0 (Alice is next to be processed)

After processing Alice:
Array:  [ Alice ][ Bob ][ Carol ][      ]
Head ──→ 1 (Bob is next)

After processing Bob:
Array:  [ Alice ][ Bob ][ Carol ][      ]
Head ──→ 2 (Carol is next)
```

The old positions (before the head) are abandoned — no shifting required. When the end of the array is reached, a circular implementation can wrap the head back around to reuse space at the front.

---

### Linked List

An array stores elements **side by side** in memory. A linked list is a completely different layout: each element (called a **node**) can be anywhere in memory, and each node holds a **pointer** (a reference or index) to the location of the next node.

```
Array layout:   [  1  ][  2  ][  3  ][  4  ]    ← all consecutive

Linked list:    [ 1 |→]  ...  [ 2 |→]  ...  [ 3 |→]  ...  [ 4 |∅]
                  ↑ pointer to next             ↑ null = end of list
```

You can simulate this with an array where each cell stores both a value and an index pointing to the next item:

```
Index:   0     1     2     3
Value: [ 1 ] [ 3 ] [ 2 ] [ 4 ]
Next:  [ 2 ] [ 3 ] [ 1 ] [-1 ]   ← -1 means "no next" (end of list)

Following the chain from index 0: 0 → 2 → 1 → 3  gives values: 1, 2, 3, 4
```

**The key advantage of linked lists: cheap insert and delete.**

In an array, inserting at position k requires shifting every element after k one step to the right — O(n) for a million-element array. In a linked list, you just break the link between the previous node and the next, insert the new node in between, and re-link. No shifting at all.

```
Array insert (expensive):   [ 1 ][ 2 ][ 3 ] → shift to insert 4 between 1 and 2
                            [ 1 ][ 4 ][ 2 ][ 3 ]   (1M elements shifted)

Linked list insert (cheap): 1 → 2 → 3
                            break link between 1 and 2, insert 4:
                            1 → 4 → 2 → 3   (only two links changed)
```

Linked lists are not covered in this course, but knowing they exist — and why — gives you a sense of how different design choices lead to different performance trade-offs.

---

## 6. Why Array Internals Matter

Higher-level languages hide all of this from you. You never have to allocate memory, track size, shift elements manually, or manage references. The language does it for you.

But there is a cost: **if you only learn a high-level language, you will not understand why certain operations are slow.**

Example: Imagine you work at a company with 1,000,000 user records in a list, and you need to insert a new VIP user at position 0. In Python, this is one line: `users.insert(0, new_user)`. It looks instant. But under the hood, every one of those 1,000,000 records just shifted one position to the right.

If you understand arrays, you recognize the problem immediately. If you only know the syntax, you might not even know there was a problem until your server starts timing out.

> Understanding the array is what separates a programmer who writes *working* code from one who writes *fast* code.

---

## 7. Low-Level Code Examples

These examples simulate a raw array using a fixed-size list. No built-in methods are used — only indexing and while loops. This is how arrays actually work at the machine level.

### Setup

```python
CAPACITY = 10
arr = [0] * CAPACITY   # fixed-size block, all zeros
N = 0                  # how many cells are actually in use
```

### Initialize

```python
i = 0
while i < CAPACITY:
    arr[i] = -1 # initialize to -1
    i += 1
```

### Push

```python
def push(arr, N, value):
    arr[N] = value
    N += 1
    return N

N = push(arr, N, 42)
N = push(arr, N, 17)
N = push(arr, N, 8)
# arr = [42, 17, 8, 0, 0, 0, 0, 0, 0, 0], N = 3
```

### Pop

```python
def pop(arr, N):
    N -= 1
    value = arr[N]
    return N, value

N, val = pop(arr, N)
# val = 8, N = 2  (the 8 is still in arr[2] in memory, but ignored)
```

### Search

```python
def search(arr, N, target):
    i = 0
    while i < N:
        if arr[i] == target:
            return i
        i += 1
    return -1

pos = search(arr, N, 17)   # returns 1
pos = search(arr, N, 99)   # returns -1
```

### Swap

```python
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
```

### Duplicate

```python
def duplicate(arr, N):
    new_arr = [0] * N
    i = 0
    while i < N:
        new_arr[i] = arr[i]
        i += 1
    return new_arr
```

### Sub-array

```python
def subarray(arr, a, b):
    new_size = b - a
    new_arr = [0] * new_size
    i = 0
    while i < new_size:
        new_arr[i] = arr[a + i]
        i += 1
    return new_arr, new_size
```

### Filter

```python
def filter_evens(arr, N):
    result = [0] * N     # worst case: all elements pass
    result_size = 0
    i = 0
    while i < N:
        if arr[i] % 2 == 0:
            result[result_size] = arr[i]
            result_size += 1
        i += 1
    return result, result_size
```

### Concatenate

```python
def concatenate(arr1, size1, arr2, size2):
    new_arr = [0] * (size1 + size2)
    i = 0
    while i < size1:
        new_arr[i] = arr1[i]
        i += 1
    j = 0
    while j < size2:
        new_arr[size1 + j] = arr2[j]
        j += 1
    return new_arr, size1 + size2
```

### Resize

```python
def resize(arr, N, new_capacity):
    new_arr = [0] * new_capacity
    i = 0
    while i < N:
        new_arr[i] = arr[i]
        i += 1
    return new_arr

# arr = resize(arr, N, CAPACITY * 2)
```

### Comparison

```python
def arrays_equal(arr1, size1, arr2, size2):
    if size1 != size2:
        return False
    i = 0
    while i < size1:
        if arr1[i] != arr2[i]:
            return False
        i += 1
    return True
```

### Reverse

```python
def reverse(arr, N):
    left = 0
    right = N - 1
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
```

### Insert at Position k

```python
def insert_at(arr, N, k, value):
    i = N - 1
    while i >= k:
        arr[i + 1] = arr[i]
        i -= 1
    arr[k] = value
    N += 1
    return N

# arr = [42, 17, ...], N = 2
N = insert_at(arr, N, 1, 99)
# arr = [42, 99, 17, ...], N = 3
```

### Delete at Position k

```python
def delete_at(arr, N, k):
    i = k
    while i < N - 1:
        arr[i] = arr[i + 1]
        i += 1
    N -= 1
    return N

# arr = [42, 99, 17, ...], N = 3
N = delete_at(arr, N, 1)
# arr = [42, 17, ...], N = 2  (old arr[2] still says 17 in memory)
```

### Delete at Position k — O(1) Last-Element Replacement

```python
def delete_fast(arr, N, k):
    arr[k] = arr[N - 1]   # copy last element into the deleted slot
    N -= 1
    return N

# arr = [1, 3, 4, 6, 9], N = 5
N = delete_fast(arr, N, 1)
# arr = [1, 9, 4, 6, 9], N = 4  (9 still in memory at index 4, but ignored)
# order changed — use only when order does not matter
```

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
