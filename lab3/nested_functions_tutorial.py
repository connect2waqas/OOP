"""
================================================================================
                    NESTED FUNCTIONS IN PYTHON - COMPLETE TUTORIAL
================================================================================

A nested function is a function defined inside another function.
This is one of Python's most powerful features for writing clean, organized code.

================================================================================
                            SECTION 1: BASICS
================================================================================
"""

# ============================================================================
# EXAMPLE 1: BASIC NESTED FUNCTION
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 1: Basic Nested Function")
print("="*70)

def outer():
    """Outer function - parent function"""
    print("  This is OUTER function")
    
    def inner():
        """Inner function - nested inside outer"""
        print("  This is INNER function (nested inside OUTER)")
    
    # Call the nested function from within outer function
    inner()

# Call outer function
outer()
print("\nExplanation:")
print("  - outer() is defined in global scope")
print("  - inner() is defined INSIDE outer() - it's nested")
print("  - inner() is ONLY accessible from within outer()")
print("  - When outer() runs, it calls inner()")


# ============================================================================
# EXAMPLE 2: NESTED FUNCTION SCOPE - WHY IT MATTERS
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 2: Nested Function Scope (LEGB Rule)")
print("="*70)

x = "GLOBAL"  # Global scope

def outer_scope():
    x = "OUTER"  # Enclosing scope
    
    def inner_scope():
        x = "INNER"  # Local scope
        print(f"  Inner can see x = {x}")
    
    inner_scope()
    print(f"  Outer can see x = {x}")

outer_scope()
print(f"  Global scope x = {x}")

print("\nExplanation (LEGB Rule):")
print("  L = Local scope (inside the current function)")
print("  E = Enclosing scope (outer function's scope)")
print("  G = Global scope (module level)")
print("  B = Built-in scope (Python's built-in names)")
print("\n  When Python looks for a variable, it searches in this order: L→E→G→B")


# ============================================================================
# EXAMPLE 3: NESTED FUNCTION ACCESSING OUTER VARIABLES (NO MODIFICATION)
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 3: Nested Function Accessing Outer Variables")
print("="*70)

def outer_with_var():
    name = "Ali"  # Variable in outer scope
    age = 21
    
    def inner_access():
        # Inner can READ outer's variables without 'nonlocal'
        print(f"  Inner accessed: name = {name}, age = {age}")
    
    inner_access()

outer_with_var()

print("\nExplanation:")
print("  - Inner function can READ outer function's variables")
print("  - Does NOT need the 'nonlocal' keyword to READ")
print("  - But if you want to MODIFY outer's variables, you need 'nonlocal'")


# ============================================================================
# EXAMPLE 4: MODIFYING OUTER VARIABLES WITH 'nonlocal'
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 4: Modifying Outer Variables with 'nonlocal'")
print("="*70)

def outer_modify():
    count = 0
    
    def inner_increment():
        nonlocal count  # This declares we want to MODIFY count from outer
        count += 1
        print(f"  Inner incremented count to: {count}")
    
    print(f"  Before: count = {count}")
    inner_increment()
    inner_increment()
    inner_increment()
    print(f"  After all inner calls: count = {count}")

outer_modify()

print("\nExplanation:")
print("  - 'nonlocal' keyword tells Python to modify the OUTER function's variable")
print("  - Without 'nonlocal', Python would try to create a NEW local variable")
print("  - This is how nested functions can change outer function's state")


# ============================================================================
# EXAMPLE 5: RETURNING NESTED FUNCTIONS (CLOSURES)
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 5: Returning Nested Functions (Closures)")
print("="*70)

def create_multiplier(factor):
    """
    Returns a nested function.
    The returned function 'remembers' the factor value.
    This is called a CLOSURE.
    """
    def multiply(number):
        return number * factor
    
    return multiply  # Return the function itself, not its result

# Create different multiplier functions
multiply_by_2 = create_multiplier(2)
multiply_by_5 = create_multiplier(5)
multiply_by_10 = create_multiplier(10)

print(f"  multiply_by_2(7) = {multiply_by_2(7)}")
print(f"  multiply_by_5(7) = {multiply_by_5(7)}")
print(f"  multiply_by_10(7) = {multiply_by_10(7)}")

print("\nExplanation (Closure):")
print("  - create_multiplier() returns multiply() function")
print("  - Even after create_multiplier() finishes, multiply() 'remembers' factor")
print("  - Each returned function has its own 'factor' value stored")
print("  - This is called a CLOSURE - function + captured variables")


# ============================================================================
# EXAMPLE 6: PRACTICAL CLOSURE - COUNTER
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 6: Practical Closure - Creating a Counter")
print("="*70)

def create_counter(start=0):
    """Create a counter that increments each time it's called"""
    count = start
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    def get_count():
        return count
    
    def reset():
        nonlocal count
        count = start
    
    # Return multiple functions
    return {
        'increment': increment,
        'get_count': get_count,
        'reset': reset
    }

counter = create_counter(start=100)

print(f"  Initial count: {counter['get_count']()}")
print(f"  After increment: {counter['increment']()}")
print(f"  After increment: {counter['increment']()}")
print(f"  Current count: {counter['get_count']()}")
counter['reset']()
print(f"  After reset: {counter['get_count']()}")

print("\nExplanation:")
print("  - create_counter() returns 3 different functions")
print("  - All 3 functions share and modify the same 'count' variable")
print("  - This lets us create stateful functions - functions with memory")


# ============================================================================
# EXAMPLE 7: DECORATORS (MOST IMPORTANT USE OF NESTED FUNCTIONS)
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 7: Decorators (Most Common Use of Nested Functions)")
print("="*70)

def my_decorator(func):
    """
    A decorator that adds behavior to a function.
    This is a function that returns a nested function.
    """
    def wrapper(*args, **kwargs):
        print(f"  [BEFORE] Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  [AFTER] {func.__name__} returned: {result}")
        return result
    
    return wrapper

# Using the decorator
@my_decorator
def greet(name):
    return f"Hello, {name}!"

print("Calling greet('Ali'):")
result = greet("Ali")

print("\nExplanation:")
print("  - @my_decorator is syntactic sugar")
print("  - greet = my_decorator(greet) happens automatically")
print("  - Now greet is actually the wrapper function")
print("  - wrapper() calls the original greet inside itself")
print("  - This adds 'before' and 'after' behavior to greet()")


# ============================================================================
# EXAMPLE 8: DECORATOR WITH ARGUMENTS
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 8: Decorator with Arguments")
print("="*70)

def repeat_decorator(times):
    """
    Decorator that repeats function execution.
    This has 3 levels of nesting!
    """
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                result = func(*args, **kwargs)
                results.append(result)
                print(f"    Execution #{i+1}: {result}")
            return results
        return wrapper
    return actual_decorator

@repeat_decorator(times=3)
def say_hello(name):
    return f"Hi {name}!"

print("Calling say_hello('Ahmed') with @repeat_decorator(times=3):")
say_hello("Ahmed")

print("\nExplanation:")
print("  - repeat_decorator(times) returns actual_decorator")
print("  - actual_decorator(func) returns wrapper")
print("  - This is 3-level nesting for maximum flexibility")


# ============================================================================
# EXAMPLE 9: NESTED LOOPS IN NESTED FUNCTIONS
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 9: Nested Loops in Nested Functions")
print("="*70)

def create_table(rows, cols):
    """Create and print a table using nested functions"""
    
    def print_row(row_num):
        for col in range(1, cols + 1):
            value = row_num * col
            print(f"{value:3d}", end=" ")
        print()  # Newline after each row
    
    def print_table():
        print(f"  Multiplication Table ({rows}x{cols}):")
        for row in range(1, rows + 1):
            print_row(row)
    
    return print_table

# Create and call the table printer
table_printer = create_table(rows=5, cols=5)
table_printer()

print("\nExplanation:")
print("  - print_row() is nested inside create_table()")
print("  - print_table() is also nested and calls print_row()")
print("  - This organizes complex logic into smaller functions")


# ============================================================================
# EXAMPLE 10: REAL-WORLD EXAMPLE - BANK ACCOUNT
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 10: Real-World Example - Bank Account")
print("="*70)

def create_bank_account(owner, initial_balance=0):
    """
    Create a bank account with private balance and public methods.
    This demonstrates encapsulation using nested functions.
    """
    balance = initial_balance
    transaction_history = []
    
    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
            transaction_history.append(f"Deposit: +{amount}")
            return f"Deposited {amount}. New balance: {balance}"
        return "Invalid amount"
    
    def withdraw(amount):
        nonlocal balance
        if amount > 0 and amount <= balance:
            balance -= amount
            transaction_history.append(f"Withdrawal: -{amount}")
            return f"Withdrew {amount}. New balance: {balance}"
        return "Invalid amount or insufficient funds"
    
    def get_balance():
        return balance
    
    def get_history():
        return transaction_history
    
    # Return public interface
    return {
        'owner': owner,
        'deposit': deposit,
        'withdraw': withdraw,
        'get_balance': get_balance,
        'get_history': get_history
    }

# Create account
account = create_bank_account("Ali", initial_balance=1000)

print(f"Account Owner: {account['owner']}")
print(f"Initial Balance: {account['get_balance']()}")
print(f"Action: {account['deposit'](500)}")
print(f"Action: {account['withdraw'](200)}")
print(f"Final Balance: {account['get_balance']()}")
print(f"Transaction History: {account['get_history']()}")

print("\nExplanation:")
print("  - 'balance' and 'transaction_history' are PRIVATE (not accessible outside)")
print("  - Only accessible through the nested functions")
print("  - This is Python's way of implementing encapsulation")
print("  - Much cleaner than using class with private variables")


# ============================================================================
# EXAMPLE 11: COMPARISON - NESTED FUNCTIONS VS CLASSES
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 11: Nested Functions vs Classes")
print("="*70)

# Using nested functions (what we've been doing)
def make_person(name, age):
    def get_info():
        return f"{name} is {age} years old"
    
    def birthday():
        nonlocal age
        age += 1
        return f"Happy birthday! Now {age} years old"
    
    return {'get_info': get_info, 'birthday': birthday}

person1 = make_person("Ali", 21)
print(f"Nested Function approach: {person1['get_info']()}")
print(f"  {person1['birthday']()}")

# Using a class (traditional OOP approach)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"
    
    def birthday(self):
        self.age += 1
        return f"Happy birthday! Now {self.age} years old"

person2 = Person("Ali", 21)
print(f"\nClass approach: {person2.get_info()}")
print(f"  {person2.birthday()}")

print("\nComparison:")
print("  Nested Functions:")
print("    + Lightweight, no class overhead")
print("    + Great for short-lived objects")
print("    + Harder to extend/inherit")
print("\n  Classes:")
print("    + Better for complex objects")
print("    + Easy to inherit and extend")
print("    + More memory overhead")


# ============================================================================
# EXAMPLE 12: COMMON MISTAKES AND GOTCHAS
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 12: Common Mistakes")
print("="*70)

print("\n❌ MISTAKE 1: Forgetting 'nonlocal' when modifying outer variable")
print("-" * 70)

def mistake_1():
    count = 0
    
    def inner_bad():
        count = count + 1  # ERROR: trying to use and modify same variable!
    
    try:
        inner_bad()
    except UnboundLocalError as e:
        print(f"  Error: {e}")
    
    print("  Solution: Use 'nonlocal count' before modifying")

mistake_1()

print("\n❌ MISTAKE 2: Late binding in loops (common gotcha)")
print("-" * 70)

def mistake_2_wrong():
    """Wrong way - all functions will use the last value"""
    functions = []
    for i in range(3):
        def func():
            return i
        functions.append(func)
    
    print("  Wrong way (late binding):")
    for f in functions:
        print(f"    Function result: {f()}")  # All return 2!

def mistake_2_correct():
    """Correct way - capture value at function definition time"""
    functions = []
    for i in range(3):
        def func(x=i):  # Default argument captures current value
            return x
        functions.append(func)
    
    print("  Correct way (early binding):")
    for f in functions:
        print(f"    Function result: {f()}")  # Returns 0, 1, 2

mistake_2_wrong()
mistake_2_correct()

print("\nExplanation:")
print("  - Variables are looked up when function is CALLED, not defined")
print("  - Use default arguments to capture value at definition time")


# ============================================================================
# EXAMPLE 13: STEP-BY-STEP EXECUTION TRACE
# ============================================================================
print("\n" + "="*70)
print("EXAMPLE 13: Step-by-Step Execution Trace (For Understanding)")
print("="*70)

def trace_example():
    print("  Step 1: Defining outer function")
    
    value = 10
    print(f"  Step 2: Setting value = {value}")
    
    def inner():
        print(f"  Step 5: Inside inner function, value = {value}")
        return value * 2
    
    print("  Step 3: Defined inner function (but didn't call it yet)")
    
    result = inner()
    print(f"  Step 6: inner() returned {result}")
    
    return result

print("\nExecution trace:")
trace_example()


# ============================================================================
# SUMMARY AND KEY POINTS
# ============================================================================
print("\n" + "="*70)
print("SUMMARY - KEY CONCEPTS OF NESTED FUNCTIONS")
print("="*70)

summary = """
1. DEFINITION: A function defined inside another function

2. SCOPE (LEGB Rule):
   - Can access outer function's variables (Read)
   - Use 'nonlocal' to modify outer variables
   - Have their own local scope

3. CLOSURES:
   - Nested functions that 'remember' outer variables
   - Even after outer function finishes
   - Useful for creating stateful functions

4. RETURNING FUNCTIONS:
   - You can return the function itself (not its result)
   - The returned function carries its closure with it
   - Enables higher-order functions

5. DECORATORS:
   - Functions that modify/wrap other functions
   - Used extensively in Python frameworks
   - Syntactic sugar: @decorator = func = decorator(func)

6. ENCAPSULATION:
   - Can hide implementation details
   - Only expose what's needed through returned dict/functions
   - "Private" variables through nested function scope

7. USE CASES:
   - Decorators for adding behavior
   - Factories for creating customized objects
   - Callbacks and event handlers
   - Protecting sensitive data

8. COMMON MISTAKES:
   - Forgetting 'nonlocal' when modifying outer variables
   - Late binding in loops (variables lookup when called)
   - Trying to access nested function from outside

"""

print(summary)

# ============================================================================
print("\n" + "="*70)
print("END OF NESTED FUNCTIONS TUTORIAL")
print("="*70)
print("\nNow run this file and experiment with each example!")
print("Try modifying the code to deepen your understanding.")
print("="*70)
