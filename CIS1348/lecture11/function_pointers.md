
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

# Function Pointers, Higher-Order Functions, and Python Functional Tools

## Table of Contents

1. [Function Pointers / References to Functions](#1-function-pointers--references-to-functions)
2. [Jump Tables — Four Forms](#2-jump-tables--four-forms)
3. [When to Use Function References](#3-when-to-use-function-references)
4. [Event-Driven Programming and Callbacks](#4-event-driven-programming-and-callbacks)
5. [Custom `apply` — Motivation for `map`](#5-custom-apply--motivation-for-map)
6. [`map()` and Lazy Evaluation](#6-map-and-lazy-evaluation)
7. [Lambda Functions (Anonymous Functions)](#7-lambda-functions-anonymous-functions)
8. [`filter()`](#8-filter)
9. [`sorted()` with a `key` Function](#9-sorted-with-a-key-function)
10. [List Comprehensions](#10-list-comprehensions)
11. [Generator Expressions](#11-generator-expressions)

---

## 1. Function Pointers / References to Functions

Every function you write lives somewhere in memory, just like a variable. When Python sees a function named `greet`, that name is actually a variable holding the **memory address (location in memory)** of the function's code/instructions — not the code itself.

This means you can copy that address into another variable and call the function using the new variable:

```python
def greet():
    return "Hello!"

x = greet        # copy the address — no parentheses!
print(x())       # works exactly like greet()
```

`x` and `greet` now point to the same function. Calling `x()` jumps to that same code.

You can also pass a function reference as an argument:

```python
def execute(func):
    return func()

def say_goodbye():
    return "Goodbye!"

print(execute(say_goodbye))   # "Goodbye!"
```

And you can return a function reference from a function:

```python
def get_operation(op):
    def add(a, b):
        return a + b
    def multiply(a, b):
        return a * b

    if op == "add":
        return add
    else:
        return multiply

operation = get_operation("add")
print(operation(3, 4))   # 7
```

> The key insight: a function name without `()` gives you the address. A function name with `()` calls it.

---

## 2. Jump Tables — Four Forms

Imagine you walk into a building and there's a directory on the wall: "Accounting → Room 201, Legal → Room 305, HR → Room 110." You look up the department you need and go straight to the right room. You don't wander the hallways checking every door — the directory tells you exactly where to go.

A **jump table** works the same way. It is any mechanism that takes some data (a string, a number, etc.) and uses it to pick which function to call — jumping directly to the right code instead of testing every possibility one by one.

There are four common forms of jump tables, each building on the previous.

### Form 1 — Switch / if-elif (no function references)

The function receives the string **and** the arguments. It decides which function to call and **calls it right there, inside the if-elif block**. No function reference is ever passed around or returned — the decision and the execution both happen in the same place. The caller never touches a function reference; it just gets back the final result.

```python
def add(x, y):      return x + y
def subtract(x, y): return x - y

def apply_switch1(s, x, y):
    if s == "add":
        return add(x, y)
    elif s == "subtract":
        return subtract(x, y)

apply_switch1("add", 2, 3)   # 5
```

If a jump table is necessary, before reaching for function references, always consider whether simply calling the functions directly is sufficient. This is the most straightforward, un-abstracted approach — it is easy to reason about, easy to follow, and requires no indirection. Prefer it when the number of cases stays small.

### Form 2 — Switch returning a reference

The function receives only the string and returns a reference to the right function. The caller is responsible for supplying the arguments:

```python
def apply_switch2(s):
    if s == "add":
        return add
    elif s == "subtract":
        return subtract

apply_switch2("add")(2, 3)   # 5  ← note the second pair of parentheses
```

### Form 3 — List (index-based)

If you want to select a function by number rather than by name, store them in a list and index into it:

```python
operations = [add, subtract]
operations[0](2, 3)   # calls add(2, 3) → 5
operations[1](2, 3)   # calls subtract(2, 3) → -1
```

Less common than the dictionary form — you need to remember which index maps to which function.

### Form 4 — Dictionary (hash table)

Replace the if-elif chain with a dictionary mapping strings to function references:

```python
operations = {
    "add":      add,
    "subtract": subtract,
}

operations["add"](2, 3)      # 5
```

Or inline, without a separate variable:

```python
{"add": add, "subtract": subtract}["add"](2, 3)
```

**When to prefer each form:**

| Form | Good when |
|---|---|
| 1 (if-elif, calls directly) | You have a small number of cases and just want to call the right function immediately — no indirection needed. |
| 2 (if-elif, returns a reference) | The caller needs to receive the function and decide *when* or *how* to call it later, possibly with different arguments. |
| 3 (list) | The functions are naturally numbered (e.g., menu option 0, 1, 2…), so an integer index is the most natural lookup key. |
| 4 (dictionary) | You have many cases, the lookup keys are strings (or other hashable values), and you want easy extensibility. Multiple keys can map to the same function (e.g., `"add"`, `"Add"`, and `"ADD"` can all point to the same `add` function), and adding a new case is just one line — no if-elif chain to update. |

---

## 3. When to Use Function References

The instructor's rule: **do not reach for function references until things become physically difficult to manage**.

What does "physically difficult" mean? It means the literal, tangible overhead of doing your work: the clicking, the scrolling, the typing, the copying and pasting, and the mental load of keeping track of which code goes where. When the requirements change and you find yourself editing the same logic in five places, scrolling back and forth between dozens of functions, or spending more time navigating your code than thinking about the problem — that is physical difficulty. It wastes your time, drains your energy, and makes mistakes more likely. That friction — not conceptual elegance, but the real cost in effort — is the signal that abstraction is justified.

> **Quote from the instructor:** "Do not do very abstract things unless you feel like you are cornered and things are getting very difficult to deal with."

A concrete example: suppose you have different Pokémon types, each with its own custom attack and defend function:

```python
def attack_pikachu(target):   ...
def attack_charizard(target): ...
def defend_pikachu():         ...
def defend_charizard():       ...
```

Your game loop is generic — it just calls `attack` and `defend` without caring which Pokémon is active. Before the loop, you use a jump table to assign the right functions based on the current Pokémon:

```python
attack_table = {"pikachu": attack_pikachu, "charizard": attack_charizard}
defend_table = {"pikachu": defend_pikachu, "charizard": defend_charizard}

attack = attack_table[pokemon_type]
defend = defend_table[pokemon_type]

for target in enemies:
    attack(target)
defend()
```

The game loop never needs to know which Pokémon is active. The jump table handled the dispatch before the loop began.

Inside `attack()`, you need to dispatch to the right function per type. One approach: a dictionary keyed by Pokémon type holding a reference to each attack function. This is much easier to maintain than a giant if-elif as you add more types.

**Trade-off:** function references add *indirection*, and indirection has a real cost.

Imagine you're reading someone else's code and you see a variable called `tomato_paste`. Nothing about that name tells you it holds a function reference. You might assume it's a string or a number. Then, deep in the code, you encounter `tomato_paste(x, y)` and have no idea what it does — you have to trace the code backwards to find where `tomato_paste` was assigned, figure out which function it points to, and then go read *that* function. Multiply this by a dozen such variables and the code becomes a maze.

This is a serious problem for anyone who has to review, debug, or maintain the code — including your future self. Every level of indirection is one more thing the reader has to mentally resolve. If the person after you cannot quickly understand what a line of code does by reading it, your abstraction is hurting more than it helps. Too much abstraction turns simple logic into a treasure hunt where every variable might secretly be a function, and every function call might go through three layers of indirection before doing anything. **Abstraction is a tool, not a goal — use it only when the cost of *not* abstracting is clearly higher.**

---

## 4. Event-Driven Programming and Callbacks

UI frameworks are **event-driven**: clicks, hovers, and releases are pushed to a queue, and the framework processes them one by one. This pattern is especially common in JavaScript and HTML — for example, `onclick`, `onmouseover`, and similar event attributes all expect a function reference.

The framework exposes variables like `onclick` that expect a function reference. You customize behaviour by assigning your own function:

```python
def my_click_handler():
    print("clicked!")

# framework's variable — you assign your function to it
onclick = my_click_handler
```

The framework then calls `onclick()` whenever a click event arrives.

**This is an unavoidable use of function references.** The framework is asking you for a reference; there is no other way to participate in the system. If you don't assign anything, the framework's default handler runs instead.

---

## 5. Custom `apply` — Motivation for `map`

### Why a simple for-loop doesn't work

```python
lst = [1, 2, 3, 4]

for x in lst:
    x = x * x        # modifies the loop variable, NOT the list
```

`x` is a fresh variable created each iteration. Changing it has no effect on `lst`.

### The correct way — index into the list

```python
for i in range(len(lst)):
    lst[i] = lst[i] * lst[i]   # modifies the list in place
```

### Wrapping it in a function

```python
def square(x):   return x * x
def negate(x):   return -1 * x

def apply(f, my_list):
    for i in range(len(my_list)):
        my_list[i] = f(my_list[i])
    return my_list

x = [1, 2, 3, 4]
apply(square, x)          # x is now [1, 4, 9, 16]
apply(negate, x)          # x is now [-1, -4, -9, -16]
```

You can stack calls:

```python
x = [1, 2, 3, 4]
apply(negate, apply(square, x))
```

**Downside of custom `apply`:** stacking like this goes over the list **twice** — once to square, once to negate. Built-in `map` solves this.

---

## 6. `map()` and Lazy Evaluation

`map(f, iterable)` does what `apply` does, but smarter.

```python
x = [1, 2, 3, 4]

y = map(square, x)        # y is a map object — NOT a list yet
z = list(y)               # force evaluation: [1, 4, 9, 16]
```

### What `map` actually returns

`map` returns a **map object** — a lazy iterator that knows what work needs to be done but hasn't done it yet. Think of it as a recipe card, not the meal.

To get a list, force it:

```python
list(map(square, x))      # [1, 4, 9, 16]
```

Or iterate directly in a `for` loop (the map object is iterable):

```python
for val in map(square, x):
    print(val)
```

### Lazy evaluation

**Lazy evaluation** means computation is deferred until results are actually needed.

Why is this useful?

1. **You choose when computation happens.** You can set up the operation now and evaluate it later, or not at all if a code path is skipped.
2. **Stacked maps traverse the list only once.** Compare:

```python
# custom apply — two passes over the list
apply(negate, apply(square, x))

# map — one pass, per element: square then negate
list(map(negate, map(square, x)))
```

With stacked `map` calls, when you force evaluation Python processes each element through both functions before moving to the next. The list is never fully materialized between steps.

### Common use

```python
nums = [1, 2, 3]
strings = list(map(str, nums))    # ['1', '2', '3']
```

---

## 7. Lambda Functions (Anonymous Functions)

> **Currently banned in this course for problem sets and projects.** AI tools (ChatGPT, Gemini) will fill your code with lambdas. Using them without understanding will get your submission auto-failed.

A **lambda** is a function defined inline, without a name. It's useful when a function is short, used once, and doesn't deserve its own definition.

### Syntax

```
lambda <parameters> : <expression>
```

- Left of `:` — parameter list (same as `def` arguments)
- Right of `:` — single expression, implicitly returned

### Equivalence

```python
# These two are identical:
lambda x: x * x

def apple(x):
    return x * x
```

### Rules

- Single expression only — no `if`/`for`/`while` blocks, no multi-line logic
- No name (anonymous)
- Can take multiple arguments: `lambda x, y: x + y`

### Examples

```python
list(map(lambda x: x ** 2, [1, 2, 3]))          # [1, 4, 9]
list(filter(lambda x: x > 0, [-2, -1, 0, 1, 2])) # [1, 2]
sorted(students, key=lambda s: s[1])             # sort by second element
```

---

## 8. `filter()`

`filter(f, iterable)` keeps elements for which `f(x)` returns `True`, discards everything else.

```python
a = [1, 2, 3, 4, 5, 6]

# keep odd numbers
odd = list(filter(lambda x: x % 2 != 0, a))    # [1, 3, 5]

# keep numbers greater than 2
big = list(filter(lambda x: x > 2, a))          # [3, 4, 5, 6]
```

Like `map`, `filter` returns a **filter object** (lazy). Wrap with `list(...)` to get a list.

The predicate function (`f`) returns `True` or `False`. Every element for which it returns `True` survives into the result. The original list is untouched.

### Under the hood

```python
def filter_list(predicate, numbers):
    result = []
    for num in numbers:
        if predicate(num):
            result.append(num)
    return result
```

`filter(f, lst)` is exactly this, but lazy.

### `map` and `filter` work with any iterable

Both `map` and `filter` accept any **iterable** — not just lists. A list, a range, a generator, even another map object all work. Internally, they ask the iterable for one item at a time using Python's iterator protocol (`__next__()`). They never pull the whole sequence into memory at once. This is what makes them lazy: each element is fetched and processed only when the output is actually consumed.

Stacked calls like `map(negate, map(square, x))` form a pipeline — one element travels through the entire chain before the next one is fetched:

```python
x = [1, 2, 3, 4]
result = list(map(negate, map(square, x)))
# element-by-element: 1→square→1→negate→-1, then 2→square→4→negate→-4, ...
```

No intermediate list is ever created. This ties directly back to lazy evaluation: the outer `map` asks the inner `map` for the next value, which in turn asks `x` for the next element. Computation flows on demand.

---

## 9. `sorted()` with a `key` Function

`sorted(iterable, key=f)` sorts by applying `f` to each element and comparing the *transformed* values. The original values are preserved in the output.

```python
a = [1, -2, 3, -5]

# sort by magnitude (ignoring sign)
sorted(a, key=lambda x: x * x)    # [1, -2, 3, -5]

# sort list of tuples by second element
pairs = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted(pairs, key=lambda t: t[1])  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```

The `key` function is applied **once per element** (not on every comparison), so it's efficient.

### How Python implements this — Decorate-Sort-Undecorate (DSU)

Python's `sorted(key=f)` works in three internal steps:

1. **Decorate:** compute `key(x)` for each element, creating temporary pairs `(key(x), x)`.
2. **Sort:** sort the pairs by their first element using Timsort.
3. **Undecorate:** strip the key values, returning the original elements in sorted order.

**Performance:**

| Step | Cost |
|---|---|
| Key function calls | Exactly n (O(n)) |
| Comparisons | O(n log n) |
| Extra memory | O(n) for the decorated list |

This is more efficient than C's `qsort`, where the comparison function is called O(n log n) times, potentially re-computing expensive logic on every comparison.

### `key` vs comparator

The `key` parameter is a **data extractor** — it returns a value, and Python uses `<` and `>` on those values. It is *not* a comparator (a function returning negative/zero/positive like C's `qsort`). For the rare case where you need custom comparison logic, Python provides `functools.cmp_to_key()` to convert a comparator into a key function.

---

## 10. List Comprehensions

> **Currently banned in this course for problem sets and projects.** Many students failed problem sets by using AI-generated code that contained list comprehensions without realizing it.

A **list comprehension** is concise syntax for building a list from a loop.

### Syntax

```python
[expression  for variable in iterable]
```

### Equivalence

```python
# traditional
squares = []
for x in range(5):
    squares.append(x ** 2)

# list comprehension — identical result
squares = [x ** 2 for x in range(5)]   # [0, 1, 4, 9, 16]
```

### With a condition

```python
# traditional
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

# list comprehension
evens = [x for x in range(10) if x % 2 == 0]   # [0, 2, 4, 6, 8]
```

### How to read it

Split it into two parts:

```
[  x * x        for x in range(10) if x % 2 == 0  ]
   ↑ expression  ↑ loop header + condition
```

The right side is the `for`/`if` part (top of the loop). The left side is what gets appended.

### More examples

```python
words = ["hello", "world"]
[word.upper() for word in words]              # ['HELLO', 'WORLD']

students = [("Alice", 85), ("Bob", 92)]
[name for name, grade in students if grade >= 85]  # ['Alice', 'Bob']
```

### Relation to `map` and `filter`

```python
# these are equivalent:
[x ** 2 for x in numbers]
list(map(lambda x: x ** 2, numbers))

[x for x in numbers if x % 2 == 0]
list(filter(lambda x: x % 2 == 0, numbers))
```

---

## 11. Generator Expressions

A **generator expression** looks exactly like a list comprehension but uses `()` instead of `[]`:

```python
squares_list = [x ** 2 for x in range(5)]   # list — computed immediately
squares_gen  = (x ** 2 for x in range(5))   # generator — computed lazily
```

That single character difference (`[]` vs `()`) changes everything about when and how the values are produced.

### What a generator actually is

A generator is an **iterator** that yields one value at a time, pausing between yields. Conceptually:

```python
# (x ** 2 for x in range(5)) is equivalent to:
def make_squares():
    for x in range(5):
        yield x ** 2        # pause here, return value, resume on next call
```

You can drive it manually with `next()`:

```python
gen = (x ** 2 for x in range(5))
next(gen)   # 0
next(gen)   # 1
next(gen)   # 4
next(gen)   # 9
next(gen)   # 16
next(gen)   # StopIteration — exhausted
```

### Memory

```python
# list comprehension — all 1,000,000 values in memory (~8 MB)
squares = [x ** 2 for x in range(1_000_000)]

# generator — tiny iterator object (~100 bytes), one value at a time
squares = (x ** 2 for x in range(1_000_000))
```

A generator expression is **lazily evaluated** — it creates an iterable that produces values one at a time, on demand.

### Consuming a generator

```python
gen = (x ** 2 for x in range(5))

list(gen)            # force all values into a list: [0, 1, 4, 9, 16]
# or
for val in gen:      # process one at a time
    print(val)
# or
sum(x ** 2 for x in range(5))   # pass directly to a function (no double parens needed)
```

### Generator chaining

Generators can be stacked into a pipeline. Each stage is lazy — no intermediate lists are created:

```python
numbers  = range(1, 20)
evens    = (x for x in numbers if x % 2 == 0)    # lazy
squared  = (x ** 2 for x in evens)               # lazy
under100 = (x for x in squared if x < 100)       # lazy

result = list(under100)    # computation finally happens: [4, 16, 36, 64]
```

Each value flows through the entire pipeline before the next one is pulled. Compare to the eager version:

```python
# eager — three full intermediate lists in memory
evens    = [x for x in range(1, 20) if x % 2 == 0]
squared  = [x ** 2 for x in evens]
under100 = [x for x in squared if x < 100]
```

The lazy version stores only the final result.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
