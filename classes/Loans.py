# Define Loan class
class Loans:


  def __init__(self):
    """Loans class constructor."""
    self.loans = list()


  def lend_book(self, user_list:object, book_list:object) -> bool:
    """Method to lend a book to the user."""

    try:
      user = user_list.find("username")
      book = book_list.find("title")

      self.loans.append({'user': user, 'book': book})
      print(f"\nBook {book.get('title')} has been lended to user {user.get('first_name')} {user.get('last_name')}.\n")
      return True

    except:
      print(f"\nFailed to lend a book!\n")
      return False

    finally:
      print("\nCouldn't find user or book!\n")
      return False


  def return_book(self, user_list:object, book_list:object) -> bool:
    """Method to return a book back to the Library."""

    try:
      user = user_list.find("username")
      book = user_list.find("title")

      if user and book:
        for idx, loan in enumerate(self.loans):
          if loan['user'].get('id') == user.get('id') and loan['book'].get('id') == book.get('id'):
            del self.loans[idx]
            print(f"Book {book.get('title')} has been returned to the Library by {user.get('first_name')} {user.get('last_name')}")
            return True

    except:
      print(f"\nFailed to return a book to the Library!\n")
      return False

    finally:
      print(f"\nCoudn't find the book on loan.\n")
      return False


  def show_borrowed_books(self, user_list:object) -> None:
    "Method to show all borrowed books by the user."

    try:
      user_loans = list()
      user = user_list.find("username")

      if user:
        for loan in self.loans:
          if loan['user'].get('id') == user.get('id'):
            user_loans.append(loan)

    except:
      print(f"Failed to retrieve {user.get('first_name')} {user.get('last_name')}'s books.")
      return False

    finally:
      if len(user_loans) > 0:
        print(f"\n{user.get('first_name')} {user.get('last_name')} has {len(user_loans)} active loans:\n")
        for loan in user_loans:
          print(f"{loan['book'].get('title')}")
        print()


  def return_overdue_books(self, user_list:object) -> bool:
    """Method to return all loaned books by the user back to the Library."""

    try:
      user = user_list.find("username")

      if user:
        for idx, loan in enumerate(self.loans):
          if loan['user'].get('id') == user.get('id'):
            print(f"Book {loan['book'].get('title')} has been returned by {user.get('first_name')}.")
            del self.loans[idx]

    except:
      print("\nFailed to returned books!\n")
      return False

    finally:
      print(f"\nAll books have been returned by {user.get('first_name')}!\n")
      return True


  def show_borrower_details(self, user_list:object) -> None:
    """Show book borrowed details."""

    try:
      user_loans = list()
      user = user_list.find("username")

      if user:
        for loan in self.loans:
          if loan['user'].get('id') == user.get('id'):
            user_loans.append(loan)

    except:
      print("\nCouldn't find the borrower!\n")

    finally:
      if len(user_loans) > 0:
        print(f"\n{user.get('first_name')} {user.get('last_name')} has {len(user_loans)} active loans:\n")
        for loan in user_loans:
          print(f"{loan['book'].get('title')}")
        print()


  # Show the total count of all loans - Added by the author
  def count(self) -> int:
    return len(self.loans)