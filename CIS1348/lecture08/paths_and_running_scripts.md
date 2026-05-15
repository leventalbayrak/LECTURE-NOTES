
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Running Python Scripts and File Paths

## Running a Python Script from the Terminal

Open a terminal, navigate to your project folder, then run:

`python` is itself a program installed on your computer. When you type `python mycode.py`, you are launching the Python application and passing it the name of your script file as an argument. Python reads that file, interprets the code line by line, and executes it — your `.py` file is just a text file; Python is the engine that runs it.

```bash
python mycode.py
```

> **Note:** On some systems (Mac/Linux) you may need `python3 mycode.py` instead.

---

## The Current Working Directory (CWD)

When you run a script, Python's starting location is your **current working directory** — wherever your terminal is when you type the command.

```bash
pwd          # print current directory (Mac/Linux)
cd Desktop   # change into Desktop folder
python mycode.py
```

Your script sees the world from that location. File paths in your code are resolved relative to it.

---

## Absolute vs Relative Paths

### Absolute Path
Starts from the root of the filesystem. Works from anywhere.

```
/home/alice/projects/data.txt        # Linux/Mac
C:\Users\Alice\projects\data.txt     # Windows
```

```python
file = open("/home/alice/projects/data.txt", "r")
```

### Relative Path
Starts from the current working directory. Shorter, but depends on where you run from.

```python
file = open("data.txt", "r")          # file is in CWD
file = open("data/scores.txt", "r")   # file is in a subfolder called data
file = open("../data.txt", "r")       # file is one folder UP from CWD
```

| Symbol | Meaning |
|--------|---------|
| `data.txt` | file in CWD |
| `folder/file.txt` | file inside a subfolder |
| `../file.txt` | one folder up |
| `../../file.txt` | two folders up |

---

## Running Scripts in Subfolders

Suppose your project looks like this:

```
project/
    mycode.py
    code/
        helper.py
    data/
        scores.txt
```

### From inside `project/`:

```bash
python mycode.py          # run mycode.py directly
python code/helper.py     # run a script inside the code/ subfolder
```

Inside `mycode.py`, to open `data/scores.txt`:
```python
file = open("data/scores.txt", "r")   # relative to project/
```

### From outside `project/` (e.g., one level up):

```bash
python project/mycode.py
```

Now the CWD is the parent folder, so relative paths in your script must account for that:
```python
file = open("project/data/scores.txt", "r")   # relative to parent/
```

**This is the most common source of "file not found" errors.**

---

## Checking and Setting the CWD in Python

```python
import os

print(os.getcwd())          # print current working directory
os.chdir("/home/alice/projects")  # change CWD (use sparingly)
```

A safer pattern — build paths relative to the script's own location:

```python
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, "data", "scores.txt")

file = open(filepath, "r")
```

This works no matter where you run the script from.

---

## Common Errors

| Error | Likely Cause |
|-------|-------------|
| `FileNotFoundError: [Errno 2] No such file or directory` | Wrong path or wrong CWD when running |
| Script runs but reads wrong file | CWD is not where you think it is |
| Works in one folder, breaks in another | Using a relative path that assumes a specific CWD |

**Debug tip:** Add `print(os.getcwd())` at the top of your script to see where Python thinks it is.

---

## Quick Reference

```bash
# Terminal commands
pwd                        # where am I?
ls                         # what's here?
cd foldername              # go into folder
cd ..                      # go up one level
python mycode.py           # run script from CWD
python code/mycode.py      # run script in subfolder
```

```python
# Python path helpers
import os
os.getcwd()                        # current working directory
os.path.abspath("data.txt")        # full absolute path of a relative path
os.path.join("data", "file.txt")   # build paths safely (handles / vs \)
os.path.dirname(__file__)          # folder containing the current script
```

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
