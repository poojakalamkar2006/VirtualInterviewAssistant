# C++ interview questions

questions = {

    "Easy": [

        {
            "question": "What is C++?",
            "expected_answer": "C++ is a general-purpose programming language that supports procedural, object-oriented, and other programming paradigms."
        },
        {
            "question": "Who developed C++?",
            "expected_answer": "C++ was developed by Bjarne Stroustrup."
        },
        {
            "question": "Why is C++ called an extension of C?",
            "expected_answer": "C++ was developed from the C language and added features such as classes, objects, inheritance, polymorphism, and other capabilities."
        },
        {
            "question": "What is the extension of a C++ source file?",
            "expected_answer": "A C++ source file commonly uses the .cpp extension."
        },
        {
            "question": "What is the main() function in C++?",
            "expected_answer": "main() is the entry point of a C++ program where program execution normally begins."
        },
        {
            "question": "What is a variable in C++?",
            "expected_answer": "A variable is a named memory location used to store a value that can change during program execution."
        },
        {
            "question": "What are basic data types in C++?",
            "expected_answer": "Common basic data types include int, float, double, char, bool, and void."
        },
        {
            "question": "What is an int in C++?",
            "expected_answer": "int is a data type used to store integer values."
        },
        {
            "question": "What is a float in C++?",
            "expected_answer": "float is a data type used to store single-precision floating-point numbers."
        },
        {
            "question": "What is a double in C++?",
            "expected_answer": "double is a floating-point data type that generally provides more precision than float."
        },
        {
            "question": "What is a char in C++?",
            "expected_answer": "char is a data type used to store a single character."
        },
        {
            "question": "What is bool in C++?",
            "expected_answer": "bool is a data type that represents true or false values."
        },
        {
            "question": "What is a constant in C++?",
            "expected_answer": "A constant is a value that cannot be modified after it is defined."
        },
        {
            "question": "What is the const keyword?",
            "expected_answer": "The const keyword specifies that a variable or object should not be modified through that declaration."
        },
        {
            "question": "What is a keyword in C++?",
            "expected_answer": "A keyword is a reserved word with a predefined meaning in the C++ language."
        },
        {
            "question": "What is an identifier in C++?",
            "expected_answer": "An identifier is a name used to identify variables, functions, classes, objects, and other program elements."
        },
        {
            "question": "What is an operator in C++?",
            "expected_answer": "An operator is a symbol that performs an operation on one or more operands."
        },
        {
            "question": "What are arithmetic operators in C++?",
            "expected_answer": "Arithmetic operators include +, -, *, /, and %."
        },
        {
            "question": "What are relational operators?",
            "expected_answer": "Relational operators compare values using operators such as ==, !=, <, >, <=, and >=."
        },
        {
            "question": "What are logical operators in C++?",
            "expected_answer": "Logical operators are &&, ||, and ! and are used to combine or negate conditions."
        },
        {
            "question": "What is the difference between = and ==?",
            "expected_answer": "= is the assignment operator, while == is the equality comparison operator."
        },
        {
            "question": "What is an if statement?",
            "expected_answer": "An if statement executes a block of code when a specified condition is true."
        },
        {
            "question": "What is an if-else statement?",
            "expected_answer": "An if-else statement executes one block when a condition is true and another block when it is false."
        },
        {
            "question": "What is a switch statement?",
            "expected_answer": "A switch statement selects one block of code from multiple possible cases based on the value of an expression."
        },
        {
            "question": "What is a loop in C++?",
            "expected_answer": "A loop repeatedly executes a block of code while a specified condition is satisfied."
        },
        {
            "question": "What are the main types of loops in C++?",
            "expected_answer": "The main loops are for, while, and do-while."
        },
        {
            "question": "What is a for loop?",
            "expected_answer": "A for loop is commonly used when the number or pattern of iterations is known."
        },
        {
            "question": "What is a while loop?",
            "expected_answer": "A while loop repeatedly executes code as long as its condition remains true."
        },
        {
            "question": "What is a do-while loop?",
            "expected_answer": "A do-while loop executes its body at least once and then continues while its condition is true."
        },
        {
            "question": "What is the break statement?",
            "expected_answer": "The break statement immediately terminates the nearest loop or switch statement."
        },
        {
            "question": "What is the continue statement?",
            "expected_answer": "The continue statement skips the remaining statements in the current loop iteration and moves to the next iteration."
        },
        {
            "question": "What is a function in C++?",
            "expected_answer": "A function is a reusable block of code designed to perform a specific task."
        },
        {
            "question": "What is a function parameter?",
            "expected_answer": "A parameter is a variable in a function definition that receives a value passed during the function call."
        },
        {
            "question": "What is a return statement?",
            "expected_answer": "A return statement ends a function and can send a value back to the caller."
        },
        {
            "question": "What is function overloading?",
            "expected_answer": "Function overloading allows multiple functions to have the same name but different parameter lists."
        },
        {
            "question": "What is an array in C++?",
            "expected_answer": "An array is a collection of elements of the same data type stored in contiguous memory locations."
        },
        {
            "question": "What is the first index of an array in C++?",
            "expected_answer": "The first index of an array is 0."
        },
        {
            "question": "What is a string in C++?",
            "expected_answer": "A string is a sequence of characters, commonly represented using the std::string class."
        },
        {
            "question": "What is the difference between C-style string and std::string?",
            "expected_answer": "A C-style string is a character array terminated by a null character, while std::string is a C++ class that manages strings more conveniently."
        },
        {
            "question": "What is a pointer in C++?",
            "expected_answer": "A pointer is a variable that stores the memory address of another variable or object."
        },
        {
            "question": "What is a reference in C++?",
            "expected_answer": "A reference is an alias for an existing variable or object."
        },
        {
            "question": "What is a class in C++?",
            "expected_answer": "A class is a user-defined type that combines data members and member functions."
        },
        {
            "question": "What is an object in C++?",
            "expected_answer": "An object is an instance of a class."
        },
        {
            "question": "What is a constructor?",
            "expected_answer": "A constructor is a special member function that is automatically called when an object is created."
        },
        {
            "question": "What is a destructor?",
            "expected_answer": "A destructor is a special member function that is automatically called when an object is destroyed."
        },
        {
            "question": "What is encapsulation?",
            "expected_answer": "Encapsulation is the concept of combining data and related functions into a class while controlling access to the data."
        },
        {
            "question": "What are access specifiers in C++?",
            "expected_answer": "The main access specifiers are public, private, and protected."
        },
        {
            "question": "What is inheritance?",
            "expected_answer": "Inheritance allows a derived class to acquire properties and behavior from a base class."
        },
        {
            "question": "What is polymorphism?",
            "expected_answer": "Polymorphism allows the same interface or function call to behave differently depending on the object or context."
        },
        {
            "question": "What is abstraction?",
            "expected_answer": "Abstraction means exposing essential features while hiding unnecessary implementation details."
        }

    ],
#medium
        "Medium": [

    {
        "question": "What is the difference between class and structure in C++?",
        "expected_answer": "The main difference is the default access level. Class members are private by default, while structure members are public by default."
    },
    {
        "question": "What is a default constructor?",
        "expected_answer": "A default constructor is a constructor that can be called without arguments and is used to initialize an object."
    },
    {
        "question": "What is a parameterized constructor?",
        "expected_answer": "A parameterized constructor is a constructor that accepts one or more arguments to initialize an object with specific values."
    },
    {
        "question": "What is a copy constructor?",
        "expected_answer": "A copy constructor creates a new object by initializing it from an existing object of the same class."
    },
    {
        "question": "When is a copy constructor called?",
        "expected_answer": "A copy constructor can be called when an object is initialized from another object, passed by value, or returned by value depending on compiler optimizations."
    },
    {
        "question": "What is constructor overloading?",
        "expected_answer": "Constructor overloading means defining multiple constructors in the same class with different parameter lists."
    },
    {
        "question": "Can a constructor return a value?",
        "expected_answer": "No. A constructor does not have a return type and cannot return a value."
    },
    {
        "question": "Can a constructor be private?",
        "expected_answer": "Yes. A private constructor can be used to control object creation, such as in the Singleton design pattern."
    },
    {
        "question": "Can a destructor take parameters?",
        "expected_answer": "No. A destructor cannot take parameters and cannot be overloaded."
    },
    {
        "question": "What is the this pointer?",
        "expected_answer": "The this pointer is an implicit pointer available inside non-static member functions that points to the current object."
    },
    {
        "question": "What is a static data member in C++?",
        "expected_answer": "A static data member belongs to the class rather than individual objects, so all objects of the class share the same member."
    },
    {
        "question": "What is a static member function?",
        "expected_answer": "A static member function belongs to the class and can be called without creating an object. It cannot directly access non-static members."
    },
    {
        "question": "What is the difference between public, private, and protected?",
        "expected_answer": "Public members can be accessed from outside the class, private members can only be accessed within the class and permitted friends, and protected members can also be accessed by derived classes."
    },
    {
        "question": "What is single inheritance?",
        "expected_answer": "Single inheritance occurs when one derived class inherits from one base class."
    },
    {
        "question": "What is multilevel inheritance?",
        "expected_answer": "Multilevel inheritance occurs when a class is derived from another derived class, forming an inheritance chain."
    },
    {
        "question": "What is multiple inheritance?",
        "expected_answer": "Multiple inheritance occurs when one derived class inherits from more than one base class."
    },
    {
        "question": "What is hierarchical inheritance?",
        "expected_answer": "Hierarchical inheritance occurs when multiple derived classes inherit from the same base class."
    },
    {
        "question": "What is hybrid inheritance?",
        "expected_answer": "Hybrid inheritance is a combination of two or more types of inheritance."
    },
    {
        "question": "What is method overriding in C++?",
        "expected_answer": "Method overriding occurs when a derived class provides its own implementation of a virtual or inherited member function with the same signature."
    },
    {
        "question": "What is a virtual function?",
        "expected_answer": "A virtual function allows a derived class implementation to be selected at runtime when accessed through a base class pointer or reference."
    },
    {
        "question": "What is runtime polymorphism?",
        "expected_answer": "Runtime polymorphism allows the appropriate overridden function to be selected during program execution, usually through virtual functions."
    },
    {
        "question": "What is compile-time polymorphism?",
        "expected_answer": "Compile-time polymorphism is achieved through features such as function overloading and operator overloading where the appropriate operation is determined during compilation."
    },
    {
        "question": "What is a pure virtual function?",
        "expected_answer": "A pure virtual function is declared using = 0 and requires derived classes to provide an implementation if they are to be concrete."
    },
    {
        "question": "What is an abstract class?",
        "expected_answer": "An abstract class is a class that cannot be instantiated directly and usually contains at least one pure virtual function."
    },
    {
        "question": "What is the difference between overloading and overriding?",
        "expected_answer": "Overloading uses the same function name with different parameter lists, while overriding provides a new implementation of an inherited virtual function in a derived class."
    },
    {
        "question": "What is operator overloading?",
        "expected_answer": "Operator overloading allows operators to be given special behavior for user-defined types such as classes."
    },
    {
        "question": "Can all operators be overloaded in C++?",
        "expected_answer": "No. Some operators such as scope resolution ::, member access ., .* and conditional ?: cannot be overloaded."
    },
    {
        "question": "What is a friend function?",
        "expected_answer": "A friend function is a non-member function that is granted access to the private and protected members of a class."
    },
    {
        "question": "What is a friend class?",
        "expected_answer": "A friend class is a class whose member functions are allowed to access the private and protected members of another class."
    },
    {
        "question": "What is a namespace in C++?",
        "expected_answer": "A namespace provides a named scope that helps organize identifiers and prevent naming conflicts."
    },
    {
        "question": "What is the purpose of std namespace?",
        "expected_answer": "The std namespace contains standard C++ library components such as cout, cin, string, vector, and many other features."
    },
    {
        "question": "What is STL in C++?",
        "expected_answer": "STL stands for Standard Template Library and provides reusable containers, algorithms, iterators, and related utilities."
    },
    {
        "question": "What is a vector in C++?",
        "expected_answer": "vector is an STL container that stores elements in a dynamically resizable contiguous array."
    },
    {
        "question": "What is the difference between array and vector?",
        "expected_answer": "An array normally has a fixed size, while a vector can dynamically change its size and provides useful member functions."
    },
    {
        "question": "What is a stack in STL?",
        "expected_answer": "stack is a container adaptor that follows the LIFO principle, meaning the last element inserted is the first one removed."
    },
    {
        "question": "What is a queue in STL?",
        "expected_answer": "queue is a container adaptor that follows the FIFO principle, meaning the first element inserted is the first one removed."
    },
    {
        "question": "What is a map in C++?",
        "expected_answer": "map is an associative container that stores key-value pairs with unique keys, typically maintaining them in sorted key order."
    },
    {
        "question": "What is an unordered_map?",
        "expected_answer": "unordered_map stores key-value pairs using hashing and does not maintain elements in sorted order."
    },
    {
        "question": "What is a set in C++?",
        "expected_answer": "set is an associative container that stores unique elements, typically in sorted order."
    },
    {
        "question": "What is an iterator in C++?",
        "expected_answer": "An iterator is an object used to traverse and access elements in STL containers."
    },
    {
        "question": "What is a range-based for loop?",
        "expected_answer": "A range-based for loop provides a simple way to iterate over elements of arrays, containers, and other iterable objects."
    },
    {
        "question": "What is a reference variable?",
        "expected_answer": "A reference variable is an alias for an existing object or variable and must normally be initialized when declared."
    },
    {
        "question": "What is the difference between pointer and reference?",
        "expected_answer": "A pointer stores an address and can be reassigned or hold null, while a reference acts as an alias and normally cannot be reseated after initialization."
    },
    {
        "question": "What is pass by reference?",
        "expected_answer": "Pass by reference allows a function to work with the original variable through a reference instead of receiving a separate copy."
    },
    {
        "question": "What is pass by value?",
        "expected_answer": "Pass by value sends a copy of the argument to the function, so changes to the parameter do not normally affect the original variable."
    },
    {
        "question": "What are templates in C++?",
        "expected_answer": "Templates allow functions and classes to be written generically so they can work with different data types."
    },
    {
        "question": "What is a function template?",
        "expected_answer": "A function template defines a generic function that can operate on different data types."
    },
    {
        "question": "What is a class template?",
        "expected_answer": "A class template defines a generic class that can work with different data types."
    },
    {
        "question": "What is exception handling in C++?",
        "expected_answer": "Exception handling is a mechanism for handling runtime errors using try, catch, and throw."
    },
    {
        "question": "What are try, catch, and throw?",
        "expected_answer": "try contains code that may generate an exception, throw signals an exception, and catch handles the exception."
    },
    {
        "question": "What is RAII in C++?",
        "expected_answer": "RAII stands for Resource Acquisition Is Initialization and ties resource lifetime to object lifetime so resources are acquired during construction and released during destruction."
    },
    {
        "question": "What is smart pointer in C++?",
        "expected_answer": "A smart pointer is a class that manages dynamically allocated memory automatically and helps prevent memory leaks."
    }

    ],

    #hard

        "Hard": [

    {
        "question": "What is a virtual destructor and why is it important?",
        "expected_answer": "A virtual destructor ensures that when a derived object is deleted through a base class pointer, the derived destructor is also called correctly."
    },
    {
        "question": "What happens if a base class destructor is not virtual?",
        "expected_answer": "Deleting a derived object through a base class pointer can result in only the base destructor being called, causing incomplete cleanup and undefined behavior."
    },
    {
        "question": "What is a pure virtual destructor?",
        "expected_answer": "A pure virtual destructor makes a class abstract, but unlike other pure virtual functions, it must still have a definition because it is called when derived objects are destroyed."
    },
    {
        "question": "What is the virtual function table?",
        "expected_answer": "The virtual function table, or vtable, is a compiler-supported mechanism commonly used to store addresses of virtual functions for dynamic dispatch."
    },
    {
        "question": "What is a vptr?",
        "expected_answer": "A vptr is an implementation detail commonly used by compilers where an object contains a pointer to its class's virtual function table."
    },
    {
        "question": "What is dynamic binding in C++?",
        "expected_answer": "Dynamic binding means the function implementation to execute is determined at runtime, commonly through virtual functions and base class pointers or references."
    },
    {
        "question": "What is static binding in C++?",
        "expected_answer": "Static binding means the function or operation to execute is determined at compile time, such as with non-virtual function calls."
    },
    {
        "question": "What is object slicing?",
        "expected_answer": "Object slicing occurs when a derived class object is copied into a base class object by value, causing the derived-specific part to be discarded."
    },
    {
        "question": "How can object slicing be avoided?",
        "expected_answer": "Object slicing can be avoided by using references, pointers, or smart pointers instead of copying derived objects into base objects by value."
    },
    {
        "question": "What is the diamond problem in C++?",
        "expected_answer": "The diamond problem occurs in multiple inheritance when a class inherits from two classes that both inherit from the same base class, potentially creating duplicate base class subobjects."
    },
    {
        "question": "How does virtual inheritance solve the diamond problem?",
        "expected_answer": "Virtual inheritance ensures that only one shared instance of the common base class exists in the derived object."
    },
    {
        "question": "What is multiple inheritance ambiguity?",
        "expected_answer": "Ambiguity can occur when multiple base classes provide members with the same name, requiring qualification to specify which member should be used."
    },
    {
        "question": "What is the difference between virtual function and pure virtual function?",
        "expected_answer": "A virtual function can have a base class implementation and may be overridden, while a pure virtual function is declared with = 0 and makes the class abstract."
    },
    {
        "question": "Can a virtual function be static?",
        "expected_answer": "No. Static member functions do not operate on a specific object and therefore cannot participate in runtime virtual dispatch."
    },
    {
        "question": "Can constructors be virtual in C++?",
        "expected_answer": "No. Constructors cannot be virtual because virtual dispatch requires an already constructed object."
    },
    {
        "question": "Can destructors be virtual?",
        "expected_answer": "Yes. Destructors can and often should be virtual in polymorphic base classes."
    },
    {
        "question": "What is the Rule of Three?",
        "expected_answer": "The Rule of Three states that if a class needs a user-defined destructor, copy constructor, or copy assignment operator, it often needs all three because it manages a resource."
    },
    {
        "question": "What is the Rule of Five?",
        "expected_answer": "The Rule of Five extends the Rule of Three by adding the move constructor and move assignment operator for proper resource management with move semantics."
    },
    {
        "question": "What is the Rule of Zero?",
        "expected_answer": "The Rule of Zero recommends designing classes so they do not need custom destructors, copy operations, or move operations by using RAII types such as standard library containers and smart pointers."
    },
    {
        "question": "What is a move constructor?",
        "expected_answer": "A move constructor transfers resources from a temporary or expiring object instead of making a deep copy."
    },
    {
        "question": "What is a move assignment operator?",
        "expected_answer": "A move assignment operator transfers resources from an existing temporary or expiring object to another existing object."
    },
    {
        "question": "What is move semantics?",
        "expected_answer": "Move semantics allows resources to be transferred from temporary or expiring objects instead of unnecessarily copying them."
    },
    {
        "question": "What is an rvalue reference?",
        "expected_answer": "An rvalue reference, written using &&, can bind to temporary or expiring objects and is commonly used to implement move semantics."
    },
    {
        "question": "What does std::move() do?",
        "expected_answer": "std::move() converts an expression into an xvalue, allowing move operations to be selected when supported. It does not itself move any data."
    },
    {
        "question": "What is a smart pointer and why is it useful?",
        "expected_answer": "A smart pointer manages dynamically allocated resources automatically according to ownership rules, reducing memory leaks and manual delete operations."
    },
    {
        "question": "What is the difference between unique_ptr and shared_ptr?",
        "expected_answer": "unique_ptr provides exclusive ownership of an object, while shared_ptr allows multiple owners using reference counting."
    },
    {
        "question": "What is weak_ptr?",
        "expected_answer": "weak_ptr is a non-owning smart pointer that observes an object managed by shared_ptr without increasing its reference count."
    },
    {
        "question": "Why can shared_ptr cause a memory leak?",
        "expected_answer": "A reference cycle between shared_ptr objects can keep their reference counts nonzero, preventing the objects from being destroyed."
    },
    {
        "question": "How does weak_ptr help prevent shared_ptr cycles?",
        "expected_answer": "weak_ptr does not increase the shared ownership count, so it can break ownership cycles between objects managed by shared_ptr."
    },
    {
        "question": "What is a dangling reference?",
        "expected_answer": "A dangling reference occurs when a reference continues to refer to an object whose lifetime has ended."
    },
    {
        "question": "What is a memory leak in C++?",
        "expected_answer": "A memory leak occurs when dynamically allocated memory is no longer accessible or needed but is not released."
    },
    {
        "question": "What is RAII and why is it important?",
        "expected_answer": "RAII binds resource management to object lifetime, ensuring resources such as memory, files, and locks are released automatically when objects are destroyed."
    },
    {
        "question": "What is exception safety in C++?",
        "expected_answer": "Exception safety describes guarantees that code provides when exceptions occur, such as no guarantee, basic guarantee, strong guarantee, or nothrow guarantee."
    },
    {
        "question": "What is the strong exception guarantee?",
        "expected_answer": "The strong exception guarantee means that if an operation fails, the program state remains unchanged as if the operation had never occurred."
    },
    {
        "question": "What is the noexcept specifier?",
        "expected_answer": "noexcept specifies that a function is not expected to throw exceptions and can enable certain compiler optimizations and move operations."
    },
    {
        "question": "What is template specialization?",
        "expected_answer": "Template specialization allows a programmer to provide a specific implementation of a template for a particular type or set of template arguments."
    },
    {
        "question": "What is partial template specialization?",
        "expected_answer": "Partial template specialization provides a specialized implementation for a subset or pattern of template arguments and is primarily used with class templates."
    },
    {
        "question": "What is SFINAE in C++?",
        "expected_answer": "SFINAE means Substitution Failure Is Not An Error. It allows invalid template substitutions to remove candidates from overload resolution instead of producing an immediate compilation error."
    },
    {
        "question": "What are variadic templates?",
        "expected_answer": "Variadic templates allow a function or class template to accept a variable number of template arguments."
    },
    {
        "question": "What is lambda expression in C++?",
        "expected_answer": "A lambda expression is an anonymous function object that can be defined directly where it is needed."
    },
    {
        "question": "What is a lambda capture list?",
        "expected_answer": "A lambda capture list specifies which variables from the surrounding scope are captured and whether they are captured by value or reference."
    },
    {
        "question": "What is perfect forwarding?",
        "expected_answer": "Perfect forwarding preserves the value category of function arguments when passing them to another function, commonly using forwarding references and std::forward()."
    },
    {
        "question": "What is std::forward()?",
        "expected_answer": "std::forward() conditionally casts a forwarding reference so that the original value category of an argument is preserved."
    },
    {
        "question": "What is const correctness?",
        "expected_answer": "Const correctness means using const appropriately to prevent unintended modification of data and to clearly communicate which functions and objects do not modify state."
    },
    {
        "question": "What is a const member function?",
        "expected_answer": "A const member function promises not to modify the observable state of the object through the implicit this pointer."
    },
    {
        "question": "What is a mutable data member?",
        "expected_answer": "A mutable data member can be modified even inside a const member function."
    },
    {
        "question": "What is the difference between stack and heap memory in C++?",
        "expected_answer": "Stack memory is commonly used for automatic storage such as local variables, while dynamically allocated objects generally use heap or free-store memory."
    },
    {
        "question": "What is undefined behavior in C++?",
        "expected_answer": "Undefined behavior occurs when a program performs an operation for which the C++ standard imposes no requirements, allowing unpredictable results."
    },
    {
        "question": "What is the difference between compile-time and runtime errors?",
        "expected_answer": "Compile-time errors are detected while translating the program, while runtime errors occur during program execution."
    },
    {
        "question": "What is an iterator invalidation?",
        "expected_answer": "Iterator invalidation occurs when an operation on a container makes an existing iterator, pointer, or reference no longer valid."
    },
    {
        "question": "Why can inserting into a vector invalidate iterators?",
        "expected_answer": "If insertion causes a vector to reallocate its storage, existing iterators, pointers, and references to its elements may become invalid."
    },
    {
        "question": "What is the difference between vector and list?",
        "expected_answer": "vector stores elements contiguously and provides fast random access, while list uses linked nodes and provides efficient insertion and removal at known positions but no constant-time random access."
    },
    {
        "question": "What is the difference between map and unordered_map?",
        "expected_answer": "map typically stores elements in sorted key order using a tree-based structure, while unordered_map uses hashing and provides average constant-time lookup."
    },
    {
        "question": "What is the difference between emplace_back() and push_back()?",
        "expected_answer": "push_back() inserts an existing object or temporary object, while emplace_back() constructs the object directly in the container using the provided arguments."
    }

    ]

}
