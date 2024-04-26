import pytest 
from book import Book

@pytest.mark.parametrize("title, isbn", [
    ("Harry Potter", "55555-55555-550"),
    ("Big Bang Theory", "111111-1111-000"),
    ("Great", "978-3-16-148410-0"),
    ("Boekje", "978-1779501127")
])

def test_valid_creation(title,isbn):
    book = Book(title,isbn)
    assert book.title == title
    assert book.isbn == isbn
    
@pytest.mark.parametrize("title,isbn, exceptionclass",[
    (None, "55555-55555-550",RuntimeError),
    ("", "111111-1111-000",RuntimeError)
])

def test_creation_with_invalid_title(title,isbn,exceptionclass):
    
    with pytest.raises(exceptionclass):
        Book(title,isbn)
    

@pytest.mark.parametrize("title,isbn,exceptionclass",[
    ("Harry Potter", "55452555-55555-550", RuntimeError),
    ("Big Bang Theory", "111111-1011-000", RuntimeError),
    ("Great", "72465-58291-370", RuntimeError),
    ("Boekje", "978-1779504527", RuntimeError)
])

def test_creation_with_invalid_isbn(title,isbn,exceptionclass):
    with pytest.raises(exceptionclass):
        Book(title,isbn)