from library_system.member import Member
def test_member_borrow_limit():
    member = Member("Test User", "M001")
    for i in range(5):
        assert member.borrow_book(str(i)) is True
    assert member.borrow_book("6") is False
