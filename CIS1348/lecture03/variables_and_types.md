
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Variables, Types, and Problem Solving in Python

## Table of Contents

- [1. Quick Review: Computer Architecture (Von Neumann)](#1-quick-review-computer-architecture-von-neumann)
- [2. Why Not Raw CPU Instructions?](#2-why-not-raw-cpu-instructions)
- [3. Variables and the Memory Model](#3-variables-and-the-memory-model)
- [4. Data Types](#4-data-types)
  - [4.1 Integer (int)](#41-integer-int)
  - [4.2 Float (float)](#42-float-float)
  - [4.3 Character (char)](#43-character-char)
  - [4.4 String (str)](#44-string-str)
- [5. Math Operations in Python](#5-math-operations-in-python)
- [6. Input, Transform, Output — A Problem-Solving Framework](#6-input-transform-output--a-problem-solving-framework)
- [7. Evolution of a Program: Temperature Converter](#7-evolution-of-a-program-temperature-converter)
  - [Phase 1: Manual Brute Force](#phase-1-manual-brute-force)
  - [Phase 2: Using Variables](#phase-2-using-variables)
  - [Phase 3: Introducing Functions](#phase-3-introducing-functions)
  - [Phase 4: Variable Incrementing (+=)](#phase-4-variable-incrementing-)
  - [Phase 5: The while Loop](#phase-5-the-while-loop)
- [8. Interactive Input with input() and float()](#8-interactive-input-with-input-and-float)
- [9. Python Quirks: Operator Overloading on Strings](#9-python-quirks-operator-overloading-on-strings)

---

## 1. Quick Review: Computer Architecture (Von Neumann)

A computer follows the **Von Neumann architecture**. There are two main pieces:

1. **Memory** — a grid (table) of storage cells. Think of it like a spreadsheet. Every cell can hold a pattern of bits.
2. **CPU** — sits on top of memory and executes **instructions**.

The CPU can do a small number of things:

| Instruction Type | What It Does |
|:---|:---|
| **Copy / Move** | Move data from one memory location to another |
| **Arithmetic** | Add, subtract, multiply, divide |
| **Jump** | Jump forward or backward to a different instruction |
| **Conditional Jump** | Jump only if a condition is true (e.g., "if X < 90, jump back") |

Instructions execute **sequentially** (top to bottom) unless a jump instruction redirects the CPU elsewhere. This ability to jump — both forward and backward, conditionally or unconditionally — is what allows computers to do complicated work.

---

## 2. Why Not Raw CPU Instructions?

Two reasons we don't just write raw CPU instructions:

1. **Instructions are too primitive.** Each instruction does one tiny thing. To accomplish anything meaningful you need an enormous number of them. It's like having to control every individual muscle fiber just to walk across the room.

2. **Different CPU architectures have different instruction sets.** For example, most desktops and laptops use x86-64 (also called AMD64) — a shared instruction set used by both AMD and Intel. But ARM-based chips like Apple M-series, Qualcomm Snapdragon, and Google Tensor use a completely different instruction set. Code written directly for one instruction set won't run on another. We need a universal, human-readable language that can be translated to any CPU's instruction set.

A programming language must be:
- **Precise** — no ambiguity (you can't say "go get bread"; you must say which store, which aisle).
- **Reproducible** — the same statement always produces the same result, regardless of the underlying CPU.

---

## 3. Variables and the Memory Model

Memory is an addressable grid. You can think of it like an Excel sheet where every cell has coordinates (e.g., D2, C5).

```
Put 2 in cell D2
Put 4 in cell C5
Cell B1 = D2 * C5    →  B1 = 8
```

This works, but addressing cells by coordinates is painful. Programming languages let you **name** cells instead:

```python
x = 2
y = 4
z = x * y
```

These named labels are called **variables**. Behind the scenes, `x`, `y`, and `z` each correspond to a location in the memory grid — but the language abstracts that away so you never have to think about coordinates.

### Why Meaningful Names Matter

Consider these two versions of the same calculation:

```python
# Version A
x = 100
y = 0.0825
z = x * y
```

```python
# Version B
price = 100
tax_rate = 0.0825
tax = price * tax_rate
```

From the computer's perspective, Version A and Version B are identical. But Version B makes your **intent** clear. If you accidentally wrote `tax = price + tax_rate`, a reader would immediately notice something is wrong — you don't *add* a tax rate to a price, you *multiply*. With `z = x + y`, no one can spot the mistake because the names carry no meaning.

Using descriptive variable names is not about elegance or style — it's a practical way of communicating code intent so you and others can catch mistakes and bugs. That said, short variable names are perfectly fine when the context is clear (e.g., `i` in a loop counter, or `x` and `y` for coordinates). The goal is correct and efficient code, not naming for its own sake.

---

## 4. Data Types

Every cell in memory is physically identical — just a pattern of bits (think of each cell as a tiny grid of LED lights that are either on or off). The **type** tells the programming language *how to interpret* that pattern.

Somewhere alongside each value, the language stores metadata: "interpret this pattern as an integer," or "interpret this pattern as a character."

### 4.1 Integer (`int`)

- Whole numbers: `10`, `-5`, `0`
- Fit in a single memory cell.
- Processed by the **ALU** (Arithmetic and Logic Unit) on the CPU.
- Faster to compute because the circuitry for whole-number arithmetic is simpler.

### 4.2 Float (`float`)

- Decimal numbers: `10.5`, `0.0825`, `-3.14`
- Fit in a single memory cell.
- Processed by the **FPU** (Floating Point Unit) — physically separate circuitry from the ALU.
- Slower than integer operations because the hardware must track the decimal point position and exponent.

**Why the distinction matters:** Integer vs. float is not just conceptual (you count students as `32`, not `32.6`). The hardware is literally different. Choosing integers over floats when appropriate can improve performance. For example, in graphics and game programming, pixel coordinates are integers — using floats for screen positions would waste processing time on unnecessary decimal precision. Similarly, when counting iterations or indexing into a list, integers are both semantically correct and faster.

### 4.3 Character (`char`)

- A single character: `'A'`, `'!'`, `'7'`
- Fits in one cell.
- In Python there is no separate `char` type — a single character is just a string of length 1. In languages like C, C++, and Java, `char` is its own type, and single quotes are strictly for characters while double quotes are for strings.

### 4.4 String (`str`)

- A sequence of characters: `"Hello"`, `"apple"`, `"Room 404"`, `"user@email.com"`, `"Price: $9.99"`, `"#trending"`, `"3.14159"`
- **Does not fit in one cell** — it stretches across multiple consecutive cells.
- Not a standard hardware type. The programming language must manage strings with extra logic.

**How strings are stored (low level):**

In C, a string is stored as consecutive characters followed by a **null terminator** (a cell where all bits are zero). The system reads characters one by one until it hits the null terminator and stops.

This is a source of security vulnerabilities:
- If the null terminator is accidentally overwritten, the system keeps reading past the string into adjacent memory — potentially leaking passwords or other sensitive data.
- This is the basis of **buffer overflow** attacks.

In Python, strings are managed safely — you never deal with null terminators or raw memory. But you should understand what's happening underneath.

### Summary Table

| Type | Python Name | Description | Example |
|:---|:---|:---|:---|
| Integer | `int` | Whole numbers | `10`, `-5` |
| Float | `float` | Decimal numbers | `10.5`, `60.0` |
| String | `str` | Sequence of characters | `"Hello World"` |
| Character | `char` | Single character (conceptual in Python) | `'A'`, `'!'` |

### String Details

- In Python, `'single'` and `"double"` quotes are interchangeable.
- In C++ and Java, single quotes are for `char`, double quotes are for `str`.
- `\n` is an escape character that produces a newline.

---

## 5. Math Operations in Python

| Operation | Symbol | Example |
|:---|:---|:---|
| Addition | `+` | `3 + 2` → `5` |
| Subtraction | `-` | `10 - 4` → `6` |
| Multiplication | `*` | `5 * 3` → `15` |
| Division | `/` | `9 / 2` → `4.5` |
| Power | `**` | `2 ** 3` → `8` |
| Increment | `+=` | `x += 5` is the same as `x = x + 5` |

Python math works exactly like typing into a calculator. Standard order of operations applies; use parentheses to control grouping.

---

## 6. Input, Transform, Output — A Problem-Solving Framework

Every computational problem has three parts:

```
INPUT  →  TRANSFORM  →  OUTPUT
```

There is always an input, there is always an output, and in the middle there is always a transform. The whole point of computers is to **transform input into output**. When you encounter any programming problem, the first thing you should do is identify all three parts. If any part is missing or vague, the problem statement is incomplete — and you need to ask questions before writing code.

This is a critical thinking skill. Problem statements in the real world are almost always incomplete. Part of your job as a programmer is to interrogate the requirements and fill in the gaps before you start coding.

### Why This Matters

Most beginners jump straight into writing code. But if you haven't clearly defined the input, the transform, and the output, you don't actually know what you're building. You'll waste time solving the wrong problem, or you'll write code that sort of works.

### Example: Temperature Conversion

> "Go over all Fahrenheit values from 60 to 90 in Celsius."

This sounds clear, but it's actually a bad problem statement. Let's break it down:

| Part | Question | Answer |
|:---|:---|:---|
| **Input** | Where does it start? Where does it end? What is the step? | Start at 60, end at 90... but step by what? |
| **Transform** | What formula? | C = (F - 32) * 5/9 |
| **Output** | What do we do with the result? | Not specified — print to screen? Save to a file? |

Without the step size, the problem is ambiguous. Do we mean 60, 60.1, 60.2...? Or 60, 61, 62...? Or 60, 65, 70...? And without specifying the output, the calculation just dissipates as CPU heat. You need to ask: what's the output? The answer here is: print each converted value to the console/terminal.

This is an important point: how carefully you analyze and define the input, transform, and output directly shapes the code you write. Different interpretations of the same problem will lead to significantly different implementations — different logic, different performance characteristics, different correctness guarantees — even when the overall goal of the program is the same. Two programmers given the same vague problem statement can produce two very different programs, and the one who analyzed the problem more precisely will almost always write better code.

A complete problem statement would be: "Convert Fahrenheit values from 60 to 90 in increments of 5 to Celsius using C = (F - 32) * 5/9, and print each result to the console."

Now all three parts are defined:
- **Input:** Fahrenheit values from 60 to 90, stepping by 5
- **Transform:** C = (F - 32) * 5/9
- **Output:** Print each Celsius value to the console

### Example: Video Games

Even a game follows this pattern — 60 times per second:

| Part | What it is |
|:---|:---|
| **Input** | Keyboard state + mouse position (sampled 60 times per second) |
| **Transform** | Game logic — apply rules, check collisions, update physics, check other players |
| **Output** | Rendered frame (pixels on screen) + audio sample (~20 milliseconds of sound) |

Think of it this way: imagine taking a snapshot of the keyboard and mouse state, and from that single snapshot, producing one frame of video and a slice of audio. The game does this 60 times every second. Each cycle is an input-transform-output problem.

### Applying the Framework

Every programming problem — from a homework exercise to a billion-dollar system — is an input-transform-output problem. Before you write a single line of code:

1. **Identify the input.** What data goes in? Where does it come from? What are the boundaries and edge cases?
2. **Define the transform.** What rules, formulas, or logic convert the input into the desired result?
3. **Specify the output.** What comes out? Where does it go? In what format?

If you can't clearly answer all three, you don't yet understand the problem well enough to solve it.

---

## 7. Evolution of a Program: Temperature Converter

**Task:** Print Celsius values for Fahrenheit 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, and 90.0.

**Formula:** C = (F - 32) x 5/9

The same problem is solved five different ways below, each improving on the last. This progression demonstrates core programming concepts: variables, functions, incrementing, and loops.

### Phase 1: Manual Brute Force

Hard-code the math for each value. Simple, but repetitive.

```python
print((60.0 - 32) * 5/9)
print((65.0 - 32) * 5/9)
print((70.0 - 32) * 5/9)
print((75.0 - 32) * 5/9)
print((80.0 - 32) * 5/9)
print((85.0 - 32) * 5/9)
print((90.0 - 32) * 5/9)
```

### Phase 2: Using Variables

Store the Fahrenheit value in a variable. The formula is slightly easier to read, but still repeated.

```python
f_temp = 60.0
c_temp = (f_temp - 32) * 5/9
print(c_temp)

f_temp = 65.0
c_temp = (f_temp - 32) * 5/9
print(c_temp)

f_temp = 70.0
c_temp = (f_temp - 32) * 5/9
print(c_temp)

f_temp = 75.0
c_temp = (f_temp - 32) * 5/9
print(c_temp)

f_temp = 80.0
c_temp = (f_temp - 32) * 5/9
print(c_temp)

f_temp = 85.0
c_temp = (f_temp - 32) * 5/9
print(c_temp)

f_temp = 90.0
c_temp = (f_temp - 32) * 5/9
print(c_temp)
```

### Phase 3: Introducing Functions

Define the conversion logic **once** with a function. Reuse it as many times as needed.

```python
def f_to_c(f):
    return (f - 32) * 5/9

print(f_to_c(60.0))
print(f_to_c(65.0))
print(f_to_c(70.0))
print(f_to_c(75.0))
print(f_to_c(80.0))
print(f_to_c(85.0))
print(f_to_c(90.0))
```

**What is a function?** A function is a named block of code that the CPU can **jump to** and **return from**.

- `def` means "define" — it tells Python: "this is a section of code you can jump to later."
- When you call `f_to_c(60.0)`, execution jumps to the function body, runs the formula, and `return` brings it back to where the call was made.
- If the formula changes (say, the constant turns out to be 4/9 instead of 5/9), you fix it in **one place** instead of hunting through every copy.

### Phase 4: Variable Incrementing (+=)

Instead of typing each value manually, use `+=` to update the variable.

```python
def f_to_c(f):
    return (f - 32) * 5/9

temp = 60.0
print(f_to_c(temp))

temp += 5.0
print(f_to_c(temp))

temp += 5.0
print(f_to_c(temp))

temp += 5.0
print(f_to_c(temp))

temp += 5.0
print(f_to_c(temp))

temp += 5.0
print(f_to_c(temp))

temp += 5.0
print(f_to_c(temp))
```

`temp += 5.0` is shorthand for `temp = temp + 5.0` — the new value of `temp` equals the old value plus 5.

### Phase 5: The while Loop

Let the computer handle the repetition automatically.

```python
def f_to_c(f):
    return (f - 32) * 5/9

temp = 60.0
while temp <= 90.0:
    print(f_to_c(temp))
    temp += 5.0
```

**How `while` works:**

1. Check the condition (`temp <= 90.0`). If true, execute the indented body.
2. At the end of the body, an invisible **jump instruction** takes you back to the condition check.
3. Repeat until the condition is false, then jump past the loop to whatever comes next.

This replaces all the manual repetition from previous phases with three lines. The loop processes 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, and 90.0 automatically.

---

## 8. Interactive Input with `input()` and `float()`

Python's `input()` function reads text from the user. It **always returns a string**, so you must convert it if you need a number.

```python
def f_to_c(f):
    return (f - 32) * 5/9

fahrenheit = input("Enter temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit)
celsius = f_to_c(fahrenheit)
print(celsius)
```

Or more concisely, nesting the calls:

```python
def f_to_c(f):
    return (f - 32) * 5/9

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = f_to_c(fahrenheit)
print(celsius)
```

Key built-in functions:

| Function | Purpose |
|:---|:---|
| `print()` | Display text or values to the console |
| `input()` | Read text from the user (always returns `str`) |
| `int()` | Convert a value to an integer |
| `float()` | Convert a value to a floating-point number |

---

## 9. Python Quirks: Operator Overloading on Strings

Python reuses the `+` and `*` operators for strings, but the behavior is **not mathematical** — it's an arbitrary design decision.

| Expression | Result | Explanation |
|:---|:---|:---|
| `2 + 3` | `5` | Normal arithmetic |
| `"apple" + "orange"` | `"appleorange"` | **Concatenation** — glues strings together |
| `"apple" + 5` | **TypeError** | Crashes — can't add a string and an integer |
| `"apple" * 2` | `"appleapple"` | **Repetition** — makes 2 copies of the string |

These are arbitrary language choices. There is no mathematical definition for "adding" two words. The Python designers simply decided that `+` on two strings means concatenation and `*` on a string and integer means repetition. Other decisions would have been equally valid.

**The takeaway:** Learn the **programming concepts** (variables, functions, loops, types) — those transfer to every language. Language-specific quirks like string multiplication are just details you memorize for whichever language you're using.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
