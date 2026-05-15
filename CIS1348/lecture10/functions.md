
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

# Functions

## Table of Contents

1. [What is a Function?](#1-what-is-a-function)
2. [Jump Mechanics — How Functions Relate to `if` and Loops](#2-jump-mechanics--how-functions-relate-to-if-and-loops)
3. [Passing Arguments](#3-passing-arguments)
4. [The Call Stack — Walkthrough 1 (nested calls)](#4-the-call-stack--walkthrough-1-nested-calls)
5. [The Call Stack — Walkthrough 2 (`add(a, b)`)](#5-the-call-stack--walkthrough-2-adda-b)
6. [Python Syntax: Defining and Calling Functions](#6-python-syntax-defining-and-calling-functions)
7. [Why Use Functions? Reason 1 — Avoid Repetition (Hash Example)](#7-why-use-functions-reason-1--avoid-repetition-hash-example)
8. [Why Use Functions? Reason 2 — Maintainability (Letter Grade Example)](#8-why-use-functions-reason-2--maintainability-letter-grade-example)
9. [Why Use Functions? Reason 3 — Abstraction (ASCII Art Example)](#9-why-use-functions-reason-3--abstraction-ascii-art-example)
10. [Importing Functions from Another File](#10-importing-functions-from-another-file)
11. [Functions for Teamwork and Modularity](#11-functions-for-teamwork-and-modularity)
12. [When to Write a Function — Design Philosophy](#12-when-to-write-a-function--design-philosophy)
13. [In-Class: Building an Interactive Calculator Incrementally](#13-in-class-building-an-interactive-calculator-incrementally)
14. [Function Variants and Default Arguments](#14-function-variants-and-default-arguments)

---

## 1. What is a Function?

When you run a Python program, all code — yours and everyone else's code that you import — is loaded into **memory** (RAM). Your own `.py` file is in memory, and so is every built-in function like `print`, every library you import, and every piece of the Python interpreter itself. There is no distinction between "your code" and "their code" at runtime; it is all just blocks of instructions sitting in memory.

Because every block of code lives in memory, every block has an **address** — a location where it starts. A function name is just a **label** for one of those addresses. Think of it like a street address: `print` is a label that says "the printing code lives *here*." When you call `print("apple")`, you are telling Python: jump to that address, run the code there, and come back. You don't have to know *how* printing works — you just need the address.

This is the core idea of a function:

> A **function** is a labeled block of code at a specific address in memory. A **function call** means: jump to that address, execute the code there, and jump back.

There is more to this jump-and-return mechanism — the chain of active function calls is tracked by the **call stack**, and any variables a function creates are pushed onto the **stack**. When the function returns, those variables are cleaned up (the stack is popped/unwound). This is covered in detail in [Section 4](#4-the-call-stack--walkthrough-1-nested-calls).

You can write your own functions — you pick a name, write the code once, and then you (or anyone else who imports your code) can jump there whenever needed.

---

## 2. Jump Mechanics — How Functions Relate to `if` and Loops

Functions are **relatives** of `if` statements and loops.

All three work through the same low-level mechanism: the **instruction pointer (IP)**. The IP is the thing that tracks which line the program is currently executing. Usually it moves forward one line at a time. But:

- An **`if` statement** causes a conditional **jump** — if the condition is false, the IP skips over the block.
- A **loop** causes a repeated **jump** — the IP jumps back to the top of the loop on each iteration.
- A **function call** causes a **jump** to a named location in memory.

The key difference with a function call is that you need to come back:

> When the function call jumps, it **writes down which line it jumped from**. When a `return` is reached inside the function, execution jumps back to the line *after* the call site.

```
main code:
  line 1: x = 5
  line 2: y = two(x)    <-- jump to `two` below; write down "line 2"
  line 3: print(y)      <-- execution resumes here after return

function two:
  line A: ...
  line B: return y      <-- jump back to "line 3" above, right after where it was called at "line 2"
```

This is exactly why functions, `if`, and loops are all in the same family: they are all just different kinds of **controlled jumps** in memory.

---

## 3. Passing Arguments

When you call a function, you can pass data to it. The values you place between the parentheses are called **arguments**:

```python
print("apple")          # one argument: the string "apple"
add(3, 5)               # two arguments: the integers 3 and 5
greet("Alice", "Hello") # two arguments: both strings
```

What happens when the call is made? Python creates **new variables** on the stack — one for each parameter in the function's definition — and initialises them with the values the caller provided. These new variables belong to the function's own stack frame. They are completely separate from whatever variables the caller used.

```python
a = 3
b = 5
result = add(a, b)   # Python creates new variables x=3, y=5 inside add's stack frame
                      # a and b in the caller's frame are untouched
```

Inside the function, the code works with these fresh variables — `x` and `y`, not `a` and `b`. When the function finishes, it can hand a value back using `return`. The `return` statement does two things back-to-back: it evaluates the value to be returned, and then it pops the function's entire frame off the stack — all of the function's local variables are gone. The saved value is what the caller receives.

```python
result = add(3, 5)   # add creates x=3, y=5 on its stack frame
                     # computes s = x + y = 8
                     # return s → value 8 is saved, frame is popped
                     # result receives 8
```

> **Arguments are how the caller supplies data *to* the function. `return` is how the function supplies data *back to* the caller.** Both work through the stack: arguments are pushed as new variables when the function is entered; the return value is carried out when the frame is popped.

The full mechanics of this — how the stack grows, how frames are created and destroyed — are traced step by step in [Section 4](#4-the-call-stack--walkthrough-1-nested-calls) and [Section 5](#5-the-call-stack--walkthrough-2-adda-b).

---

## 4. The Call Stack — Walkthrough 1 (nested calls)

The mechanism that makes all this work is the **call stack**. Every time a variable is created, it is **pushed** onto the stack. Every time a function returns, everything that was pushed for that function is **popped** off.

Let's trace through this code step by step:

```python
x = 5
y = two(x)
print(y)
print(x)

def two(x):
    y = one(x * 2)
    return y

def one(x):
    return x + 1
```

**Step-by-step stack trace:**

```
Start executing main code
┌──────────────────┐
│ x(main) = 5      │  ← push x=5
└──────────────────┘

Encounter y = two(x). Cannot assign y yet — must resolve two(x) first.
Push the argument (value 5) for the call to two.

┌──────────────────┐
│ x(main) = 5      │
│ x(two)  = 5      │  ← new x, belonging to two
└──────────────────┘

Inside two: encounter y = one(x * 2) = one(10). Must resolve one(10) first.
Push the argument (value 10) for the call to one.

┌──────────────────┐
│ x(main) = 5      │
│ x(two)  = 5      │
│ x(one)  = 10     │  ← yet another x, belonging to one (5 * 2 = 10)
└──────────────────┘

Inside one: compute x + 1 = 11. Return 11.
Pop one's frame. Return value 11 goes back to two.

┌──────────────────┐
│ x(main) = 5      │
│ x(two)  = 5      │
│ y(two)  = 11     │  ← one returned 11, stored as y inside two
└──────────────────┘

Return y (11). Pop two's frame. Value 11 assigned to y in main.

┌──────────────────┐
│ x(main) = 5      │
│ y(main) = 11     │  ← y is now 11
└──────────────────┘
```

**What does `print(y)` output?** It prints `11`. And what about `print(x)`? It prints `5` — `x` in main was never touched. Even though all three scopes had a variable called `x`, they are **three completely different variables** stored in three different places on the stack.

> **Critical insight:** Variable names mean nothing by themselves. `x` inside `two`, `x` inside `one`, and `x` inside `main` are three different variables. Python keeps them separate by remembering *where in the call stack* each one lives.

Think of the stack like rooms inside a building. You walk into the building (one level), then into a classroom (two levels). To leave, you first exit the classroom, then exit the building — exactly the order you entered, in reverse. A function call *enters* a room; a return *exits* it.

---

## 5. The Call Stack — Walkthrough 2 (`add(a, b)`)

Here is a cleaner, second example:

```python
a = 5
b = 2
c = add(a, b)
print(c)

def add(x, y):
    s = x + y
    return s
```

**Stack trace:**

```
Push a=5
Push b=2

Call add(a, b) — push arguments as x=5, y=2 inside add's frame:

┌──────────────────┐
│ a(main) = 5      │
│ b(main) = 2      │
│ x(add)  = 5      │
│ y(add)  = 2      │
│ s(add)  = 7      │  ← x + y = 7
└──────────────────┘

return s → pop add's frame (x, y, s all removed).
Value 7 is handed back and assigned to c:

┌──────────────────┐
│ a(main) = 5      │
│ b(main) = 2      │
│ c(main) = 7      │  ← stack shrinks, then grows by 1 for c
└──────────────────┘

Program ends → implicit return, everything popped.
```

Key points:
- Every time you **enter** a function, a fresh page opens. Variables inside are isolated from everything outside.
- Every time you **return** from a function, everything pushed for that function is popped.
- The return value is transferred out before the pop happens.
- There is an **implicit return** at the end of a program — you do not always have to write `return` explicitly.

> **Two things to remember about arguments and return:**
>
> **Arguments are brand-new variables.** When you call `add(a, b)`, Python does not hand `a` and `b` themselves into the function — it creates fresh variables `x` and `y` inside the function's frame and initialises them with the *values* of `a` and `b`. Those new variables live on the stack for the duration of the call. When the function returns, its entire frame — including `x`, `y`, and anything else declared inside — is popped off and gone.
>
> **`return X` is two separate operations.** It looks like one thing, but it is really two steps happening back-to-back: first, the value of `X` is evaluated and set aside; then, the function's frame is terminated and popped from the stack. That saved value is what gets handed back to the caller — it is what ends up in the variable waiting on the outside (e.g., `c = add(a, b)`). The `X` in `return X` and the variable `c` outside are completely different variables in completely different frames; `return` is the bridge that carries the value from one to the other.

---

## 6. Python Syntax: Defining and Calling Functions

In Python, you declare a function with the `def` keyword:

```python
def add(x, y):
    s = x + y
    return s
```

**Defining** a function is not executing it. It just tells Python: "in the future, when you see a call to `add`, here is what to do." Nothing runs until you actually **call** it:

```python
c = add(5, 2)   # this is the call — this is what triggers the jump
```

A function:
- **May or may not** take arguments (inputs)
- **May or may not** return a value (output)
- You decide what makes sense for what you need

The whiteboard showed four patterns, using the actual examples from lecture:

```python
# one() — no input, no return. Just does something.
def one():
    print("hello")

one()           # works fine, no arguments needed


# two(a, b) — takes input, no return. Prints the result internally.
def two(a, b):
    print(a + b)

two(3, 4)       # prints 7, but the caller gets nothing back


# three(a, b) — takes input, returns the result. Caller can use it.
def three(a, b):
    return a + b

result = three(3, 4)
print(result)   # 7


# four() — tries to return x, but x is not defined inside the function.
# This will crash at runtime with a NameError.
def four():
    return x    # ERROR: x does not exist in this scope
```

The last example (`four`) is a deliberate warning: a function only has access to variables defined **inside its own frame** (and its parameters). If you reference a variable that does not exist in the local scope, Python will crash. This is called a **scope error**.

There is no single "correct" pattern for the others. You decide based on what the caller needs to do with the result.

> **A broader view: input → transform → output.** Every function — every piece of computation, really — follows the same universal pattern: it *consumes* data, *transforms* it, and *produces* a result. Arguments and `return` are just one mechanism for getting data in and out. They are not the only one. `one()` above takes no arguments and returns nothing, yet it still produces output — it writes text to the screen via `print`. A function could read from the keyboard, a file, or the network (input) and write to the screen, a file, or a database (output), all without a single argument or `return` statement. The four patterns above are not four different kinds of functions — they are four different *wirings* of the same input → transform → output model. The model is the constant; arguments and `return` are just the most common plugs.

---

## 7. Why Use Functions? Reason 1 — Avoid Repetition (Hash Example)

**`e1_before.py` — the problem:**

```python
firstname = input("enter name:")
lastname = input("enter lastname:")
address = input("enter address:")

hfirstname = 5381
for c in firstname:
    hfirstname = hfirstname * 33 + ord(c)

hlastname = 5381
for c in lastname:
    hlastname = hlastname * 33 + ord(c)

haddress = 5381
for c in address:
    haddress = haddress * 33 + ord(c)

print(hfirstname)
print(hlastname)
print(haddress)
```

The same loop is copy-pasted three times with only the variable name changed. This causes three real problems:

1. **Tedious to write.** You are typing the same logic over and over.
2. **Silent bugs from copy-paste.** If you forget to rename a variable (e.g., write `lastname` where you meant `address`), the code still runs — it just silently produces the wrong answer.
3. **Bugs must be fixed in multiple places.** If the starting hash value `5381` is wrong, you have to find and fix it in every copy. In a 10,000-line codebase, you might miss one.

**`e1_after.py` — the solution:**

```python
def gethash(s):
    x = 5381
    for c in s:
        x = x * 33 + ord(c)
    return x

firstname = input("enter name:")
lastname = input("enter lastname:")
address = input("enter address:")

hfirstname = gethash(firstname)
hlastname = gethash(lastname)
haddress = gethash(address)

print(hfirstname)
print(hlastname)
print(haddress)
```

The loop lives in exactly one place. Fix it once; all three uses are fixed. The calling code is also easier to read — you can understand the intent at a glance without decoding the loop.

---

## 8. Why Use Functions? Reason 2 — Maintainability (Letter Grade Example)

**`e2_before.py` — the problem:**

```python
grade = float(input("enter grade avg:"))

lettergrade = 'F'
if grade >= 90.0:
    lettergrade = 'A'
elif grade >= 80.0:
    lettergrade = 'B'
elif grade >= 65.0:
    lettergrade = 'C'

print(lettergrade)
```

This works fine as-is. But imagine this same block of `if/elif` code copied into 10 different places across 20,000 lines of code. Now someone notices that the C threshold should be `70`, not `65`. You have to hunt down all 10 copies and fix them. Miss one? You have a silent inconsistency that is very hard to debug.

**`e2_after.py` — the solution (corrected):**

```python
def get_letter_grade(x):
    lettergrade = 'F'
    if x >= 90.0:
        lettergrade = 'A'
    elif x >= 80.0:
        lettergrade = 'B'
    elif x >= 70.0:
        lettergrade = 'C'
    return lettergrade

grade = float(input("enter grade avg:"))
print(get_letter_grade(grade))
```

Now the logic lives in one place. If the C threshold needs to change, you change it once. Every call site automatically gets the updated behaviour.

> **Note:** This function is justified because the grading logic is the kind of code that gets copy-pasted across a codebase — the problem may not be visible in this small example, but in a real project with 10 copies of the same `if/elif` chain, the repetition is real and the maintenance cost is concrete.
>
> **Do not make a function because you think you might need it in the future.** "You never know when you'll need it" is not a justification — it is speculation, and speculation is not a reason to write code. If there is actual evidence of future use — for example, you know from experience that this kind of logic always grows — that is different. But a vague "maybe someday" is not enough.

**The careless version — looks almost right:**

```python
def get_letter_grade(x):
    lettergrade = 'F'
    if x >= 90.0:
        lettergrade = 'A'
    elif x >= 80.0:
        lettergrade = 'B'
    elif x >= 70.0:
        lettergrade = 'C'
    print(lettergrade)      # <-- added this
    return lettergrade
```

To a beginner, this looks fine — it prints *and* returns. But this reveals unclear design thinking.

**Ask yourself: what is this function's job?**

- **Option A — compute and return for further processing.** You are going to call this on 10,000 student records, collect the results, and write them to a file silently. In that case, `print()` is noise. It floods the terminal with 10,000 lines nobody asked for, and you cannot suppress it without rewriting the function.
- **Option B — just print the grade to the screen.** Then why are you returning anything? The caller ignores the return value. The `return` is dead weight that misleads future readers.

Doing both makes the function's contract ambiguous. It has a hidden side effect (printing) baked in, so every caller is forced to accept that side effect whether they want it or not. That is the carelessness: not thinking through who calls this, in what context, and what they need.

**Any of the three goals is legitimate** — the problem is not the goal itself, it is the lack of deliberate thought. A function that just prints, just returns, or does both can all be the right choice depending on context. But that choice must be made consciously, and the **function name must reflect it**.

| Intent | Appropriate name | Body |
|---|---|---|
| Compute and return only | `get_letter_grade(x)` | `return lettergrade` |
| Print only (no further use) | `print_letter_grade(x)` | `print(lettergrade)` |
| Print *and* return (rare, explicit) | `display_and_return_letter_grade(x)` | `print(...)` then `return` |

The name `get_letter_grade` signals "I compute and hand back a value." Adding a silent `print` inside it violates that contract — the caller asked for a value, not a terminal side effect. If printing is the actual goal, rename the function `print_letter_grade` and drop the return. If both are truly needed, make that explicit in the name so no caller is surprised.

The carelessness is not the print — it is writing a function without deciding what it is for, and then naming it as if that decision had been made.

---

## 9. Why Use Functions? Reason 3 — Abstraction (ASCII Art Example)

**`e3_before.py` — flat, hard to read:**

```python
print("-------------------")
print("HI!")
print("xoxoxoxoxoxo")
print("O_o <-- me")
print("xoxoxoxoxoxo")
print("-------------------")
print("thehehehe")

```

There is no copy-paste problem here. Each line is different. But the code is a wall of `print()` calls. Reading it, you have no idea what the *intent* is. You're stuck decoding the details instead of understanding the big picture.

**`e3_after.py` — abstracted, easy to read:**

```python
def line():
    print("-------------------")

def hi():
    print("HI!")

def xo():
    print("xoxoxoxoxoxo")

def confused(s):
    print("O_o <--" + s)

def lol():
    print("thehehehe")

lol()
lol()
lol()
confused("YOU")
xo()
lol()
lol()
hi()
print("lets eat lunch")
line()
```

Reading the bottom section is now almost like reading English: lol, lol, lol, confused, xo... You understand the *story* of the program without needing to read the implementation of each function. The details are hidden away inside each function, and you only look at them when you care.

This is **abstraction**: hiding complexity behind a meaningful name so you can think at a higher level.

> Functions used for abstraction are not about avoiding copy-paste. They are about **giving things names** so the calling code expresses *what* is happening, not *how*.

This scales dramatically. Imagine those functions contained complex loops, calculations, and conditionals. From the outside, the calling code still just says `lol()` and `confused("YOUJ")`. You can reason about the program without holding all the details in your head at once.

Think of it like Lego: instead of always working with individual bricks, you build functional sub-assemblies — a wheel unit, a wing, a cockpit — and then you put *those pieces* together. The small details are already handled; you think at the level of the components. Or think of a landscape: instead of worrying about placing every leaf, you have already built the trees. Now you only need to decide where to place the trees.

---

## 10. Importing Functions from Another File

You can put your functions in a separate file and import them.

**`myfunctions.py`:**
```python
def hello():
    print("HELLO!")
```

**`e4.py`:**
```python
import myfunctions

myfunctions.hello()
```

The dot notation (`myfunctions.hello()`) specifies which file's `hello` you mean. Multiple files might each define a `hello` function. The prefix acts as a **namespace** — it tells Python "I want the `hello` from this particular file, not from any other."

If your file lives inside a folder (package), the import path must reflect that folder structure:

```python
# myfunctions.py is inside a folder called "utils":
from utils import myfunctions
myfunctions.hello()

# If folders are nested (utils/helpers/myfunctions.py):
from utils.helpers import myfunctions
myfunctions.hello()
```

Each dot in the path represents one level deeper into the folder hierarchy.

> This will be covered in more depth in a later lecture. For now, just know that functions can live in separate files and be imported.

---

## 11. Functions for Teamwork and Modularity

Functions are also the primary tool for working on code in a team. Consider building a game:

**Without functions:** A senior engineer would have to say "go to `main.py`, find line 336, insert this loop between these two lines" — fragile, confusing, and error-prone.

**With functions:** The senior engineer says "write me a function `draw_enemy_outlines(enemies)` that takes a list of enemies and draws a red outline around each one." The junior developer works on that function independently; the senior engineer calls it when ready.

The benefits:

1. **Clear task assignment.** The function signature defines the scope of work precisely.
2. **Isolation.** If the function breaks, the caller just removes the call. No need to understand what the other person changed or touch their code at all.
3. **Parallel development.** Multiple developers write different functions simultaneously. One works on enemy rendering, another on the HUD, another on physics. These tasks don't overlap and can happen in parallel.
4. **Independent testing.** You can test a function in isolation. If it passes, you know it works. If the larger program fails, you know to look elsewhere.

> Functions are not just a coding tool — they are a **project management tool**. They create clean boundaries between pieces of work.

---

## 12. When to Write a Function — Design Philosophy

This is the most important section philosophically. The question is: when should you sit down and decide to write a function?

**The wrong approach:** spend time up front designing all your functions, their signatures, how they interact, what they return. You can spend a week on this "design phase" and still be completely wrong, because you cannot predict what the code will actually need until you have written it.

> "You can spend a week thinking about how everything is going to interact, and the moment you start typing, midway through you'll realize how wrong you were."

Design absolutely works — but only when it comes from *experience*. A developer building their fifth database system or their fourth racing game can sit down, sketch out the modules, and get it right quickly. That is because they are not designing from scratch — they are recalling what worked last time and repeating it. What courses often present as "design skill" is really accumulated experience: someone has built the same kind of software multiple times, learned what failed, and now knows the pattern. Without that experience, upfront design is mostly guessing.

**The right approach:**

1. Get a rough idea of the main pieces and start writing code — flat, simple, as straightforward as possible.
2. Run it. See if it works.
3. **Look at the result.** Where is there repetition? Where is the code getting hard to read? Where are you copying and pasting?
4. At *that point*, extract a function.

You will know exactly what arguments the function needs and what it should return, because you already wrote the code and saw what was needed. You cannot know this in advance without the experience of having written it.

> "The laziness will lead you to an easier to maintain solution."

When you feel the urge to copy-paste code a second time, that urge is the right signal to stop and write a function. Not before — when it actually happens.

This approach also applies to experienced engineers. When a senior engineer "designs" a system quickly, they are not designing from scratch — they are **recalling** patterns from previous projects they have built. They already know which modules will be needed because they have done it before. That is not design; that is experience.

> **Avoid speculative design and premature abstraction.** Do not create functions, modules, or structures for hypothetical future needs with no basis in evidence. This applies to everything: function signatures you might need, helpers you might reuse, abstractions you might want later. If the need does not exist right now, the function should not exist right now. The exception is when experience provides evidence — if you have built this kind of system before and *know* from that experience what will be needed, that is informed anticipation, not speculation. Without that prior experience, upfront design is mostly guessing.

### When can you justify a function?

A function is never *required* unless the algorithm itself demands it. But if you find yourself asking whether you should create one, these are valid reasons to go ahead:

- **This code is getting in your way.** It's cluttering the flow and pulling your attention away from what the program is actually doing. Giving it a name and hiding it away is a reasonable justification.
- **It's looking redundant and bothering you.** You've written similar code more than once and the repetition feels wrong. A function is a reasonable response.
- **It's too complicated to safely copy-paste.** If you'd have to carefully rename variables and could easily introduce a mistake, a function solves that — the arguments do the renaming automatically and there is only one copy to get right.
- **You want to work at a higher level.** You want to think about how behaviours connect without being pulled into the internals every time you read the code. A function lets you name the behaviour and reason about it from the outside.
- **An `if` condition is carrying too much logic.** If the condition itself needs explanation, a function with a descriptive name makes the intent readable without forcing the reader to decode the expression.

### Why not just make functions for everything?

A natural follow-up question: if functions make code organised and readable, why not wrap *everything* in a function?

The problem is that every function you create is a dependency — a place you have to go visit to understand what the code does. When functions call functions that call other functions, you end up chasing a chain: to understand `A`, you have to open `B`; to understand `B`, you have to open `C`; by the time you get to `C` you have completely lost the context of why you started. This is sometimes called **dependency hell**, and it makes code *harder* to reason about, not easier.

Consider a formula sitting directly in the code:

```python
score = (hits * 10 + combos * 50) / max_possible * 100
```

You can read that and understand it immediately — right there, in context, with all the surrounding variables visible. Now imagine it is wrapped:

```python
score = calculate_score(hits, combos, max_possible)
```

Now you have to go find `calculate_score`. When you get there, you find:

```python
def calculate_score(hits, combos, max_possible):
    raw = hits * 10 + combos * 50
    return normalize(raw, max_possible)
```

It calls *another* function. So you go find `normalize`:

```python
def normalize(value, maximum):
    return value / maximum * 100
```

By the time you finish reading `normalize`, you have forgotten what `hits` and `combos` were, why `max_possible` matters, and what the score is even for. You have made three stops to understand one formula that fit on a single line. The formula was actually *easier* to understand in its original place, even if it looked like "it should probably be a function."

More functions also means more **glue** — the connective code that passes data between them, manages return values, and wires everything together. Too much of it and the program structure becomes harder to see than the logic it was supposed to clarify.

The goal is not maximum organisation. The goal is **minimum friction when reading the code**. Sometimes that means a function; sometimes it means leaving the logic exactly where it is.

---

## 13. In-Class: Building an Interactive Calculator Incrementally

This example demonstrates the design philosophy in action. We look at two versions of the same program — first without any functions, then after extracting them. The difference in readability makes the case better than any argument could.

### Part 1 — Before: everything inline

```python
while True:
    op = input("op:")
    addops = ["add", "+", "plus", "Add", "ADD", "AAAADDDD"]

    if op == "quit":
        break

    if op in addops:
        x = float(input("x:"))
        y = float(input("y:"))
        result = x + y
    elif op == "sub" or op == '-':
        x = float(input("x:"))
        y = float(input("y:"))
        result = x - y
    else:
        print("unknown operation")
        continue

    print("result: ", result)
```

This works, but reading the `while True` loop is hard. The `addops` list, the arithmetic, and the `input()` calls all sit in the same place, competing for attention. Trying to understand the program's top-level flow — what operations exist, when does it quit, what does it print — means reading through all the implementation detail at once. Adding a new operation means finding the right place in the middle of this tangle. The condition `op in addops` is already growing and would only get worse.

### Part 2 — After: extract functions

```python
def get_op():
    r = input("op:")
    return r

def handle_add():
    x = float(input("x:"))
    y = float(input("y:"))
    return x + y

def handle_sub():
    x = float(input("x:"))
    y = float(input("y:"))
    return x - y

def should_run_add(op):
    addops = ["add", "+", "plus", "Add", "ADD", "AAAADDDD"]
    if op in addops:
        return True
    return False

while True:
    op = get_op()

    if op == "quit":
        break

    if should_run_add(op):
        result = handle_add()
    elif op == "sub" or op == '-':
        result = handle_sub()
    else:
        print("unknown operation")
        continue

    print("result: ", result)
```

**How this was built — the incremental process:**

1. Start with just a `while True` loop and a raw `input("op:")` call. Extract it immediately into `get_op()` — not because the code is already messy, but because input processing is the kind of thing that will grow: validation, normalisation, aliases, trimming. Giving it its own function now establishes a clean seam for that future expansion. This is one of the rare cases where anticipating growth is justified — not speculative design, but recognising a predictable expansion point.
2. Add handling for `add` — write `handle_add()` when the body of the `if` block starts to feel cluttered. Don't plan it; extract it when the code asks for it.
3. Add `handle_sub()` the same way.
4. Notice that the condition `op == "add" or op == "+"` is growing and getting messy. Extract that logic into `should_run_add(op)`.

At no point was any of this designed in advance. Each function was extracted at the moment when the code without it became annoying or hard to read.

**What the final code communicates:**

Reading the `while True` loop, you understand the program's intent at a glance: get an operation, quit if asked, run add or sub, print the result. You do not need to know how `should_run_add` works to understand the flow. That complexity is hidden away.

If later you want `should_run_add` to also recognise voice commands or emoji, you add that logic inside `should_run_add`. The rest of the program does not change at all.

---

## 14. Function Variants and Default Arguments

### Whiteboard: `five` and `six`

The whiteboard introduced default arguments through two examples:

```python
# five(x, y=5) — y is optional; if not provided, it defaults to 5
def five(x, y=5):
    return x + y

five(2)     # x=2, y=5 (default)  → 7
five(2, 3)  # x=2, y=3 (override) → 5


# six(x=1, y=1) — both parameters have defaults; keyword args can be in any order
def six(x=1, y=1):
    return x * y

six(y=4, x=3)   # x=3, y=4 → 12
```

The stack diagram on the board showed exactly what happens when you call `five(2)`: the value `2` is pushed for `x`, and because no `y` was provided, the default value `5` is pushed for `y` instead. The stack frame looks the same whether the value came from the caller or from the default — the function body never knows the difference.

### Coded example: `e6.py`

**`e6.py`:**

```python
def one(x, y=2, z=3):
    return x + y + z

print(one(1))         # x=1, y=2(default), z=3(default) → 6
print(one(1, 2))      # x=1, y=2, z=3(default)          → 6
print(one(1, 2, 3))   # x=1, y=2, z=3                   → 6
print(one(1, y=6))    # x=1, y=6, z=3(default)          → 10
print(one(1, z=6))    # x=1, y=2(default), z=6          → 9
print(one(1, z=7, y=6)) # x=1, y=6, z=7 (order doesn't matter for keyword args) → 14
```

### Rules for default (optional) arguments

- Parameters with `=` in the definition are **optional**. If the caller doesn't provide them, the default value is used.
- Parameters without `=` are **required**. The caller must always provide them.
- Required parameters must come **before** optional ones in the definition.
- When calling, you can pass optional arguments by **name** (`y=6`) in any order, as long as all required arguments are provided.

**What is illegal:**

```python
# one(z=7, 1, y=6)  — cannot put a positional arg after a keyword arg
# one(z=7, y=6)     — x is required and missing
```

### A note on design

Default arguments are very common in Python. They are convenient for short scripts where you want sensible defaults without forcing the caller to always specify everything.

However, be aware of the trade-off: if you have never seen the function's definition, you have no idea what optional arguments exist or what they default to. The function appears to work with fewer arguments than it actually uses — which can be confusing in large codebases.

> Optional arguments tend to produce bloated functions that behave differently depending on which defaults are active. This is a form of hidden control flow — the function's behaviour changes based on arguments the caller may not even know exist. The result is code that is harder to read and harder to test, because you must account for every combination of defaults. When a function does meaningfully different things depending on which arguments are omitted, that functionality can be split into separate, clearly named functions.

Python is designed for short, quickly-written scripts where this is not a major concern. For large-scale production code, default arguments require more care.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
