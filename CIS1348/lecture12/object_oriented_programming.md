
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

# Object-Oriented Programming (OOP)


## Table of Contents
1. [What Is OOP?](#1-what-is-oop)
2. [The Core Shift in Thinking: Procedural vs. OOP](#2-the-core-shift-in-thinking-procedural-vs-oop)
3. [Classes and Instances](#3-classes-and-instances)
4. [Instance Variables and Methods](#4-instance-variables-and-methods)
5. [The Dot Operator](#5-the-dot-operator)
6. [Encapsulation](#6-encapsulation)
7. [Abstraction](#7-abstraction)
8. [Polymorphism](#8-polymorphism)
9. [Constructors](#9-constructors)
10. [Inheritance](#10-inheritance)
11. [Object Composition](#11-object-composition)
12. [OOP in Python — Syntax](#12-oop-in-python--syntax)
13. [Operator Overloading and Magic Methods](#13-operator-overloading-and-magic-methods)
14. [Class Variables vs. Instance Variables](#14-class-variables-vs-instance-variables)
15. [Class Methods](#15-class-methods)
16. [Inheritance in Python — `super()`](#16-inheritance-in-python--super)
17. [Python's Relationship With OOP Rules](#17-pythons-relationship-with-oop-rules)
18. [When to Actually Use OOP](#18-when-to-actually-use-oop)
19. [OOP Terminology Cheat Sheet](#19-oop-terminology-cheat-sheet)

---

## 1. What Is OOP?

Object-Oriented Programming is a **programming philosophy** — a way of thinking about and organizing code. It is not tied to any specific hardware or programming language; it is an idea about how to design software.

The core idea: instead of thinking directly about data and algorithms, you first think about the **objects** that exist in your problem and how they **interact** with each other.

> Think of it like writing a short story. Who are the characters (class instances/objects)? What features do they have (data/variables)? What actions and behaviors can they do (functions/methods)?

OOP is built into many widely-used languages (Python, Java, C++, C#) and underpins enormous amounts of existing code. You need to understand it to read, use, and work with those systems — even if you don't always use it yourself.

---

## 2. The Core Shift in Thinking: Procedural vs. OOP

> This is the single most important idea to understand about OOP. Everything else — encapsulation, inheritance, polymorphism — is built on top of this shift.

### Two Ways to Think About the Same Code

Imagine you have a chair object in your program and you want to rotate it.

**The procedural way:**

```python
rotate(chair)
```

A function called `rotate` takes the chair as an argument and does the rotation. *You* are in control. You are the one holding the chair and spinning it. The function is the actor; the chair is just data being passed around.

**The OOP way:**

```python
chair.rotate()
```

You are *asking* the chair to rotate itself. In this mental model, the chair is not just data — it is an individual, an autonomous entity that knows how to do things. You send it a request, and it carries out the action.

---

### Why This Distinction Matters

These two lines can produce identical output at runtime. The difference is not in what the computer does — **the difference is in how you think about the problem.**

In procedural programming, you think:
- Here is some data.
- Here is a function that operates on that data.
- I call the function and pass the data.

In OOP, you think:
- Here is an object that *is* something.
- That object knows how to do certain things.
- I ask the object to do those things, and it handles the rest.

This mental model — imagining that the chair lives inside the computer and knows how to rotate itself — is the defining feature of OOP thinking. And it is worth pausing on, because it is also where the first danger enters. The chair does not know anything. It is data. The rotation is a function. OOP syntax makes it *look* like the chair is acting, but under the hood nothing has changed — you are still passing data to a function. The moment you start believing the fiction too literally is the moment you start designing objects as if they are real autonomous beings, which is exactly the trap described in the next section.

---

### What Actually Happens Under the Hood

When Python executes `chair.rotate()`, it is *not* magic. What really happens is:

1. Python looks at the type of `chair`.
2. It finds the `rotate` method defined on that class.
3. It calls `rotate(chair)` — passing the object as the first argument (`self`).

So procedurally, it is still just a function call with data being passed in. The OOP syntax is a **layer of abstraction** on top of that reality. `chair.rotate()` is a cleaner, more readable way of writing "take this chair and run the rotate logic on it" — but under the hood, that is exactly what Python does.

This is why Python makes you write `self` as the first argument to every method. It is an acknowledgment that the "ask the object" syntax is a useful fiction — `self` is the chair being passed in.

---

### The Philosophical Payoff

Once you adopt this mental model, it becomes natural to:

- Group related data and behavior together (encapsulation)
- Hide implementation details behind an interface (abstraction)
- Have one method name (`scream`, `draw`) mean different things depending on the object (polymorphism)
- Build new types by extending existing ones (inheritance)

These are the **four pillars of OOP**:
- **Encapsulation** — grouping data and behavior together
- **Abstraction** — hiding implementation behind an interface
- **Polymorphism** — one method name, different behavior per type
- **Inheritance** — building new types by extending existing ones

All four follow directly from the idea that **objects are individuals that carry their own data and know how to act on it** — not just passive containers being manipulated by outside functions.

---
### The "Daydreaming" Trap — A Worked Example
OOP has a well-known distraction: **getting pulled into designing objects instead of solving the actual problem.**

Consider Project 1's criminal dataset. A procedural approach looks at the file, sees rows of data, and starts processing. An OOP-first approach stops and asks: *what is a criminal, really?*

You might design a `Criminal` class with fields:
- `name`, `last_name`
- `wallet`
- `friends_list`
- `criminal_record`
- `address`, `id`
- `status` (boss, street-level, etc.)

And methods like:
- `send_money()`
- `receive_money()`
- `intimidate()`

This took 5–10 minutes of design work and maybe 1/10th of it actually applies to your project. But someone at the whiteboard proposes: *"We should also define a `CriminalNetwork` class."* So you design that too — a list of criminals, with connection data between them. Then someone proposes a `StatewideNetwork` that wraps multiple criminal networks together. And on it goes.

The instructor's point: you have been busy the whole time — imagining, writing things down, proposing new classes — and you look productive. But you haven't moved the project forward by a single line. Every new class proposal opens the door to another. The design work can spiral indefinitely without producing anything. This is what the instructor calls "daydreaming."

The instructor uses a surgeon analogy to illustrate this: instead of looking at the wound first and then identifying the best tool to use, you imagine what the wound could be, design a tool you think would work for it, and then attempt the operation. It will hurt.

The backwards nature: in OOP, you invent an architecture and then figure out how to apply it to your problem. In procedural thinking, you look at the problem first and pick the right tool.

> **Takeaway:** Design follows from problems, not the other way around.

---

## 3. Classes and Instances

### The Class: A Blueprint

A **class** is a design — a template or recipe that describes:
1. What **data** objects of this type should have.
2. What **behaviors** objects of this type can perform.

Think of a class like a factory blueprint. The blueprint describes how to build something, but it is not the thing itself.

```python
class Animal:
    ...
```

> **Python analogy:** A class is like a dictionary — it has named variables and named functions where you assign things. The main difference is that a class bundles data *and* behavior together, and every instance gets its own copy of the data.

### The Instance: A Concrete Object

An **instance** (also called an **object**) is a specific item created from a class blueprint. You can create as many instances as you want from one class.

```python
cat1 = Animal()   # one instance
cat2 = Animal()   # another instance
dog1 = Animal()   # yet another instance
```

Each instance is independent — changing one does not affect the others.

**Analogy:** The `Animal` class is like a cookie cutter. Each cookie you cut out is an instance. The cutter defines the shape; the cookies are the real things.

---

## 4. Instance Variables and Methods

### Instance Variables (Attributes)

**Instance variables** are the data fields that every object of a class carries. They are what makes each instance unique.

For an `Animal` class, every animal might have:
- `name`
- `age`
- `weight`
- `color`

Each instance of `Animal` gets its own copy of these variables.

> You may also hear instance variables called **attributes** or **fields** — these all mean the same thing.

### Methods

**Methods** are functions that belong to a class. They define what an object can *do*.

For an `Animal` class:
- `scream()` — make a sound
- `eat()` — consume food
- `move()` — change position

> "Method" is just the word for a function that is part of a class definition. If someone says "call the method", they mean call a function on an object.

---

## 5. The Dot Operator

When you write `x.y`, Python looks at the object `x` and finds `y` on it. `y` is one of two things:

- **An instance variable** — `x.y` simply reads (or writes) that piece of data stored inside `x`.
- **A method** — `x.y(...)` calls that function, and `x` is automatically passed in as the first argument.

```python
x.name        # reads the 'name' variable stored on x
x.rotate()    # calls rotate, passing x as the first argument
```

Both cases follow the same rule: **the thing on the right of the dot belongs to the object on the left.**

### Methods: the first argument is always the object itself

When Python sees `x.rotate()`, it does not just call `rotate()`. Under the hood it calls `rotate(x)` — the object on the left side of the dot gets injected as the first argument automatically.

This is why every method declaration in a class takes `self` as its first parameter:

```python
class Chair:
    def rotate(self):   # self is x — the object the method was called on
        print("rotating")
```

When you *call* the method you don't pass `self` explicitly:

```python
chair = Chair()
chair.rotate()   # Python passes chair as self for you
```

The declaration keeps `self`; the call site omits it. Python handles the handoff invisibly.

> The instructor's summary: *"In Python, in order for you to be able to do `bob.draw`, you need to pass `bob` as the first argument. When Python sees this dot notation, it will automatically grab the left side and pass it to the function."*

---

## 6. Encapsulation

**Encapsulation** means bundling data (instance variables) and behavior (methods) together inside an object, and controlling how the outside world can interact with that data.

### The Rule

In strict OOP, you are **not** allowed to directly read or change an object's internal variables from outside. Instead, you must use the methods the class provides.

```python
# NOT allowed in strict OOP:
x.name = "Bob"
print(x.name)

# Correct OOP style:
x.set_name("Bob")
print(x.get_name())
```

### Why This Exists

It gives the class author control over how their data is used. For example, a `set_speed()` method can check that the value isn't dangerously high before applying it — something direct assignment can't do.

```python
def set_speed(self, value):
    if value > 200:
        print("Too fast, rejected.")
    else:
        self.speed = value
```

### Getters and Setters

Functions used to read or write a single variable are called **getters** and **setters** by convention:

| Convention | Meaning |
|---|---|
| `get_name()` | Return the value of `name` |
| `set_name(val)` | Set the value of `name` |

These names (`get_`, `set_`) are a **universal convention** across most OOP languages. They are **not** reserved keywords — Python will let you name anything `get` or `set`. The prefix is purely a signal to other programmers that this method is a getter or setter.

**`get_area` vs. `calculate_area` — why the name matters**

A getter (`get_something`) signals: *"just return the stored value, no work done."* If a class stored area as an instance variable (e.g., `self.area`), then `get_area()` returning `self.area` is appropriate.

But if the area is *derived* from other attributes (width × height), calling it `get_area()` is misleading — there is computation happening. The honest name is `calculate_area()`. The choice of name communicates intent: readers know whether they're fetching a value or triggering a calculation.

---

## 7. Abstraction

**Abstraction** means hiding the internal implementation of an object and exposing only what is necessary.

When you use a method like `pokemon.attack()`, you don't need to know how the attack is calculated internally. You just know that calling it does something meaningful. The internals are hidden — the object is "opaque."

This is the same principle behind how Python's built-in types work: you call `list.append(x)` without knowing anything about the memory management happening underneath.

---

## 8. Polymorphism

**Polymorphism** means that different classes can provide methods with the **same name**, and the correct version is called automatically based on the object's type.

### Example

Suppose both `Rectangle` and `Circle` have a `.draw()` method and a `.get_area()` method, but implemented differently.

```python
shapes = [Rectangle(), Circle(), Rectangle(), Circle()]

for shape in shapes:
    shape.draw()   # calls Rectangle.draw() or Circle.draw() automatically
```

You write one loop. Python figures out which `.draw()` to call based on the type of each object. You do not need:
- Separate function names (`draw_rectangle`, `draw_circle`)
- `if/elif` blocks to check type

### Another Example

```python
class Animal:
    def scream(self):
        print("woo")

class Cat(Animal):
    def scream(self):
        print("meow")

class Dog(Animal):
    def scream(self):
        print("woof")

zoo = [Animal(), Cat(), Dog()]
for animal in zoo:
    animal.scream()

# Output:
# woo
# meow
# woof
```

### What's Actually Happening

The word "polymorphism" (meaning "many forms") can be misleading. **Objects do not change or morph at runtime.** A `Cat` instance is always a `Cat`; a `Dog` instance is always a `Dog`. Nothing transforms.

What actually happens is **method dispatch**: Python looks at the type of the object being called on and routes the call to the correct implementation.

> **Connection to function pointers (Lecture 11):** Remember that functions are just variables in Python — you can store them, pass them around. Under the hood, when you create a `Cat` object, Python sets a function pointer inside it pointing to `Cat.scream`. When you do `a.scream()`, Python is just invoking whatever function pointer was already set. There is no magic decision happening at runtime — it's already decided the moment the object was created. This is the same mechanism as vtables in C++.

The "many forms" refers to the fact that one method *name* (`scream`, `draw`) can resolve to different *implementations* depending on the object's type.

---

## 9. Constructors

A **constructor** is a special method that is called **automatically when an object is created**. Its job is to set up the object — create its variables, assign default values, and perform any initialization needed.

In Python, the constructor is always named `__init__`:

```python
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
```

When you write `r = Rectangle(3, 5)`, Python automatically calls `__init__` with `width=3` and `height=5`.

> **Destructor:** Some OOP languages (like C++) have a **destructor** — a method called automatically when an object is destroyed, used for cleanup (closing files, freeing memory). Python has `__del__`, but it is called by the garbage collector at unpredictable times — you cannot rely on it. Use **context managers** (`with` statements) for guaranteed cleanup instead.

---

## 10. Inheritance

**Inheritance** lets a class (the **child**) automatically receive all the variables and methods of another class (the **parent**), and then add its own on top. Inheritance models an **"is-a" relationship**: a `Cat` *is an* `Animal`. This is the defining question for whether inheritance applies — if you can truthfully say "X is a Y", inheritance may be appropriate.

### The Problem It Solves: Redundancy

Imagine you have both a `Rectangle` class and a `Circle` class. You notice they share a lot: both need an `x` position, a `y` position, and a `color`. You're typing the same variables in two places.

Inheritance's answer: pull the shared stuff into a new parent class called `Shape`. Then `Rectangle` and `Circle` declare `Shape` as their parent and they automatically get `x`, `y`, and `color` for free.

```
Shape          (parent / base / super class)
├── x, y, color
├── draw()        ← default: draws a "?"
└── get_area()    ← default: returns 0

Rectangle      (child / sub / derived class)
├── width, height
├── draw()        ← overrides Shape's version
└── get_area()    ← overrides Shape's version

Circle         (child / sub / derived class)
├── radius
├── draw()        ← overrides Shape's version
└── get_area()    ← overrides Shape's version
```

> **Note:** Returning 0 as a default area works for this example, but in practice a base class method with no meaningful default should raise `NotImplementedError` — that way, if a child class forgets to override it, the error is immediate and obvious rather than silently returning a wrong value.

> Think of it as a **copy-paste facility**. When Python processes `class Rectangle(Shape)`, it conceptually copies everything from `Shape` into `Rectangle` first, then adds what `Rectangle` defines on top.

### Key Terms (all mean the same thing, just different names)

| Role | Synonyms |
|---|---|
| The class being inherited from | parent class, base class, super class |
| The class doing the inheriting | child class, subclass, derived class |

There are many synonyms because textbook authors need to justify new editions. Don't let the terminology confuse you — the concept is always the same.

### Overriding

A child class can **override** any method it inherits by simply defining it again. When that method is called on a child instance, the child's version runs — not the parent's.

```python
# Shape's default get_area returns 0 (meaningless for unknown shape)
# Rectangle overrides it with the real formula:
class Rectangle(Shape):
    def get_area(self):
        return self.width * self.height
```

If the child does **not** define a method, the parent's version is used automatically. You can also add methods that don't exist in the parent at all — no restriction there.

### Multiple Inheritance and the Diamond Problem

Most OOP languages (and Python) allow a class to inherit from **more than one parent**. This sounds useful, but it creates serious problems.

**Example:** You have `Animal → Cat` and `Animal → Dog`. Six months into a project someone says "we need a `CatDog` class." So you do:

```python
class CatDog(Cat, Dog):   # inherits from both
    ...
```

Now a question arises: `Animal` is the grandparent of both `Cat` and `Dog`, and `CatDog` inherits from both of them. This creates a **diamond shape** in the inheritance hierarchy:

```
        Animal
       /      \
     Cat      Dog
       \      /
        CatDog
```

This is called the **diamond inheritance problem**. If `Cat` and `Dog` both have an `eat()` method, which one does `CatDog` inherit? Should it eat like a cat or like a dog? There is no obvious right answer, and this gets messy fast — especially after you have 120,000 lines of code built on top of the hierarchy and cannot easily refactor.

> Multiple inheritance exists in Python but is widely considered a bad idea. Avoid it unless you have a very clear reason.

### Why OOP / Inheritance Was Adopted Industry-Wide

Inheritance has real problems (more on that below), yet it became the dominant paradigm for decades. The reason is primarily **communication and the ability to transmit an architectural idea** — not technical superiority. A class hierarchy can be drawn on a whiteboard, explained in two sentences, and immediately understood by everyone in the room. That made it an unusually effective tool for coordinating large teams.

**1. Easy to explain to juniors.** Instead of talking about look-up tables and function pointers, you say: "There's a `Skeleton` base class. `SkeletonArcher` inherits from it. `SkeletonMage` inherits from it." Almost anyone can follow that — even someone with very little programming experience.

**2. Self-documenting to-do list.** A senior developer can write empty class shells with variables and method signatures, annotate what each method should do, and hand them to juniors who just fill in the blanks. The inheritance structure tells each developer exactly what they can call, what they shouldn't touch, and what they need to implement.

**3. Access control as guard rails.** In strictly-typed languages like C++ or Java, `private` variables won't compile if accessed from outside the class. A junior developer doesn't need to ask "can I call this function?" — the compiler will just refuse.

These three things together made OOP a very efficient way to manage large teams and large codebases.

### The Problems With Inheritance

Despite its adoption, inheritance has significant downsides:

**Rigidity.** Once you design a class hierarchy, it bakes itself in. When requirements change — and they always do — it becomes very hard to restructure. Adding "a wizard archer skeleton that shoots magic arrows" to a carefully designed hierarchy can require rethinking large portions of the design.

**You're solving the wrong problem.** In an OOP-first approach, developers spend hours in the design phase asking: *Who are the classes? What are their relationships? Who is the parent? Should `Boss` be a subclass of `Criminal`?* These are abstract, man-made questions. The actual problem you were hired to solve gets deferred while you architect an idea.

**Maintenance at scale.** As code bases grew, the number of classes ballooned into the millions. Nobody could keep track of the hierarchy. Code became brittle and expensive to change.

> **The drawer analogy:** Imagine organizing everything in a set of drawers. Each drawer is a class. Sounds tidy. But inside every drawer are opaque boxes, and inside each opaque box are more boxes. Now try to find a screwdriver. You can't just open a drawer and grab it — you open the drawer, find the right box, open that, find another container, and dig through it. And if you discover the screwdriver isn't where you expected, you can't easily reorganize everything because the whole system is already built around the current arrangement. That's what deeply nested inheritance hierarchies feel like in practice.

**Performance.** Calling methods through inheritance involves pointer indirection (vtables in C++, attribute lookup in Python). For tight loops or performance-sensitive code, this overhead adds up.

> Inheritance is not the right tool for every job. **Composition ("has-a" relationships) must be the priority design choice over inheritance ("is-a" relationships) for complex systems.**

> **Further watching:** Mike Acton's 2014 CppCon talk *"Data-Oriented Design and C++"* (YouTube) presents a well-argued alternative to OOP thinking. Acton was the lead engine developer at Insomniac Games — the studio behind Ratchet & Clank and Spider-Man — which is known for consistently shipping polished, on-time releases. If you've ever wondered why some studios ship broken games and others don't, his talk is worth your time.

---

## 11. Object Composition

### Data Bundling Is Not New

Bundling related data together is something programmers have been doing long before OOP was invented — and still do to this day. In C, you use `struct`s. In earlier lectures, we saw this idea when discussing SoA (Structure of Arrays) vs. AoS (Array of Structures). Classes make this easy to implement in Python, but the idea itself is older than OOP.

### Composition: "Has-A" Instead of "Is-A"

Inheritance models an **"is-a"** relationship: a `Cat` *is an* `Animal`. But many real-world relationships are better described as **"has-a"**: a `Car` *has an* `Engine`. This is called **object composition** — an object stores other objects as its instance variables.

```python
class Engine:
    def __init__(self, horsepower, weight):
        self.horsepower = horsepower
        self.weight = weight

class Tires:
    def __init__(self, grip_level, diameter):
        self.grip_level = grip_level
        self.diameter = diameter

class Car:
    def __init__(self, make, model, engine_component, tire_component):
        self.make = make
        self.model = model
        self.engine = engine_component
        self.tires = tire_component

v8_engine = Engine(horsepower=450, weight=400)
racing_tires = Tires(grip_level=0.95, diameter=18)

my_car = Car(make="Ford", model="Mustang", engine_component=v8_engine, tire_component=racing_tires)

print(my_car.make)              # Ford
print(my_car.engine.horsepower) # 450
print(my_car.tires.grip_level)  # 0.95
```

Notice how the dot operator chains naturally: `my_car.engine.horsepower` reads as "my car's engine's horsepower." Each `.` steps into a nested object.

### Why Composition Is Often Preferred Over Inheritance

With inheritance, you lock yourself into a rigid hierarchy. With composition, you snap pieces together — and you can swap them out. Want a different engine? Just pass a different `Engine` object. No class hierarchy to restructure.

> **Favor composition over inheritance.** Inheritance is useful for true "is-a" relationships, but composition handles "has-a" relationships more flexibly and is easier to change later.

---

## 12. OOP in Python — Syntax

### Defining a Class

```python
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                print('.', end='')
            print()

    def calculate_area(self):
        return self.width * self.height
```

### Rules to Know

**1. `__init__` is the constructor.**
It must be named exactly `__init__`. It is called automatically when you create an instance.

**2. `self` is the first argument of every method.**
`self` is a reference to the object itself. You can name it anything, but `self` is the universal convention.

```python
def draw(self):          # correct
def draw(tomato):        # also works, but don't do this
```

**3. Instance variables must use `self.`**
Inside any method, you access or create instance variables with `self.varname`:

```python
self.width = 5       # create / set
print(self.width)    # read
```

**4. The dot notation.**
Outside the class, use the dot to access methods and variables on an instance:

```python
r = Rectangle(3, 5)
r.draw()
print(r.calculate_area())
```

**5. Creating an instance.**
Write the class name followed by parentheses (with constructor arguments if needed):

```python
a = Rectangle()       # uses default width=1, height=1
b = Rectangle(2, 5)   # width=2, height=5
```

Note: you do *not* pass `self` — Python handles that automatically.

---

## 13. Operator Overloading and Magic Methods

Python has a set of **magic methods** (also called dunder methods, because they start and end with double underscores). These are special functions Python calls automatically in response to operators and built-in functions.

You can **override** them in your class to define custom behavior.

### Common Magic Methods

| Magic method | Triggered by | Example use |
|---|---|---|
| `__init__(self, ...)` | `MyClass(...)` | Constructor |
| `__str__(self)` | `print(obj)`, `str(obj)` | Human-readable string |
| `__repr__(self)` | `repr(obj)`, typing `obj` in REPL | Developer/debug string |
| `__add__(self, other)` | `a + b` | Adding two objects |
| `__lt__(self, other)` | `a < b` | Less than comparison |
| `__le__(self, other)` | `a <= b` | Less than or equal comparison |
| `__len__(self)` | `len(obj)` | Length of object |

> **Note on `__lt__` vs `__le__`:** `__lt__` is strictly *less than* (`<`). For *less than or equal* (`<=`), you need `__le__`. You don't need to memorize all of these — just know the pattern exists and look up the specific name when you need it. AI is useful for this: ask "what magic method handles `<=` in Python" and it will tell you `__le__`.

### Example: `__lt__` (less than)

```python
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def __lt__(self, other):
        return self.calculate_area() < other.calculate_area()

a = Rectangle(2, 6)   # area = 12
b = Rectangle(3, 5)   # area = 15

if a < b:
    print("a is smaller")   # prints: a is smaller
```

### Example: `__str__` (string representation)

Without `__str__`, printing an object shows something like `<__main__.Rectangle object at 0x...>`. This happens because every Python object inherits from a built-in base object that provides a default `__str__`. When you define your own `__str__`, you are overriding that inherited default.

```python
def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

r = Rectangle(4, 3)
print(r)   # Rectangle(width=4, height=3)
```

### Example: `__add__`

```python
def __add__(self, other):
    new_width = self.width + other.width
    new_height = self.height + other.height
    return Rectangle(new_width, new_height)

c = a + b   # creates a new Rectangle
print(c)
```

---

## 14. Class Variables vs. Instance Variables

### Instance Variable
- Defined inside `__init__` using `self.varname`.
- **Each object has its own copy.**
- 5 Rectangle objects → 5 separate `width` variables.

### Class Variable
- Defined directly in the class body, outside any method.
- **Shared by all instances.** Only one copy exists for the whole class.
- Accessed via `ClassName.varname`.

```python
class Rectangle:
    num_created = 0   # class variable — shared by all rectangles

    def __init__(self, width=1, height=1):
        self.width = width         # instance variable
        self.height = height       # instance variable
        Rectangle.num_created += 1 # increment the shared counter

a = Rectangle()
b = Rectangle(2, 5)
c = Rectangle(3, 3)

print(Rectangle.num_created)   # 3
```

### Important Gotcha: Operator Overloading Creates Real Objects

This is a subtle but important consequence of combining class variables with operator overloading.

```python
class Rectangle:
    num_created = 0

    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
        Rectangle.num_created += 1

    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)  # ← creates a new Rectangle!

a = Rectangle()       # num_created = 1
b = Rectangle(2, 5)   # num_created = 2
c = Rectangle(3, 3)   # num_created = 3
d = Rectangle(1, 1)   # num_created = 4

e = a + b             # num_created = 5  ← SURPRISE!

print(Rectangle.num_created)   # 5, not 4
```

Why 5 instead of 4? Because `a + b` calls `__add__`, which runs `return Rectangle(new_width, new_height)`. That `Rectangle(...)` call is a constructor call — it runs `__init__`, which increments the counter. The temporary object created by the `+` operation counts just like any other instance.

This is not a bug — it is the correct behavior. It is a reminder that **operator overloading creates real objects**, not magic values. Every `Rectangle(...)` call anywhere in your code increments the counter.

---

## 15. Class Methods

A **class method** belongs to the class itself, not to any individual instance. It doesn't operate on `self`; it operates on the class as a whole.

Use the `@classmethod` decorator and `cls` (convention) as the first parameter:

```python
class Rectangle:
    num_created = 0

    @classmethod
    def get_count(cls):
        return cls.num_created
```

Class variables and class methods are the **"one copy for the whole class"** counterpart to instance variables and instance methods.

> **`@staticmethod`:** Python also has **static methods** — functions defined inside a class that receive neither `self` nor `cls`. They are just regular functions that live in the class namespace for organizational purposes. Use `@staticmethod` when the method doesn't need access to the instance or the class.

---

## 16. Inheritance in Python — `super()`

To inherit from a parent class, put the parent's name in parentheses after the child class name:

```python
class Animal:
    def __init__(self):
        self.weight = 1

    def scream(self):
        print("woo")


class Cat(Animal):
    def __init__(self):
        super().__init__()       # REQUIRED — runs Animal's __init__
        self.claw_sharpness = 0.1


class Dog(Animal):
    def __init__(self, name):
        super().__init__()       # REQUIRED — runs Animal's __init__
        self.name = name

    def scream(self):            # override Animal's scream
        print("woof")
```

### Why `super().__init__()` Is Required

This trips people up. Here is what actually happens:

In Python, **an instance variable only comes into existence the moment the line `self.var = ...` executes.** It does not matter that a variable is "supposed to" belong to the class — if the assignment line never ran, the variable does not exist.

When you write `class Cat(Animal)`, Python does *not* automatically run `Animal.__init__`. It just makes the methods of `Animal` available on `Cat` objects. The variables (`self.weight`) in `Animal.__init__` only get created if you explicitly call `Animal.__init__` at some point.

That is what `super().__init__()` does. Inside `Cat.__init__`, calling `super()` gives you a reference to `Animal` (Python knows this because `Cat` declared `Animal` as its parent). Then `.__init__()` calls `Animal`'s constructor, which runs `self.weight = 1` and creates the variable.

**The live demo that showed this clearly:**

```python
class Animal:
    def __init__(self):
        self.weight = 1

    def scream(self):
        print("woo")

class Cat(Animal):
    def __init__(self):
        # NO super().__init__() here — intentionally broken
        self.claw_sharpness = 0.1

whiskers = Cat()
whiskers.scream()          # works — method is inherited fine
print(whiskers.claw_sharpness)  # works — Cat's own variable
print(whiskers.weight)     # AttributeError: 'Cat' object has no attribute 'weight'
```

`scream()` worked because it is a method — methods are looked up on the class, not stored per-instance. But `weight` is an instance variable. It only exists if `Animal.__init__` ran. Since we skipped `super().__init__()`, it never ran, so `weight` was never created on `whiskers`.

> **Rule:** In Python, if you override `__init__` in a child class, you must call `super().__init__()` to inherit the parent's instance variables. In other languages (C++, Java), instance variables can be declared separately from the constructor and are created automatically. Python does not have that — variables only exist after the assignment line runs.

### `super().__init__()` vs. `Parent.__init__(self)`

Both of these do the same thing in simple single-inheritance:

```python
class Cat(Animal):
    def __init__(self):
        super().__init__()          # option A — recommended
        # Animal.__init__(self)     # option B — also works, but avoid
        self.claw_sharpness = 0.1
```

Option B hardcodes the parent class name. This breaks in **multiple inheritance** scenarios. Python has a mechanism called the **Method Resolution Order (MRO)** — a fixed, predictable sequence that defines which class gets called next in the chain when multiple parents are involved. `super()` respects the MRO; hardcoding the class name skips it entirely.

```python
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()   # follows MRO: B → A
        print("B init")

class C(A):
    def __init__(self):
        super().__init__()   # follows MRO: C → A
        print("C init")

class D(B, C):               # diamond: D → B → C → A
    def __init__(self):
        super().__init__()   # follows MRO: D → B → C → A (A's __init__ runs once)
        print("D init")

D()
# Output:
# A init
# C init
# B init
# D init
```

With `super()`, each class in the chain calls the *next* class according to the MRO, and `A.__init__` runs exactly once. If `B` and `C` had used `A.__init__(self)` directly, `A.__init__` would have run twice — once through `B`, once through `C`.

> **Rule:** Always use `super().__init__()` instead of hardcoding the parent class name. It is safe for single inheritance and essential for correct behavior in multiple inheritance.

### Putting It Together — Polymorphism

```python
whiskers = Cat()
bobby = Dog("Bobby")
generic = Animal()

zoo = [generic, whiskers, bobby]

for animal in zoo:
    animal.scream()

# Output:
# woo
# woo       <- Cat inherits Animal's scream (no override)
# woof      <- Dog overrides Animal's scream
```

What you observe in that loop is polymorphism: one loop, one method name (`scream`), three different behaviors based on the actual type of each object. Under the hood, Python is doing method lookup — it checks each object's type and dispatches the call to the correct implementation.

---

## 17. Python's Relationship With OOP Rules

Python is fully object-oriented (everything in Python is an object), but it **does not enforce encapsulation** the way languages like C++ do.

| Language | Access control |
|---|---|
| C++ | Compiler refuses to compile if you access a `private` variable directly |
| Python | No enforcement — you can always access any variable |

### Python's Convention

Since Python won't stop you, the community uses **naming conventions** to signal intent:

| Prefix | Meaning |
|---|---|
| `name` | Public — use freely |
| `_name` | Protected — please don't touch from outside (convention only) |
| `__name` | Name-mangled — Python renames it internally to make accidental access harder |

These are agreements between programmers, not language rules.

**How name mangling works in practice:**

```python
class BankAccount:
    def __init__(self):
        self.__balance = 1000   # Python internally stores this as _BankAccount__balance

account = BankAccount()

# account.__balance        → AttributeError (looks like it doesn't exist)
# account._BankAccount__balance → 1000  (still reachable if you know the mangled name)
```

The double underscore doesn't make the variable truly private — a determined programmer can still access it. But it prevents *accidental* access and makes it clearly off-limits by convention.

---

## 18. When to Actually Use OOP

OOP is a tool, not a requirement. The instructor's practical advice:

> "If you made an object to package/bundle data together and it would make it easier to put things in a list and sort the list — do it. Do what makes sense. If it makes sense to bundle a bunch of variables together and that means making a class, make a class. Does putting them in a dictionary make more sense? Put them in a dictionary. You don't feel like putting them in a dictionary? Then don't. Put them in a class."

**Use a class when:**
- You have data and behavior that naturally belong together
- You want to create multiple independent instances of the same "type" of thing
- You want to sort or compare objects (operator overloading makes this clean)
- You're working with an existing codebase that is already OOP

**Don't force OOP when:**
- You have a simple data-processing task — just process the data
- You're spending more time designing classes than writing code that solves the problem
- A dictionary or list already does the job cleanly

A class is, in a sense, like a named dictionary with behavior attached. If you already know how to use dicts, you already understand the core idea. The question is always: *does wrapping this in a class make the code cleaner and easier to reason about — or does it add unnecessary complexity?*

---

## 19. OOP Terminology Cheat Sheet

| Term | Meaning |
|---|---|
| Class | Blueprint/template for creating objects |
| Instance / Object | A specific item created from a class |
| Instance variable / Attribute / Field | Data stored in each object |
| Method | A function defined inside a class |
| Constructor | `__init__` — called when object is created |
| Encapsulation | Bundling data + methods; controlling access |
| Abstraction | Hiding internals; exposing only an interface |
| Polymorphism | Same method name, different behavior per class |
| Inheritance | Child class acquires parent class's variables and methods |
| Parent / Base / Super class | The class being inherited from |
| Child / Sub / Derived class | The class doing the inheriting |
| Override | Redefining a parent method in a child class |
| Getter / Setter | Methods to read (`get_`) or write (`set_`) a variable |
| Class variable | One variable shared across all instances |
| Class method | A method that belongs to the class, not an instance |
| Magic method / Dunder method | Special `__method__` Python calls automatically |
| Operator overloading | Using magic methods to define behavior for `+`, `<`, etc. |
| Composition | An object stores other objects as instance variables ("has-a") |
| `self` | Reference to the current object instance |
| `super()` | Reference to the parent class |

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*