class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrow = False
    def get_info(self):
        st = 'borrowed' if self.is_borrow else "not borrowed"
        return f"{self.title} by {self.author} ({self.pages} pages) ({st})"
    
    
    def borrow(self):
        self.is_borrow = True
        print(f"{self.title} is borrowed successfully.")

    def return_book(self):
        self.is_borrow = False
        print(f"{self.title} is returned successfully.")

book_1 = Book("Atomic Habits","James clear",300)
book_2 = Book("The art of being alone", "niploean",200)
book_3 = Book("The Great Gatsby","F. Scott Fitzgerald",200)

ls = [book_1,book_2,book_3]

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.extend(book)
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                print(f"Borrowed: '{title}'")
                return 
        print(f"'{title}' not in library")

    def list_books(self):
        for book in self.books:
            print(book.get_info())

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"{title} is not found in library")
l = Library()
l.add_book(ls)
l.borrow_book("Atomic Habits")
l.list_books()  # Check if status changed to "borrowed"!
l.borrow_book("Nonexistent Book")  # Should show "not in library"