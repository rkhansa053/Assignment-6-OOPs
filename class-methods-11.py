class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1 

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

book1 = Book("The prisoner of Zenda", "Anthony Hope")
book2 = Book("David Copperfield" , "Charles Dickens")

print(f"Total books: {Book.total_books}")
