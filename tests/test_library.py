from library_system.library import Library
from library_system.book import Book
from library_system.member import Member
def test_library_borrow_return():
    lib = Library()
    book = Book("Test Book", "Author", "111")
    member = Member("John", "M001")
    lib.add_book(book)
    lib.register_member(member)
    result = lib.borrow_book("M001", "111")
    assert "Due date" in result
    result = lib.return_book("M001", "111")
    assert "Returned" in result
