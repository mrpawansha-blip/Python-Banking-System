# Module 03 — Object-Oriented Python

## Learning Notes

### 1. Introduction to OOP
Object-Oriented Programming organizes code around classes and objects. It helps structure larger programs, reuse code and model real-world entities.

### 2. Classes and Objects
- A **class** is a blueprint that defines attributes and methods.
- An **object** is an instance of a class.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, I am", self.name)

student1 = Student("Aman")
student1.introduce()
```

### 3. Constructors and Methods
`__init__()` is called when an object is created and initializes its attributes. An instance method takes `self` as its first parameter and works with object data.

### 4. Encapsulation
Encapsulation bundles data and methods inside a class and controls access to internal state. In Python, a double-underscore attribute such as `__balance` is name-mangled to discourage direct access. Properties can provide controlled access.

### 5. Inheritance
Inheritance allows a child class to reuse and extend a parent class.

```python
class SavingsAccount(BankAccount):
    pass
```

`super()` can call a parent-class method or constructor.

### 6. Polymorphism
Polymorphism allows different classes to provide their own implementations of a common method name. For example, SavingsAccount and CurrentAccount each implement `account_type()`.

### 7. Abstraction
Abstraction exposes essential operations while hiding implementation details. Python's `abc` module provides `ABC` and `@abstractmethod` for abstract base classes.

### 8. Clean Code Principles
- Use meaningful class, method and variable names.
- Keep each method focused on one responsibility.
- Validate input at program boundaries.
- Handle expected errors with clear messages.
- Add docstrings and comments where they clarify intent.
- Avoid duplicating code.

### 9. Project: Python Banking System
The project includes:
- Account creation
- Deposit
- Withdrawal
- Balance and account detail display
- Transaction history

The `BankAccount` base class stores account information and common operations. `SavingsAccount` and `CurrentAccount` extend it. `BankingSystem` provides the interactive menu and manages accounts.

### 10. Class Design Summary
- `BankAccount` (abstract): common account data and operations.
- `SavingsAccount`: savings-specific account type and minimum-balance withdrawal rule.
- `CurrentAccount`: current account type.
- `BankingSystem`: creates and manages account objects.

### Practice Questions
1. Add a feature to transfer money between two accounts.
2. Add a daily withdrawal limit to SavingsAccount.
3. Create a FixedDepositAccount subclass.
4. Add a method to calculate simple interest.
5. Explain where encapsulation, inheritance, polymorphism and abstraction are used in this project.

## Important limitation
This educational version keeps account and transaction data in memory. Data is lost when the program exits. It is not a real banking application and must not be used for real financial transactions.
