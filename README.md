# OOP (Python) — practice repo

This repository is basically my OOP practice notebook — but in code.

It’s a collection of small Python scripts I wrote while learning / revising Object-Oriented Programming concepts (and a few general Python topics from labs/lectures). The files are intentionally simple and focused, so it’s easy to open one, run it, and see what’s going on.

## Tech stack

- **Language:** Python

## What’s inside (quick map)

### Top-level practice files

- **`day1.py`** — basic classes + inheritance (`Person`, `Student`, `Teacher`) and a simple grade calculation.
- **`day2.py`** — a mini banking example using class variables, `@classmethod`, `@staticmethod`, plus a `SavingAccount` subclass.
- **`day3.py`** — polymorphism examples (functions, method overriding, operator overloading, duck typing, and a small payment example).
- **`day4.py`** — inheritance + polymorphism via an employee payroll example (`FullTimeEmployee`, `PartTimeEmployee`, `Contractor`).
- **`day5.py`** — vehicle rental example (base `Vehicle` class with `Car`, `Motorcycle`, `Truck` subclasses).
- **`day6.py`** — operator overloading using a simple 2D vector class (`__add__`, `__sub__`, `__sub__`, `__mul__`, `__truediv__`).
- **`day7.py`** — currently empty / placeholder.

### Labs

- **`lab3/`** — small practice tasks and mini-programs (ATM withdrawal, shopping cart, robot, calculator, student/user profile systems, etc.).
  - A bigger file here is **`lab3/nested_functions_tutorial.py`**, which is a detailed walkthrough of nested functions, closures, decorators, and common mistakes.

### Lectures

- **`lecture2/code.py`** — basic task-style practice (grading + simple inventory total calculation).
- **`lecture3/code.py`** — a cleaner grading example using `zip()`.

## How to run

You can run any file directly with Python.

```bash
# Example:
python day1.py
python day3.py
python lab3/Robot.py
```

> Tip: If you have both `python` and `python3`, use whichever matches your setup.

## Topics covered

A few things this repo touches (with small, runnable examples):

- Classes & objects
- Inheritance (`super()`)
- Method overriding
- Polymorphism (including duck typing)
- Class variables, `@classmethod`, `@staticmethod`
- Operator overloading (magic methods like `__add__`)
- Nested functions, closures, and decorators (see `lab3/nested_functions_tutorial.py`)

## Notes

- This repo is for learning, so some code is intentionally straightforward (and some files may be a bit messy while I’m experimenting).
- If you notice a bug or want to suggest a cleaner approach, feel free to open an issue or PR.

## License

No license has been added yet. If you plan to reuse or share this more broadly, adding a license (like MIT) would be a good next step.