class Book:
    def __init__(self, title, auther):
        self.title = title
        self.auther = auther
class Library:
    def __init__(self):
        self.book = []
        self.issued_book = []
    def add_book(self, name):
        if isinstance(name, list):
            self.book.extend(name)
        else:
            self.book.append(name)
        print(f"{self.book} is added to library")
    def issue_book(self,book):
        if book in self.issued_book:
            print("book already issued")
            return (self.issued_book, self.book)
        if book not in self.book:
            print("book is not available in library")
            return (self.issued_book, self.book)
        self.issued_book.append(book)
        self.book.remove(book)
        return (self.issued_book, self.book)
    def return_book(self, book):
        if book not in self.issued_book:
            print("book was not issued")
            return (self.issued_book, self.book)
        self.issued_book.remove(book)
        self.book.append(book)
        return (self.issued_book, self.book)

ls_books = ["python basics","Ml basics", "Deep learning basics"]
li = Library()
li.add_book(ls_books)
print(li.issue_book("Ml basics"))
