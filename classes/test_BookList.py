from .BookList import BookList
from .Book import Book


class Test_BookList:


  def test_add_book(self):
    """Method to test addition of book to the collection."""

    first_book_list = BookList()
    first_book = Book()

    first_book.create_book({
      "title": "First Man",
      "author": "James R. Hansen",
      "year": 2005,
      "publisher_name": "Simon & Schuster",
      "publication_date": "01/01/2018",
      "num_copies": 1
    })

    assert first_book_list.add_book(first_book)
    assert first_book_list.find_book("First Man")
    assert first_book_list.num_books() == 1


  def test_update_book_details(self):
    """Method to test updating of the book details in the collection."""

    first_book_list = BookList()
    first_book = Book()

    first_book.create_book({
      "title": "First Man",
      "author": "James R. Hansen",
      "year": 2005,
      "publisher_name": "Simon & Schuster",
      "publication_date": "01/01/2018",
      "num_copies": 1
    })

    first_book_list.add_book(first_book)

    new_book_details = {
      "title": "First Man",
      "author": "James Hansen",
      "year": 2018,
      "publisher_name": "Simon & Schuster",
      "publication_date": "01/01/2018",
      "num_copies": 5
    }

    assert first_book_list.update_book_details(new_book_details) == True
    assert first_book_list.find_book("First Man") == True

    for book in first_book_list.show_all():
      assert book.get("title") == "First Man"
      assert book.set("title", "First Man: The Life of Neil A. Armstrong") == True

    assert first_book_list.find_book("First Man: The Life of Neil A. Armstrong") == True


  def test_remove_book(self):
    """Method to test removal of the book from the collection."""

    first_book_list = BookList()
    first_book = Book()

    first_book.create_book({
      "title": "First Man",
      "author": "James R. Hansen",
      "year": 2005,
      "publisher_name": "Simon & Schuster",
      "publication_date": "01/01/2018",
      "num_copies": 1
    })

    first_book_list.add_book(first_book)

    assert first_book_list.remove("title", "First Man") == True
    assert first_book_list.count() == 0



