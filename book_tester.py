

class Book:
    """
    A class representing a book in a library
    """
    def __init__(self, title_param:str, checked_out_param: bool = False) -> None:
        """
        sets up attributes for a book instance
        """
        self.title = title_param
        self.checked_out = checked_out_param

    def __str__(self):
        """
        returns string representation of a book
        """
        str_rep = f"{self.title} is checked out: {self.checked_out}"
        return str_rep

    def check_out(self) -> None:
        if self.checked_out:
            print(f"{self.title} is already checked out")
        else:
            self.checked_out = True

    def __eq__(self, other) -> bool:
        print(f"checking equality between {self.title} and {other.title}")
        return self.title == other.title
# Task:
# 1. Add a method for check_out()
# 
# 2. Let’s make a list of Books called book_shelf. Fill it with data for a few books. 
#   - What is the type hint for book_shelf?
#   - Iterate over the list, check each book out, and print each book.

# 3. Compare book_shelf[0] to b1 using the == operator and again using the is keyword. What are the results? Make a copy of b1 and compare it to b1 again using == and is. Do these results make sense?


b1 = Book("The Circle")
print(b1)
print(b1.title)
print(b1.checked_out)
b2 = Book("The Martian")
print(b2)

book_shelf:list[Book] = [b1, b2, Book("Project Hail Mary", True), Book("The Hobbit")]
print("Book shelf")
for book in book_shelf:
    book.check_out()
    print(book)



b1_2 = Book("The Circle")
b1_2.check_out()
print(b1)
print(b1_2)
print(f"b1 == book_shelf[0]: {b1 == book_shelf[0]}")
print(f"b1 == b1_2: {b1 == b1_2}")

print(f"b1 is book_shelf[0]: {b1 is book_shelf[0]}")
print(f"b1 is b1_2: {b1 is b1_2}")
print(b1 == b2)