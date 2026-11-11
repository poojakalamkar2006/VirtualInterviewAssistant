# Python interview questions

questions = {
    "Easy": [
    ],

    "Medium": [
    ],

    "Hard": [
    ]
}
# Python interview questions

questions = {
    "Easy": [
        {
            "question": "What is Python?",
            "expected_answer": "Python is a high-level, interpreted, general-purpose programming language known for its simple and readable syntax."
        },
        {
            "question": "What are the main features of Python?",
            "expected_answer": "Python is easy to learn, interpreted, dynamically typed, object-oriented, portable, open-source, and has a large standard library."
        },
        {
            "question": "What is a variable in Python?",
            "expected_answer": "A variable is a name used to store a value in Python."
        },
        {
            "question": "What are the basic data types in Python?",
            "expected_answer": "Common Python data types include int, float, str, bool, list, tuple, set, and dictionary."
        },
        {
            "question": "What is a list in Python?",
            "expected_answer": "A list is an ordered and mutable collection that can store multiple values."
        },
        {
            "question": "What is a tuple in Python?",
            "expected_answer": "A tuple is an ordered and immutable collection of values."
        },
        {
            "question": "What is a dictionary in Python?",
            "expected_answer": "A dictionary is a mutable collection that stores data as key-value pairs."
        },
        {
            "question": "What is a set in Python?",
            "expected_answer": "A set is an unordered collection of unique elements."
        },
        {
            "question": "What is the difference between a list and a tuple?",
            "expected_answer": "A list is mutable, while a tuple is immutable."
        },
        {
            "question": "What is indentation in Python?",
            "expected_answer": "Indentation is the whitespace used to define blocks of code in Python."
        },
        {
            "question": "What is a function in Python?",
            "expected_answer": "A function is a reusable block of code designed to perform a specific task."
        },
        {
            "question": "How do you define a function in Python?",
            "expected_answer": "A function is defined using the def keyword followed by the function name and parameters."
        },
        {
            "question": "What is a loop?",
            "expected_answer": "A loop is used to repeatedly execute a block of code."
        },
        {
            "question": "What is the difference between for and while loops?",
            "expected_answer": "A for loop is generally used to iterate over a sequence, while a while loop continues executing as long as a condition is true."
        },
        {
            "question": "What is the purpose of the if statement?",
            "expected_answer": "The if statement is used to execute code when a specified condition is true."
        },
        {
            "question": "What is the difference between == and = in Python?",
            "expected_answer": "The = operator assigns a value, while == compares two values."
        },
        {
            "question": "What is None in Python?",
            "expected_answer": "None represents the absence of a value or a null value in Python."
        },
        {
            "question": "What is a comment in Python?",
            "expected_answer": "A comment is text ignored by Python and is used to explain or document code."
        },
        {
            "question": "What is type casting?",
            "expected_answer": "Type casting is the process of converting a value from one data type to another."
        },
        {
            "question": "What is the len() function?",
            "expected_answer": "The len() function returns the number of items in an object such as a string, list, tuple, or dictionary."
        }
    ],

    "Medium": [
        {
            "question": "What is the difference between mutable and immutable objects in Python?",
            "expected_answer": "Mutable objects can be changed after creation, while immutable objects cannot be changed after creation."
        },
        {
            "question": "What is a list comprehension?",
            "expected_answer": "A list comprehension is a concise way to create a list using an expression and an iteration."
        },
        {
            "question": "What is a lambda function?",
            "expected_answer": "A lambda function is a small anonymous function defined using the lambda keyword."
        },
        {
            "question": "What are *args and **kwargs?",
            "expected_answer": "*args allows a function to accept a variable number of positional arguments, while **kwargs allows a variable number of keyword arguments."
        },
        {
            "question": "What is exception handling in Python?",
            "expected_answer": "Exception handling is used to handle runtime errors using mechanisms such as try, except, else, and finally."
        },
        {
            "question": "What is the difference between try, except, else, and finally?",
            "expected_answer": "try contains code that may raise an exception, except handles the exception, else runs when no exception occurs, and finally runs regardless of whether an exception occurs."
        },
        {
            "question": "What is a module in Python?",
            "expected_answer": "A module is a Python file containing code such as functions, classes, and variables that can be imported into another program."
        },
        {
            "question": "What is a package in Python?",
            "expected_answer": "A package is a collection of related Python modules organized in a directory."
        },
        {
            "question": "What is the difference between a module and a package?",
            "expected_answer": "A module is generally a single Python file, while a package is a directory containing related modules."
        },
        {
            "question": "What is object-oriented programming?",
            "expected_answer": "Object-oriented programming is a programming approach based on objects and classes."
        },
        {
            "question": "What is a class in Python?",
            "expected_answer": "A class is a blueprint for creating objects and defining their attributes and methods."
        },
        {
            "question": "What is an object in Python?",
            "expected_answer": "An object is an instance of a class containing data and behavior."
        },
        {
            "question": "What is inheritance?",
            "expected_answer": "Inheritance allows one class to acquire attributes and methods from another class."
        },
        {
            "question": "What is polymorphism?",
            "expected_answer": "Polymorphism allows the same interface or method name to work with different types of objects."
        },
        {
            "question": "What is encapsulation?",
            "expected_answer": "Encapsulation is the concept of combining data and methods inside a class and controlling access to them."
        },
        {
            "question": "What is the __init__() method?",
            "expected_answer": "The __init__() method is a special method that is commonly used to initialize an object's attributes when an object is created."
        },
        {
            "question": "What is self in Python?",
            "expected_answer": "self refers to the current instance of a class and is used to access its attributes and methods."
        },
        {
            "question": "What is the difference between shallow copy and deep copy?",
            "expected_answer": "A shallow copy copies the outer object but may share nested objects, while a deep copy recursively copies nested objects."
        },
        {
            "question": "What is an iterator in Python?",
            "expected_answer": "An iterator is an object that produces values one at a time using the iterator protocol."
        },
        {
            "question": "What is a generator in Python?",
            "expected_answer": "A generator is a special type of iterator that produces values lazily, commonly using the yield keyword."
        }
    ],

    "Hard": [
        {
            "question": "Explain decorators in Python.",
            "expected_answer": "A decorator is a function that modifies or extends the behavior of another function or class without changing its source code."
        },
        {
            "question": "What is a context manager in Python?",
            "expected_answer": "A context manager manages resources and their cleanup, commonly used with the with statement."
        },
        {
            "question": "What is the Global Interpreter Lock?",
            "expected_answer": "The Global Interpreter Lock, or GIL, is a mechanism in standard CPython that allows only one thread to execute Python bytecode at a time."
        },
        {
            "question": "What is the difference between multiprocessing and multithreading in Python?",
            "expected_answer": "Multithreading uses multiple threads within a process, while multiprocessing uses separate processes. Multiprocessing can execute CPU-bound Python code in parallel across processes."
        },
        {
            "question": "What is monkey patching?",
            "expected_answer": "Monkey patching is the practice of modifying or replacing attributes or methods of classes or modules at runtime."
        },
        {
            "question": "What are Python descriptors?",
            "expected_answer": "Descriptors are objects that define methods such as __get__, __set__, or __delete__ to customize attribute access."
        },
        {
            "question": "What is metaprogramming in Python?",
            "expected_answer": "Metaprogramming is the technique of writing code that can inspect, modify, or generate other code or program behavior."
        },
        {
            "question": "What are metaclasses in Python?",
            "expected_answer": "A metaclass is a class whose instances are classes. It controls how classes are created and can customize class creation."
        },
        {
            "question": "Explain Python memory management.",
            "expected_answer": "Python manages memory automatically using mechanisms such as private memory management, reference counting, and garbage collection in CPython."
        },
        {
            "question": "What is garbage collection in Python?",
            "expected_answer": "Garbage collection automatically identifies and removes objects that are no longer needed, including certain reference cycles."
        },
        {
            "question": "What is duck typing?",
            "expected_answer": "Duck typing means that an object's suitability is determined by its behavior and available methods rather than its explicit type."
        },
        {
            "question": "What is method resolution order?",
            "expected_answer": "Method resolution order, or MRO, defines the order in which Python searches classes for attributes and methods, especially with inheritance."
        },
        {
            "question": "What are abstract base classes?",
            "expected_answer": "Abstract base classes define common interfaces and can require subclasses to implement specific methods."
        },
        {
            "question": "What is asynchronous programming in Python?",
            "expected_answer": "Asynchronous programming allows tasks to cooperate and progress without blocking while waiting for operations such as I/O."
        },
        {
            "question": "What is asyncio?",
            "expected_answer": "asyncio is Python's library for writing asynchronous programs using an event loop, coroutines, and awaitable objects."
        },
        {
            "question": "What is the difference between __str__ and __repr__?",
            "expected_answer": "__str__ is intended to provide a readable string representation, while __repr__ is intended to provide an unambiguous representation useful for debugging."
        },
        {
            "question": "What are positional-only and keyword-only arguments?",
            "expected_answer": "Positional-only arguments must be passed by position, while keyword-only arguments must be passed using their parameter names."
        },
        {
            "question": "What is a closure in Python?",
            "expected_answer": "A closure is a function that remembers and can access variables from its enclosing scope even after that scope has finished executing."
        },
        {
            "question": "What is the difference between an iterable and an iterator?",
            "expected_answer": "An iterable can provide an iterator, while an iterator maintains its state and produces the next value when requested."
        },
        {
            "question": "How can Python code be optimized for better performance?",
            "expected_answer": "Python performance can be improved by choosing suitable algorithms and data structures, avoiding unnecessary work, profiling bottlenecks, and using appropriate libraries or concurrency techniques."
        }
    ]
}