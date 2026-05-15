
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Programming Languages

## Table of Contents

- [1. Review: Computer Architecture (Von Neumann)](#1-review-computer-architecture-von-neumann)
- [2. Why Not Just Use CPU Instructions?](#2-why-not-just-use-cpu-instructions)
- [3. Programming Languages as Abstraction Layers](#3-programming-languages-as-abstraction-layers)
- [4. Understanding Hardware Still Matters](#4-understanding-hardware-still-matters)
- [5. The Programming Language Hierarchy](#5-the-programming-language-hierarchy)
- [6. High-Level vs Low-Level: What Does It Mean?](#6-high-level-vs-low-level-what-does-it-mean)
- [7. Compiled vs Interpreted Languages](#7-compiled-vs-interpreted-languages)
- [8. Python for IT & Cybersecurity](#8-python-for-it--cybersecurity)
- [9. Assembly Language & Reverse Engineering Tools](#9-assembly-language--reverse-engineering-tools)
- [10. Pragmatism in Programming](#10-pragmatism-in-programming)

---

## 1. Review: Computer Architecture (Von Neumann)

A Von Neumann machine has two main components:

1. **Memory** — a grid of storage cells that hold data.
2. **CPU** — sits on top of memory and executes **instructions**.

The CPU can perform a small set of instruction types:

| Instruction Type | What It Does |
|:---|:---|
| **Copy / Move** | Move data from one memory location to another |
| **Arithmetic** | Add, subtract, multiply, divide |
| **Jump** | Skip forward or backward to a different instruction |
| **Conditional Jump** | Jump only if a condition is met (e.g., "jump if value > 0") |

Instructions execute **sequentially** (top to bottom), but jump instructions allow the CPU to move forward or backward to any point. Conditional jumps give the CPU the ability to make choices — like reaching a fork and going left or right depending on some condition. This is what allows computers to perform complex calculations.

---

## 2. Why Not Just Use CPU Instructions?

If the CPU runs instructions directly, why don't we just write those instructions ourselves?

**Problem 1: Instructions are too simple.**
Each instruction does one tiny thing. To accomplish anything useful, you need an enormous number of them. Analogy: when you walk across a room, you think "walk to the desk." You don't consciously control every individual muscle contraction. Writing raw CPU instructions is like having to specify every muscle movement — technically possible, but impractical.

**Problem 2: Every CPU has a different instruction set.**
AMD, Intel, and Apple M-series processors all use different instruction sets. On one CPU, a "copy" instruction might move one cell of data. On another, it always copies 4 cells at a time. On yet another, an "add" instruction adds 8 pairs of values simultaneously. Code written for one instruction set **will not work** on another CPU.

**The solution:** We need a language that is:

- **Human-readable** — close to English, easy to learn.
- **Precise and unambiguous** — you can't say "go get bread"; you must specify which store, which aisle, which brand.
- **Unambiguous and deterministic** — In English, "I saw the man with the telescope" could mean you used a telescope to see him, or that you saw a man holding one. The meaning changes depending on context, tone, and interpretation. A programming language cannot allow this — every statement must have exactly one meaning, regardless of when, where, or by whom it is read. The same code must always produce the same result, on any CPU, every time.

This is what programming languages provide.

---

## 3. Programming Languages as Abstraction Layers

A programming language creates an **abstraction layer** on top of the instruction set and hardware.

**What does abstraction mean here?** It means separating the programmer's concerns from the hardware engineer's concerns. As a programmer:

- You think of the machine as a Von Neumann computer — it has memory and a CPU that executes instructions.
- You do **not** need to know the electrical engineering details of the chip.
- You do **not** need to know the exact instruction set.

The programming language handles the translation from your human-readable code down to the specific CPU instructions.

---

## 4. Understanding Hardware Still Matters

Abstraction doesn't mean you should be completely ignorant of hardware. A good programmer knows the strengths and weaknesses of the system they're targeting.

**Example — Parallel grading:** A professor has 2 tutors and 150 students. Instead of having one tutor grade all 150 papers sequentially, you split the students into two groups and grade in parallel — finishing in half the time. The model (teacher + tutors) hasn't changed, but knowing you have two tutors lets you work more efficiently.

**Example — CPU vs GPU:**

| | CPU | GPU |
|:---|:---|:---|
| **Architecture** | One powerful processor | Many small, slow processors |
| **Strength** | Fast at serial work (do this, then this, then this) | Fast at parallel work (do all of these at once) |
| **Example** | General computation | Turn all red pixels blue simultaneously |

There is a **slow connection** between CPU and GPU. To use the GPU effectively:

- Send data in **bulk** (one large package).
- Let the GPU work without interruption.
- **Avoid** sending one pixel at a time back and forth — the communication overhead will kill performance.

This kind of architectural knowledge helps you write faster programs, even when using a high-level language.

---

## 5. The Programming Language Hierarchy

Languages exist on a spectrum from low-level (close to hardware) to high-level (close to human thinking):

```
More Abstract (Higher Level)
 ▲
 │   Python, JavaScript         ← Scripting / interpreted languages
 │   C#, Java                   ← High-level compiled languages
 │   C++                        ← Systems language with more features
 │   C                          ← Low-level systems language
 │   Assembly                   ← Nearly raw instruction set
 ▼
Less Abstract (Lower Level)
```

### Assembly

- Nearly a direct representation of the CPU instruction set, but in human-readable form.
- Still used for **codecs** (video encoding/decoding) — the compression and decompression that lets you stream YouTube video efficiently. These must be extremely fast, so they are written in assembly.
- Very few instructions to learn, but it takes an enormous number of them to accomplish anything.

### C

- A low-level systems language. **Linux** is written in C. **Windows** has its performance-critical parts (the NT kernel) written in C, with C++ mixed in elsewhere.
- Extremely simple — you can learn the language itself in about two weeks (the reference book is very small).
- But writing C **well** takes 5–10 years of experience. Mistakes can crash or destroy a system.

### C++

- Built on top of C with many additional features.
- Used for **games** and **graphical user interfaces** (desktop applications).

### C# and Java

- High-level languages that compile to **intermediate bytecode** (CIL for C#, JVM bytecode for Java), which is then executed by a runtime (CLR / JVM) using **Just-In-Time (JIT) compilation**.
- Unlike Python, the entire source code is compiled before execution — no code is being dynamically interpreted line by line. Unlike C/C++, the compilation target is bytecode rather than native machine code, and the runtime provides features like garbage collection and managed memory.
- Used for **business applications** and **Microsoft ecosystem** software.
- Note: **Java and JavaScript are not related** despite the similar name.

### Python and JavaScript

- Very high-level, highly abstract languages.
- Python can be learned in about a week; you can build productive applications within two weeks.
- JavaScript is similarly accessible (though it has some quirks).

### Job Market

The higher you go in the hierarchy, the more jobs are available:


*The numbers below are not precise figures — they are rough approximations meant to illustrate the general trend.*

- For every 1 job in C/C++, there are roughly 100 in C#/Java.
- For every 1 in C#/Java, there are far more in Python/JavaScript.

---

## 6. High-Level vs Low-Level: What Does It Mean?

"High-level" and "low-level" refer to the **level of abstraction** — how much detail the language hides from you.

### The HEB Analogy

Task: "Go to HEB and buy bread."

| Language Level | What You'd Have to Specify |
|:---|:---|
| **Python** | "Go buy bread from HEB at the corner of the street." |
| **C#** | "Walk out the door. Get in the car. Drive to HEB. Park. Walk to aisle 3. Pick up bread. Walk to checkout..." |
| **C** | "Lift left foot 6 inches. Move it 18 inches forward. Place it down. Shift weight. Lift right foot..." |
| **Assembly** | "Contract left quadriceps 40%. Extend left hip flexor 15 degrees. Activate left tibialis anterior..." |

### Concrete Example: Playing a Sound File

**In Python** (high-level):
```python
sound_system.play("hello.mp3")
```

You don't worry about the operating system, the file system, the audio driver, the buffer size, or how MP3 compression works. You just say "play this."

**In C** (low-level), you would need to:

1. Detect whether you're on Linux, Windows, or macOS.
2. Locate the correct audio service for that OS.
3. Request a buffer from the audio driver.
4. Read the MP3 file from disk into memory.
5. Decode the compressed audio data.
6. Feed samples into an audio buffer at the correct rate. The audio hardware continuously reads from this buffer to drive the speakers — if your code can't fill the buffer with the correct samples fast enough, the waveform amplitudes won't line up, resulting in audible artifacts like clicks, pops, and distortion.
7. Handle all error cases yourself.

### The Tradeoff

More abstraction means **more overhead**. The language has to:

- Add safety checks (Python can't assume you know what you're doing).
- Handle all the details you're not specifying.
- Run many extra instructions under the hood.

This makes high-level languages **slower** than low-level ones. Low-level languages can skip safety checks and take shortcuts because the programmer is explicitly managing the details.

**Important warning:** Because Python completely hides the fact that your code is running on a physical computer, learning Python *without* understanding computer architecture can lead you to believe that computers work the way Python works. This creates **wrong assumptions** that will follow you through your career and cause bad technical decisions.

---

## 7. Compiled vs Interpreted Languages

### Natively Compiled Languages (C, C++)

1. A **compiler** reads your entire source code from start to finish.
2. It fully understands the structure and logic of your program.
3. It translates the code directly into **native machine instructions** for the target CPU.
4. Because it sees everything, it can **optimize** — for example, removing code that will never execute (dead code elimination).
5. This translation happens **once**. The resulting program runs directly and efficiently.

**Example:** If your code says "play a sound 20 million times" but the compiler can prove the sound file is empty, it may skip the entire operation. It sees ahead and knows the work is pointless.

### Bytecode-Compiled Languages (C#, Java)

1. A compiler reads your entire source code and compiles it to **intermediate bytecode** — not native machine code, but a platform-independent instruction set (CIL for C#, JVM bytecode for Java).
2. At runtime, the bytecode is executed by a managed runtime (CLR for C#, JVM for Java) which uses **Just-In-Time (JIT) compilation** to translate bytecode into native instructions as the program runs.
3. The key distinction from interpreted languages: the **entire source code is compiled before execution**. The code is not being dynamically read and generated line by line — the compiler has already analyzed, validated, and translated everything.
4. The key distinction from C/C++: the runtime provides **garbage collection**, **managed memory**, and **safety checks** that C/C++ do not have.

### Interpreted Languages (Python, JavaScript)

1. An **interpreter** reads your code **one line at a time**.
2. It translates and executes each line immediately, without looking ahead.
3. It cannot optimize based on future lines because it hasn't seen them yet.
4. Every time you run the program, the code is re-read and re-translated from scratch.

**Note:** CPython (the standard Python implementation) does compile source code to bytecode (.pyc files) internally, but this bytecode is then interpreted by the Python virtual machine — it is not JIT-compiled to native code the way C#/Java runtimes do it. The overall behavior is still fundamentally interpreted compared to the more static compilation of C#/Java.

**Example:** If your code says "play a sound 20 million times" and the file is empty, the interpreter will dutifully play all 20 million empty samples — it never looked ahead to realize the task was pointless.

### The UN Interpreter Analogy

- **Compiled** = receiving the entire speech transcript in advance, having time to edit and improve the translation before presenting it.
- **Interpreted** = real-time interpretation at the United Nations — you translate word by word as the speaker talks, with no knowledge of what comes next.

### Summary

| | Natively Compiled | Bytecode-Compiled | Interpreted |
|:---|:---|:---|:---|
| **When is code translated?** | Once, before running | Source compiled before running; bytecode JIT-compiled at runtime | Every time, during running |
| **Sees entire code?** | Yes | Yes | No (one line at a time) |
| **Can optimize?** | Yes (at compile time) | Yes (at compile time and JIT) | No |
| **Speed** | Fastest | Fast | Slower |
| **Runtime features** | None (manual memory management) | Garbage collection, managed memory | Garbage collection, dynamic typing |
| **Examples** | C, C++ | C#, Java | Python, JavaScript |

---

## 8. Python for IT & Cybersecurity

If you're going into IT or cybersecurity, **Python is extremely valuable** — more so than any other single language for these fields.

Why?

- **There is a library for everything.** Want to scan a network for open ports? `nmap` library — a few lines. Want to capture and analyze network packets? `scapy` — build and send custom packets in 3 lines. Want to automate web browser interactions for testing or scraping? `selenium` — launch a browser and navigate programmatically. Want to crack password hashes? `hashlib` plus a wordlist and a short loop. Need to spin up a web server? `flask` — about 5 lines of code. Want to program an embedded system like your fridge or a microcontroller? `MicroPython` — run Python directly on the hardware.
- **Accessibility.** In C, if you want to play an MP3 file, you need to find a suitable library yourself, learn its API, handle its dependencies, and write significantly more integration code. The ecosystem of ready-to-use libraries in C is far smaller and less accessible than Python's — what takes one `pip install` and three lines in Python might take days or weeks of setup and coding in C.
- **Quick prototyping.** Python lets you build working tools and applications extremely fast, which is critical in cybersecurity and IT automation.

---

## 9. Assembly Language & Reverse Engineering Tools

Though you won't write assembly in this course, understanding how to **read** it is useful — especially for cybersecurity.

### ARM7 Assembly Example

```
LDR R0, [address]    ; Load (read) data from memory into register R0
MOV R1, #2           ; Move the value 2 into register R1
ADD R2, R0, R1       ; Add R0 and R1, store result in R2
```

Key concepts:

- **LDR** (Load) = read from memory. **STR** (Store) = write to memory.
- **R0, R1, R2** = registers (small, fast temporary storage buffers inside the CPU).
- **MOV** = move a value into a register.
- **ADD** = add two values.

Assembly is **easy to read** (small number of instructions to learn — about a week of study). It is **hard to write well** because you need deep experience to know the most efficient sequence of instructions.

### Reverse Engineering Tools

| Tool | Purpose |
|:---|:---|
| **Cheat Engine** | Originally a game hacking tool — lets you watch memory addresses change in real-time and step through instructions. A good introduction to how binaries work under the hood |
| **OllyDbg / x64dbg** | Professional debuggers — load an executable and view its disassembled instructions; step through execution instruction by instruction |

Cheat Engine is a well-known tool in the gaming community for modifying game memory in real-time. It was mentioned here as an accessible, beginner-friendly example of software that lets you peek inside a running binary and see what's actually happening in memory. Tools like OllyDbg and x64dbg serve a similar purpose but are used professionally in cybersecurity for **malware analysis** — examining what a piece of software actually does at the instruction level.

---

## 10. Pragmatism in Programming

Programming is **problem-solving**, not art.

- Your computer does not care if your code looks elegant, clever, or well-organized.
- What matters is, in this order: **1. Correctness** — does it work? Does it handle edge cases? Does it produce the right result every time? **2. Efficiency** — does it make good use of the hardware it runs on?
- Five solid, no-nonsense, correct, and efficient codebases are worth more than one "beautiful" codebase. Why five to one? Because the time and effort spent obsessing over design elegance and aesthetic perfection is time not spent solving real problems. That same energy could have produced four more working solutions.
- This by no means suggests doing a half job — quite the opposite. You learn to be efficient, to focus your energy on what actually matters (correctness and performance), and to be tolerant of code that others might view as "not elegant." A pragmatic programmer ships working, reliable software. An idealistic programmer is still refactoring.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
