# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes the book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when an instance is deleted, prints a message."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: Used with print() or str(), returns a readable description."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: Used with repr(), returns a string to recreate the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
