
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Computer Architecture

## Table of Contents

1. [Why Computer Architecture Matters](#why-computer-architecture-matters)
2. [What Is a Computer?](#1-what-is-a-computer)
   - [Alan Turing](#alan-turing)
3. [Decidability and Computability](#2-decidability-and-computability)
   - [Example: A Formal Language](#example-a-formal-language)
   - [Key Takeaway](#key-takeaway)
4. [The Von Neumann Architecture](#3-the-von-neumann-architecture)
   - [Memory as a Grid](#memory-as-a-grid)
   - [The Instruction Set](#the-instruction-set)
   - [Sequential Execution](#sequential-execution)
   - [That's It](#thats-it)
5. [CPU and Memory](#4-cpu-and-memory)
6. [Instruction Sets and Programming Languages](#5-instruction-sets-and-programming-languages)
   - [Instruction Sets](#instruction-sets)
   - [Why Programming Languages Exist](#why-programming-languages-exist)
7. [Memory Hierarchy](#6-memory-hierarchy)
   - [Why It Matters](#why-it-matters)
8. [Clock Speed vs. Cache Size](#7-clock-speed-vs-cache-size)
9. [GPU Architecture -- Parallel Processing](#8-gpu-architecture----parallel-processing)
   - [When GPUs Excel](#when-gpus-excel)
   - [When GPUs Don't Help](#when-gpus-dont-help)
   - [CPU vs. GPU Summary](#cpu-vs-gpu-summary)
10. [Universality of Computer Architecture](#9-universality-of-computer-architecture)

---

## Why Computer Architecture Matters

Understanding computer architecture removes the "magic" from technology. When you understand how computers fundamentally work, you can make reasonable assumptions about any new technology you encounter -- whether it's a PS5, a Nintendo Switch, a smartwatch, or a network router. They all follow the same principles.

---

## 1. What Is a Computer?

A computer is a device that can **compute what is computable**. It can be built out of any material -- silicon, Legos, even Minecraft redstone -- as long as it follows a very specific set of rules known as the **von Neumann model**.

There is only one known model of computation. It is backed by **automata theory**, a branch of mathematics. It has been mathematically proven that if you build a device according to the von Neumann model, it can compute everything that is computable.

### Alan Turing

Alan Turing is the person who figured out the mathematics behind a system that can compute anything that is computable. The movie *The Imitation Game* is based on his life and work.

---

## 2. Decidability and Computability

"Computable" does not mean "easy." In computer science, we distinguish between different levels of computational possibility:

- **Decidable**: A problem is decidable if there exists an algorithm that can solve it and **halt with the correct answer** for every possible input.
- **Recognizable** (Recursively Enumerable): A problem is recognizable if a machine can verify "yes" answers (and will eventually find them if they exist), but may run forever on "no" answers.

These concepts are formalized by the **Church-Turing Thesis**: anything a human can calculate with pencil and paper using a fixed set of rules, a Turing machine can compute. This thesis equates human-computable functions with machine-computable functions.

### Example: A Formal Language

Consider an alphabet **{A, B, C}** with a simple grammar:
- Any letter can follow any other letter (concatenation).
- Spaces separate words.
- No limit on word length.

**Problem 1:** Given a sentence, can we determine whether it belongs to this language?
- **Yes** -- just check that every character is A, B, or C. This is **decidable**.

**Problem 2:** List all two-letter words in this language.
- **Yes** -- AA, AB, AC, BA, BB, BC, CA, CB, CC. That's 9 words (3^2). This is **decidable**.

**Problem 3:** List all words of length 1000.
- There are **3^1000** such words, which is approximately **10^477**. For comparison, the estimated number of atoms in the observable universe is about 10^80.
- This is still **decidable**. The answer is knowable -- we just don't have enough physical resources to actually enumerate them all. Given a sufficiently powerful machine, you could draw the decision tree 1000 levels deep and list every word.

**Problem 4:** List **all** words in this language (of every possible length), then stop.
- This is **recognizable but not decidable**. The set is infinite. A machine *can* enumerate words forever (A, B, C, AA, AB, AC, ...), and it will eventually produce any particular word you ask for. However, it can never produce a *complete* list and halt -- there's no way to know when you're "done" because there's always another word to generate.
- This is a classic example of a **recognizable** (recursively enumerable) set that is **not decidable**. The machine can recognize/generate members of the set, but cannot decide the question "Have I listed them all?" and halt.

### Key Takeaway

- **Decidable** = An algorithm exists that can solve the problem and halt with the correct answer for every input. The answer is knowable and obtainable (even if impractical with current resources).
- **Recognizable (Recursively Enumerable)** = A machine can verify "yes" answers and will eventually find them, but may run forever without halting on "no" answers or completion questions.
- **Undecidable** = No algorithm exists that can solve the problem and halt for all inputs. Some problems are fundamentally unsolvable.

If a problem is decidable, a machine built according to the von Neumann model **can** solve it and halt with the answer. How *quickly* it solves it depends on the hardware.

> **Note:** The **halting problem** is a classic example of a truly undecidable problem: given any program and input, no algorithm can determine whether that program will eventually halt. This was proven by Alan Turing and shows fundamental limits on computation -- some things are mathematically impossible to compute, regardless of how powerful the computer is.

---

## 3. The Von Neumann Architecture

### Memory as a Grid

Imagine an addressable grid labeled with rows and columns (e.g., A--H across, 1--6 down). Each cell holds a value. You can address any location on the grid (e.g., G5).

> In reality, memory is a one-dimensional address space (like a very long list), but thinking of it as a grid makes it easier to understand.

### The Instruction Set

A small device (the processor) can perform a handful of basic operations on the grid:

| Instruction | What It Does |
|---|---|
| **COPY** src dst | Copy the value at one grid location to another (e.g., `COPY C2 G5` copies the value in C2 into G5) |
| **ADD** a b dst | Add the values at two locations and store the result (e.g., `ADD E3 C2 G5`) |
| **SUBTRACT** | Subtract one value from another |
| **JUMP** n | Jump to instruction number *n* (unconditional) |
| **JUMP IF** cond n | Jump to instruction *n* only if a condition is true (e.g., `JUMP 6 IF G5 < E3`) |

With addition you can derive subtraction, multiplication, and other basic math.

### Sequential Execution

Instructions are numbered (0, 1, 2, 3, ...). The processor starts at instruction 0 and executes them **one by one, in order** -- unless a JUMP instruction redirects it elsewhere.

### That's It

With roughly **~7 basic instructions** (copy, add, subtract, jump, conditional jump, and a couple more), this machine can solve **any computable problem**. This is the von Neumann model.

> **Note on Turing Machine vs. von Neumann Architecture:**
> - **Turing Machine**: A mathematical abstraction with an infinite tape and no physical constraints. It's a theoretical model used to reason about what is computable.
> - **von Neumann Architecture**: A physical design with a CPU, stored-program memory, and registers. It's a practical blueprint for building real computers.
> - A von Neumann machine is **Turing Complete**, meaning it can compute anything a Turing machine can compute (given enough memory). They are computationally equivalent -- the von Neumann architecture is essentially a physical implementation of the abstract computational power of a Turing machine.

---

## 4. CPU and Memory

- **CPU (Central Processing Unit):** The device that reads and executes the list of instructions. It understands a very limited set of simple instructions, visits them sequentially, and can jump forward or backward when told to.
- **Memory:** The grid -- the scratchboard where data is stored and results are computed. This is what makes computation possible.

---

## 5. Instruction Sets and Programming Languages

### Instruction Sets

The basic idea (von Neumann architecture) is always the same, but different CPU manufacturers may implement the instruction set slightly differently. For example, one manufacturer's COPY instruction might put the source first, while another puts the destination first. One might have side effects that another doesn't.

### Why Programming Languages Exist

Two problems with writing raw instructions:
1. **It's confusing for humans.** Reading sequences of COPY, JUMP, ADD with grid addresses gets overwhelming fast.
2. **Instruction sets vary between manufacturers.** Code written for one CPU's instruction set won't necessarily work on another's.

**Programming languages** solve both problems. You write code in something close to English with formal syntax rules. Software (compilers/interpreters) translates that code into the appropriate machine instructions for the target CPU.

> Python, C++, and every other programming language are "just syntax rules" -- a human-friendly way to express instructions that ultimately get translated into the basic operations the CPU understands.

---

## 6. Memory Hierarchy

In real hardware, memory is **tiered by speed and cost**:

| Tier | Speed | Size | Cost |
|---|---|---|---|
| **L1 Cache** | Fastest | Smallest | Most expensive |
| **L2 Cache** | Fast | Small | Expensive |
| **L3 Cache** | Moderate | Medium | Moderate |
| **RAM** | Slower | Large | Cheaper |
| **SSD / NVMe** | Slowest (of these) | Largest | Cheapest |

All of these are storage -- you can think of them as one big grid where different regions have different speeds. The physical makeup of the memory (materials, wiring) determines its performance.

### Why It Matters

- **Intel Xeon processors** (~$2,000) are expensive because they have very large amounts of fast cache. A larger portion of their memory grid is the fast kind.
- **Historical example:** In the Athlon/Phenom era (mid-2000s), AMD tended to allocate more silicon to larger L3 caches while keeping L1/L2 smaller, then advertised the total cache size. A box might say "24 MB cache" while Intel said "2 MB cache" -- but most of AMD's was slower L3, while Intel's was faster L1/L2. This illustrated how cache tier allocation affects both price and performance. (Note: Modern AMD processors, particularly since the Zen architecture in 2017+, use different and more competitive cache strategies.)

---

## 7. Clock Speed vs. Cache Size

**Clock speed (GHz)** = how many "ticks" per second the CPU can perform.
- 4 GHz = 4 billion ticks per second.
- Each instruction takes multiple ticks (cycles) to complete.

A higher clock speed does **not** automatically mean better performance:

| | CPU A (e.g., Xeon) | CPU B (e.g., i9) |
|---|---|---|
| Clock speed | 2 GHz | 4 GHz |
| Cycles per COPY | ~40 | ~110 |
| Price | ~$2,000 | ~$300-500 |

CPU B ticks twice as fast, but each operation takes nearly 3x as many cycles because its memory is slower. CPU A completes the same operation faster in real time despite having a lower clock speed.

**Bottom line:** Clock speed tells you how fast the clock ticks. Cache quality tells you how many ticks each operation actually needs. Both matter.

---

## 8. GPU Architecture -- Parallel Processing

NVIDIA GPUs use the **same fundamental architecture** (von Neumann), but arrange resources differently:

- **Many small CPUs**, each with very small local memory.
- If they need large memory, they **share** a big common grid.

### When GPUs Excel

GPUs are ideal for tasks where many data points can be processed **independently** and in **parallel**. Example: calculating taxes for thousands of people -- each person's calculation is independent of everyone else's. Give each small CPU one person's data, and they all work simultaneously.

### When GPUs Don't Help

Sequential, dependent tasks -- like summing everyone's ages where each addition depends on the previous result -- don't benefit much from massive parallelism. For that, you want fewer cores with higher clock speeds and larger fast caches (a traditional CPU).

### CPU vs. GPU Summary

| | CPU | GPU |
|---|---|---|
| Cores | Few (powerful) | Many (simple) |
| Per-core memory | Large, fast cache | Small local memory |
| Best for | Sequential, dependent tasks | Parallel, independent tasks |
| Example | Running an OS, single-threaded apps | Graphics rendering, machine learning, batch processing |

---

## 9. Universality of Computer Architecture

**Every computing device uses the von Neumann architecture.** There is no alternative.

- Phones
- Smartwatches (Apple Watch, Galaxy Watch)
- Laptops and desktops
- Routers and switches
- Gaming consoles

The only difference between them is **how they arrange the components**: how many CPUs, how much cache at each tier, how the memory is connected, how fast the clock runs. These are business and engineering trade-offs -- not fundamentally different designs.

Understanding this one architecture gives you a foundation for understanding operating systems, networking, cybersecurity, and troubleshooting. It's like understanding how an engine works -- once you know the fundamentals, diagnosing problems becomes much easier.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
