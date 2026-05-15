
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Linux Command Line and Terminal-Based Development

## Table of Contents
1. [Introduction](#introduction)
2. [Why Learn the Command Line?](#why-learn-the-command-line)
3. [Terminal Setup](#terminal-setup)
4. [Basic Navigation Commands](#basic-navigation-commands)
5. [File and Directory Operations](#file-and-directory-operations)
6. [Writing Python Code in the Terminal](#writing-python-code-in-the-terminal)
7. [Understanding Standard Input and Output](#understanding-standard-input-and-output)
8. [Git Workflow from the Command Line](#git-workflow-from-the-command-line)
9. [Command Reference](#command-reference)

---

## Introduction

The command line (terminal) is a text-based interface for interacting with your computer. While graphical user interfaces (GUIs) like Visual Studio Code provide convenience, understanding the command line is essential for any IT professional. Many tools, servers, and remote systems only provide command-line access, making this skill indispensable.

**Key Insight:** Visual Studio Code and similar tools are just text editors with helpful features. They don't actually run your code - they use the terminal to do it for you.

---

## Why Learn the Command Line?

**Reasons to learn command line:**
- **Industry Standard:** Most servers run Linux and are managed via command line
- **Remote Work:** SSH connections to servers provide only terminal access
- **Automation:** Shell scripts automate repetitive tasks
- **Understanding:** Know what's really happening when you click buttons in IDEs
- **Efficiency:** Many operations are faster via command line
- **Professional Skill:** Expected knowledge in IT careers

---

## Terminal Setup

### Getting Started with the Terminal

**Mac Users:**
- Open Terminal (Applications → Utilities → Terminal, or search for "Terminal")
- You're ready to go - Mac is Unix-based and has all the standard commands

**Windows Users:**
- Open Git Bash by searching for "Git Bash" in the Windows application menu (Start menu)
- Git Bash provides a Linux-compatible terminal environment
- For this class, use Git Bash instead of PowerShell or Command Prompt. Git Bash uses Linux-style commands that work the same way on servers and other systems.

**Linux Users:**
- Open your default terminal (usually Ctrl+Alt+T)
- You're already in a native Linux environment

**VS Code Users:**
- You can also use the integrated terminal: View → Terminal (or Ctrl+` )
- Make sure to select Git Bash in the dropdown on Windows

---

## Basic Navigation Commands

### Understanding Your Location

The file system is organized like a tree. You're always "in" a specific folder (directory). Think of it like using File Explorer, but with text commands instead of clicking.

### Essential Navigation Commands

#### pwd - Print Working Directory
Shows your current location in the file system.

```bash
pwd
```

**Example Output:**
```
/home/username/Documents
```

This is like looking at the address bar in File Explorer - it tells you exactly where you are.

---

#### ls - List Directory Contents
Shows files and folders in your current location.

```bash
ls                # Basic listing
ls -l             # Detailed listing with permissions and sizes
ls -a             # Show hidden files (files starting with .)
ls -la            # Combination: detailed listing including hidden files
```

**Example Output:**
```bash
$ ls
Documents  Downloads  Music  Pictures

$ ls -l
drwxr-xr-x  5 username  staff   160 Feb 10 14:30 Documents
drwxr-xr-x  3 username  staff    96 Feb 10 09:15 Downloads
drwxr-xr-x  2 username  staff    64 Feb 09 18:22 Music
drwxr-xr-x  4 username  staff   128 Feb 10 12:45 Pictures
```

---

#### cd - Change Directory
Navigate between folders.

```bash
cd Documents           # Go into Documents folder
cd ..                  # Go up one level (to parent directory)
cd ../..               # Go up two levels
cd ~                   # Go to your home directory
cd /                   # Go to root directory
```

**Tab Completion:** Type the first few letters of a folder name and press Tab - the terminal will auto-complete it for you.

**Example:**
```bash
cd Doc<press Tab>     # Auto-completes to "cd Documents/"
```

---

## File and Directory Operations

### Creating Directories

#### mkdir - Make Directory
Creates new folders.

```bash
mkdir my_project              # Create single folder
mkdir -p path/to/nested/dir   # Create nested folders (-p creates parent directories)
```

**Example:**
```bash
mkdir problem_set_1
cd problem_set_1
pwd
# Output: /home/username/Documents/problem_set_1
```

---

### File Operations

#### touch - Create Empty File
Creates a new, empty file.

```bash
touch main.py
touch notes.txt
```

---

#### cp - Copy Files
Copies files from source to destination.

```bash
cp source.txt destination.txt           # Copy file
cp source.txt /path/to/destination/     # Copy to different directory
cp -r folder_name new_folder_name       # Copy entire directory (-r = recursive)
```

**Example:**
```bash
cp README.md backup_README.md
```

---

#### mv - Move or Rename Files
Moves files to a new location OR renames them.

```bash
mv old_name.txt new_name.txt                    # Rename file
mv file.txt /path/to/destination/               # Move file
mv file.txt /path/to/destination/newname.txt    # Move and rename
```

**Example:**
```bash
# Rename a file
mv mycode.txt mycode.py

# Move a file into a folder
mv mycode.py problem_600/
```

---

## Writing Python Code in the Terminal

One of the most powerful aspects of the command line is the ability to write and execute code without ever opening a GUI application. This is exactly how you'd work on a remote server.

### Using Nano Text Editor

**Nano** is a simple, beginner-friendly text editor that runs in the terminal.

#### Step-by-Step: Writing Your First Python Program

**Step 1: Navigate to your desired folder**
```bash
cd ~/Documents
mkdir python_practice
cd python_practice
```

**Step 2: Create and edit a Python file**
```bash
nano hello.py
```

This opens the nano editor. You'll see a blank screen with menu options at the bottom.

**Step 3: Write your Python code**
Type the following in the nano editor:
```python
x = input()
print("You typed:", x)
```

**Step 4: Save and exit**
- Press `Ctrl+O` (WriteOut) to save
- Press `Enter` to confirm the filename
- Press `Ctrl+X` to exit nano

**Nano Quick Reference:**

| Command | Action |
|---------|--------|
| `Ctrl+O` | Save (WriteOut) |
| `Ctrl+X` | Exit |
| `Ctrl+K` | Cut line |
| `Ctrl+U` | Paste |
| `Ctrl+W` | Search |
| `Ctrl+G` | Help |

---

### Running Your Python Program

Now that you've written a Python file, you need to run it with the Python interpreter.

```bash
python hello.py
# or on some systems:
python3 hello.py
```

**What happens:**
1. The terminal passes the filename `hello.py` to the Python interpreter
2. Python opens the file and reads it line by line
3. Python executes each instruction
4. The program waits for input (because of `input()`)
5. You type something and press Enter
6. Python prints your output

**Example session:**
```bash
$ python hello.py
test input
You typed: test input
```

---

### Important: Python Files Are Just Text

**Key Understanding:**
- `.py` files are plain text files
- The `.py` extension is cosmetic - it helps you and the OS identify Python code
- You could open a `.py` file in Notepad - it's just text
- The Python interpreter (`python.exe` or `python`) is a program that reads and executes Python code

**What VS Code Actually Does:**
When you click the "Run" button in VS Code, it:
1. Opens a terminal (in the bottom panel)
2. Types `python your_file.py`
3. Presses Enter for you

VS Code doesn't run Python - it just automates typing terminal commands for you.

---

## Understanding Standard Input and Output

### How Programs Communicate

When a Python program runs in the terminal, it needs two things:
1. A way to receive input from the user (**stdin** - standard input)
2. A way to send output to the user (**stdout** - standard output)

These are communication channels between your program and the terminal.

**Flow of data:**
1. You type input in the terminal
2. When you press Enter, that text flows through stdin (standard input) to your Python program
3. Your program processes the data
4. Output flows through stdout (standard output) from your program to the terminal
5. The terminal displays the output on your screen

---

### Standard Input (stdin)

**What is it?**
- A stream of text data that flows FROM the terminal TO your program
- Everything comes in as strings (text)
- Created when the user types and presses Enter

**In Python: The `input()` Function**

```python
x = input()
```

**What happens:**
1. Python hits the `input()` function
2. Execution **blocks** (freezes, waits)
3. Python watches stdin for data
4. User types text and presses Enter
5. The text is captured as a string
6. The string is stored in variable `x`
7. Execution continues to the next line

**Blocking Behavior:**
"Blocking" means your program stops and waits. It cannot continue until the user provides input. This is intentional - the program needs that data to proceed.

**Important: Input is ALWAYS a String**

```python
x = input()  # User types: 123
# x = "123" (string, not integer)

# To use it as a number:
y = int(x)   # y = 123 (integer)
```

---

### Standard Output (stdout)

**What is it?**
- A stream of text data that flows FROM your program TO the terminal
- Displays text on the screen
- Created when you use `print()`

**In Python: The `print()` Function**

```python
print("Hello, World!")
```

**What happens:**
1. Python evaluates the string `"Hello, World!"`
2. Python writes it to stdout
3. The terminal reads from stdout
4. The terminal displays the text on screen

---

### Example: Echo Program

**File: `echo.py`**
```python
x = input()
print(x)
```

**Session:**
```bash
$ python echo.py
hello there    ← You type this and press Enter
hello there    ← Program outputs this
```

**What happened:**
1. `input()` blocks and waits for stdin
2. You type "hello there" and press Enter
3. The string "hello there" is stored in `x`
4. `print(x)` writes "hello there" to stdout
5. Terminal displays it

---

### Example: Type Conversion

**File: `add_numbers.py`**
```python
x = input()      # Read first number as string
y = input()      # Read second number as string

num1 = int(x)    # Convert to integer
num2 = int(y)    # Convert to integer

result = num1 + num2
print(result)
```

**Session:**
```bash
$ python add_numbers.py
5       ← First input
3       ← Second input
8       ← Output
```

---

### Common Mistake: Prompts in `input()`

Python allows you to put a prompt string inside `input()`:

```python
x = input("Please enter a number: ")
```

**This will display:**
```bash
Please enter a number: _
```

**Why is this a problem for assignments?**

The prompt "Please enter a number: " gets written to **stdout**. Your program's output now includes this text, which doesn't match the expected output format.

**Problem Set Rule:**
Unless explicitly told to include a prompt, use empty `input()`:

```python
x = input()  # Correct - no prompt
```

Not:
```python
x = input("Enter something: ")  # Wrong - adds unwanted output
```

---

### Stdin/Stdout in Problem Sets

**Typical Problem Format:**

**Input Format:** Two integers, one per line

**Output Format:** Their sum

**Example:**
```
Input:
5
3

Output:
8
```

**Your Code:**
```python
x = int(input())
y = int(input())
print(x + y)
```

**Why this matters:**
Your program is tested automatically. A testing program:
1. Writes test input to your stdin
2. Captures your stdout
3. Compares your stdout to expected output
4. Any extra text (like prompts) causes mismatch → failure

---

## Git Workflow from the Command Line

Git is version control software that tracks changes to your code. GitHub is a website that hosts Git repositories. All Git operations can be done from the command line.

### Initial Setup: Configure Git

**First time only:** Tell Git who you are.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Note:** The email doesn't have to be real - it's just an identifier for your commits. The `--global` flag makes these settings apply to all your Git repositories.

---

### Typical Workflow: GitHub Classroom Assignment

#### Step 1: Clone the Repository

**What is cloning?**
Copying a repository from GitHub to your local computer.

```bash
# Navigate to where you want the project
cd ~/Documents

# Clone the repository
git clone https://github.com/yourusername/assignment-repo.git
```

**What happens:**
- Git downloads the repository
- Creates a new folder with the repository name
- Sets up Git tracking inside that folder

**Example:**
```bash
$ cd ~/Documents/class_work
$ git clone https://github.com/student123/problem-set-1.git

Cloning into 'problem-set-1'...
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (10/10), done.
Receiving objects: 100% (15/15), done.

$ ls
problem-set-1

$ cd problem-set-1
$ ls
problem_600  problem_601  problem_602  README.md
```

---

#### Step 2: Work on Your Code

Navigate to the specific problem folder and create your solution.

```bash
cd problem_600
nano main.py
```

Write your code in nano, save, and exit.

Test your code:
```bash
python main.py
```

---

#### Step 3: Stage Your Changes (git add)

**What is staging?**
Marking files to be included in your next commit. It's like selecting which changes you want to save.

```bash
git add -A
```

**Common Options:**

| Command | What it does |
|---------|-------------|
| `git add -A` | Add all changes (modified, new, deleted files) everywhere in the repository |
| `git add .` | Add all changes in current directory and subdirectories |
| `git add main.py` | Add specific file only |

**Recommendation:** Use `git add -A` for assignments. Since problem sets have multiple folders (problem_600, problem_601, etc.) and you may work on several problems, `-A` ensures all your changes are captured no matter where you are in the directory structure.

---

#### Step 4: Commit Your Changes (git commit)

**What is a commit?**
A snapshot of your code at a point in time. It's like saving a checkpoint in a game.

```bash
git commit -m "Solved problem 600"
```

**The `-m` flag** provides a commit message describing what you changed.

**Good commit messages:**
- "Solved problem 600"
- "Fixed bug in input handling"
- "Completed all problems"

**Bad commit messages:**
- "stuff"
- "asdf"
- "final" (never truly final)

---

#### Step 5: Push to GitHub (git push)

**What is pushing?**
Uploading your commits from your local computer to GitHub.

```bash
git push
```

**What happens:**
1. Git compares your local repository to GitHub's version
2. Git uploads new commits
3. GitHub updates to match your local version

**Example Output:**
```bash
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 298 bytes | 298.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/student123/problem-set-1.git
   a1b2c3d..e4f5g6h  main -> main
```

---

### Complete Example Workflow

Let's walk through a complete example of cloning a repository, solving a problem, and submitting it.

**Scenario:** You've been assigned Problem Set 1 via GitHub Classroom. The assignment has multiple problems.

```bash
# 1. Navigate to your class folder
cd ~/Documents/CIS1314

# 2. Clone the assignment repository
git clone https://github.com/yourusername/problem-set-1-yourusername.git

# Example output:
# Cloning into 'problem-set-1-yourusername'...
# remote: Enumerating objects: 20, done.
# remote: Counting objects: 100% (20/20), done.
# Receiving objects: 100% (20/20), done.

# 3. Enter the repository folder
cd problem-set-1-yourusername

# 4. See what's inside
ls
# Output: problem_600/  problem_601/  problem_602/  README.md

# 5. Go into the first problem
cd problem_600

# 6. Check what's required
ls
# Output: README.md

# 7. Read the instructions (optional but recommended)
cat README.md

# 8. Create your solution file
nano main.py

# --- In nano, write your code: ---
x = input()
print(x)
# --- Then save (Ctrl+O, Enter) and exit (Ctrl+X) ---

# 9. Test your code
python main.py
# Type: hello
# Output: hello
# (Looks good!)

# 10. Go back to repository root
cd ..

# 11. Check status (see what changed)
git status
# Output:
# On branch main
# Untracked files:
#   problem_600/main.py

# 12. Stage all changes
git add -A

# 13. Verify staging
git status
# Output:
# On branch main
# Changes to be committed:
#   new file:   problem_600/main.py

# 14. Commit with a message
git commit -m "Completed problem 600 - echo program"
# Output:
# [main a1b2c3d] Completed problem 600 - echo program
#  1 file changed, 2 insertions(+)

# 15. Push to GitHub
git push
# Output:
# Enumerating objects: 5, done.
# Writing objects: 100% (4/4), 367 bytes, done.
# Total 4 (delta 0), reused 0 (delta 0)
# To https://github.com/yourusername/problem-set-1-yourusername.git
#    e4f5g6h..a1b2c3d  main -> main

# Done! Your solution is now on GitHub.
```

---

### Checking Your Work on GitHub

After pushing, verify your submission:

1. Go to your repository on GitHub (the URL you cloned from)
2. Click on the `problem_600` folder
3. You should see `main.py` listed
4. Click on `main.py` to view your code
5. Check the commit message and timestamp

---

### Common Git Commands Summary

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `git clone <url>` | Copy repository from GitHub to local | Once per assignment, at the start |
| `git status` | See what files have changed | Anytime you want to check what's modified |
| `git add -A` | Stage all changes | Before committing |
| `git commit -m "msg"` | Save snapshot with message | After completing work |
| `git push` | Upload commits to GitHub | After committing, to submit |
| `git pull` | Download updates from GitHub | If repository changed on GitHub |

---

## Command Reference

### Navigation & Information

```bash
pwd                    # Print working directory
ls                     # List files
ls -l                  # List with details
ls -a                  # List including hidden files
cd folder_name         # Change to folder
cd ..                  # Go up one level
cd ~                   # Go to home directory
```

### File & Directory Management

```bash
mkdir folder_name      # Create directory
mkdir -p path/to/dir   # Create nested directories
touch file.txt         # Create empty file
cat file.txt           # Display file contents
cp source dest         # Copy file
cp -r folder1 folder2  # Copy directory
mv old new             # Move or rename
rm file.txt            # Delete file (PERMANENT! No undo!)
rm -r folder           # Delete directory and contents (VERY DANGEROUS!)
```

### Text Editors

```bash
nano file.py           # Edit file with nano
vim file.py            # Edit file with vim (advanced)
```

### Python

```bash
python file.py         # Run Python script
python3 file.py        # Run with Python 3 (some systems)
```

### Git

```bash
git clone <url>              # Clone repository
git status                   # Check status
git add -A                   # Stage all changes
git add file.py              # Stage specific file
git commit -m "message"      # Commit changes
git push                     # Push to remote
git pull                     # Pull from remote
git log                      # View commit history
```

### Useful Shortcuts

```bash
Tab                    # Auto-complete file/folder names
Ctrl+C                 # Cancel current command
Ctrl+L                 # Clear screen
Ctrl+D                 # Exit terminal
↑ / ↓                  # Navigate command history
```

---

## Best Practices

### For Problem Sets

1. **No prompts in `input()`** - Use `input()` not `input("prompt")`
2. **Test with provided examples** - Your output must match exactly
3. **Work in the correct folder** - Each problem has its own `main.py`
4. **Test before pushing** - Run your code locally first
5. **Use `git add -A`** - Ensures all changes are captured

### For Terminal Work

1. **Use Tab completion** - Type less, make fewer mistakes
2. **Check with `pwd` and `ls`** - Know where you are
3. **Prefer Git Bash on Windows** - More universal commands
4. **Read error messages** - They tell you what's wrong
5. **Start assignments early** - Time to ask questions and get help

### For Git

1. **Clone once** - Don't re-clone unless starting over
2. **Commit often** - Small checkpoints are good
3. **Write clear messages** - Your future self will thank you
4. **Push when ready** - But test first
5. **Check GitHub after pushing** - Verify submission

---

## Troubleshooting

### "Command not found"

**Problem:** Terminal says `python: command not found`

**Solutions:**
- Try `python3` instead of `python`
- Python may not be installed - install it
- Python may not be in your PATH - check installation

---

### "No such file or directory"

**Problem:** Terminal can't find your file

**Solutions:**
- Use `ls` to see what's in the current directory
- Use `pwd` to see where you are
- Make sure you're in the right folder
- Check spelling of filename (case-sensitive!)

---

### Git asks for credentials

**Problem:** Git asks for username/password when pushing

**Solutions:**
- You may need to set up SSH keys or personal access token
- GitHub no longer accepts passwords - use token or SSH
- See CIS Help or professor for setup assistance

---

### "Permission denied"

**Problem:** Can't write file or execute command

**Solutions:**
- You might not have permission in that directory
- Try working in your home directory (`cd ~`)
- On shared systems, stay in your user folder

---

## Next Steps

**Practice exercises:**
1. Create a folder structure for your class work
2. Write a Python program using nano that asks for your name and age, then prints a greeting
3. Create a test Git repository and practice the add/commit/push workflow
4. Write a program that reads two numbers from stdin and outputs their product

**Remember:** The command line is powerful but takes practice. Start with these basics, and you'll become more comfortable with each use.

---

## Additional Resources

- **Git Documentation:** https://git-scm.com/doc
- **Nano Editor Guide:** https://www.nano-editor.org/dist/latest/nano.html
- **Linux Command Reference:** https://man7.org/linux/man-pages/
- **Python Documentation:** https://docs.python.org/3/

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
