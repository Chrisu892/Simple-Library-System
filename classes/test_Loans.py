from .Loans import Loans
from .UserList import UserList
from .BookList import BookList
from .User import User
from .Book import Book


class Test_Loans:


  def test_lend_book(self):

    loans = Loans()
    book = Book()
    user = User()
    book_list = BookList()
    user_list = UserList()

    assert loans.lend_book() == False

    book.create_book({
      "title": "Sapiens",
      "author": "Yuval Noah Harari",
      "year": 2015,
      "publisher_name": "Vintage",
      "publication_date": "01/01/2015",
      "num_copies": 10
    })
    assert book.get('title') == 'Sapiens'

    book_list.add_book(book)
    assert book_list.count() > 0

    user.create_user({
      "username": "Ayesha123",
      "first_name": "Ayesha",
      "last_name": "Bahadur",
      "dob": "22/10/1994",
      "house_no": 12,
      "street_name": "Trafalgar Street",
      "postcode": "NE1 2LA",
      "email_address": "ayesha@email.com"
    })
    assert user.get_full_name() == 'Ayesha Bahadur'

    user_list.add_new_user(user)
    assert user_list.count() > 0
    
    for user in user_list.show_all():
      assert user.get("username") == "Ayesha123"

    loans.lend_book(user_list, book_list, "Ayesha123", "Sapiens")
    assert loans.count() > 0
    assert loans.show_all_loans() == True
