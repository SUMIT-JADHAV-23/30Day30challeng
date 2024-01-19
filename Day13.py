"""task
Given a Book class and a Solution class, write a MyBook class that does the following:
Inherits from Book
Has a parameterized constructor taking these 3 parameters:
1.string title
2.string author
3.int price 
Implements the Book class' abstract display() method so it prints these  lines:
1.title:, a space, and then the current instance's titel.
2.author:, a space, and then the current instance's author.
3.price:, a space, and then the current instance's price.
Note: Because these classes are being written in the same file, you must not use an access modifier (e.g.:public) when declaring MyBook or your code will not execute.

Input Format
You are not responsible for reading any input from stdin. The Solution class creates a Book object and calls the MyBook class constructor (passing it the necessary arguments).
It then calls the display method on the Book object.

Output Format
The display() method should print and label the respective title,author, and price of the MyBook object's instance (with each value on its own line) like so:
Title: $title
Author: $author
Price: $price
Note: The  is prepended to variable names to indicate they are placeholders for variables.

Sample Input
The following input from stdin is handled by the locked stub code in your editor:
The Alchemist
Paulo Coelho
248
Sample Output
The following output is printed by your display() method:
Title: The Alchemist
Author: Paulo Coelho
Price: 248

@abstractmethod
It seems like you are referring to the @abstractmethod decorator. This decorator is used to define abstract methods in abstract base classes (ABCs) in Python. 
An abstract method is a method that is declared in the abstract class but doesn't provide an implementation. 
Subclasses are required to provide their own implementation for these abstract methods.
"""

# from abc import ABCMeta, abstractmethod

# class Book(object, metaclass=ABCMeta):
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     @abstractmethod
#     def display(self):
#         pass

# class MyBook(Book):
#     def __init__(self, title, author, price):
#         super().__init__(title, author)  # Call the superclass constructor
#         self.price = price

#     def display(self):
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Price:", self.price)

# # Write MyBook class

# title = input("Enter title: ")
# author = input("Enter author: ")
# price = int(input("Enter price: "))
# new_novel = MyBook(title, author, price)
# new_novel.display()


class Student:
    # constructor
    # initialize instance variable
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('All variables initialized')
    # instance Method
    def show(self):
        print('Hello, my name is', self.name)
# create object using constructor
s1 = Student('Emma')
s1.show()