
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Data Structures Built on Arrays — An Overview

## Table of Contents
1. [Arrays as the Foundation](#1-arrays-as-the-foundation)
2. [Lookup Tables](#2-lookup-tables)
3. [Hash Tables](#3-hash-tables)
4. [Binary Search Tree (BST)](#4-binary-search-tree-bst)
5. [Heap / Priority Queue](#5-heap--priority-queue)
6. [Disjoint Set / Union-Find](#6-disjoint-set--union-find)
7. [Segment Tree](#7-segment-tree)
8. [Comparison at a Glance](#8-comparison-at-a-glance)

---

## 1. Arrays as the Foundation

All of the data structures in this overview are built on top of a plain array. An array is just a contiguous block of memory — a row of slots, each with an integer index.

What changes between data structures is **how you use the array**: the rules you follow when inserting, reading, and organizing data inside it.

```
[  slot 0  |  slot 1  |  slot 2  |  slot 3  |  ...  ]
```

Understanding this matters: performance, memory use, and the operations each structure supports all follow from these organizational rules.

---

## 2. Lookup Tables

**What it is:** The most direct use of an array. Each slot stores a value; you access it by its integer index.

**How it works:**

```python
student_grades = [None] * 100    # 100 student slots
student_grades[42] = [88, 92, 75]  # store Joe's grades at index 42
joe_grades = student_grades[42]    # instant retrieval
```

**Use it when:** You have integer keys (IDs) and need the absolute fastest access.

**Limitations:**
- Key must be an integer within the array's bounds.
- Hard to use with natural identifiers like names.
- Requires knowing the index in advance.

**Performance:** O(1) read and write.

---

## 3. Hash Tables

**What it is:** A lookup table with a built-in conversion step — a *hash function* turns any data (strings, numbers, etc.) into an integer index.

**How it works:**

```
"Joe"  →  hash function  →  318  →  318 % 7 = 3  →  array[3]
```

Because collisions are possible (two keys mapping to the same slot), each slot holds a short list of entries. Lookups jump to the right slot instantly, then scan the short list. In practice, this scan is negligible.

In Python, hash tables are called **dictionaries** (`dict`).

**Use it when:** You want O(1) access but your keys are not convenient integers — names, product IDs, words, etc.

**Performance:** O(1) average for read, write, and membership testing.

---

## 4. Binary Search Tree (BST)

**What it is:** A data structure that organizes values in a specific order so that searching can skip large portions of the data at each step.

**How it works — the idea:**

Imagine guessing a number between 0 and 1000. Instead of guessing one-by-one, you guess 500 first. The answer is either in the lower half or the upper half — you eliminate 500 candidates in one step. Repeat on the remaining half.

```
         7
        / \
       3   10
      / \  / \
     1   5 9  14
               \
                15
```

At each node, go left if the target is smaller, right if larger. You never look at the half you eliminated.

**Array encoding:** This tree can be stored flat in an array:

| Relationship | Index formula |
|---|---|
| Left child of node at index `i` | `2 * i` |
| Right child of node at index `i` | `2 * i + 1` |

> **Note:** Index 0 is left unused. The root is placed at index 1 so the formulas `2*i` (left child) and `2*i+1` (right child) work correctly throughout the tree.

**Use it when:** You have a large sorted dataset and need fast search. Not for lookup by an arbitrary key — for *searching* when you do not know the exact location.

**Performance:** O(log n) search — 32 steps for 4 billion records.

> **Quick fact:** 2^32 = 4,294,967,296 — about 4 billion. So 32 levels of halving in a BST covers 4 billion items.
---

## 5. Heap / Priority Queue

**What it is:** An array-backed structure that always keeps the highest-priority item instantly accessible at the top, without fully sorting the array.

You could get items in minimum order by sorting the whole array once and consuming it left to right — but that only works if all the data exists upfront. A heap works dynamically: new items can arrive at any time, and the heap partially rearranges itself (O(log n)) after each insertion or removal to stay correct, without ever needing a full re-sort.

**How it works:**

Items are inserted with a priority value. The structure automatically reorganizes itself (a process called *sifting* or *heapifying*) so the minimum (or maximum) is always at the root. When you remove the top item, the next highest priority bubbles up.

- **Min-heap:** smallest value = highest priority (e.g., lower number means more urgent).
- **Max-heap:** largest value = highest priority.

**Use it when:** Your data changes dynamically and you always need to process the most urgent item next.

**Real-world examples from lecture:**

| Scenario | Priority |
|---|---|
| Call center | High-value customers answered first, regardless of call order |
| Emergency room | Most critical patients treated first, even as new patients arrive |
| Operating system scheduler | Processes with higher CPU priority get more time, even as tasks are added or removed |

```python
import heapq

queue = []
heapq.heappush(queue, (3, "patient C"))   # priority 3
heapq.heappush(queue, (1, "patient A"))   # priority 1 — most urgent
heapq.heappush(queue, (2, "patient B"))

priority, patient = heapq.heappop(queue)
print(patient)  # "patient A" — always the minimum priority value
```

**Performance:** O(log n) insert and remove; O(1) peek at the top.

> **Side note — "heap" in memory:** You may also hear "heap" used to describe the region of memory where dynamically allocated data lives (as opposed to the stack). This is a different use of the word — the naming is coincidental. The memory heap simply means "a pile of available memory"; the heap data structure (used in heapsort) was named independently. The two concepts are unrelated.
---

## 6. Disjoint Set / Union-Find

**What it is:** A structure that efficiently tracks which items belong to the same group (connected component), and can merge two groups in nearly constant time.

**How it works — the idea:**

Think of a social network. Each person starts in their own group. When two people become friends, their groups merge. If you later ask "are person A and person B in the same network?" — the structure answers instantly without traversing every friendship.

**The coloring analogy (think: painting each person a distinct color — red, blue, green, etc.):**

- Start: every person is painted their own unique color (A is red, B is blue, C is green, …).
- Connect A and B: one adopts the other's color. Everyone connected to the newly colored person also updates.
- Query: "same color?" → same group.

The array stores a *parent pointer* for each node. Finding the root of a chain of parent pointers tells you which group the node belongs to.

**Use it when:** You need to dynamically track connected components in a graph — and quickly answer "are these two nodes connected?"

**Real-world examples:**
- Network topology: which computers are reachable from which others?
- Social graphs: are these two users in the same community?
- Image processing: which pixels belong to the same region?

**Performance:** Nearly O(1) per operation with path compression optimization.

---

## 7. Segment Tree

**What it is:** A tree structure built over an array that pre-computes aggregate values (e.g., sums, minimums) for every possible subrange, so range queries are answered without iterating.

**How it works — the idea:**

Given an array of numbers, you might want to answer: "what is the sum of elements from index 3 to index 9?" Normally you'd loop and sum. A segment tree pre-computes this so any range query is answered in O(log n) steps.

```
Array: [2, 4, 1, 7, 3, 5, 8, 6]   (indices 0–7)

Tree (sums):
                     36           ← sum of everything
                /         \
             14              22   ← left half | right half
            /  \            /  \
           6    8          8    14  ← pairs
          / \  / \        / \  / \
         2   4  1  7     3   5  8  6  ← individual elements
```

When a value in the original array changes, only the nodes on the path from that leaf to the root need updating — O(log n) updates instead of recomputing everything.

**Use it when:** You have an array whose values change dynamically, and you frequently need the sum (or min, max, etc.) of arbitrary ranges.

**Real-world examples:**
- Financial data: running totals over time windows that update as new transactions arrive.
- Game leaderboards: range queries on player scores.
- Database engines: range aggregate queries on changing data.

**Performance:** O(log n) for both range queries and point updates.

---

## 8. Comparison at a Glance

| Structure | Primary Use | Key Operation | Performance |
|---|---|---|---|
| **Lookup Table** | Retrieve by integer ID | `array[i]` | O(1) |
| **Hash Table** | Retrieve by arbitrary key | `dict[key]` | O(1) avg |
| **Binary Search Tree** | Search sorted data | find a value | O(log n) |
| **Heap / Priority Queue** | Always-next-most-urgent | peek / pop top | O(log n) insert/remove |
| **Disjoint Set** | Track connected groups | union, find | ~O(1) |
| **Segment Tree** | Range queries on changing data | range sum/min/max | O(log n) |

**Which one to reach for:**

- Know the integer index → **Lookup Table**
- Know the key (name, ID string, etc.) → **Hash Table**
- Need to search a large sorted dataset → **Binary Search Tree**
- Need the next most / least urgent item from a changing list → **Heap**
- Need to know if two nodes are connected in a graph → **Disjoint Set**
- Need fast range aggregates on a changing array → **Segment Tree**

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
