# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading '{self.title}' by {self.author}...")

    def info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

# Add an inheritance layer to explore polymorphism or encapsulation.
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def read(self):
        print(f"Reading '{self.title}' (eBook) by {self.author}... File size: {self.file_size}MB")


# Activity 2: Polymorphism Challenge! 🎭
# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() 
# prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Animal:
    def move(self):
        print("The animal moves.")

class Dog(Animal):
    def move(self):
        print("The dog runs. 🐶")

class Cat(Animal):
    def move(self):
        print("The cat jumps. 🐱")

# Create instances of each class and call their move() methods.
book = Book("1984", "George Orwell", 328)
ebook = EBook("Brave New World", "Aldous Huxley", 268, 1.5)
dog = Dog()
cat = Cat()

book.read()
print(book.info())
ebook.read()
print(ebook.info())
dog.move()
cat.move()
