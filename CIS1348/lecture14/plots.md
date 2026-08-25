
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

# Types of Plots: When and Where to Use Them


## Table of Contents
1. [Why Plots Matter](#1-why-plots-matter)
2. [Line Plot — One Variable Over Time](#2-line-plot--one-variable-over-time)
3. [Scatter Plot — Relationship Between Two Variables](#3-scatter-plot--relationship-between-two-variables)
4. [Line Plot vs Scatter Plot — How to Choose](#4-line-plot-vs-scatter-plot--how-to-choose)
5. [Bar Plot — Comparing Categories](#5-bar-plot--comparing-categories)
6. [Histogram — Distribution and Frequency](#6-histogram--distribution-and-frequency)
7. [Histogram — Binning](#7-histogram--binning)
8. [Histogram vs Bar Plot — The Key Difference](#8-histogram-vs-bar-plot--the-key-difference)
9. [Histogram — Observing Peaks and Clusters](#9-histogram--observing-peaks-and-clusters)
10. [The Three Most Fundamental Plots](#10-the-three-most-fundamental-plots)

---

## 1. Why Plots Matter

Raw numbers are hard to interpret. If someone tells you "Xbox sold 1 million units, PlayStation sold 1.2 million, and Switch sold 3 million," you have to hold those numbers in your head and compare them yourself. A plot shows you the comparison instantly — you see it instead of calculating it.

Plots are how you communicate data. Whether you are writing a report, presenting findings, or exploring a dataset for yourself, choosing the right type of plot determines whether your message is clear or confusing.

---

## 2. Line Plot — One Variable Over Time

A line plot tracks how a **single variable** changes over a series of observations. You plot the values and connect each one to the next with a line.

**When to use it:** You have one thing you are measuring, and you want to see how it changes over time (or over some ordered sequence).

**Example — Temperature over a day:**

You measure the temperature every hour. Each measurement becomes a point, and the line connecting them shows the trend: rising in the morning, peaking in the afternoon, falling at night.

```
Hour:   6am   9am   12pm   3pm   6pm   9pm
Temp:   15°   20°   28°    32°   25°   18°
```

The line connecting these points immediately shows you the rise and fall. You see the pattern — something that is hard to spot from a table of numbers.

**Other examples:**
- Stock price over months
- Number of website visitors per day
- Your running speed across training sessions

The key idea: **one variable, watched over time.** The x-axis is usually time or a sequence, and the y-axis is the value you are observing.

---

## 3. Scatter Plot — Relationship Between Two Variables

A scatter plot is used when you have **two variables** measured together, and you want to see how they relate. Each observation becomes a point on a two-dimensional grid — one variable on the x-axis, the other on the y-axis.

**When to use it:** You have paired measurements and want to see if there is a relationship, pattern, or grouping between them.

**Example — Temperature vs noise level in a classroom:**

Every 10 minutes, you measure both the room temperature and the noise level in decibels. Each pair of measurements becomes one dot on the plot:

```
Observation 1:  22°C,  45 dB
Observation 2:  24°C,  52 dB
Observation 3:  27°C,  60 dB
Observation 4:  23°C,  48 dB
```

Each observation gives you one point (temperature, noise). When you plot all your points, you might notice that higher temperatures tend to come with higher noise levels — a correlation becomes visible.

**Another example — Height vs weight of people:**

Each person is one dot. Their height is one axis, their weight is the other. You can see whether taller people tend to weigh more, whether there are outliers, and whether there are clusters (maybe one group of children and one group of adults).

The key idea: **two variables, paired together.** Every point represents one observation with two measurements.

---

## 4. Line Plot vs Scatter Plot — How to Choose

The decision is straightforward:

| Situation | Plot type |
|---|---|
| You have **one variable** and want to see how it changes over time or a sequence | **Line plot** |
| You have **two variables** measured together and want to see their relationship | **Scatter plot** |

**Example decision:** "I measured the temperature every hour today." → You are watching **one** variable (temperature) over time → **line plot.**

**Example decision:** "I measured both the temperature and the humidity every hour." → You have **two paired** variables → **scatter plot** (temperature on one axis, humidity on the other).

---

## 5. Bar Plot — Comparing Categories

A bar plot shows a **single value** for each of several **categories**. Each category gets one bar, and the height of the bar represents its value.

**When to use it:** You have a set of distinct categories and want to compare them visually.

**Example — Game console sales:**

```
Xbox:         1.0 million
PlayStation:  1.2 million
Switch:       3.0 million
```

Instead of reading three numbers and comparing them in your head, a bar plot makes the comparison immediate. You see that the Switch bar is much taller — the difference jumps out.

**Key property: order does not matter.** You can put PlayStation before Xbox or Switch first — the meaning does not change. The categories are independent. You are not showing change over time; you are showing side-by-side comparisons.

**Other examples:**
- Average salary by department
- Number of students per major
- Population of different countries

---

## 6. Histogram — Distribution and Frequency

A histogram is one of the most important types of plots. It shows you the **distribution** of a variable — how frequently different values appear in your data.

**When to use it:** You have many observations of a single variable and want to understand the pattern of those observations. How are the values spread out? Where do most of them fall? Are there outliers?

**Example — Measuring cat ear sizes:**

You go out and measure the ear size (in centimeters) of 200 cats. You write down every measurement. Then you count: how many cats had ears between 3 and 4 cm? How many between 4 and 5 cm? Each count becomes a bar.

The result tells you: most cats have ears around a certain size, and fewer cats have very small or very large ears. You see the **shape** of the data.

**Example — Car speeds on a highway:**

You stand by the highway and record the speed of every car that passes. After 500 cars, you have 500 numbers. A histogram answers: how many cars were going 60 mph? How many were going 70? Where does the majority cluster?

Unlike a line plot (which tracks change over time), a histogram answers: **"What values did I see, and how often did I see them?"**

---

## 7. Histogram — Binning

When you have continuous data (like speeds or measurements), you often **bin** the values — group nearby values together into ranges.

**Why bin?** If you recorded 500 car speeds, you might have cars going 60, 61, 62, 63... all the way to 90. Showing a separate bar for every single speed makes the plot noisy and hard to read. Instead, you group them:

```
60–65 mph:  one bar
65–70 mph:  one bar
70–75 mph:  one bar
```

This gives you a smoother, more readable picture.

**Bin width matters:**
- **Smaller bins** (e.g., 1 mph ranges) → more fluctuation, more detail, possibly too noisy
- **Larger bins** (e.g., 10 mph ranges) → smoother picture, but you lose detail

You choose bin width based on how much detail you need. The histogram tool does the binning and counting for you — you just supply the raw measurements.

---

## 8. Histogram vs Bar Plot — The Key Difference

Histograms and bar plots look similar (both use bars), but they represent fundamentally different things.

| | Bar Plot | Histogram |
|---|---|---|
| **What it shows** | A value for each independent category | The frequency of values across a continuous range |
| **Can you reorder the bars?** | Yes — categories are independent | No — the order represents a continuous scale |
| **Example** | Xbox vs PlayStation vs Switch sales | Distribution of car speeds on a highway |

**The swapping test:** In a bar plot, you can swap "Xbox" and "PlayStation" and the meaning does not change. In a histogram, if you have "500 cats with 1-inch ears" and "300 cats with 2-inch ears," you cannot swap those — you would be lying about your observations. The position of each bar on the x-axis has meaning because it represents a value on a continuous scale.

---

## 9. Histogram — Observing Peaks and Clusters

One of the most powerful things a histogram reveals is **hidden structure** in your data.

**Example — Two peaks in highway speeds:**

You record car speeds on a highway and plot a histogram. Instead of one smooth hump, you see **two peaks** — one cluster of cars around 48 mph and another cluster around 70 mph. What does this mean?

Maybe the highway has two lanes with different speed patterns. Maybe trucks drive around 48 mph and cars drive around 70 mph. The histogram reveals these two distinct groups that you could not see from the raw numbers.

This is called a **bimodal distribution** — data with two peaks. A histogram makes these patterns visible immediately.

**From frequency to probability:** You can also translate histogram frequencies into probabilities. If 200 out of 500 cars were going between 65 and 75 mph, there is a 40% probability that a randomly observed car falls in that range. This turns observation into inference.

---

## 10. The Three Most Fundamental Plots

These three plot types are the most fundamental tools for communicating data:

| Plot | Purpose | Variables | Key question it answers |
|---|---|---|---|
| **Line plot** | Observe change over time | One variable over a sequence | "How does this value change?" |
| **Scatter plot** | Observe relationships | Two paired variables | "How do these two things relate?" |
| **Histogram** | Observe distribution | One variable, many observations | "What values appear, and how often?" |

The bar plot is also common and useful, but it is less fundamental — it compares categories rather than revealing patterns in data.

If you learn to use these three correctly, you can communicate almost any basic data analysis clearly and effectively.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
