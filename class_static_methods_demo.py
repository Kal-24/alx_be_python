
Back-End Web Development
Average: 67.19%
More about OOP
 Novice
 Weight: 1
 Project will start Aug 4, 2025 12:00 AM, must end by Aug 11, 2025 12:00 AM
 Checker was released at Aug 4, 2025 12:00 AM
 An auto review will be launched at the deadline


This project dives deeper into the world of Object-Oriented Programming (OOP) in Python.

You’ll explore advanced concepts like constructors, destructors, magic methods, inheritance, composition, polymorphism, and more.

Project Objectives:
By the end of this project, you should be able to:

Describe the functionalities of constructors (__init__), destructors (__del__), and common magic methods (e.g., __str__, __repr__) in Python classes.
Implement inheritance to create new classes that inherit properties and methods from existing classes.
Utilize composition as an alternative to inheritance for building complex objects.
Explain the concepts of single, multiple, and multilevel inheritance in Python.
Understand the method resolution order (MRO) in Python and how it affects method calls in inheritance hierarchies.
Implement polymorphism and method overriding to create flexible and reusable code.
Explain and use Python’s duck typing to achieve polymorphic behavior.
Distinguish between class methods and static methods based on their usage and purpose.
Apply @classmethod and @staticmethod decorators appropriately in your Python classes.
This project will equip you with a comprehensive understanding of advanced OOP concepts in Python, enabling you to design and build robust and maintainable object-oriented applications.

Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Dive into Python Magic Methods
mandatory
Objective: Master Python magic methods by implementing a Book class that incorporates constructors (__init__), destructors (__del__), and the representation methods (__str__ and __repr__).

Task Description:
Create a Python script named book_class.py. In this script, define a Book class that uses specific magic methods to enhance its functionality. This class will model a book with attributes for the title, author, and publication year.

Requirements for Book Class in book_class.py:
Attributes:

title (str): The title of the book.
author (str): The author of the book.
year (int): The publication year of the book.
Magic Methods:

Constructor (__init__): Initializes a Book instance with title, author, and year.
Destructor (__del__): Prints "Deleting (title of the book)" upon object deletion.
String Representation (__str__): Returns a string in the format "(title) by (author), published in (year)".
Official Representation (__repr__): Returns a string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})".
Provided for Testing: main.py
To test your Book class, use the following main.py script, which demonstrates creating a Book instance and utilizing the implemented magic methods:

from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
Expected Output:
1984 by George Orwell, published in 1949
Book('1984', 'George Orwell', 1949)
Deleting 1984
Repo:

GitHub repository: alx_be_python
Directory: oop
File: book_class.py
 
1. Mastering Inheritance and Composition in Python
mandatory
Objective: Deepen your understanding of inheritance and composition in Python by creating a system that models a library with different types of books.

Task Description:
Develop two Python scripts: library_system.py and main.py. In library_system.py, you’ll define a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance. Additionally, implement a Library class demonstrating composition by managing a collection of books.

library_system.py:
Base Class - Book:

Attributes: title (str) and author (str).
Method: __init__(self, title, author) for initializing book attributes.
Derived Classes - EBook and PrintBook:

Both classes inherit from Book.
EBook additional attribute: file_size (int).
PrintBook additional attribute: page_count (int).
Each derived class should have its own __init__ method that properly calls the base class __init__ while also initializing its unique attribute.
Composition - Library:

Attributes: books (a list to store instances of Book, EBook, and PrintBook).
Methods:
add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
list_books(self): Prints details of each book in the library.
main.py (Provided for Testing):
This script tests the functionality of your classes in library_system.py by adding different types of books to a Library instance and listing them.

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
Expected Output:
Your output should list the details of each book added to the library, reflecting the specific attributes of EBook and PrintBook, as well as the common attributes inherited from Book.

Book: Pride and Prejudice by Jane Austen
EBook: Snow Crash by Neal Stephenson, File Size: 500KB
PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234
Repo:

GitHub repository: alx_be_python
Directory: oop
File: library_system.py
2. Exploring Polymorphism and Method Overriding
mandatory
Objective: Enhance your understanding of polymorphism in Python by creating a set of classes that demonstrate method overriding and polymorphic behavior.

Task Description:
You are tasked with creating a Python script named polymorphism_demo.py. In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, each overriding the area() method to calculate their respective areas.

polymorphism_demo.py:
Base Class - Shape:

Method: area(self), which simply raises a NotImplementedError, indicating that derived classes need to override this method.
Derived Class - Rectangle:

Inherits from Shape.
Attributes: length and width.
Overrides the area() method to calculate the rectangle’s area using the formula: length × width.
Derived Class - Circle:

Inherits from Shape.
Attributes: radius.
Overrides the area() method to calculate the circle’s area using the formula: π × radius² (use math.pi for π).
main.py (Provided for Testing):
This script demonstrates polymorphism by creating instances of Rectangle and Circle, invoking their area() method, and showing that each class calculates the area according to its shape.

from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
Expected Output:
When you run main.py, the output should reflect the areas of the different shapes, showcasing polymorphism through method overriding.

The area of the Rectangle is: 50
The area of the Circle is: 153.93804002589985
Note for you:
Ensure your derived classes Rectangle and Circle correctly override the area method from the Shape base class. This is key to demonstrating polymorphism.
The NotImplementedError in the base area method serves as a reminder that this method is expected to be overridden in any subclass of Shape.
Through this task, you’ll see how different objects can be treated uniformly, yet behave differently based on their respective class implementations—a core concept of polymorphism.
Repo:

GitHub repository: alx_be_python
Directory: oop
File: polymorphism_demo.py
3. Distinguishing Between Class Methods and Static Methods
mandatory
Objective: Solidify your understanding of class methods and static methods in Python by implementing examples of each in a class, demonstrating their usage and differences.

Task Description:
Create a Python script named class_static_methods_demo.py. In this script, define a class Calculator that includes both a class method and a static method to perform calculations. This task aims to illustrate when and how to use @classmethod and @staticmethod decorators, highlighting their differences and practical applications.

class_static_methods_demo.py:
Calculator Class:

Static Method - add(a, b): Returns the sum of two numbers. Use the @staticmethod decorator.
Class Method - multiply(cls, a, b): Returns the product of two numbers. Use the @classmethod decorator and ensure it prints a class attribute named calculation_type before performing the multiplication.
Class Attribute:

Define a class attribute calculation_type with a value of "Arithmetic Operations" that the multiply class method will reference.
Implementation Example:
class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
main.py (Provided for Testing):
This script will test the Calculator class’s static and class methods, demonstrating their functionality and how they are called.

from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
Expected Output:
When you run main.py, it should produce the following output, which includes the printed message from the class method and the results of the calculations:

The sum is: 15
Calculation type: Arithmetic Operations
The product is: 50
Note for you:
Understand the use of @staticmethod for functions that perform a task in isolation, without needing access to class or instance-specific data.
Grasp the concept of @classmethod for functions that need to access class attributes or methods and understand how the cls parameter allows access to class-level attributes.
This task underscores the distinction between class methods and static methods in Python, providing clarity on their appropriate use cases and advantages.
