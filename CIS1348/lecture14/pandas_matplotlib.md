
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

# Pandas and Matplotlib in Python


## Table of Contents
1. [Pandas — Excel in Python](#1-pandas--excel-in-python)
2. [Installing Pandas](#2-installing-pandas)
3. [Importing Pandas](#3-importing-pandas)
4. [Loading Data from a TSV File](#4-loading-data-from-a-tsv-file)
5. [Selecting a Single Column — Series](#5-selecting-a-single-column--series)
6. [Selecting Multiple Columns](#6-selecting-multiple-columns)
7. [Row Slicing](#7-row-slicing)
8. [Computing Column Statistics](#8-computing-column-statistics)
9. [Filtering with Boolean Conditions](#9-filtering-with-boolean-conditions)
10. [Pandas Quick Reference](#10-pandas-quick-reference)
11. [Why Pandas Is Forbidden in This Course](#11-why-pandas-is-forbidden-in-this-course)
12. [Matplotlib — Plotting in Python](#12-matplotlib--plotting-in-python)
13. [Installing and Importing Matplotlib](#13-installing-and-importing-matplotlib)
14. [Displaying vs Saving Plots](#14-displaying-vs-saving-plots)
15. [Line Plot](#15-line-plot)
16. [Scatter Plot](#16-scatter-plot)
17. [Bar Plot](#17-bar-plot)
18. [Histogram](#18-histogram)
19. [Matplotlib Quick Reference](#19-matplotlib-quick-reference)

---

## 1. Pandas — Excel in Python

There is a library called **Pandas** that turns your Python into Excel. If you need to work with tabular data — rows and columns, like a spreadsheet — Pandas gives you all that functionality and more. You can select any column by name, any row by index, compute averages, filter data, and rearrange everything with a few lines of code.

Pandas is what data scientists, analysts, and engineers use worldwide. It is insanely powerful. And this is a skill that pays — there are many jobs, especially data analyst roles, that specifically require Pandas (and Matplotlib or NumPy) experience. Instead of manually parsing files and building lists, you load your data into Pandas and it handles the heavy lifting.

Behind the scenes, Pandas works with the same things you already know — lists, dictionaries, indexing. It just wraps them in a more convenient interface.

---

## 2. Installing Pandas

You install it once on your computer:

```
pip install pandas
```

---

## 3. Importing Pandas

The standard convention is to import Pandas with the alias `pd`:

```python
import pandas as pd
```

The `as pd` part means: every time you want to use something from this library, instead of typing `pandas.something()`, you type `pd.something()`. Everyone uses `pd` — follow the convention.

---

## 4. Loading Data from a TSV File

Suppose you have a tab-separated file called `data.tsv`:

```
Name	Balance	Address
Bob	200	123 Main St
Alice	100	456 Oak Ave
Joe	150	789 Pine Rd
David	300	321 Elm St
Eve	50	654 Maple Dr
```

You load it into a **DataFrame** — Pandas' version of an Excel sheet:

```python
df = pd.read_csv('data.tsv', sep='\t')
print(df)
```

Output:
```
    Name  Balance      Address
0    Bob      200  123 Main St
1  Alice      100  456 Oak Ave
2    Joe      150  789 Pine Rd
3  David      300  321 Elm St
4    Eve       50  654 Maple Dr
```

The function is called `read_csv` even though the file is tab-separated — you just tell it the separator with `sep='\t'`. For actual CSV files (comma-separated), you would omit the `sep` parameter or use `sep=','`.

> **Common gotcha — VS Code converts tabs to spaces:** When you create a TSV file in VS Code and press the Tab key, VS Code may silently convert your tab to spaces. Your file looks correct visually, but `sep='\t'` will fail because there are no real tab characters. If you get a "column not found" error on a file you just created in VS Code, open the file in a plain text editor (like Vim or Notepad) to verify the separators are actual tabs. In VS Code, you can see real tabs as a faint arrow character (→) in the editor if you enable "Render Whitespace."

---

## 5. Selecting a Single Column — Series

To grab a single column, use its name as an index:

```python
names = df['Name']
print(names)
```

Output:
```
0      Bob
1    Alice
2      Joe
3    David
4      Eve
Name: Name, dtype: object
```

What you get back is called a **Series**. A DataFrame is the whole sheet. When you grab a single column (or a single row), it is a Series. Think of it this way: a DataFrame is a collection of Series.

---

## 6. Selecting Multiple Columns

Instead of passing a single column name, pass a **list** of column names:

```python
subset = df[['Name', 'Address']]
print(subset)
```

Output:
```
    Name       Address
0    Bob  123 Main St
1  Alice  456 Oak Ave
2    Joe  789 Pine Rd
3  David  321 Elm St
4    Eve  654 Maple Dr
```

You are indexing the DataFrame with a list. Notice the double brackets — the outer brackets are the indexing syntax, and the inner brackets define the list.

You can reorder columns however you want:

```python
reordered = df[['Address', 'Balance', 'Name']]
print(reordered)
```

You can even include the same column multiple times if you have a reason to. It is just a list — Pandas processes whatever you give it.

To make this clearer, you can separate the index list into a variable:

```python
columns_i_want = ['Address', 'Name']
subset = df[columns_i_want]
print(subset)
```

It is just a list being passed as an index. Exactly like Excel, except you type it instead of clicking.

---

## 7. Row Slicing

You can select ranges of rows using slicing, the same way you would drag and select in Excel:

```python
# Get rows 1 through 3
some_rows = df[1:4]
print(some_rows)
```

For more precise row and column selection, Pandas provides `.loc[]` (select by label/name) and `.iloc[]` (select by position number):

```python
# Get a specific cell: row 2, column 'Name'
cell = df.loc[2, 'Name']
print(cell)  # Output: Joe

# Get rows 1-3, only 'Name' and 'Balance' columns
subset = df.loc[1:3, ['Name', 'Balance']]
print(subset)

# Get first 3 rows, first 2 columns by position
subset = df.iloc[0:3, 0:2]
print(subset)
```

---

## 8. Computing Column Statistics

Pandas gives you built-in statistical functions, just like Excel formulas:

```python
average = df['Balance'].mean()
print(average)
```

This gives you the average of the entire Balance column — one line of code. No loops, no manual summing.

Other useful functions:

```python
df['Balance'].sum()    # total
df['Balance'].min()    # smallest value
df['Balance'].max()    # largest value
df['Balance'].median() # median value
df['Balance'].std()    # standard deviation
```

It is literally Excel, but way more powerful — because you have access to everything Python offers on top of it.

---

## 9. Filtering with Boolean Conditions

You can filter rows based on a condition. For example, find everyone with a balance below 150:

```python
balance = df['Balance']
filter_mask = balance < 150
print(filter_mask)
```

Output:
```
0    False
1     True
2    False
3    False
4     True
Name: Balance, dtype: bool
```

This gives you a Series of `True`/`False` values — a boolean mask. You can use this mask to filter the DataFrame:

```python
low_balance = df[df['Balance'] < 150]
print(low_balance)
```

Output:
```
    Name  Balance       Address
1  Alice      100  456 Oak Ave
4    Eve       50  654 Maple Dr
```

Only the rows where the condition is `True` are kept. This is the equivalent of Excel's AutoFilter — but in one line of code.

---

## 10. Pandas Quick Reference

| Operation | Code | Excel Equivalent |
|-----------|------|------------------|
| Load TSV file | `pd.read_csv('file.tsv', sep='\t')` | Open file |
| Get one column | `df['Name']` | Select column A |
| Get multiple columns | `df[['Name', 'Address']]` | Select columns A and C |
| Get a row by index | `df.loc[2]` | Select row 3 |
| Get a cell | `df.loc[2, 'Name']` | Cell A3 |
| Get a range | `df.loc[1:3, ['Name', 'Balance']]` | Drag-select a range |
| Get by position | `df.iloc[0:3, 0:2]` | Range A1:B3 |
| Column average | `df['Balance'].mean()` | `=AVERAGE(B:B)` |
| Filter rows | `df[df['Balance'] < 150]` | AutoFilter |

---

## 11. Why Pandas Is Forbidden in This Course

The instructor specifically forbids using Pandas in course assignments. The reason: if you use Pandas, you will not learn the fundamental concepts. You will not learn what a list is, what indexing is, how to manually parse and process data. You can probably guess what Pandas does behind the scenes — it takes data, dumps it into internal structures, rearranges it, and gives it back. But you need to be able to do that yourself first, using raw Python, before you rely on a library to do it for you.

Learn the fundamentals first. Use Pandas when you move into real-world work.

---

## 12. Matplotlib — Plotting in Python

In Excel, you can not only work with data — you can also make graphs. Pandas handles the data side of things, but what about plots? That is where **Matplotlib** comes in.

Matplotlib produces plots that are much nicer than Excel's, and it is extremely customizable because everything is code-based. There is no clicking, double-clicking, or dragging. You type exactly what you want: the title, the font, the colors, the labels. You have full control.

The plots Matplotlib produces are much higher quality than what you get from spreadsheet programs. And it takes very little code — often just one line to create a plot.

---

## 13. Installing and Importing Matplotlib

Install once:

```
pip install matplotlib
```

Import the `pyplot` module with the standard alias `plt`:

```python
import matplotlib.pyplot as plt
```

You specifically import `pyplot` from the `matplotlib` package, and everyone abbreviates it as `plt`. Follow the convention.

---

## 14. Displaying vs Saving Plots

To display a plot in a window on your computer:

```python
plt.show()
```

If you are running Python in a browser or remote environment where a window cannot pop up, save the plot as an image file instead:

```python
plt.savefig('plot.png')
```

This creates a PNG file you can open and view.

---

## 15. Line Plot

A line plot shows how a variable changes over a series. You provide x-values and y-values, and Matplotlib connects them with a line.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.savefig('lineplot.png')
```

That is it. One line of plotting code (`plt.plot(x, y)`) and you have a line plot.

**When to use it:** You are watching one variable change over time or over a sequence.

---

## 16. Scatter Plot

A scatter plot shows individual points — no connecting lines. Each point represents a pair of measurements plotted as coordinates on a 2D grid.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 5, 6]

plt.scatter(x, y)
plt.savefig('scatterplot.png')
```

**When to use it:** You have two variables measured at the same time and want to see their relationship. For example, measuring temperature and noise level simultaneously — each observation becomes a point on the grid.

---

## 17. Bar Plot

A bar plot compares single values across categories. The order of the bars does not matter — swapping them does not change the meaning.

```python
import matplotlib.pyplot as plt

categories = ['Xbox', 'PlayStation', 'Switch']
values = [1.0, 1.2, 3.0]

plt.bar(categories, values)
plt.savefig('barplot.png')
```

**When to use it:** You have discrete categories and one value for each, and you want to compare them visually. Telling someone "Xbox 1, PlayStation 1.2, Switch 3" as numbers is harder to parse than showing them as bars side by side.

---

## 18. Histogram

A histogram shows the **distribution** of a variable — how frequently different values occur. You give it raw data, and it counts and bins the values automatically.

```python
import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 3, 2, 4, 5, 6]

plt.hist(data)
plt.savefig('histogram.png')
```

**How it works:** Matplotlib takes all the raw values, groups them into bins (ranges), and counts how many values fall in each bin. The height of each bar shows the frequency.

**When to use it:** You have a collection of measurements and want to see the overall pattern — where values cluster, how they spread out, whether there are peaks.

**Do not confuse it with a bar plot.** In a bar plot, the bars represent independent categories that can be reordered. In a histogram, the bars represent continuous ranges — reordering them would destroy the meaning.

**Multiple peaks reveal hidden groups.** If your histogram shows two separate peaks instead of one, that means your data has two distinct clusters. For example: you stand by a highway all day and record every car's speed. Your histogram might show a peak around 48 mph and another peak around 70 mph. That tells you there are two types of drivers in your data — cautious drivers and fast drivers — even though you never labeled them. A histogram can surface these hidden patterns automatically.

---

## 19. Matplotlib Quick Reference

| Plot Type | Code | When to Use |
|-----------|------|-------------|
| Line plot | `plt.plot(x, y)` | One variable over time/sequence |
| Scatter plot | `plt.scatter(x, y)` | Relationship between two paired variables |
| Bar plot | `plt.bar(categories, values)` | Comparing single values across categories |
| Histogram | `plt.hist(data)` | Distribution/frequency of one variable |
| Show plot | `plt.show()` | Display in a window |
| Save plot | `plt.savefig('file.png')` | Save as image file |

---

## Complete Example — Pandas + Matplotlib Together

Pandas handles the data. Matplotlib handles the visualization. Here they are combined:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.tsv', sep='\t')

# Show all data
print(df)

# Get the average balance
avg = df['Balance'].mean()
print(f"Average balance: {avg}")

# Filter: who has a balance below 150?
low = df[df['Balance'] < 150]
print("Below 150:")
print(low)

# Plot balances as a bar chart
plt.bar(df['Name'], df['Balance'])
plt.savefig('balances.png')
```

This loads a TSV file, computes statistics, filters data, and produces a plot — all in about 10 lines of code. This is why Pandas and Matplotlib are standard tools in the industry.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
