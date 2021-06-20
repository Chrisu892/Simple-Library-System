# Import required modules
from classes.BookList import BookList
from classes.UserList import UserList
from classes.Loans import Loans
import sys


# Define the Library interface class
class Library:


  # Define the class constructor
  def __init__(self):
    self.book_list = BookList()
    self.user_list = UserList()
    self.loans = Loans()
    self.start()


  # Method to show the main menu
  def start(self):
    menu = {
      1: self.manage_collections,
      2: self.manage_loans,
      3: self.quit
    }

    print("-----------------------------")
    print("WELCOME TO THE LIBRARY SYSTEM")

    while True:
      try:
        print("What would you like to do?")
        for key, action in menu.items():
          print(f"{key}: {action.__name__.replace('_', ' ')}")
        print("-----------------------------") 

        selection = int(input(f"Please select {list(menu.keys())}: "))

        if selection not in range(1, len(menu) + 1):
          raise ValueError
        else:
          menu[selection]()

      except ValueError:
        print("Selection out of range, please try again.")


  # Method to show manage collections menu
  def manage_collections(self):
    menu = {
      1: self.book_list.add_book,
      2: self.book_list.remove_book,
      3: self.book_list.find_book,
      4: self.book_list.num_books,
      5: self.start,
    }

    print("-----------------------------")
    print("MANAGE BOOKS")

    while True:
      try:
        print("What would you like to do?")
        for key, action in menu.items():
          print(f"{key}: {action.__name__.replace('_', ' ')}")
        print("-----------------------------")

        selection = int(input(f"Please select {list(menu.keys())}: "))

        if selection not in range(1, len(menu) + 1):
          raise ValueError
        else:
          menu[selection]()

      except ValueError:
        print("Selection out of range, please try again.")


  # Method to show the manage loans menu
  def manage_loans(self):
    menu = {
      1: self.loans.lend_book,
      2: self.loans.return_book,
      3: self.loans.show_borrowed_books,
      4: self.loans.return_overdue_books,
      5: self.loans.show_borrower_details,
      6: self.start
    }

    print("-----------------------------")
    print("MANAGE BOOK LOANS")

    while True:
      try:
        print(f"There are {self.loans.count()} active loans.")
        print("What would you like to do?")

        for key, action in menu.items():
          print(f"{key}: {action.__name__.replace('_', ' ')}")

        print("-----------------------------")

        selection = int(input(f"Please select {list(menu.keys())}: "))

        if selection not in range(1, len(menu) + 1):
          raise ValueError
        else:
          menu[selection]()

      except ValueError:
        print("Selection out of range, please try again.")


  # Method to stop and exit the program
  def quit(self):
    sys.exit()


if __name__ == '__main__':
  # Instantiate the Library interface class
  Library()