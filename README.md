# Object-Oriented Programming (OOP) Learning Repository

Welcome to the **OOP Learning Repository**! This is a comprehensive collection of Python Object-Oriented Programming concepts, examples, and practical exercises designed for students learning OOP fundamentals.

## 📚 Repository Overview

This repository contains structured learning materials covering core OOP principles including **Inheritance**, **Polymorphism**, **Encapsulation**, and practical applications. All materials are written in **Python** and include both theoretical examples and hands-on lab exercises.

---

## 🗂️ Directory Structure

### **Daily Learning Lessons**
- **`day1.py`** - Inheritance Basics
  - Introduction to inheritance concepts
  - `Person`, `Student`, and `Teacher` classes demonstrating parent-child relationships
  - Method overriding and super() usage

- **`day2.py`** - Intermediate OOP Concepts
  - Advanced class features and relationships

- **`day3.py`** - Polymorphism Complete Guide
  - Function polymorphism
  - Class method polymorphism
  - Inheritance-based polymorphism
  - Method overriding
  - Operator overloading (special methods)
  - Duck typing
  - Real-world payment system example

- **`day4.py`** - Additional OOP Patterns
  - More advanced OOP concepts and patterns

- **`day5.py`** - Practical Applications
  - Real-world use cases of OOP

- **`day6.py`** - Advanced Topics
  - Complex OOP scenarios

- **`day7.py`** - Review and Practice

### **Encapsulation Folder** (`/Encapsulation`)
Deep dive into encapsulation - one of the four pillars of OOP:
- **`pipeline.py`** - Pipeline processing with encapsulation
- **`practice_1.py`** - Basic encapsulation exercises
- **`practice_2.py`** - Intermediate encapsulation exercises

### **Laboratory Exercises**

#### **Lab 3** (`/lab3`)
Comprehensive collection of practical exercises:
- **`Atm_withdrwal.py`** - ATM withdrawal system
- **`Robot.py`** - Robot class implementation
- **`Shopping_cart.py`** - E-commerce shopping cart
- **`company_employee_record.py`** - Employee management system
- **`student_info_system.py`** - Student information management
- **`Nest_function.py`** - Nested function examples
- **`Resturant_order.py`** - Restaurant ordering system
- **`Smart_calculater.py`** - Calculator with smart features
- **`deposit_balance.py`** - Bank deposit system
- **`elecltricity_bill.py`** - Electricity billing system
- **`give_discount.py`** - Discount calculation system
- **`global_var.py`** - Global variable scope examples
- **`greet.py`** - Simple greeting program
- **`nested_functions_tutorial.py`** - Comprehensive nested functions tutorial
- **`pass_fail.py`** - Grade pass/fail system
- **`studentID.py`** - Student ID management
- **`temprature_converter.py`** - Temperature conversion utility
- **`user_profile_system.py`** - User profile management

#### **Lab 4** (`/lab4`)
Advanced practice problems and projects

#### **Lab 5** (`/lab5`)
Final lab exercises and comprehensive projects

### **Lecture Materials**
- **`/lecture2`** - Lecture 2 code examples
- **`/lecture3`** - Lecture 3 code examples
- **`/lecture5`** - Lecture 5 code examples
- **`/lecture6`** - Lecture 6 code examples

---

## 🎯 Key OOP Concepts Covered

### 1. **Inheritance** (Day 1)
Learn how to create class hierarchies and reuse code through parent-child relationships.

```python
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Student(Person):
    def __init__(self, name, age, address, roll_no, marks):
        super().__init__(name, age, address)
        self.roll_no = roll_no
        self.marks = marks
```

### 2. **Polymorphism** (Day 3)
Understand how the same interface can be used with different data types.

**Types covered:**
- Function polymorphism (method overloading)
- Class method polymorphism
- Inheritance-based polymorphism
- Method overriding
- Operator overloading
- Duck typing

**Example:**
```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius ** 2
```

### 3. **Encapsulation** (`/Encapsulation`)
Learn how to bundle data and methods while controlling access through public, private, and protected members.

### 4. **Practical Applications**
Each lab folder contains real-world applications:
- Bank account management
- E-commerce systems
- Employee records
- Student management
- Restaurant ordering
- And more!

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system
- Basic understanding of Python syntax

### Running the Examples

1. **Clone the repository:**
   ```bash
   git clone https://github.com/connect2waqas/OOP.git
   cd OOP
   ```

2. **Run any Python file:**
   ```bash
   python day1.py
   python day3.py
   python lab3/Atm_withdrwal.py
   ```

### Learning Path

**Recommended progression:**
1. Start with `day1.py` - Learn inheritance basics
2. Progress through `day2.py` through `day6.py`
3. Study `day3.py` for deep polymorphism understanding
4. Explore `/Encapsulation` folder for encapsulation principles
5. Work through `/lab3` exercises for practical application
6. Challenge yourself with `/lab4` and `/lab5`
7. Review lecture materials in `/lecture*` folders

---

## 💡 Learning Highlights

### Day 1: Inheritance Foundation
- Parent-child class relationships
- The `super()` function
- Method overriding
- Real example: Person → Student/Teacher hierarchy

### Day 3: Polymorphism Mastery
Complete guide with 7 types of polymorphism:
1. Basic function polymorphism
2. Built-in polymorphic functions
3. Class method polymorphism
4. Inheritance-based polymorphism
5. Method overriding
6. Operator overloading
7. Duck typing

### Practical Labs
Hands-on exercises including:
- Banking systems (ATM, deposits, balance)
- E-commerce (shopping cart, discounts)
- Educational systems (students, grades, IDs)
- Utility programs (calculators, converters, billing)

---

## 📖 Topics by Difficulty Level

**Beginner:**
- `day1.py` - Basic inheritance
- `lab3/greet.py` - Simple programs
- `lab3/pass_fail.py` - Conditional logic

**Intermediate:**
- `day2.py` - Advanced OOP features
- `day3.py` - Polymorphism concepts
- `lab3/Shopping_cart.py` - Class interactions
- `lab3/company_employee_record.py` - Complex structures

**Advanced:**
- `/Encapsulation` folder - Deep encapsulation patterns
- `lab3/nested_functions_tutorial.py` - Advanced scoping
- `/lab4` and `/lab5` - Complex projects

---

## 🔍 File Details

### Core Learning Files
| File | Size | Topic |
|------|------|-------|
| day1.py | 1.59 KB | Inheritance |
| day2.py | 1.98 KB | Intermediate OOP |
| day3.py | 5.96 KB | Polymorphism |
| day4.py | 1.84 KB | OOP Patterns |
| day5.py | 1.69 KB | Applications |
| day6.py | 1.28 KB | Advanced Topics |

### Encapsulation Materials
| File | Focus |
|------|-------|
| practice_1.py | Basic Encapsulation |
| practice_2.py | Intermediate Encapsulation |
| pipeline.py | Advanced Pipeline Pattern |

---

## 📝 Notes

- All code examples follow Python 3.x syntax
- Comments are provided to explain key concepts
- Real-world scenarios are used throughout for better understanding
- Each lab folder contains independent exercises that can be worked on separately

---

## 🎓 Educational Goals

By working through this repository, you will:
✅ Master the four pillars of OOP: Inheritance, Polymorphism, Encapsulation, Abstraction  
✅ Understand real-world applications of OOP principles  
✅ Write clean, maintainable, object-oriented code  
✅ Solve practical programming problems using OOP  
✅ Build confidence in Python programming  

---

## 📞 Support

For questions or clarifications about the material, feel free to check the comments in the code or create an issue in the repository.

---

## 📄 License

This repository is open source and available for educational purposes.

---

**Happy Learning! 🚀**

*Keep coding, keep learning!*