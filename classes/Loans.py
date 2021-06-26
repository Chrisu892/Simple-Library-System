# Import required modules
from .TableGenerator import TableGenerator


# Define Loan class
class Loans:


  def __init__(self):
    """Loans class constructor."""

    self.loans = list()
    self.Table = TableGenerator()


  def lend_book(self, user_list:object, book_list:object) -> bool:
    """Method to lend a book to the user."""

    # Check if the list of users is empty
    if user_list.count() == 0:
      print("\nThe Library does not have any users.")
      return False

    # Check if the list of books is empty
    if book_list.count() == 0:
      print("\nThe Library's book collection is empty.")
      return False

    try:
      # Find users that match the provided username
      users = user_list.find("username", "id", "user")

      if len(users) > 1:
        print("\nThere is more than 1 user with this username:\n")

        for idx, user in enumerate(users):
          print(f"{idx+1}. {user.get('first_name')} {user.get('last_name')} ({user.get('username')})")

        while True:
          selection = int(input("Please select [1,2,3...]: "))

          if selection in range(1, len(users) + 1):
            the_user = users[idx]
            break

      elif len(users) == 1:
        the_user = users[0]

      else:
        print("\nThis user does not exists, please try again.")
        return False

      books = book_list.find("title", "id", "book")

      if len(books) > 1:
        print("\nThere is more than 1 book with this title:\n")
        
        for idx, book in enumerate(books):
          print(f"{idx+1}. {book.get('title')} (author: {book.get('author')})")

        while True:
          selection = int(input("Please select [1,2,3...]: "))

          if selection in range(1, len(books) + 1):
            the_book = books[idx]
            break

      elif len(books) == 1:
        the_book = books[0]

      else:
        print("\nThis book does not exists, please try again.")
        return False

      num_copies = the_book.get('num_copies')

      for loan in self.loans:
        if loan['book'].get('id') == the_book.get('id'):

          if int(num_copies) > 0:
            num_copies = int(num_copies) - 1

          else:
            break

      if int(num_copies) > 0:
        self.loans.append({'user': the_user, 'book': the_book})

      else:
        raise Exception

    except Exception:
      print(f"\nInsufficient number of copies left.")
      return False

    except:
      print(f"\nFailed to lend a book!")
      return False

    else:
      print(f"Book {the_book.get('title')} has been loaned to {the_user.get_full_name()}.")
      return True


  def return_book(self, user_list:object, book_list:object) -> bool:
    """Method to return a book back to the Library."""

    # Check if the list of loans is empty
    if len(self.loans) == 0:
      print("\nThere are 0 active loans in the Library.")
      return False

    try:
      users = user_list.find("username", "username", "user")
      books = book_list.find("title", "title", "book")

      if users and books:
        if len(users) > 1:
          print(f"\nThere is more than 1 user with this username:\n")

          for idx, user in enumerate(users):
            print(f"{idx+1}. {user.get_full_name()} ({user.get('username')})")

          while True:
            user_selection = int(input("Please select a user [1,2,3...]: "))

            if user_selection in range(1, len(users) + 1):
              the_user = users[user_selection - 1]
              break

        elif len(users) == 1:
          the_user = users[0]

        else:
          print("\nUser not found!")
          return False

        if len(books) > 1:
          print(f"\nThere is more than 1 book with this title:\n")

          for idx, book in enumerate(books):
            print(f"\n{idx+1}. {book.get('title')} (author: {book.get('author')})")

          while True:
            book_selection = int(input("Please select a book [1,2,3...]: "))

            if book_selection in range(1, len(books) + 1):
              the_book = books[book_selection - 1]
              break

        elif len(books) == 1:
          the_book = books[0]

        else:
          print("\nBook not found!")
          return False

        for idx, loan in enumerate(self.loans):
          if loan['user'].get('id') == the_user.get('id') and loan['book'].get('id') == the_book.get('id'):
            del self.loans[idx]
            break

    except:
      print(f"\nFailed to return a book to the Library!\n")
      return False

    else:
      print(f"\nBook {the_book.get('title')} has been returned to the Library by {the_user.get_full_name()}.")
      return True


  def show_all_loans(self) -> None:
    """Method to show all loaned books."""

    try:
      if self.count() > 0:
        print(f"\nThere {'are' if self.count() > 1 else 'is'} {self.count()} book{'s' if self.count() > 1 else ''} on loan:\n")

        self.Table.create_table_row("Book Title", "Borrower")

        for loan in self.loans:
          self.Table.create_table_row(loan['book'].get('title'), loan['user'].get_full_name())
        self.Table.create_table_border(2)

      else:
        print("\nThere are 0 active loans in the Library.")

    except:
      print("\nFailed to retrieve loaned books!")


  def show_borrower_details(self, user_list:object) -> bool:
    """Show book borrower details."""

    if len(self.loans) == 0:
      print("\nThe Library has 0 active loans.")
      return False

    try:
      users = user_list.find("username", "username", "user")
      user_loans = list()

      if len(users) > 1:
        print("\nYour search returned more than 1 user:\n")

        for idx, user in enumerate(users):
          print(f"{idx+1}. {user.get_full_name()} ({user.get('username')})")

          while True:
            selection = int(input(f"\nPlease select user [1,2,3...]: "))

            if selection in range(1, len(users) + 1):
              the_user = users[idx]
              break

      else:
        the_user = users[0]

      for loan in self.loans:
        if loan['user'].get('id') == the_user.get('id'):
          user_loans.append(loan)

      if len(user_loans) > 0:
        print(f"{the_user.get_full_name()} has {len(user_loans)} active loan{'s' if len(user_loans) > 1 else ''}:\n")
        for loan in user_loans:
          print(f"{loan['book'].get('title')}")

      else:
        print(f"\n{user.get('first_name')} {user.get('last_name')} has 0 active loans.")

    except:
      print("\nCouldn't find the borrower!")
      return False

    else:
      return True


  def count(self) -> int:
    """Return total number of loans."""
    return len(self.loans)