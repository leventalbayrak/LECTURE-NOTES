
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Branching and Loops

## Table of Contents
- [Introduction to Branching](#introduction-to-branching)
- [Code Block Notation](#code-block-notation)
- [If Statements](#if-statements)
- [If-Else Statements](#if-else-statements)
- [Elif Chains (Else-If)](#elif-chains-else-if)
- [Nested If Statements](#nested-if-statements)
- [Python Indentation](#python-indentation)
- [While Loops](#while-loops)
- [Decision Complexity](#decision-complexity)
- [Summary](#summary)
- [Practice](#practice)

## Introduction to Branching

**Branching** is the ability to make decisions in your code and execute different blocks of instructions based on conditions. Think of it like driving to school - you make a decision at each intersection: should I take the exit to McDonald's or drive straight to class? Each decision creates a "branch" in the possible paths your program can take.

In programming, branching allows you to:
- Execute code only when certain conditions are met
- Choose between different courses of action
- Skip blocks of code that aren't needed
- Create complex decision-making logic

## Code Block Notation

In the examples below, we'll use letters (A, B, C, D, E) to represent blocks of code. This helps visualize the execution flow:

- **A** = Code that executes before the decision
- **B, C, D** = Code blocks inside conditional statements
- **E** = Code that executes after the decision

## If Statements

The simplest form of branching is the **if statement**. It checks a condition, and if the condition is true, it executes a block of code. If the condition is false, it skips that block.

### Basic Syntax

```python
A
if condition:
    B
C
```

### Execution Patterns

| Condition | Execution Sequence |
|-----------|-------------------|
| True      | A → B → C         |
| False     | A → C             |

### Example

```python
age = int(input())

if age > 10:
    print("You can eat ice cream")

print("Goodbye")
```

**Explanation:**
- Read age from standard input
- If age is greater than 10, print "You can eat ice cream"
- Always print "Goodbye" regardless of the condition

## If-Else Statements

The **if-else statement** forces you to choose one branch or the other. You cannot skip both - exactly one block will execute.

### Syntax

```python
A
if condition:
    B
else:
    C
D
```

### Execution Patterns

| Condition | Execution Sequence |
|-----------|-------------------|
| True      | A → B → D         |
| False     | A → C → D         |

**Key Point:** You must pick one or the other. If you execute B, you don't execute C. If you execute C, you don't execute B.

### Example

```python
stars = float(input())

if stars < 4.8:
    print("No food for a month")
else:
    print("Enjoy these three Oreos")
```

## Elif Chains (Else-If)

When you have multiple conditions to check sequentially, use **elif** (short for "else if"). Python checks conditions from top to bottom and executes the first matching block.

### Syntax

```python
A
if condition1:
    B
elif condition2:
    C
elif condition3:
    D
else:
    E
F
```

### Key Properties

- Conditions are checked **sequentially from top to bottom**
- Once a condition is true, that block executes and **all others are skipped**
- The `else` block is **optional** - you can omit it if you want
- Only **one block** will ever execute

### Example

```python
temperature = int(input())

if temperature > 85:
    print("Very hot")
elif temperature > 75:
    print("Hot")
elif temperature > 65:
    print("OK")
else:
    print("Cold")
```

**Execution Examples:**

| Temperature | Output    | Reason                                      |
|-------------|-----------|---------------------------------------------|
| 90          | Very hot  | First condition (>85) is true              |
| 80          | Hot       | First fails, second (>75) is true          |
| 70          | OK        | First two fail, third (>65) is true        |
| 50          | Cold      | All conditions fail, else block executes   |

### Without Else

You can omit the `else` block:

```python
A
if condition1:
    B
elif condition2:
    C
elif condition3:
    D
E
```

If all conditions fail, none of the blocks execute and the code continues to E.

## Nested If Statements

You can place if statements inside other if statements. This is called **nesting**.

### Example

```python
A
if condition1:
    B
    if condition2:
        C
    D
E
```

### Execution Example

```python
age = int(input())

if age > 10:
    print("Old enough")
    stars = float(input())
    if stars < 4.8:
        print("Parents are disappointed")
    print("Thank you for being a kid")
```

**Execution scenarios:**

| Age | Stars | Output                                                                    |
|-----|-------|---------------------------------------------------------------------------|
| 5   | N/A   | "Thank you for being a kid"                                              |
| 11  | 5.0   | "Old enough" → "Thank you for being a kid"                               |
| 11  | 4.0   | "Old enough" → "Parents are disappointed" → "Thank you for being a kid" |

### Warning: Avoid Deep Nesting

While nesting is sometimes necessary, too much nesting makes code hard to read and maintain:

- **2 levels:** Acceptable
- **3 levels:** Suspicious - consider alternatives
- **4+ levels:** Investigate whether there's a better approach

Sometimes you can reduce nesting by using boolean operators (AND, OR, NOT) to combine conditions.

## Python Indentation

**IMPORTANT:** Unlike many programming languages that use curly braces `{}` to define code blocks, Python uses **indentation** (tabs or spaces).

```python
if age > 10:
    # This line is indented - it's inside the if block
    print("You can eat ice cream")
    # This line is also indented - still inside the block
    x = 5
# This line is NOT indented - it's outside the if block
print("Goodbye")
```

**Rules:**
- Press the Tab key to indent one level
- All lines at the same indentation level belong to the same block
- Python will give an error if indentation is inconsistent

## While Loops

A **while loop** has nearly identical syntax to an if statement, but with one crucial difference: it repeats the code block as long as the condition remains true.

### Syntax Comparison

```python
# If statement
A
if condition:
    B
C
```

```python
# While loop
A
while condition:
    B
C
```

### How While Loops Work

**CRITICAL:** The while loop condition is checked **only at the beginning** of each iteration, never mid-execution.

**Step-by-step execution:**

1. **Check the condition** - Test if the condition is true or false
2. **Make a decision** - If false, skip the block entirely and continue to C. If true, proceed to step 3
3. **Execute the entire block** - Run all code inside the block from top to bottom, completely
4. **Automatically jump back** - Once the block finishes, automatically return to step 1
5. **Test again** - Check the condition again to decide if the block should execute one more time
6. **Repeat** - Continue this cycle until the condition becomes false

**Important:** The condition is checked at the **start** of each loop iteration. Once you begin executing the block, you will complete the entire block before checking the condition again. The condition is **never** checked in the middle of executing the block.

### Execution Patterns

| Condition State | Execution Sequence | Description                  |
|----------------|-------------------|------------------------------|
| False initially | A → C            | Block never executes         |
| True once      | A → B → C        | Executes once, then exits    |
| True 4 times   | A → B → B → B → B → C | Loops 4 times           |
| Always true    | A → B → B → B... | Infinite loop (never reaches C) |

### Example: Counting

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
print("Done")
```

**Output:**
```
0
1
2
3
4
Done
```

**Detailed execution breakdown showing condition checking:**

| Iteration | Before Block | Condition Check | Decision | Execute Block | After Block |
|-----------|--------------|-----------------|----------|---------------|-------------|
| 1st       | count = 0    | 0 < 5? **True** | Enter block | print(0), count = 1 | Jump back to condition |
| 2nd       | count = 1    | 1 < 5? **True** | Enter block | print(1), count = 2 | Jump back to condition |
| 3rd       | count = 2    | 2 < 5? **True** | Enter block | print(2), count = 3 | Jump back to condition |
| 4th       | count = 3    | 3 < 5? **True** | Enter block | print(3), count = 4 | Jump back to condition |
| 5th       | count = 4    | 4 < 5? **True** | Enter block | print(4), count = 5 | Jump back to condition |
| -         | count = 5    | 5 < 5? **False** | Exit loop | *(block skipped)* | Continue to print("Done") |

**Key observations:**
- The condition `count < 5` is checked **6 times** (once before each potential iteration, plus the final check that exits)
- The block executes **5 times** (iterations 1-5)
- After each complete execution of the block, we **automatically jump back** to check the condition
- Once count becomes 5, the condition fails and we exit the loop
- The condition is **never checked** while we're in the middle of `print(count)` or `count = count + 1`

### Key Differences: If vs While

| Feature           | If Statement                      | While Loop                           |
|-------------------|-----------------------------------|--------------------------------------|
| Execution         | Block executes at most once       | Block can execute many times         |
| Condition check   | Checked once at the beginning     | Checked before each iteration        |
| After block       | Continue to next statement        | Return to condition check            |
| Use case          | Make a one-time decision          | Repeat actions until condition fails |

### Important Notes

- The condition is **checked at the beginning** of each iteration, not during execution
- The code must change something that affects the condition, or you'll create an infinite loop
- You execute the entire block before checking the condition again

## Decision Complexity

Each decision point in your code creates **two possible outcomes** (true or false). As you add more decisions, the number of possible execution paths grows exponentially:

| Number of Decisions | Possible Outcomes |
|--------------------:|------------------:|
| 1                   | 2                 |
| 2                   | 4                 |
| 3                   | 8                 |
| 10                  | 1,024             |
| 30                  | 1,073,741,824 (over 1 billion) |

**Example:** Driving from home to school involves more than 30 yes/no decisions. At each decision point, the universe conceptually "splits" - one version of you makes one choice, another version makes a different choice. By the time you reach school, there are billions of parallel universes where you made different decisions!

This illustrates why:
- Code with many conditional branches can be difficult to test (you can't test all paths)
- Reducing unnecessary nesting and decisions improves code quality
- Sometimes combining conditions with boolean operators is clearer than deep nesting

## Summary

**Branching** gives your programs the ability to make decisions:

- **if** - Execute code only when a condition is true
- **if-else** - Choose between two alternatives
- **elif** - Check multiple conditions in sequence
- **Nested ifs** - Make decisions within decisions (use sparingly)

**While loops** allow you to repeat code:

- Same syntax as if, but repeats while condition is true
- Must ensure condition eventually becomes false
- Condition checked before each iteration

With these tools, you can:
- Build interactive programs that respond to user input
- Create games with repeating game loops
- Implement complex decision-making logic
- Control program flow based on conditions

---

## Practice

Try creating programs that:
1. Read a number and print whether it's positive, negative, or zero
2. Use a while loop to print numbers from 1 to 10
3. Combine conditions to check if someone is eligible for a discount (age > 65 OR age < 12)
4. Read temperatures and print warnings only when they're outside a safe range

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
