
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# In-Class Code Examples

## Example 1: Parallel Arrays and Battle Simulation

**File:** [e1.py](e1.py)

```python
name = ["gengar", "pikachu", "wailord", "lucario", "bulbasaur"]
health = [100, 100, 300, 100, 100]
reflectdamage = [2.0,0,0.8,0,0]

file = open("log_ids_only.log", "r")
lines = file.readlines()
file.close()

for line in lines:
    parts = line.strip().split('\t')
    attackerid = int(parts[0])
    defenderid = int(parts[1])
    damage = int(parts[2])

    health[defenderid] -= damage
    if reflectdamage[defenderid] > 0:
        health[attackerid] -= damage * reflectdamage[defenderid]
        print("REFLECT!!!")

    print(f"{name[attackerid]} spit on {name[defenderid]} for {damage} water damage")
    print(f"attacker:{health[attackerid]} defender:{health[defenderid]}")
```

### What This Code Does:
- **Parallel Arrays as Lookup Tables**: Uses three parallel arrays (`name`, `health`, `reflectdamage`) to store Pokemon attributes where the index represents the Pokemon ID
- **Battle Log Processing**: Reads a tab-separated log file containing attacker ID, defender ID, and damage values
- **Damage Calculation**:
  - Applies damage to the defender's health
  - If the defender has reflect damage > 0, the attacker takes reflected damage
- **Array Indexing**: Uses integer IDs as indices to quickly look up Pokemon names and stats
- **Real-time Updates**: Modifies health values in the arrays as battles progress

---

## Example 2: String Slicing and Secret Message Extraction

**File:** [e2.py](e2.py)

```python
file = open("mydiary.txt", "r")
text = file.read()
file.close()

#secret message characters from 23 to 39 in reverse
msg = text[39:22:-1]

file = open("secretmessage.txt", "w")
file.write("your secret message is:\n")
file.write(msg)
file.write('\n')
file.write("\n******\ngoodbye!")
file.close()
```

### What This Code Does:
- **File Reading**: Reads the entire contents of `mydiary.txt` into a string
- **String Slicing with Negative Step**: Extracts characters from position 39 down to position 23 in reverse order using `[39:22:-1]`
  - Start at index 39
  - Stop before index 22
  - Step backward (-1) through the string
- **File Writing**: Creates a new file `secretmessage.txt` and writes the extracted secret message
- **Demonstrates**: Advanced string slicing techniques for extracting and reversing substrings

---

## Example 3: Parsing Structured Log Files

**File:** [e3.py](e3.py)

```python
file = open("log.log", "r")
lines = file.readlines()
file.close()

for line in lines:
    parts = line.strip().split(',')
    attacker = parts[0].split(':')[1]
    defender = parts[1].split(':')[1]
    damage = parts[2].split(':')[1]
    print(f"{attacker} attacked {defender} for {damage}")
```

### What This Code Does:
- **CSV Parsing**: Reads a comma-separated log file with key:value pairs
- **Two-Level String Splitting**:
  1. First split by comma to separate fields
  2. Then split each field by colon to extract values
- **Data Format**: Expects format like `attacker:name,defender:name,damage:value`
- **Output**: Prints formatted battle information extracting the actual names and damage from the structured data
- **Demonstrates**: Parsing structured text files with nested delimiters

---

## Example 4: Bulk File Generation with Random Data

**File:** [e4.py](e4.py)

```python
import random

for i in range(4):
    file = open(f"pokemon{i}.txt", "r")
    name = file.readline().strip()[1:-1]
    file.close()
    print(name)

for i in range(100000):
    file = open(f"spagett_{i}.exe", "w")

    filesize = random.randint(100,1000000)
    for j in range(filesize):
        c = chr( ord('a') + random.randint(0,25) )
        if c == 'y':
            file.write('\n')
        else:
            file.write(c)

    file.close()
```

### What This Code Does:
- **Part 1 - Reading Pokemon Names**:
  - Loops through 4 files named `pokemon0.txt` through `pokemon3.txt`
  - Reads the first line and strips the first and last characters (likely quotes)
  - Demonstrates f-string formatting for dynamic file names

- **Part 2 - Mass File Creation**:
  - Creates 100,000 files with random content
  - Each file gets a random size between 100 and 1,000,000 characters
  - Generates random lowercase letters (a-z) using ASCII math: `chr(ord('a') + random.randint(0,25))`
  - Uses 'y' as a newline character

- **Demonstrates**: File I/O in loops, f-string formatting, random data generation, and ASCII character manipulation

---

## Example 5: Arrays as Lookup Tables for Battle Logs

**File:** [e5.py](e5.py)

```python
names = [0]*4

for i in range(4):
    file = open(f"pokemon{i}.txt", "r")
    name = file.readline().strip()[1:-1]
    file.close()
    names[i] = name

file = open("log_ids_only.log", "r")
lines = file.readlines()
file.close()

for line in lines:
    parts = line.strip().split('\t')
    attackerid = int(parts[0])
    defenderid = int(parts[1])
    damage = int(parts[2])

    print(f"{names[attackerid]} spit on {names[defenderid]} for {damage} water damage")
```

### What This Code Does:
- **Array Initialization**: Creates a list of 4 zeros using `[0]*4` as placeholders
- **Loading Lookup Table**:
  - Reads Pokemon names from files `pokemon0.txt` through `pokemon3.txt`
  - Stores each name at its corresponding index in the array
  - Strips quotes from the names using `[1:-1]`

- **Using the Lookup Table**:
  - Reads a battle log with tab-separated values (attacker ID, defender ID, damage)
  - Uses IDs as indices to look up Pokemon names from the `names` array
  - Prints formatted battle messages

- **Key Concept**: Demonstrates how arrays function as lookup tables where:
  - The index represents an ID number
  - The value at that index is the associated data (in this case, names)
  - This allows O(1) constant-time lookups instead of searching through data

---

## Common Themes Across Examples

1. **File I/O Operations**: Reading from and writing to files using `open()`, `read()`, `readlines()`, `write()`, and `close()`
2. **String Manipulation**: Using `strip()`, `split()`, slicing, and f-strings for formatting
3. **Arrays as Lookup Tables**: Using list indices to represent IDs and quickly retrieve associated data
4. **Parallel Arrays**: Maintaining multiple arrays where corresponding indices represent the same entity
5. **Loop Patterns**: Using `for` loops with `range()` and iterating over file lines
6. **Data Parsing**: Breaking down structured text data into usable components

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
