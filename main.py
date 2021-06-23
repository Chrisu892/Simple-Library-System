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
      1: self.manage_books,
      2: self.manage_users,
      3: self.manage_loans,
      4: self.quit
    }

    print("\nWELCOME TO THE LIBRARY SYSTEM")

    while True:
      try:
        print("\nWhat would you like to do?")
        print("1. Manage Books")
        print("2. Manage Users")
        print("3. Manage Loans")
        print("4. Exit Program\n")

        selection = int(input(f"Please select [1,2,3,4]: "))

        if selection not in range(1,5):
          raise ValueError
        else:
          menu[selection]()

      except ValueError:
        print("\nSelection out of range, please try again.\n")


  def manage_books(self):
    """Public method show the Library book collection management menu."""

    menu = {
      1: self.book_list.add_book,
      2: self.book_list.remove_book,
      3: self.book_list.find_book,
      4: self.book_list.num_books,
      5: self.start,
    }

    print("\nMANAGE BOOKS")

    while True:
      try:
        print("\nWhat would you like to do?")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Find a book")
        print("4. Number of books")
        print("5. Go back\n")

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
      3: self.user_list.find_user,
      4: self.user_list.show_users,
      5: self.start
    }

    print("\nMANAGE USERS")

    while True:
      try:
        print("\nWhat would you like to do?")
        print("1. Add a user")
        print("2. Remove a user")
        print("3. Find a user")
        print("4. Show all users")
        print("5. Go back\n")

        selection = int(input("Please select [1,2,3,4,5]: "))

        if selection not in range(1,6):
          raise ValueError
        else:
          menu[selection]()

      except ValueError:
        print("Selection out of range, please try again.")


  def manage_loans(self):
    """Public method to show the Library loans management menu."""

    menu = {
      1: self.loans.lend_book,
      2: self.loans.return_book,
      3: self.loans.show_all_loans,
      4: self.loans.show_borrower_details,
      5: self.start
    }

    print("\nMANAGE BOOK LOANS")

    while True:
      try:
        print("\nWhat would you like to do?")
        # Lend a book to the borrower
        print("1. Lend a book")
        # Return a book to the library
        print("2. Return a book")
        # Show count of the total number of books a user is currently borrowing
        print("3. Show user's loans")
        # Show all the overdue books along with the users’ username and firstname
        print("4. Show all loans")
        # Show the firstname, surname and email address name of a borrower of a given book
        print("5. Show borrower details")
        # Go back to the main menu
        print("6. Go back\n")

        # Prompt the user to select 1 of the 6 options
        selection = int(input(f"Please select [1,2,3,4,5]: "))

        if selection not in range(1,6):
          raise ValueError

        else:
          if selection in [1,2]:
            # If lending or returning books
            menu[selection](self.user_list, self.book_list)

          elif selection in [3,4]:
            # If showing user's loans and overdue books
            menu[selection](self.user_list)

          elif selection in [5]:
            # If showing book's borrower details
            menu[selection](self.book_list)

          else:
            # If going back to the main menu
            menu[selection]()


      except:
        print("\nSelection out of range, please try again.")


  def quit(self):
    """Method to quit the program."""
    sys.exit()


if __name__ == '__main__':
  # Instantiate the Library interface class
  Library()