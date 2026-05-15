
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Parallel Arrays (Structure of Arrays) vs. Array of Arrays (Array of Structures)

The examples are in Python, but this is a data layout decision that exists in every language. The trade-offs are the same whether you're writing C, Java, or assembling spreadsheets.

---

## The Core Question

When you have a collection of entities — each with multiple properties — how do you lay that data out in memory? Say you have a company's employees, and each employee has an ID, a name, a salary, and a department. How do you organize that?

There are two answers, and they reflect a deep trade-off in how computers and humans think about data.

Humans think in terms of *things*. You look at a car and see one object — engine, body, tires, steering wheel all fused together. You don't think "there is an engine floating in space, and somewhere else a body, and somewhere else four tires, and they happen to share the number 7." You think "that is *one car*." Array of Structures mirrors this instinct: each entity is stored as a single bundled unit, all its properties side by side. One employee, one container — ID, name, salary, department all together.

Computers don't care about "things." They care about doing the same operation on a long run of identical data as fast as possible. If you need to compute the average salary across 10,000 employees, the computer wants all the salaries lined up in a row — it doesn't want to dig through each employee's name, ID, and department just to find the next salary. Structure of Arrays mirrors this reality: each property type gets its own contiguous list, optimized for bulk processing. All salaries in one list, all names in another, all departments in another.

AoS is easier for humans to read, reason about, and keep correct. SoA is easier for computers to process efficiently, and it makes certain structural changes — like adding a new property to every entity, or removing one — trivial. The rest of these notes show you *why*.

---

## Option 1 — Array of Structures (AoS) / Encapsulated Layout

Everything about one entity lives together. You store an employee as one unit — ID, name, salary, department all in one container. Then you store all your employees in a list of those containers.

```python
# Each inner list is one complete employee record
employees = [
    [1001, "sara",   72000, "engineering"],
    [1002, "mike",   65000, "marketing"],
    [1003, "priya",  91000, "engineering"],
    [1004, "carlos", 58000, "sales"],
]
```

Each inner list is one employee — one indivisible record. To access priya's salary:

```python
print(employees[2][2])   # 91000
```

`employees[2]` is the entity (priya's row). `[2]` is the property within that entity (salary).

Because the entity is bundled, moving, deleting, or swapping an employee moves all their properties simultaneously. You can't accidentally leave someone's salary behind while their name drifts to another row.

This idea — bundling related data into a single unit — is the root of **object-oriented programming**. A Python `class`, a C `struct`, a Java object: these are all the same instinct made formal. Instead of inner lists you get named fields and methods, but the underlying principle is identical: keep data that belongs together, together.

---

## Option 2 — Structure of Arrays (SoA) / Parallel Arrays

Each property gets its own list. Think of a spreadsheet: one column for IDs, one for names, one for salaries, one for departments. The row number (index) is what ties them together.

```python
ids         = [1001,    1002,       1003,    1004]
names       = ["sara",  "mike",     "priya", "carlos"]
salaries    = [72000,   65000,      91000,   58000]
departments = ["engineering", "marketing", "engineering", "sales"]
```

Priya is at index 2 in every list:

```python
print(names[2])      # 'priya'
print(salaries[2])   # 91000
```

The data is correct as long as all lists stay in sync. Nothing in the code enforces that — the contract is entirely implicit. The integrity of the entire dataset rests on the developer being careful.

---

## Why Parallel Arrays Exist

The parallel layout isn't just an accident. It gives you capabilities that the encapsulated layout makes awkward or expensive.

**Bulk processing without touching irrelevant data.** Want the average salary? With SoA, you hand the `salaries` list to a function and you're done. With AoS, you have to loop through every employee record, pull out `[2]` from each one, and collect them — hopping through names, IDs, and departments you don't care about.

```python
# SoA — direct, one list
avg_salary = sum(salaries) / len(salaries)

# AoS — have to dig through each record
avg_salary = sum(emp[2] for emp in employees) / len(employees)
```

**Adding or removing a property is trivial.** Say every employee now needs a `start_year`. With SoA, you create one new list. The existing lists are untouched — nothing breaks. With AoS, you have to go into every single inner list and append a value. If you have 10,000 employees, that's 10,000 modifications.

```python
# SoA — add a property: create one new list
start_years = [2019, 2021, 2018, 2022]

# AoS — add a property: modify every single record
for emp in employees:
    emp.append(???)   # you need a value for each one
```

Removing a property is the same story. With SoA, delete one list. With AoS, loop through every record and delete an element.

**Isolation.** You can hand the `salaries` list to a function, a library, or a separate part of your program without exposing names, IDs, or departments. Each property exists independently. In AoS, you hand over complete employee records every time, even if the recipient only needs one field.

**Parallel processing.** When you need to apply the same operation to every value — give everyone a 5% raise, convert all salaries from dollars to euros, flag every employee in a specific department — SoA lets you hand one array to one processor (or thread, or core) and let it rip through the data without coordination. You could even process salaries and departments simultaneously on different cores, because the arrays are independent. With AoS, every thread needs to touch the same employee records, and you're constantly stepping over data you don't need to reach the one field you do.

### What's Happening in the Hardware

CPUs don't read one value at a time from RAM. They load data in blocks called **cache lines** — chunks of adjacent memory pulled into fast on-chip cache.

With SoA, all salaries sit next to each other in memory. The CPU loads a cache line and it's full of salaries — every byte is useful work.

With AoS, the salaries are interleaved with names, IDs, and departments. The CPU loads a cache line and most of it is data you don't care about. You're paying for memory bandwidth you're wasting.

This is one reason SoA dominates in data science (Pandas, NumPy), database engines, and GPU programming.

> *Note: Standard Python lists are arrays of pointers, so the cache behavior described here applies most directly in C/C++ or libraries like NumPy that allocate contiguous memory blocks. The conceptual trade-off is the same regardless.*

---

## The Synchronization Hazard: Sorting

Sorting exposes the critical failure mode of parallel arrays. If you sort one list, the indices no longer correspond across lists. The data is now silently broken.

### AoS — sort by salary (safe)

`sort()` compares the first element of each inner list by default. To sort by salary (index 2), you can either temporarily move it to position 0, or use a `key` function:

**Approach 1 — Rearrange to put the sort key first:**

```python
employees = [
    [1001, "sara",   72000, "engineering"],
    [1002, "mike",   65000, "marketing"],
    [1003, "priya",  91000, "engineering"],
    [1004, "carlos", 58000, "sales"],
]

tmp = []
for emp in employees:
    tmp.append([emp[2], emp[0], emp[1], emp[3]])

tmp.sort()
print(tmp)
# [[58000, 1004, 'carlos', 'sales'],
#  [65000, 1002, 'mike', 'marketing'],
#  [72000, 1001, 'sara', 'engineering'],
#  [91000, 1003, 'priya', 'engineering']]
```

Each entity moves as a whole. Salary, ID, name, and department stay bound together through the sort.

**Approach 2 — Use a `key` function** (covered in a later lecture):

```python
employees.sort(key=lambda emp: emp[2])
```

Same result, less manual rearranging. The `lambda` tells `sort()` which element to compare by.

---

### SoA — sorting breaks the data (hazard)

```python
ids         = [1001,   1002,   1003,   1004]
names       = ["sara", "mike", "priya", "carlos"]
salaries    = [72000,  65000,  91000,  58000]
departments = ["engineering", "marketing", "engineering", "sales"]

salaries.sort()
# salaries is now: [58000, 65000, 72000, 91000]
# names is still:  ["sara", "mike", "priya", "carlos"]
#
# index 0: salary=58000, name="sara"   ← WRONG. sara's salary was 72000.
# index 2: salary=72000, name="priya"  ← WRONG. priya's salary was 91000.
```

The data is corrupted. Only `salaries` moved; every other list stayed in place.

To sort parallel arrays correctly, you either write a custom sort that performs the same swap across every list whenever it swaps in one, or temporarily pack the arrays together, sort, and unpack:

```python
tmp = list(zip(salaries, ids, names, departments))
tmp.sort()
salaries, ids, names, departments = zip(*tmp)
```

Using `key=` with lambda functions is also an option for controlling what the sort compares — this will be covered in a later lecture.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---
