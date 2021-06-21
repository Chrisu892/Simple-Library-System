# Import required modules
from classes.BookList import BookList
from classes.UserList import UserList
from classes.Loans import Loans
import sys


# Define the Library interface class
class Library:


  def __init__(self):
    """Library class constructor."""

    self.book_list = BookList()
    self.user_list = UserList()
    self.loans = Loans()

    self.start()


  def start(self):
    """Public method to show the main program menu."""
    menu = {
      1: self.manage_collections,
      2: self.manage_loans,
      3: self.quit
    }

    print()
    print("WELCOME TO THE LIBRARY SYSTEM")

    while True:
      try:
        print("What would you like to do?")
        print("1. Manage Books")
        print("2. Manage Loans")
        print("3. Exit Program")
        print() 

        selection = int(input(f"Please select [1,2,3]: "))

        if selection not in range(1,4):
          raise ValueError
        else:
          menu[selection]()

      except ValueError:
        print("\nSelection out of range, please try again.\n")


  def manage_collections(self):
    """Public method show the Library book collection management menu."""

    menu = {
      1: self.book_list.add_book,
      2: self.book_list.remove_book,
      3: self.book_list.find_book,
      4: self.book_list.num_books,
      5: self.start,
    }

    print()
    print("MANAGE BOOKS")

    while True:
      try:
        print("What would you like to do?")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Find a book")
        print("4. Number of books")
        print("5. Go back")
        print()

        selection = int(input(f"Please select [1,2,3,4,5]: "))

        if selection not in range(1,6):
          raise ValueError
        else:
          menu[selection]()

      except ValueError:
        print("Selection out of range, please try again.")


  def manage_users(self):
    """Public method to show the Library users management menu."""

    menu = {
      1: self.user_list.add_user,
      2: self.user_list.remove_user,
      3: self.find_user,
      4: self.show_users,
      5: self.start
    }



  def manage_loans(self):
    """Public method to show the Library loans management menu."""

    menu = {
      1: self.loans.lend_book,
      2: self.loans.return_book,
      3: self.loans.show_borrowed_books,
      4: self.loans.return_overdue_books,
      5: self.loans.show_borrower_details,
      6: self.start
    }

    print()
    print("MANAGE BOOK LOANS")

    while True:
      try:
        print("What would you like to do?")
        print("1. Lend a book")
        print("2. Return a book")
        print("3. Show all books on loan")
        print("4. Return user's overdue books")
        print("5. Show user details")
        print("6. Go back")
        print()

        selection = int(input(f"Please select [1,2,3,4,5,6]: "))

        if selection not in range(1,7):
          raise ValueError
        else:
          menu[selection](self.user_list.find_id_by("username"), self.book_list.find_id_by("title"))

      except ValueError:
        print("Selection out of range, please try again.")

      except TypeError:
        print("Missing user_id and book_id!")


  def quit(self):
    """Method to quit the program."""
    sys.exit()


if __name__ == '__main__':
  # Instantiate the Library interface class
  Library()