from datetime import datetime, timedelta
class Book:
    def __init__(self, title, author, isbn, year=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True
        self.borrowed_by = None
        self.due_date = None
    def check_out(self, member_id, loan_period=14):
        if not self.available:
            return False, "Book already borrowed"
        self.available = False
        self.borrowed_by = member_id
        self.due_date = (datetime.now() + timedelta(days=loan_period)).strftime('%Y-%m-%d')
        return True, f"Book borrowed. Due date: {self.due_date}"
    def return_book(self):
        overdue = self.is_overdue()
        self.available = True
        self.borrowed_by = None
        self.due_date = None
        return overdue
    def is_overdue(self):
        if self.due_date:
            return datetime.now() > datetime.strptime(self.due_date, '%Y-%m-%d')
        return False
    def to_dict(self):
        return self.__dict__
    @classmethod
    def from_dict(cls, data):
        book = cls(data['title'], data['author'], data['isbn'], data.get('year'))
        book.available = data['available']
        book.borrowed_by = data['borrowed_by']
        book.due_date = data['due_date']
        return book
    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrowed_by}"
        return f"{self.title} | {self.author} | {self.isbn} | {status}"
