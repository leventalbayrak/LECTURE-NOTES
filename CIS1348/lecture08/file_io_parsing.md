
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# File I/O, Basic File Parsing, and Reporting

## 0. What is a File? How the OS Handles Files

A **file** is a named sequence of bytes stored on disk. The operating system (OS) manages all files through a layer called the **filesystem**, which tracks:

- where each file's data is physically stored on disk
- the file's name and location in the directory tree
- **permissions** — who is allowed to read, write, or execute the file

### Permissions

Every file has an owner and a set of permission bits that control access for three categories of users: the owner, the owner's group, and everyone else. A typical permission set looks like:

```
-rw-r--r--   (owner can read+write, group and others can only read)
```

Permissions exist because a computer can have multiple users and running programs. Without them, any program or user could read private data or overwrite system files. The OS enforces permissions — if your program doesn't have read access to a file, `open()` will raise an error.

### The file lifecycle: open → use → close

A program cannot directly access a file on disk. It must go through the OS by following three steps:

1. **Open** — the program asks the OS for access to a named file. The OS checks permissions and, if allowed, returns a **file handle** (a connection to the file). In Python this is the object returned by `open()`.
2. **Read / Write** — the program uses the handle to read data from or write data to the file. All I/O goes through the OS, which manages the actual disk access.
3. **Close** — the program tells the OS it is done. The OS flushes any buffered data to disk, releases the handle, and frees system resources. Failing to close a file can leave data unwritten or lock the file from other programs.

```
Program  →  open("data.txt")  →  OS checks permissions  →  returns file handle
Program  →  read / write via handle  →  OS moves data to/from disk
Program  →  close()  →  OS flushes buffer, releases handle
```

---

## 1. Opening and Closing Files

```python
file = open("data.txt", "r")
# ... read from file ...
file.close()
```

`open()` takes two arguments: the filename and the **mode**:
- `"r"` — read
- `"w"` — write (overwrites file)
- `"a"` — append (adds to end)

Always call `.close()` when done. Forgetting to close a write can cause data loss.

---

## 2. Three Ways to Read a File

### Method 1: `file.read()` — entire file as one string

```python
file = open("data.txt", "r")
content = file.read()   # one big string, newlines included
print(content)
file.close()
```

Best for small files where you need the whole content at once.

### Method 2: `file.readlines()` — all lines as a list

```python
file = open("data.txt", "r")
lines = file.readlines()   # ["line1\n", "line2\n", "line3\n"]
file.close()

for line in lines:
    print(line.strip())    # .strip() removes the \n
```

Best when you need to go through lines **more than once**, or need to access a specific line by index (e.g., `lines[5]`). Data stays in memory after the file is closed.

### Method 3: `for line in file` — one line at a time

```python
file = open("data.txt", "r")
for line in file:
    print(line.strip())
file.close()
```

Best for large files — processes one line at a time without loading everything into memory. Most common pattern for log processing.

### Which to use?

| Method | When |
|---|---|
| `read()` | Small file, need whole content as one string |
| `readlines()` | Need to process lines multiple times, or access by index |
| `for line in file` | Large file, single-pass processing |

---

## 3. Cleaning Lines: `.strip()`

Every line read from a file has `\n` at the end. Strip it before comparing or storing:

```python
line = "alice\n"
line = line.strip()   # → "alice"
```

Without `.strip()`, `"alice\n" == "alice"` is `False` — this causes silent bugs in searches.

---

## 4. Writing to Files

### Write mode `"w"` — creates or overwrites

```python
file = open("report.txt", "w")
file.write("Name\tScore\n")
file.write("alice\t85\n")
file.write("bob\t92\n")
file.close()
```

If `report.txt` already exists, it is **completely replaced**. If it doesn't exist, it is created.

### Append mode `"a"` — adds to end

```python
file = open("report.txt", "a")
file.write("carol\t78\n")
file.close()
```

Existing content is preserved. New lines go at the end.

**Rule:** Use `"w"` to generate a fresh report. Use `"a"` to accumulate data across multiple runs.

Note: `file.write()` does **not** add a newline automatically — you must include `\n` yourself.

---

## 5. Iterating Over Lines and Processing

The most common workflow: open → read line by line → do something with each line.

```python
file = open("scores.txt", "r")
total = 0
count = 0

for line in file:
    score = int(line.strip())
    total += score
    count += 1

file.close()
print(f"Average: {total / count}")
```

---

## 6. Parsing Structured Lines with `.split()`

Most data files have structured lines — fields separated by a delimiter. `.split(delimiter)` breaks a string into a list of substrings.

```python
"alice,85,B".split(',')    # → ["alice", "85", "B"]
"0 1 12".split()           # → ["0", "1", "12"]   (no arg = split on whitespace)
```

### Example: comma-separated data

```python
file = open("students.txt", "r")
for line in file:
    parts = line.strip().split(',')
    name  = parts[0]
    score = int(parts[1])
    grade = parts[2]
    print(f"{name} scored {score} ({grade})")
file.close()
```

### Nested delimiters

Some formats use two levels of delimiters. Parse from outside in:

```python
# Line format: "name:alice,score:85,grade:B"

line = "name:alice,score:85,grade:B"
parts = line.split(',')          # ["name:alice", "score:85", "grade:B"]

name  = parts[0].split(':')[1]   # "alice"
score = int(parts[1].split(':')[1])  # 85
grade = parts[2].split(':')[1]   # "B"
```

**Strategy:** identify the outer delimiter (`,`), split by it first. Then identify the inner delimiter (`:`), split each piece by it. Take `[1]` to get the value after the colon.

Verbose version (same result, easier to follow):

```python
name_part   = parts[0]              # "name:alice"
name_pieces = name_part.split(':')  # ["name", "alice"]
name        = name_pieces[1]        # "alice"
```

---

## 7. Dynamic Filenames with F-Strings

F-strings let you build strings with variables substituted in:

```python
name = "alice"
score = 85
print(f"{name} scored {score}")   # "alice scored 85"
```

Anything inside `{}` is evaluated and inserted. The `f` before the quote makes it an f-string.

**Using f-strings for dynamic filenames** — essential when data is spread across many numbered files:

```python
# Files: student_0.txt, student_1.txt, student_2.txt, ...

for i in range(10):
    filename = f"student_{i}.txt"
    file = open(filename, "r")
    name = file.read().strip()
    file.close()
    print(f"Student {i}: {name}")
```

The loop generates the correct filename each iteration. This pattern is how you load data from a numbered file system into a parallel list indexed by ID.

---

## 8. Full Workflow: Read → Parse → Process → Write Report

Real programs follow this pipeline:

**Step 1 — Load reference data** (e.g., names by ID):
```python
names = [""] * 100
for i in range(100):
    f = open(f"member_{i}.txt", "r")
    names[i] = f.readline().strip()
    f.close()
```

**Step 2 — Read and parse the main data file**:
```python
file = open("data.txt", "r")
lines = file.readlines()
file.close()

values = []
for line in lines:
    parts = line.strip().split(',')
    values.append(int(parts[1]))
```

**Step 3 — Process** (aggregate, filter, compute):
```python
total = sum(values)
average = total / len(values)
```

**Step 4 — Write the report**:
```python
report = open("output.txt", "w")
report.write("Summary Report\n")
report.write(f"Total: {total}\n")
report.write(f"Average: {average:.2f}\n")
report.close()
```

Tab-separated format is common for columnar reports:
```python
report.write("id\tname\tvalue\n")    # header
for i in range(len(names)):
    report.write(f"{i}\t{names[i]}\t{values[i]}\n")
```

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
