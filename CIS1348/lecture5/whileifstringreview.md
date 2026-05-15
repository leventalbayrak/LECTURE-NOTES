
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Practice with While Loops, Operators, and Strings

## Table of Contents

- [1. Review: Type Conversions and String Concatenation](#1-review-type-conversions-and-string-concatenation)
- [2. While Loops](#2-while-loops)
  - [2.1 While Loop with a Condition](#21-while-loop-with-a-condition)
  - [2.2 Infinite Loops with `while True`](#22-infinite-loops-with-while-true)
  - [2.3 `break` — Exit a Loop Early](#23-break--exit-a-loop-early)
  - [2.4 `continue` — Skip to the Next Iteration](#24-continue--skip-to-the-next-iteration)
- [3. Operators](#3-operators)
  - [3.1 Equality `==` and Inequality `!=`](#31-equality--and-inequality-)
  - [3.2 Modulus `%`](#32-modulus-)
  - [3.3 Integer Division `//`](#33-integer-division-)
  - [3.4 Exponentiation `**`](#34-exponentiation-)
  - [3.5 Operator Overloading](#35-operator-overloading)
- [4. Strings](#4-strings)
  - [4.1 `len()` — String Length](#41-len--string-length)
  - [4.2 String Comparison](#42-string-comparison)
  - [4.3 Indexing (Brief Intro)](#43-indexing-brief-intro)
- [5. F-Strings and Formatting](#5-f-strings-and-formatting)
  - [5.1 Basic F-Strings](#51-basic-f-strings)
  - [5.2 Controlling Decimal Places (`.2f`, `.4f`)](#52-controlling-decimal-places-2f-4f)
  - [5.3 Scientific Notation](#53-scientific-notation)
- [6. Escape Characters](#6-escape-characters)
- [7. Importing Libraries — `import random`](#7-importing-libraries--import-random)
- [8. Common Patterns](#8-common-patterns)
  - [8.1 Accumulator Pattern](#81-accumulator-pattern)
  - [8.2 Counter Pattern](#82-counter-pattern)
  - [8.3 `+=` Shorthand](#83--shorthand)
  - [8.4 Flags (Boolean Variables for Tracking State)](#84-flags-boolean-variables-for-tracking-state)
- [9. How to Write Code — The "Sculptor" Approach](#9-how-to-write-code--the-sculptor-approach)
- [10. Code Examples](#10-code-examples)
  - [Example 0a: Count from 1 to N](#example-0a-count-from-1-to-n)
  - [Example 0b: Count from N Down to 1](#example-0b-count-from-n-down-to-1)
  - [Example 0c: Sum of Even Numbers](#example-0c-sum-of-even-numbers)
  - [Example 1a: Password Checker](#example-1a-password-checker)
  - [Example 1b: String Equality Check](#example-1b-string-equality-check)
  - [Example 2: Mini Calculator](#example-2-mini-calculator)
  - [Example 3: Shopping Cart](#example-3-shopping-cart)
  - [Example 4: Rock Paper Scissors](#example-4-rock-paper-scissors)
  - [Example 5: Baby Math School](#example-5-baby-math-school)

---

## 1. Review: Type Conversions and String Concatenation

From previous lectures you already know these — quick refresher:

- **`int()`** — converts a value to an integer. Most commonly used around `input()` to turn user input (which is always a string) into a number: `int(input("enter N:"))`.
- **`float()`** — converts a value to a floating-point number. Use this when the value can have decimals: `float(input("enter price:"))`.
- **`str()`** — converts a value to a string.
- **String concatenation with `+`** — you can glue strings together: `"hello" + " " + "world"` gives `"hello world"`.

---

## 2. While Loops

A `while` loop repeats a block of code as long as a condition is `True`. The moment the condition becomes `False`, the loop stops and the program continues to the code below it.

### 2.1 While Loop with a Condition

The most common form — you set up a variable, loop while some condition holds, and update the variable inside the loop:

```python
x = 1
while x <= 10:
    print(x)
    x += 1
```

**Important:** the condition is only checked at the **top** of the loop. If `x` changes inside the loop body, the loop does not immediately stop — it finishes the current iteration and *then* checks again at the top.

For example, if `x` is `6` and the condition is `x <= 6`, and inside the loop you do `x += 2` (making `x` become `8`), any code *after* that `x += 2` in the same iteration still runs. The loop only realizes `x` is now `8` (and therefore `> 6`) when it goes back to the top to check the condition.

### 2.2 Infinite Loops with `while True`

Sometimes you don't know in advance how many times the loop should run. You want it to keep going until the user decides to stop. Use `while True` for this — it creates a loop that runs forever, and you use `break` to exit:

```python
while True:
    command = input("enter command: ")
    if command == "quit":
        break
    # ... do work ...
```

This pattern is used for menu-driven programs, calculators, games — anything that should keep running until the user says stop.

### 2.3 `break` — Exit a Loop Early

`break` immediately exits the loop. Execution jumps to the first line of code *after* the loop.

```python
while True:
    pw = input("enter password: ")
    if pw == "secret":
        print("Access granted!")
        break        # <-- exits the loop right here
    print("Wrong, try again.")

print("This runs after the loop ends.")
```

You can use `break` in any loop, not just `while True` loops.

### 2.4 `continue` — Skip to the Next Iteration

`continue` skips the rest of the current iteration and jumps back to the top of the loop (where the condition is checked again).

```python
while True:
    price = float(input("enter price: "))
    if price < 0:
        print("Price must be positive!")
        continue     # <-- goes back to the top, asks for input again
    # ... process the valid price ...
```

**`break` vs `continue`:**
| Keyword    | What it does                                    |
|------------|------------------------------------------------|
| `break`    | Exits the loop entirely                        |
| `continue` | Skips the rest of this iteration, loops again  |

---

## 3. Operators

### 3.1 Equality `==` and Inequality `!=`

- `==` checks if two values are **equal**. Returns `True` or `False`.
- `!=` checks if two values are **not equal**. Returns `True` or `False`.

```python
if password == "secret":
    print("correct")

if a != b:
    print("not the same")
```

**Do not confuse `=` (assignment) with `==` (comparison).** `x = 5` stores the value 5 in `x`. `x == 5` asks "is `x` equal to 5?"

### 3.2 Modulus `%`

The modulus operator gives you the **remainder** of an integer division.

```python
6 % 4    # result: 2   (6 divided by 4 = 1 remainder 2)
10 % 3   # result: 1   (10 divided by 3 = 3 remainder 1)
8 % 2    # result: 0   (8 divides evenly by 2)
```

Classic use: checking if a number is even or odd. If `x % 2 == 0`, then `x` is even.

### 3.3 Integer Division `//`

Regular division `/` in Python always gives you a float:

```python
100 / 10   # result: 10.0  (float, not int)
100 / 8    # result: 12.5
```

Integer division `//` throws away the decimal part and gives you just the whole number:

```python
100 // 10  # result: 10
100 // 8   # result: 12   (not 12.5 — the .5 is discarded)
```

`%` and `//` are closely related. `100 // 8` gives 12 (the quotient), and `100 % 8` gives 4 (the remainder). Together: 12 × 8 + 4 = 100.

### 3.4 Exponentiation `**`

Raises a number to a power:

```python
2 ** 4     # result: 16    (2 × 2 × 2 × 2)
2 ** -1    # result: 0.5   (1 / 2)
3 ** 3     # result: 27
```

### 3.5 Operator Overloading

The same operator can behave differently depending on the **type** of data it operates on. This is called **operator overloading**. It applies to all operators — `!=`, `==`, `+`, `>`, `<`, and others.

For example, `!=` with integers compares two numbers. `len()` returns an integer (the character count), so `len(a) != len(b)` is an integer comparison:

```python
len(a) != len(b)    # len() returns an int — this compares two integers (the lengths)
```

But `!=` with strings goes character by character through both strings to check if they match:

```python
a != b    # compares two strings, character by character
```

From the outside they look identical — both use `!=`. But behind the scenes they are two completely different operations. The integer comparison is instant. The string comparison has to walk through every character, which can be slow for very long strings.

This is why checking the length first is a smart shortcut: if the lengths don't match, you already know the strings can't be equal, and you saved the cost of comparing them character by character.

---

## 4. Strings

### 4.1 `len()` — String Length

`len()` returns the number of characters in a string:

```python
len("hello")    # result: 5
len("")          # result: 0
```

### 4.2 String Comparison

You can compare strings with `==` and `!=`. Python compares them character by character:

```python
"apple" == "apple"    # True
"apple" == "Apple"    # False  (case matters!)
"abc" != "xyz"        # True
```

### 4.3 Indexing (Brief Intro)

An **index** is an offset from the beginning of a sequence. In Python, indexing starts at **0**:

```
 A   P   P   L   E
 0   1   2   3   4
```

So the first character is at index 0, the second at index 1, and so on. You access individual characters with square brackets:

```python
word = "APPLE"
word[0]    # "A"
word[2]    # "P"
word[4]    # "E"
```

We will use this more in future lectures.

---

## 5. F-Strings and Formatting

### 5.1 Basic F-Strings

An f-string lets you embed variables directly inside a string. Put an `f` before the opening quote and wrap variables in `{}`:

```python
name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 20 years old.
```

Whatever is inside `{}` gets evaluated and its value is inserted into the string.

### 5.2 Controlling Decimal Places (`.2f`, `.4f`)

When displaying floats, you often want a fixed number of decimal places. Add `:.Nf` after the variable inside the braces, where `N` is the number of decimal digits:

```python
x = 1.543
print(f"{x:.2f}")    # Output: 1.54

x = 1.547
print(f"{x:.2f}")    # Output: 1.55  (rounds correctly)

x = 3.14159
print(f"{x:.4f}")    # Output: 3.1416  (4 decimal places)
```

This is primarily for **display purposes** — it rounds for printing but does not change the actual value of the variable.

### 5.3 Scientific Notation

**Why we need it.** When working with very large or very small numbers, writing them out in full is error-prone. If you forget a single zero, the value changes by a factor of 10. If you add an extra zero, same problem in the other direction. For example, it is easy to miscount the zeros in `10000000` vs `100000000` — they differ by 10×, but both look similar at a glance. With scientific notation, `1e7` vs `1e8` makes the exponent (the number of zeros) explicit. The magnitude is impossible to misread.

Scientific notation is a way to write very large or very small numbers compactly:

- `1e5` means 1 × 10⁵ = 100,000
- `1e-5` means 1 × 10⁻⁵ = 0.00001
- `3.1415e5` means 3.1415 × 10⁵ = 314,150

You can display a number in scientific notation with `:e` in an f-string:

```python
x = 3.1415e5
print(f"{x:e}")      # Output: 3.141500e+05

x = 3.1415e-5
print(f"{x:e}")      # Output: 3.141500e-05
```

When you see a number like `3.14e+05` in output, don't be confused — it's just a regular number displayed differently.

---

## 6. Escape Characters

Escape characters are special sequences inside strings that produce characters you can't type directly:

| Escape | What it produces          |
|--------|--------------------------|
| `\n`   | New line (line break)    |
| `\t`   | Tab (horizontal indent)  |
| `\"`   | A literal quote mark `"` |

```python
print("Line one\nLine two")
# Output:
# Line one
# Line two

print("Name:\tAlice")
# Output:
# Name:   Alice

print("She said \"hello\"")
# Output:
# She said "hello"
```

---

## 7. Importing Libraries — `import random`

Python has built-in libraries that provide extra functionality. To use one, `import` it at the top of your program:

```python
import random
```

**`random.randint(a, b)`** — returns a random integer between `a` and `b`, **inclusive of both endpoints**. So `random.randint(0, 2)` can return 0, 1, or 2.

```python
import random
number = random.randint(1, 100)    # random number from 1 to 100
```

---

## 8. Common Patterns

### 8.1 Accumulator Pattern

Start with a variable at 0 (or empty), then keep adding to it inside a loop:

```python
total = 0
# inside a loop:
total = total + price
```

Used whenever you need to build up a sum, a string, a running total, etc.

### 8.2 Counter Pattern

A variable that counts how many times something happens:

```python
count = 0
# inside a loop:
count = count + 1
```

### 8.3 `+=` Shorthand

`x += 1` is the same as `x = x + 1`. Works with other operators too:

```python
x += 5     # same as x = x + 5
x -= 1     # same as x = x - 1
x *= 2     # same as x = x * 2
```

### 8.4 Flags (Boolean Variables for Tracking State)

A **flag** is a variable that you use to remember whether something happened. You set it before a loop, update it inside the loop when the event occurs, and check it after the loop to decide what to do.

```python
found = False              # flag starts as False

while ...:
    if some_condition:
        found = True       # event happened — flip the flag
        break

if found:
    print("found it!")
else:
    print("not found")
```

Flags are useful when a loop can end for multiple reasons and you need to know *which* reason after the loop is done. Instead of trying to figure it out from counters or other variables, a flag gives you a clear, unambiguous answer: did the thing happen or not?

#### The `bool` Type

A flag is typically a **`bool`** — short for *boolean*. `bool` is a type in Python, just like `int` or `float`. A `bool` variable can hold exactly one of two values: `True` or `False`.

```python
type(True)     # <class 'bool'>
type(42)       # <class 'int'>
```

Under the hood, `bool` is a special kind of integer: `True` is literally `1` and `False` is literally `0`. Python just gives them readable names.

```python
True == 1      # True
False == 0     # True
True + True    # 2  (bool arithmetic works exactly like integers)
```

This is why you sometimes see `if correctlyguessed == True:` written simply as `if correctlyguessed:` — they mean the same thing. Both forms are correct; the shorter one is more common in practice.

#### Integer Flags

A flag does not have to be `True`/`False`. Sometimes an integer is more useful when you need to track more than two states:

```python
state = 0        # 0 = not started, 1 = in progress, 2 = done, -1 = error
```

For simple yes/no decisions, `bool` is clearer and more readable. Use an integer flag when you need to distinguish more than two outcomes from a loop.

---

## 9. How to Write Code — The "Sculptor" Approach

This is one of the most important lessons from this lecture. When you write code:

1. **Start rough.** Don't try to write perfect code in one shot. Get the basic structure down first, even if parts are wrong or incomplete. Think like a sculptor — start with the big block and carve the rough shape before adding detail.

2. **One change at a time.** Make one small change, then run the program. Don't make five changes and then try to figure out which one broke things.

3. **Predict before you run.** Before pressing Enter, tell yourself what you *expect* to see. Then compare your prediction to reality. If they don't match, the gap tells you exactly where to look.
   - Don't observe output and try to make sense of it after the fact.
   - Instead: form an expectation, run, compare.

4. **Don't worry about details early.** Need user input? Hard-code a number for now (`N = 10`). Get the loop working first, then replace the hard-coded value with `input()`.

5. **Refactor after it works.** Once the code runs correctly, look for redundancies and clean them up.

---

## 10. Code Examples

### Example 0a: Count from 1 to N

**Problem:** Write a program that asks the user for a number N and prints all numbers from 1 to N.

**Concepts used:** `while` loop, counter increment, `int(input())`

```python
"""
program to print out numbers from 1 to N, ask user to enter N
"""

x = 1
N = int(input("enter N:"))
while x <= N:
    print(x)
    x += 1
```

Commented version:

```python
x = 1                          # start counting from 1
N = int(input("enter N:"))     # get upper limit from user, convert to int
while x <= N:                  # keep going as long as x hasn't passed N
    print(x)                   # print the current number
    x += 1                     # move to the next number
```

---

### Example 0b: Count from N Down to 1

**Problem:** Write a program that asks the user for a number N and counts down from N to 1.

**Concepts used:** `while` loop, decrementing counter

```python
"""
program to print out numbers from N down to 1
"""

current = int(input("enter N:"))
while current >= 1:
    print(current)
    current -= 1
```

Commented version:

```python
current = int(input("enter N:"))   # user enters the starting number
while current >= 1:                # keep going until we pass 1
    print(current)                 # print current number
    current -= 1                   # decrement (go down by 1)
```

Note how this version uses a single variable `current` instead of having a separate `start` variable. During the live demo, the instructor started with both (`start = 10`, `current = start`) and then refactored by removing the redundancy.

---

### Example 0c: Sum of Even Numbers

**Problem:** Write a program that prints the sum of even numbers from 0 to a given limit.

**Concepts used:** Accumulator pattern, stepping by 2

```python
"""
program to print out sum of even numbers from 0 to 6
"""

total = 0
x = 0
while x <= 6:
    total += x
    x += 2

print(total)
```

Commented version:

```python
total = 0              # accumulator — starts at 0
x = 0                  # first even number
while x <= 6:          # loop through 0, 2, 4, 6
    total += x         # add current even number to the running sum
    x += 2             # jump to the next even number (skip odds entirely)

print(total)           # prints 12  (0 + 2 + 4 + 6 = 12)
```

**Why step by 2 instead of checking `x % 2 == 0`?** If you start at 0 and add 2 each time, every value of `x` is guaranteed to be even. There is no need to check — it's a shortcut.

**Order matters inside the loop.** This was demonstrated live in class:
- If you put `total += x` **before** `x += 2`: you add 0, 2, 4, 6 → sum is 12 (correct).
- If you put `x += 2` **before** `total += x`: you add 2, 4, 6, 8 → sum is 20 (wrong). The value of `x` gets updated before you use it, so you skip 0 and include 8 (which is past the intended range).

The condition `x <= 6` is only checked at the **top** of the loop. If `x` becomes 8 inside the loop body, the loop doesn't notice until the next check.

**What if you swap the order?** Here is the same loop with `x += 2` moved *before* `total += x`:

```python
# WRONG order — do NOT do this:
total = 0
x = 0
while x <= 6:
    x += 2       # x is updated first: becomes 2, 4, 6, 8
    total += x   # then added: skips 0, includes 8
print(total)     # prints 20, not 12
```

`x` reaches 8 inside the loop body, but the condition `x <= 6` isn't checked again until the top of the next iteration — by then it's too late, 8 has already been added. And 0 was never added because `x` was incremented before the first addition. This is the same principle as Section 2.1: the condition is only checked at the top.

---

### Example 1a: Password Checker

**Problem:** Write a program that checks a password. The password is stored in the code. The user gets a limited number of attempts.

**Concepts used:** `while` loop with condition, `break`, string equality `==`, counter, flag

There are two natural ways to write this program. Both work. They differ in *how they communicate the outcome* after the loop ends.

---

#### Version A — With a Flag

```python
"""
user enters a password program checks to see if they can login
3 tries maximum
"""

secretpassword = "!1234!"

correctlyguessed = False
count = 0
while count < 3:
    userinput = input("enter your password:")

    if userinput == secretpassword:
        correctlyguessed = True
        break

    count += 1
    print(f"you tried {count} times")

if correctlyguessed == True:
    print("welcome to the matrix")
else:
    print("the last 4 digits of your SSN is 3893, to find out more call 1-800-xxx-xxxx")
```

Commented version:

```python
secretpassword = "!1234!"

correctlyguessed = False          # flag — starts False, becomes True only on success
count = 0

while count < 3:                  # loop while tries remain
    userinput = input("enter your password:")

    if userinput == secretpassword:
        correctlyguessed = True   # flip the flag — correct guess!
        break                     # exit immediately, don't increment count

    count += 1                    # wrong guess — count this attempt
    print(f"you tried {count} times")

# after the loop: the flag tells us clearly why we stopped
if correctlyguessed == True:
    print("welcome to the matrix")
else:
    print("the last 4 digits of your SSN is 3893, to find out more call 1-800-xxx-xxxx")
```

**How it works:** the loop can exit for two reasons — correct password (`break`) or used all 3 tries (condition `count < 3` becomes `False`). The flag `correctlyguessed` is the unambiguous answer: it is only ever set to `True` when the password matched. After the loop, one simple check is all you need.

---

#### Version B — Without a Flag (Using the Counter Instead)

```python
"""
user enters a password and program tells them whether they can login or not
3 tries allowed
"""

password = "12345!"

count = 0
while count < 3:
    userinput = input("enter password:")

    if userinput == password:
        print("welcome to your bank account")
        break
    else:
        print("denied")

    count += 1

if count >= 3:
    print("locked out welcome to fbi jail")
```

Commented version:

```python
password = "12345!"

count = 0
while count < 3:
    userinput = input("enter password:")

    if userinput == password:
        print("welcome to your bank account")
        break                      # exit on success — count stays below 3
    else:
        print("denied")

    count += 1                     # wrong guess — increment

# after the loop: if count reached 3, we know the user never succeeded
if count >= 3:
    print("locked out welcome to fbi jail")
```

**How it works:** instead of a dedicated flag, this version repurposes the counter. If the user breaks out on a correct guess, `count` never reaches 3. If all tries are exhausted, `count` ends up at 3. So `count >= 3` is an indirect way of detecting "never logged in". It works, but you have to think about it more carefully than checking a flag.

---

**Version A vs Version B — which to use?**

| | Version A (flag) | Version B (counter) |
|---|---|---|
| Clarity | Very clear — `correctlyguessed` tells you exactly what happened | Requires reasoning about the counter value |
| Extra variable | Yes — one extra boolean | No — reuses the counter |
| When to prefer | When the loop can end for many reasons | When the counter alone is enough to distinguish outcomes |

For simple yes/no outcomes, the flag is usually cleaner. Use the counter approach when you already need the count and there are only two possible exit paths.

---

### Example 1b: String Equality Check

**Problem:** Let the user enter 2 strings and print whether they are equal or not.

**Concepts used:** `len()`, `!=` (not equal), operator overloading, `exit()`

```python
"""
let the user enter 2 strings and print TRUE if they are equal, FALSE otherwise
"""

# OPERATOR OVERLOADING !=

a = input("a:")
b = input("b:")

if len(a) != len(b):       # integer comparison
    print("length does not match")
    exit()

if a != b:                 # string comparison
    print("content does not match")
    exit()

print("MATCH!")
```

Commented version:

```python
a = input("a:")                  # get first string from user
b = input("b:")                  # get second string

if len(a) != len(b):            # FIRST CHECK: are the lengths different?
    print("length does not match")  # lengths differ — strings can't possibly match
    exit()                       # exit() terminates the entire program

if a != b:                       # SECOND CHECK: compare character by character
    print("content does not match")  # same length but different content
    exit()

print("MATCH!")                  # if we reach here, both checks passed
```

**Operator overloading in action:**
- `len(a) != len(b)` — compares two **integers**. Fast, simple number comparison.
- `a != b` — compares two **strings**. Must walk through each character one by one.

Same `!=` symbol, two completely different operations happening behind the scenes. The length check is a smart optimization: if the lengths differ, you already know the strings aren't equal, and you save the cost of character-by-character comparison. This matters when strings are very long.

---

### Example 2: Mini Calculator

**Problem:** Write a program that asks the user for an operator and two numbers, performs the math, and prints the result. Support `+`, `-`, `*`, `/`, `%`, `//`, `**`. Quit on `q`. Reject unknown operators.

**Concepts used:** `while True`, `break`, `if/elif/else`, `float()`, `int()`, all arithmetic operators

```python
"""
write a program that asks user to enter an operator and two numbers
and performs the math and prints the result.
the program should quit if it receives 'q',
ask user to re enter operator if it does not understand
"""

print("WELCOME TO BABY CALCULATOR")

while True:
    operator = input("enter op:")

    if operator == 'q':
        print("BYE")
        break

    if operator == '+':
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        result = a + b
        print(result)
    elif operator == '-':
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        result = a - b
        print(result)
    elif operator == '/':
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        result = a / b
        print(result)
    elif operator == '*':
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        result = a * b
        print(result)
    elif operator == '%':
        a = int(input("enter a:"))
        b = int(input("enter b:"))
        result = a % b
        print(result)
    elif operator == "//":
        a = int(input("enter a:"))
        b = int(input("enter b:"))
        result = a // b
        print(result)
    elif operator == "**":
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        result = a ** b
        print(result)
    else:
        print("UNKNOWN OPERATOR")
```

Commented version:

```python
print("WELCOME TO BABY CALCULATOR")

while True:                                    # infinite loop — runs until user quits
    operator = input("enter op:")

    if operator == 'q':                        # user wants to quit
        print("BYE")
        break                                  # exit the loop

    if operator == '+':
        a = float(input("enter a:"))           # get two numbers as floats
        b = float(input("enter b:"))
        result = a + b                         # addition
        print(result)
    elif operator == '-':
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        result = a - b                         # subtraction
        print(result)
    elif operator == '/':
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        result = a / b                         # float division (always returns float)
        print(result)
    elif operator == '*':
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        result = a * b                         # multiplication
        print(result)
    elif operator == '%':
        a = int(input("enter a:"))             # modulus needs integers
        b = int(input("enter b:"))
        result = a % b                         # remainder of a / b
        print(result)
    elif operator == "//":
        a = int(input("enter a:"))             # integer division needs integers
        b = int(input("enter b:"))
        result = a // b                        # whole number part of a / b
        print(result)
    elif operator == "**":
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        result = a ** b                        # a raised to the power of b
        print(result)
    else:
        print("UNKNOWN OPERATOR")              # anything we don't recognize
```

**How this program flows:**
1. Print welcome message.
2. Ask for an operator.
3. If it's `q`, print "BYE" and `break` out of the loop → program ends.
4. If it's a known operator, ask for two numbers, compute, print result, then loop back to step 2.
5. If it's unknown, print "UNKNOWN OPERATOR" and loop back to step 2.

**Operator summary demonstrated in this example:**

| Operator | Name              | Example         | Result |
|----------|-------------------|-----------------|--------|
| `+`      | Addition          | `2 + 3`         | `5`    |
| `-`      | Subtraction       | `5 - 2`         | `3`    |
| `*`      | Multiplication    | `4 * 3`         | `12`   |
| `/`      | Float division    | `100 / 8`       | `12.5` |
| `//`     | Integer division  | `100 // 8`      | `12`   |
| `%`      | Modulus           | `6 % 4`         | `2`    |
| `**`     | Exponentiation    | `2 ** 4`        | `16`   |

---

### Example 3: Shopping Cart

**Problem:** Write a shopping cart program. The user enters item prices one at a time. When done, display the total with tax. Reject negative prices.

**Concepts used:** `while True`, `break`, `continue`, accumulator, counter, f-strings with `:.2f`, escape characters `\n`, scientific notation

```python
"""
write a shopping cart program...
"""

total = 0.0
count = 0

while True:
    userinput = input("enter item:")

    if userinput == "quit" or userinput == "q":
        print("---")
        break

    price = float(userinput)
    if price < 0.0:
        print("enter positive value for price")
        continue

    total += price
    count += 1

totalplustax = total + total*0.0825
print(f"you purchased {count} items\n*****\nTOTAL: {totalplustax:.2f}\n*****")

# ROUNDING WITH F STRINGS
x = 1.543
print(f"{x:.2f}")       # 1.54

x = 1.547
print(f"{x:.2f}")       # 1.55

# SCIENTIFIC NOTATION
x = 3.1415e5
print(f"{x:e}")          # 3.141500e+05

x = 3.1415e-5
print(f"{x:e}")          # 3.141500e-05
```

Commented version:

```python
total = 0.0                                     # accumulator for total price
count = 0                                       # counter for number of items

while True:                                     # infinite loop
    userinput = input("enter item:")            # get input as string first

    if userinput == "quit" or userinput == "q": # check for quit BEFORE converting
        print("---")
        break                                   # exit the loop

    price = float(userinput)                    # now safe to convert to float
    if price < 0.0:                             # reject negative prices
        print("enter positive value for price")
        continue                                # skip back to top — ask again

    total += price                              # add this item's price to running total
    count += 1                                  # one more item purchased

# after loop: calculate and display receipt
totalplustax = total + total * 0.0825           # 8.25% tax rate
print(f"you purchased {count} items\n*****\nTOTAL: {totalplustax:.2f}\n*****")
#       {count} replaced with actual count ──┘                  │
#       \n creates a new line ──────────────────────────────────┘
#       :.2f rounds to 2 decimal places ────────────────────────┘

# --- F-STRING ROUNDING EXAMPLES ---
x = 1.543
print(f"{x:.2f}")       # prints 1.54  (3 rounds down)

x = 1.547
print(f"{x:.2f}")       # prints 1.55  (7 rounds up)

# --- SCIENTIFIC NOTATION EXAMPLES ---
x = 3.1415e5             # = 3.1415 × 10^5 = 314150.0
print(f"{x:e}")          # prints 3.141500e+05

x = 3.1415e-5            # = 3.1415 × 10^-5 = 0.000031415
print(f"{x:e}")          # prints 3.141500e-05
```

**Why check for "quit" before converting to float?** Because `float("quit")` would crash the program. We split the input handling: first check if the user wants to stop (while it's still a string), then convert to a number.

**Why use `continue` for negative prices?** We don't want to `break` (that would end the whole shopping session). We just want to reject the bad input and ask again. `continue` jumps back to the top of the loop.

---

### Example 4: Rock Paper Scissors

**Problem:** Write a rock-paper-scissors game where the user plays against the computer. The computer picks randomly.

**Concepts used:** `import random`, `random.randint()`, `if/elif/else` chain, string comparison, `and` boolean operator, f-strings, `\t` and `\n` escape characters

```python
"""
play rock paper scissors with human
"""
import random

print("WELCOME TO ROCK\tPAPER\tSCISSORS\n********\n---------------\n")
userpick = input("enter R, P, S:")

computerrandomnumber = random.randint(0,2)

computerpick = "NOTHING"
if computerrandomnumber == 0:
    computerpick = 'R'
elif computerrandomnumber == 1:
    computerpick = 'P'
else:
    computerpick = 'S'

print(f"COMPUTER ROLLED {computerpick}")

if userpick == computerpick:
    print("DRAW")
elif userpick == 'R' and computerpick == 'P':
    print("YOU LOSE!")
elif userpick == 'R' and computerpick == 'S':
    print("YOU WIN!")
elif userpick == 'P' and computerpick == 'R':
    print("YOU WIN!")
elif userpick == 'P' and computerpick == 'S':
    print("YOU LOSE!")
elif userpick == 'S' and computerpick == 'R':
    print("YOU LOSE!")
elif userpick == 'S' and computerpick == 'P':
    print("YOU WIN!")
else:
    print("NO IDEA WHATS GOING ON USE YOUR HANDS")
```

Commented version:

```python
import random                                   # library for random number generation

print("WELCOME TO ROCK\tPAPER\tSCISSORS\n********\n---------------\n")
#                      \t = tab          \n = new line

userpick = input("enter R, P, S:")              # user enters R, P, or S

computerrandomnumber = random.randint(0, 2)     # random int: 0, 1, or 2 (inclusive)

# translate the random number into R, P, or S
computerpick = "NOTHING"                        # default (will be overwritten)
if computerrandomnumber == 0:
    computerpick = 'R'                          # 0 → Rock
elif computerrandomnumber == 1:
    computerpick = 'P'                          # 1 → Paper
else:
    computerpick = 'S'                          # 2 → Scissors (only option left)

print(f"COMPUTER ROLLED {computerpick}")        # show what computer picked

# determine winner using all possible combinations
if userpick == computerpick:
    print("DRAW")                               # same choice → tie
elif userpick == 'R' and computerpick == 'P':
    print("YOU LOSE!")                           # paper covers rock
elif userpick == 'R' and computerpick == 'S':
    print("YOU WIN!")                            # rock smashes scissors
elif userpick == 'P' and computerpick == 'R':
    print("YOU WIN!")                            # paper covers rock
elif userpick == 'P' and computerpick == 'S':
    print("YOU LOSE!")                           # scissors cut paper
elif userpick == 'S' and computerpick == 'R':
    print("YOU LOSE!")                           # rock smashes scissors
elif userpick == 'S' and computerpick == 'P':
    print("YOU WIN!")                            # scissors cut paper
else:
    print("NO IDEA WHATS GOING ON USE YOUR HANDS")  # invalid input
```

**How `random.randint(0, 2)` works:** it returns 0, 1, or 2 with equal probability. Both endpoints are included.

**The `and` operator:** `userpick == 'R' and computerpick == 'P'` is `True` only when *both* conditions are `True`. This lets us check a specific combination.

**Extension idea (mentioned in class):** wrap this in a `while True` loop, add win/loss counters, and let the user play multiple rounds until they type `Q`.

---

### Example 5: Baby Math School

**Problem:** Write a program that gives the user 5 random multiplication problems, checks their answers, and reports a score.

**Concepts used:** `import random`, `random.randint()`, counter-controlled `while` loop, `==` equality, `+=` shorthand, scoring logic with `if/elif/else`

```python
"""
BABY MATH SCHOOL: ask baby whats x times y
and get answer and count how many right wrong
"""

import random

numberofquestions = 5
currentquestion = 0
babycorrect = 0
while currentquestion < numberofquestions:
    a = random.randint(1,20)
    b = random.randint(1,20)
    print(f"LOOK HERE BABY WHATS {a} times {b} HMM???")
    babyanswer = int(input("baby: "))
    answer = a * b
    if babyanswer == answer:
        print("GOOD JOB")
        babycorrect += 1
    else:
        print("dO_ob")

    currentquestion+=1


babywrong = numberofquestions - babycorrect
babyscore = babycorrect - 2*babywrong
maxscorepossible = numberofquestions

if babyscore < 0:
    print("DISAPPOINT")
elif babyscore < maxscorepossible:
    print("TRY AGAIN")
else:
    print("YOU ARE INVITED TO HEB BABY FOOD ISLE")
```

Commented version:

```python
import random

numberofquestions = 5                            # total questions to ask
currentquestion = 0                              # which question we're on (0-indexed)
babycorrect = 0                                  # how many correct answers so far

while currentquestion < numberofquestions:        # loop exactly 5 times
    a = random.randint(1, 20)                    # random number 1-20
    b = random.randint(1, 20)                    # another random number 1-20
    print(f"LOOK HERE BABY WHATS {a} times {b} HMM???")
    babyanswer = int(input("baby: "))            # get answer, convert to int
    answer = a * b                               # compute the correct answer
    if babyanswer == answer:                     # did baby get it right?
        print("GOOD JOB")
        babycorrect += 1                         # increment correct counter
    else:
        print("dO_ob")                           # sad face

    currentquestion += 1                         # move to next question

# scoring: correct answers give +1, wrong answers penalize -2
babywrong = numberofquestions - babycorrect       # wrong = total - correct
babyscore = babycorrect - 2 * babywrong           # penalize wrong answers heavily
maxscorepossible = numberofquestions              # best possible = all correct

if babyscore < 0:                                # negative score = very bad
    print("DISAPPOINT")
elif babyscore < maxscorepossible:               # some right, not all
    print("TRY AGAIN")
else:                                            # perfect score
    print("YOU ARE INVITED TO HEB BABY FOOD ISLE")
```

**Scoring formula:** `score = correct - 2 × wrong`. This means getting one wrong costs you more than getting one right earns. With 5 questions:
- 5 correct, 0 wrong → score = 5 (perfect)
- 3 correct, 2 wrong → score = 3 - 4 = -1 (DISAPPOINT)
- 4 correct, 1 wrong → score = 4 - 2 = 2 (TRY AGAIN)

---

## New Concepts Summary

Everything listed here was introduced in this lecture and is your responsibility to learn:

| Concept | Example |
|---------|---------|
| `while` loop with condition | `while x <= N:` |
| `while True` (infinite loop) | `while True:` |
| `break` | Exit loop immediately |
| `continue` | Skip to next iteration |
| `==` equality | `if pw == password:` |
| `!=` inequality | `if a != b:` |
| `%` modulus | `6 % 4` → `2` |
| `//` integer division | `100 // 8` → `12` |
| `**` exponentiation | `2 ** 4` → `16` |
| `len()` | `len("hello")` → `5` |
| Operator overloading | Same `!=` works differently on ints vs strings |
| `import random` | `random.randint(0, 2)` |
| F-strings | `f"total: {x:.2f}"` |
| Escape characters | `\n`, `\t`, `\"` |
| Scientific notation | `1e5`, `{x:e}` |
| `+=` shorthand | `x += 1` same as `x = x + 1` |
| Accumulator pattern | `total += price` |
| Counter pattern | `count += 1` |
| Flags (boolean state) | `logged_in = False` … `logged_in = True` |
| `exit()` | Terminate the program |
| String indexing (intro) | Index = offset from beginning, starts at 0 |

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
