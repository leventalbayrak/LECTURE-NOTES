# In-Class Demo — Loops, Files, and a Pokémon Combat Simulator

This is a follow-along guide for the Tuesday in-class demo. The pieces are
designed to be typed and run in the order below. Each script builds on files
produced by the previous one, and by the end you'll have a working combat
simulator fed by data you generated yourself.

Wherever you've put the `followalong` project folder, `cd` into it before
running anything. The actual location on disk doesn't matter — what matters
is that your terminal is sitting inside the folder when you run the scripts,
because every command below uses relative paths from the project root.

The source data for all of this is `followalongdata/pokemon_names.txt` (1025 Pokémon names,
one per line).

---

## 1. `loop_review.py` — three ways to walk through a list

We start by reviewing loops. The same job (print every grocery) is done three
different ways. The progression is the whole point:

- **`while` with a counter** — the manual, index-driven version.
- **`for i in range(len(...))`** — Python gives us the counter.
- **`for item in groceries`** — we drop the counter entirely and iterate over
  the objects themselves.

**Convention worth saying out loud:** when the loop variable is an *index into a
list*, we name it `i` (or `j`, `k`). When the loop variable is *the actual
object*, we name it `item`, `x`, `line`, `pokemon` — something descriptive. If
you see `i` in a `for` loop it should be an integer index; if you see `item` it
should be the thing itself. This naming distinction will come back in every
script below.

```python
groceries = ["apple","orange","mango","banana", "pineapple"]

i = 0
while i<len(groceries):
    print(groceries[i])
    i+=1

print("---------------------------")
for i in range(len(groceries)):
    print(groceries[i])

print("---------------------------")
for item in groceries:
    print(item)
```

Run it:

```bash
python loop_review.py
```

---

## Interlude — relative vs absolute file paths

Before we start opening files, we need to be clear about **how Python finds
the file we're asking for**. Whenever you type a path — in a `cd` command, in
`open("…")`, or on the command line — that path is either **absolute** or
**relative**.

### Absolute paths

An absolute path starts from the root of the filesystem. On Linux/macOS it
starts with `/`, on Windows it starts with a drive letter like `C:\`. It is
unambiguous — it means the same thing no matter where you run it from.

```
/absolute/path/to/followalong/followalongdata/pokemon_names.txt
```

If you handed that string to `open(...)`, Python would find the file whether
you ran the script from your home directory, from `/tmp`, or from Mars.

Absolute paths are safe but they're also brittle — the moment someone else
clones your project, or you move the folder, every absolute path breaks. So
for the files that live **inside the project**, we use relative paths.

### Relative paths

A relative path is interpreted **starting from the current working directory**
— the directory your terminal is sitting in right now. You can see it with:

```bash
pwd
```

For this demo, `pwd` should print the path to wherever *you* put the
`followalong` folder — the exact location doesn't matter, as long as you're
inside it. Everything that follows assumes you've `cd`'d into the project
folder first:

```bash
cd /path/to/followalong        # whatever the real path to your folder is
```

Once you're there, these two commands open **the same file**:

```bash
python pickfavoritepokemon.py followalongdata/pokemon_names.txt
python pickfavoritepokemon.py /absolute/path/to/followalong/followalongdata/pokemon_names.txt
```

The first is a relative path. Python glues your current working directory
onto the front of it and looks for `./followalongdata/pokemon_names.txt`.

A few relative-path building blocks you'll see:

| Written as   | Means                                                |
| ------------ | ---------------------------------------------------- |
| `foo.txt`    | the file `foo.txt` in the current directory           |
| `./foo.txt`  | same thing, the `./` is just explicit                 |
| `data/foo.txt` | `foo.txt` inside the `data/` subfolder               |
| `../foo.txt` | `foo.txt` in the **parent** directory (one level up) |
| `../../foo.txt` | two levels up                                      |

### Which directory does Python use?

A common gotcha: when you run `python script.py`, Python's "current working
directory" is **the directory you ran the command from** — *not* the
directory where `script.py` lives. So, imagine your project folder is at
`/path/to/followalong`:

```bash
cd /path/to/followalong
python pickfavoritepokemon.py followalongdata/pokemon_names.txt     # works — relative to followalong
```

```bash
cd /path/to                                                         # one level up from the project
python followalong/pickfavoritepokemon.py followalongdata/pokemon_names.txt   # BREAKS — Python looks for followalongdata/ next to this directory, not inside followalong/
```

If you ever get `FileNotFoundError`, the first thing to check is `pwd` and
make sure the relative path makes sense from there.

### Where our demo files live

Keep this map in mind for the rest of the walk-through:

```
followalong/              ← cd here before running anything
├── followalongdata/
│   └── pokemon_names.txt  ← referenced as followalongdata/pokemon_names.txt
├── mylistA.txt            ← referenced as mylistA.txt (same directory as the script)
├── pokemon0.txt
├── combatlog.txt
└── pickfavoritepokemon.py, givepokemon.py, ...
```

All of the scripts below use **relative paths**. That's deliberate — it means
the demo keeps working for anyone who copies the folder somewhere else.

---

## 2. `pickfavoritepokemon.py` — `open`, `.read()`, `.split()`, and command-line arguments

First real file script. It introduces four things at once:

- `sys.argv` — command-line arguments. `sys.argv[0]` is the script name,
  `sys.argv[1]` is the first argument we pass.
- `open(filename, "r")` — open a file for **r**eading.
- `.read()` — slurps the entire file into one big string.
- `.split('\n')` — turns that one string into a list of lines.

It then opens a second file in `"w"` (**w**rite) mode and writes 10 randomly
picked Pokémon names into it, one per line. Note the `'\n'` we add when
writing — `write()` does not add newlines for you.

```python
"""pick 10 random pokemon names and print"""

import sys
import random

#command line arguments
print(sys.argv[0])
print(sys.argv[1])
filename = sys.argv[1]
hello = open(filename,"r")
text = hello.read()
pokemons = text.split('\n')

myfavpokemonfile = open("myfav.txt","w")

for k in range(10):
    randomindex = random.randint(0,len(pokemons)-1)
    print(pokemons[randomindex])
    myfavpokemonfile.write(pokemons[randomindex] + '\n')

myfavpokemonfile.close()
```

Run it (pass the names file as the argument):

```bash
python pickfavoritepokemon.py followalongdata/pokemon_names.txt
```

Afterwards, open `myfav.txt` — that's the file the script just wrote.

---

## 3. `givepokemon.py` — same idea, trimmed, and redirect `stdout` to a file

Now we strip `pickfavoritepokemon.py` down. No more writing a file from inside Python — the
script just **prints** 10 random Pokémon. We'll let the shell handle writing
to a file by **redirecting stdout** with `>`.

```python
"""pick 10 random pokemon names and print"""

import sys
import random

#command line arguments
filename = sys.argv[1]
hello = open(filename,"r")
text = hello.read()
pokemons = text.split('\n')

for k in range(10):
    randomindex = random.randint(0,len(pokemons)-1)
    print(pokemons[randomindex])
```

Run it a few times, routing the output into different files. This is how
`mylistA.txt`, `mylistB.txt`, `mylistC.txt`, `newpokemonlist.txt`, and
`coolestpokemons.txt` came to exist:

```bash
python givepokemon.py followalongdata/pokemon_names.txt
python givepokemon.py followalongdata/pokemon_names.txt > mylistA.txt
python givepokemon.py followalongdata/pokemon_names.txt > mylistB.txt
python givepokemon.py followalongdata/pokemon_names.txt > mylistC.txt
python givepokemon.py followalongdata/pokemon_names.txt > newpokemonlist.txt
python givepokemon.py followalongdata/pokemon_names.txt > coolestpokemons.txt
```

### `>` vs `>>` — redirecting stdout

The `>` operator is a **shell feature**, not a Python feature — the script
has no idea whether its `print` goes to the terminal or a file. The shell
sees `>` and `>>` on the command line, strips them off *before* launching
Python, and silently rewires where stdout lands.

Two flavors you'll use constantly:

| Operator | What it does                                                      |
| -------- | ----------------------------------------------------------------- |
| `>`      | **Overwrite.** Open the file fresh (creating it if it doesn't exist, truncating it to zero bytes if it does). Everything printed goes into the new file. The old contents are gone. |
| `>>`     | **Append.** Open the file for writing *at the end*. Anything printed is tacked onto whatever was already there. Also creates the file if it doesn't exist. |

Concretely:

```bash
python givepokemon.py followalongdata/pokemon_names.txt >  mylist.txt   # mylist.txt now has exactly 10 names
python givepokemon.py followalongdata/pokemon_names.txt >  mylist.txt   # mylist.txt STILL has 10 names (the previous ones were wiped)
python givepokemon.py followalongdata/pokemon_names.txt >> mylist.txt   # mylist.txt now has 20 names (10 new ones appended)
python givepokemon.py followalongdata/pokemon_names.txt >> mylist.txt   # mylist.txt now has 30 names
```

Mental model: `>` is "save as" (replaces the file), `>>` is "append to"
(adds to the end). Reach for `>>` when you want to grow a log or
accumulate results across runs; reach for `>` when you want a clean
file each time. If you ever use `>` on a file you cared about, there is
no undo — the old contents are gone the instant the shell opens the file.

---

## 4. `createpokemonfiles_readlines.py` — `.readlines()`

**Note on the name:** these next two scripts (`_readlines.py` and
`_readline.py`) are a matched pair. Despite the shared `createpokemonfiles`
prefix, the one in this section — the plural `_readlines.py` — doesn't
actually create any pokemon files; it just reads lines and prints them. The
*real* file generator is `_readline.py` (singular) in the next section. We
keep both so you can see the difference between `.readlines()` and
`.readline()` side by side — and so you can see for yourself *why* the next
script has to call `.strip()`.

Where `.read()` gives you one giant string, `.readlines()` gives you a
**list of strings**, one per line (newline characters still attached).

```python
import sys
import random

file = open(sys.argv[1], "r")
#read all lines in 1 list, 1 line per list element
lines = file.readlines()
print(lines)
```

Run it on one of the lists we just generated:

```bash
python createpokemonfiles_readlines.py mylistA.txt
```

You'll see something like `['tynamo\n', 'hydreigon\n', 'florges\n', ...]`.
Notice the `\n` on each entry — that's why we need `.strip()` in the next step.

---

## 5. `createpokemonfiles_readline.py` — `.readline()`, `.strip()`, and generating files in a loop

Now we meet the third reading method, `.readline()` (singular), which reads
**one line at a time**. We loop with `while True` and break out when
`.readline()` returns an empty string (EOF).

Each iteration:

- strips the trailing `\n` off the name,
- rolls random health and damage,
- opens a brand-new file named `pokemon{i}.txt`,
- writes three lines: name, health, damage.

The result is `pokemon0.txt` through `pokemon9.txt`.

```python
import sys
import random

file = open(sys.argv[1], "r")

i = 0
while True:
    line = file.readline()
    if line=="": break
    name = line.strip()
    newfile = open(f"pokemon{i}.txt","w")
    health = random.randint(10,100)
    damage = random.randint(10,20)
    content = f"{name}\n{health}\n{damage}"
    newfile.write(content)
    newfile.close()
    i+=1
```

Run it on one of our 10-name lists:

```bash
python createpokemonfiles_readline.py mylistA.txt
```

Peek at the result:

```bash
cat pokemon0.txt
```

You should see something like:

```
tynamo
31
19
```

---

## 6. `createcombatlog.py` — generate a combat log, redirect to a file

Now we need something for our 10 Pokémon to fight over. This script prints 100
random combat events. Each line is `attackerId<TAB>defenderId<TAB>damage`. IDs
run 0–9 so they line up with the `pokemon0.txt` … `pokemon9.txt` files.

```python
import random

for i in range(100):
    attackerid = random.randint(0,9)
    defenderid = random.randint(0,9)
    damage = random.randint(1,20)
    print(f"{attackerid}\t{defenderid}\t{damage}")
```

Run it and redirect into `combatlog.txt`:

```bash
python createcombatlog.py > combatlog.txt
```

Peek:

```bash
head combatlog.txt
```

---

## 7. `runcombat.py` — put it all together

This is the simulator. It:

1. Reads `combatlog.txt` into a list of lines with `.readlines()`.
2. Reads `pokemon0.txt`–`pokemon9.txt` into two parallel lists: `name` and
   `health`.
3. Prints the roster.
4. Walks the combat log one line at a time, splits each line into fields,
   subtracts damage from the defender's health, and prints a play-by-play.
5. Afterwards, partitions the Pokémon into `dead` and `alive` and prints the
   result.

Notice how both loop styles from §1 show up here:

- `for i in range(10):` — we need the integer `i` because it indexes **two
  parallel lists** (`name[i]` and `health[i]`).
- `for line in combatloglines:` — we only need the line itself, so we iterate
  over the objects.

```python
combatlogfile = open("combatlog.txt","r")
combatloglines = combatlogfile.readlines()

health = [0]*10
name = ["unknown"]*10

for i in range(10):
    file = open(f"pokemon{i}.txt", "r")
    namestring = file.readline().strip()
    healthstring = file.readline().strip()
    health[i] = int(healthstring)
    name[i] = namestring
    file.close()


for i in range(10):
    print(name[i], health[i])


for line in combatloglines:
    parts = line.split()
    attackerid = int(parts[0])
    defenderid = int(parts[1])
    damage = float(parts[2])

    attackername = name[attackerid]
    defendername= name[defenderid]
    health[defenderid] -= damage
    print(f"{attackername} attacked {defendername} for {damage}")
    print(f"{defendername} has {health[defenderid]}")


dead = []
alive = []


for i in range(10):
    if health[i] <= 0:
        dead.append(i)
    else:
        alive.append(i)


for i in range(len(dead)):
    print(f"RIP {name[dead[i]]}")

for i in range(len(alive)):
    print(f"{name[alive[i]]} alive with {health[alive[i]]} health!")
```

Run it:

```bash
python runcombat.py
```

Things to point out while reading it:

- `line.split()` with **no argument** splits on any whitespace (handles the
  tab from `createcombatlog.py` without us caring).
- `int(parts[0])` and `float(parts[2])` — everything read from a file is a
  string. If you want to do math on it, you convert it yourself.
- `health[defenderid] -= damage` — this is where the "parallel lists" idea
  pays off: the attacker's ID in the log file is also the index into our
  `name` and `health` lists.

---

## 8. `runcombatshort.py` — same program, Pythonic

Same behavior, rewritten using list comprehensions. Nothing new happens, but
it's a nice before/after to show how much the comprehension form compresses.

```python
combatlog = open("combatlog.txt").readlines()

files = [open(f"pokemon{i}.txt") for i in range(10)]
name = [f.readline().strip() for f in files]
health = [int(f.readline()) for f in files]

for i in range(10):
    print(name[i], health[i])

for line in combatlog:
    attacker, defender, damage = int(line.split()[0]), int(line.split()[1]), float(line.split()[2])
    health[defender] -= damage
    print(f"{name[attacker]} attacked {name[defender]} for {damage}")
    print(f"{name[defender]} has {health[defender]}")

dead  = [i for i in range(10) if health[i] <= 0]
alive = [i for i in range(10) if health[i] > 0]

for i in dead:  print(f"RIP {name[i]}")
for i in alive: print(f"{name[i]} alive with {health[i]} health!")
```

Run it:

```bash
python runcombatshort.py
```

Compare the two scripts side-by-side — same inputs, same outputs, very
different number of lines. Both are valid; one is easier to debug, the other
is easier to read once you're used to the syntax.

---

## Full replay — the whole demo from scratch

If you want to blow away the generated files and reproduce everything in one
shot:

```bash
python loop_review.py

python pickfavoritepokemon.py followalongdata/pokemon_names.txt

python givepokemon.py followalongdata/pokemon_names.txt > mylistA.txt

python createpokemonfiles_readlines.py mylistA.txt
python createpokemonfiles_readline.py mylistA.txt

python createcombatlog.py > combatlog.txt

python runcombat.py
python runcombatshort.py
```

## Cheatsheet — file reading methods

| Call             | Returns                                   | When to reach for it            |
| ---------------- | ----------------------------------------- | ------------------------------- |
| `.read()`        | one big string with the whole file        | small file, want to `.split()`  |
| `.readlines()`   | list of strings, one per line (keeps `\n`) | want all lines upfront          |
| `.readline()`    | one string, one line at a time (keeps `\n`) | streaming / unknown-size files  |

And remember `.strip()` — the newline is still attached whenever you read a
line, and it will absolutely bite you when you try to compare strings or
convert to `int`.
