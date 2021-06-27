from .Book import Book


class Test_Book:


  def test_create_book(self):
    """Method to test creation of a new book."""

    first_book = Book()

    details = {
      "title": "Sapiens",
      "author": "Yuval Noah Harari",
      "year": 2015,
      "publisher_name": "Vintage",
      "publication_date": "01/01/2015",
      "num_copies": 10
    }

    assert first_book.create_book(details) == True
    assert first_book.get("title") == "Sapiens"
    assert first_book.get("publication_date") == "01/01/2015"


  def test_update_book(self):
    """Method to test updating of the book."""

    first_book = Book()

    details = {
      "title": "Sapiens",
      "author": "Yuval Noah Harari",
      "year": 2015,
      "publisher_name": "Vintage",
      "publication_date": "03/04/2015",
      "num_copies": 3
    }

    first_book.create_book(details)

    assert first_book.update_book(details) == True
    assert first_book.get("num_copies") == 3
    assert first_book.set("num_copies", 10)
    assert first_book.get("num_copies") == 10