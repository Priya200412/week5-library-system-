import json
import os
from .book import Book
from .member import Member
# project root folder (week5-library-system)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
BOOK_FILE = os.path.join(DATA_DIR, "books.json")
MEMBER_FILE = os.path.join(DATA_DIR, "members.json")


class Library:
    def __init__(self):
        self.books = {}     # isbn -> Book
        self.members = {}   # member_id -> Member
        self.load_data()
    def add_book(self, book):
        self.books[book.isbn] = book

    def find_book(self, isbn):
        return self.books.get(isbn)
    def register_member(self, member):
        self.members[member.member_id] = member

    def find_member(self, member_id):
        return self.members.get(member_id)
    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if not member or not book:
            return "Invalid member ID or book ISBN"
        if not book.available:
            return "Book is already borrowed"
        success, msg = member.borrow_book(isbn)
        if not success:
            return msg
        book.check_out(member_id)
        return "Book borrowed successfully"
    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if not member or not book:
            return "Invalid member ID or book ISBN"
        success, _ = member.return_book(isbn)
        if not success:
            return "This member did not borrow this book"
        book.return_book()
        return "Book returned successfully"
    def search_books(self, keyword):
        keyword = keyword.lower()
        return [
            book for book in self.books.values()
            if keyword in book.title.lower()
            or keyword in book.author.lower()
            or keyword == book.isbn
        ]
    def save_data(self):
        os.makedirs(DATA_DIR, exist_ok=True)

        with open(BOOK_FILE, "w") as f:
            json.dump(
                {isbn: book.to_dict() for isbn, book in self.books.items()},
                f,
                indent=4
            )
        with open(MEMBER_FILE, "w") as f:
            json.dump(
                {mid: member.to_dict() for mid, member in self.members.items()},
                f,
                indent=4
            )
    def load_data(self):
        # Load books
        if os.path.exists(BOOK_FILE):
            try:
                with open(BOOK_FILE, "r") as f:
                    content = f.read().strip()
                    if content:
                        data = json.loads(content)
                        for isbn, book_data in data.items():
                            self.books[isbn] = Book.from_dict(book_data)
            except json.JSONDecodeError:
                print("Warning: books.json is empty or corrupted.")
        if os.path.exists(MEMBER_FILE):
            try:
                with open(MEMBER_FILE, "r") as f:
                    content = f.read().strip()
                    if content:
                        data = json.loads(content)
                        for mid, member_data in data.items():
                            self.members[mid] = Member.from_dict(member_data)
            except json.JSONDecodeError:
                print("Warning: members.json is empty or corrupted.")
