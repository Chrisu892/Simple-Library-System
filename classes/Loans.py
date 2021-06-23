# Define Loan class
class Loans:


  def __init__(self):
    """Loans class constructor."""
    self.loans = list()


  def lend_book(self, user_list:object, book_list:object) -> bool:
    """Method to lend a book to the user."""

    try:
      user = user_list.find("username", "id", "user")
      book = book_list.find("title", "id", "book")

      self.loans.append({'user': user, 'book': book})
      print(f"\nBook {book.get('title')} has been lended to user {user.get('first_name')} {user.get('last_name')}.\n")
      return True

    except:
      print(f"\nFailed to lend a book!\n")
      return False


  def return_book(self, user_list:object, book_list:object) -> bool:
    """Method to return a book back to the Library."""

    try:
      user = user_list.find("username")
      book = book_list.find("title")

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


  def show_all_loans(self) -> None:
    """Method to show all loaned books."""

    try:
      if len(self.loans) > 0:
        print(f"\nThere are {len(self.loans)} book{'s' if len(self.loans) > 0 else ''} on loan:\n")

        for loan in self.loans:
          print(f"{loan['book'].get('title')} is loaned to {loan['user'].get('first_name')} {loan['user'].get('last_name')}.")

      else:
        print("\nThere are no books on loan.\n")

    except:
      print("\nFailed to show books on loans!\n")


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


  # Show the total count of all loans - Added by the author
  def count(self) -> int:
    return len(self.loans)