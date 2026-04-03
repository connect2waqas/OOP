class Book:
    def __init__(self, title, auther):
        self.title = title
        self.auther = title

class Library:
    def __init__(self):
        self.all_book_with_authers = {}
        self.all_books = []
        self.authers = []
        self.all_issued_books = []
        # for i in range(len(self.all_books)):
        #     self.all_book_with_authers[self.all_books[i]] = self.authers[i]
        for book , auther in zip(self.all_books, self.authers):
            self.all_book_with_authers[book] = auther

    def adding_books(self,books, auther):
        self.all_books.extend(books)
        self.authers.extend(auther)
        print(f"{books} is added!")
        print("all auther is added")


    def check_book_avilable(self, book, auther):
       return True if self.all_book_with_authers.get(book) == auther else False
    
    def issuing_book(self, book, auther):
        if self.check_book_avilable(book, auther):
            print(f"{book} is avialable and issued now!")
            self.all_issued_books.append(book)
        else:
            print(f"{book} with such auther {auther} is not avialable")
    def returning_book(self, book):
        self.all_books.extend(book)
b_1 = Book("Python basics","Waqas")
b_2 = Book("ML basics","Waqas")

l = Library()
l.adding_books(["python","ml","dp","nlp"],["waqas","bashir","ilyas","abbas"])
print(l.all_books)
print(l.authers)
print(l.all_book_with_authers)
print(l.issuing_book("python","waqas"))