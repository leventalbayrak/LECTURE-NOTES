
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Boolean Algebra

## Table of Contents

- [Introduction](#introduction)
- [The Three Fundamental Boolean Operators](#the-three-fundamental-boolean-operators)
  - [The AND Operator](#the-and-operator)
  - [The OR Operator](#the-or-operator)
  - [The NOT Operator](#the-not-operator)
- [Boolean Algebra Notation](#boolean-algebra-notation)
- [De Morgan's Laws](#de-morgans-laws)
- [Operator Precedence](#operator-precedence)
- [Ways to Think About Boolean Logic](#ways-to-think-about-boolean-logic)
  - [1. Arithmetic Analogy](#1-arithmetic-analogy)
  - [2. Number Line (for range conditions)](#2-number-line-for-range-conditions)
  - [3. Venn Diagrams (for set membership)](#3-venn-diagrams-for-set-membership)
- [Exclusive OR (XOR)](#exclusive-or-xor)
- [Boolean Logic in Hardware](#boolean-logic-in-hardware)
- [Practical Tips](#practical-tips)
- [Summary](#summary)

## Introduction

Boolean algebra is a fundamental concept in computer science that deals with binary logic - operations that result in either **true** or **false** values. These concepts are the foundation of how computers make decisions and perform computations at the hardware level.

## The Three Fundamental Boolean Operators

There are three basic boolean operators that form the building blocks of all logical operations:

1. **AND** - Both conditions must be true
2. **OR** - At least one condition must be true
3. **NOT** - Flips/inverts the boolean value

### The AND Operator

The AND operator returns true **only when both** inputs are true.

**Truth Table:**

| A | B | A AND B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

**Think of it as multiplication:** Using 1 for true and 0 for false, AND works like multiplication:
- 1 × 1 = 1 (true AND true = true)
- 1 × 0 = 0 (true AND false = false)
- 0 × 1 = 0 (false AND true = false)
- 0 × 0 = 0 (false AND false = false)

**Syntax variations across languages:**
- `and` (Python)
- `.` (mathematical notation)
- `&` or `&&` (many programming languages)

**Example:**
```python
if age > 10 and gpa > 4.8:
    print("play Nintendo")
```
This only executes if **both** age is greater than 10 **and** GPA is greater than 4.8.

### The OR Operator

The OR operator returns true when **at least one** input is true. It only returns false when **both** inputs are false.

**Truth Table:**

| A | B | A OR B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

**Think of it as addition:** Using 1 for true and 0 for false, OR works like addition (where anything non-zero is true):
- 1 + 1 = 2 → true (true OR true = true)
- 1 + 0 = 1 → true (true OR false = true)
- 0 + 1 = 1 → true (false OR true = true)
- 0 + 0 = 0 → false (false OR false = false)

**Syntax variations across languages:**
- `or` (Python)
- `+` (mathematical notation)
- `|` or `||` (many programming languages)

**Example:**
```python
if age > 10 or gpa > 4.8:
    print("play Nintendo")
```
This executes if **either** age is greater than 10 **or** GPA is greater than 4.8 (or both).

### The NOT Operator

The NOT operator inverts/flips the boolean value. True becomes false, false becomes true.

**Truth Table:**

| A | NOT A |
|---|-------|
| True | False |
| False | True |

**Syntax variations across languages:**
- `not` (Python)
- `!` (many programming languages)
- `~` (bitwise NOT in some languages)
- Bar over the expression (mathematical notation)
- Hat/caret symbol (in some notations)

**Example:**
```python
if not(age <= 10):
    print("old enough")
```

## Boolean Algebra Notation

In mathematical notation, we often represent boolean operations as:

- **AND** as `·` (like multiplication): `A · B` or just `AB`
- **OR** as `+` (like addition): `A + B`
- **NOT** as a bar over the variable: `Ā` (or `!A` in code)

This notation helps because AND behaves like multiplication and OR behaves like addition when using 1 for true and 0 for false.

## De Morgan's Laws

De Morgan's Laws are powerful transformation rules that let you rewrite boolean expressions in equivalent forms:

**Law 1:** `NOT(A AND B) = NOT A OR NOT B`

**Law 2:** `NOT(A OR B) = NOT A AND NOT B`

**Practical Example:**

These two statements are logically equivalent:

```python
# Version 1
if age > 10 and gpa > 4.8:
    print("play nintendo")

# Version 2 (using De Morgan's Law)
if not(age <= 10 or gpa <= 4.8):
    print("play nintendo")
```

**Why it works:**
- NOT(age > 10) becomes (age <= 10)
- NOT(gpa > 4.8) becomes (gpa <= 4.8)
- AND becomes OR when you apply NOT to the entire expression

**Memory trick:** When you distribute the NOT:
1. Flip each condition (> becomes <=, < becomes >=, etc.)
2. Flip the operator (AND becomes OR, OR becomes AND)

## Operator Precedence

When combining multiple boolean operators, the order of evaluation matters. Python evaluates boolean operators in this order:

1. **NOT** (highest precedence)
2. **AND**
3. **OR** (lowest precedence)

**Examples:**

```python
# Expression: not A or B and C
# Evaluates as: (not A) or (B and C)
# NOT is done first, then AND, then OR

# Expression: A and B or C
# Evaluates as: (A and B) or C
# AND is done before OR

# Expression: A or B and not C
# Evaluates as: A or (B and (not C))
# NOT first, then AND, then OR
```

**Best Practice:** Use parentheses to make your intentions clear, even when not strictly necessary:

```python
# Less clear
if age > 10 and gpa > 4.0 or stars > 4.5:
    # Does this mean: (age > 10 AND gpa > 4.0) OR stars > 4.5?
    # Or: age > 10 AND (gpa > 4.0 OR stars > 4.5)?
    pass

# More clear
if (age > 10 and gpa > 4.0) or stars > 4.5:
    # Clearly: either both age AND gpa conditions, OR high stars
    pass
```

## Ways to Think About Boolean Logic

Boolean logic can be understood through several different mental models. Use whichever helps you understand a particular problem.

### 1. Arithmetic Analogy

- **AND = Multiplication** (anything × 0 = 0, must have all 1s to get 1)
- **OR = Addition** (anything + 1 gives non-zero result)
- **NOT = Negation** (flips the value)

### 2. Number Line (for range conditions)

When working with numeric ranges, draw a number line and mark the regions:

**Example:** "Temperature between 65 and 74 is comfortable"
```python
if temperature > 65 and temperature < 74:
    print("comfortable")
```

- Draw a number line
- Mark 65 and 74
- Shade the region above 65 (first condition)
- Shade the region below 74 (second condition)
- The **AND** means the **intersection** (overlap) of shaded regions

**Example:** "Extreme temperatures (very cold or very hot)"
```python
if temperature < 60 or temperature > 80:
    print("extreme")
```

- Mark 60 and 80 on number line
- Shade everything below 60 (first condition)
- Shade everything above 80 (second condition)
- The **OR** means the **union** (all shaded regions combined)

### 3. Venn Diagrams (for set membership)

Think of each condition as a circle, with the full space representing all possibilities.

**AND = Intersection** (the overlapping middle region)
- Example: People wearing glasses AND watches
- Only people with both glasses and watches

**OR = Union** (all covered regions)
- Example: People wearing glasses OR watches
- Anyone with glasses, watches, or both

**NOT = Outside the circle**
- Example: NOT wearing glasses
- Everyone outside the "wearing glasses" circle

## Exclusive OR (XOR)

XOR is a special operator that returns true when inputs are **different**, and false when they're the **same**.

**Truth Table:**

| A | B | A XOR B |
|---|---|---------|
| True | True | False |
| True | False | True |
| False | True | True |
| False | False | False |

**Key Properties:**
- XOR is a **difference detector** - it "lights up" when inputs differ
- It's false when both inputs are the same (both true or both false)

**Building XOR from basic operators:**
```python
# XOR can be expressed as:
# (A and not B) or (not A and B)

# Example: People with glasses OR watches, but NOT both
# True for: only glasses, or only watch
# False for: both glasses and watch, or neither
```

**Why XOR Matters:**
- XOR is fundamental to computer arithmetic (binary addition)
- In binary: 1 + 1 = 10 (0 with carry), which is exactly what XOR produces (0) plus a carry bit
- This is how calculators and CPUs perform addition

## Boolean Logic in Hardware

Boolean operations can be implemented using physical switches and circuits:

**AND Gate (Series Circuit):**
- Two switches in series with a light bulb
- Light only turns on when **both** switches are closed
- If either switch is open, circuit is broken

**OR Gate (Parallel Circuit):**
- Two switches in parallel with a light bulb
- Light turns on when **either** switch is closed
- Only stays off when **both** switches are open

**Building Complex Operations:**
- NOT, AND, and OR gates can be combined to create XOR
- XOR gates can be combined to create adders
- Adders can be combined to create calculators
- This is the foundation of all computer processors

**Modern Computers:**
- Everything in memory is represented as on/off states (1s and 0s)
- All computation reduces to billions of boolean operations
- Boolean algebra is what makes computers possible

## Practical Tips

1. **Combining conditions:** You can combine multiple conditions to avoid deep nesting
   ```python
   # Instead of nested ifs:
   if age > 10:
       if gpa > 4.8:
           print("reward")

   # Use AND:
   if age > 10 and gpa > 4.8:
       print("reward")
   ```

2. **Complex expressions:** Break them down step by step, or transform using De Morgan's Laws

3. **Number line technique:** For numeric ranges, drawing a number line helps visualize AND (intersection) vs OR (union)

4. **Use parentheses:** Make complex expressions clear and avoid relying on precedence rules

5. **Truth tables:** When confused, write out a truth table to understand what an expression does

## Summary

- **AND:** Both must be true (multiplication, intersection)
- **OR:** At least one must be true (addition, union)
- **NOT:** Inverts the value
- **XOR:** True when inputs differ
- **Precedence:** NOT > AND > OR (use parentheses for clarity)
- **De Morgan's Laws:** Transform between AND/OR by flipping operators and conditions
- **Think:** Arithmetic, number lines, Venn diagrams, or circuits - use what helps!

Boolean algebra is fundamental to programming logic and computer hardware. Mastering these concepts will help you write better conditional logic and understand how computers work at the most basic level.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
