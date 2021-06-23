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
      print(f"\nBook {book.get('title')} has been lended to user {user.get('first_name')} {user.get('last_name')}.")

    except:
      print(f"\nFailed to lend a book!\n")


  def return_book(self, user_list:object, book_list:object) -> None:
    """Method to return a book back to the Library."""

    try:
      user = user_list.find("username", "username", "user")
      book = book_list.find("title", "title", "book")

      if user and book:
        for idx, loan in enumerate(self.loans):
          if loan['user'].get('id') == user.get('id') and loan['book'].get('id') == book.get('id'):
            del self.loans[idx]
            print(f"\nBook {book.get('title')} has been returned to the Library by {user.get('first_name')} {user.get('last_name')}.")
            break

    except:
      print(f"\nFailed to return a book to the Library!\n")


  def show_all_loans(self) -> None:
    """Method to show all loaned books."""

    try:
      if self.count() > 0:
        print(f"\nThere {'are' if self.count() > 1 else 'is'} {self.count()} book{'s' if self.count() > 1 else ''} on loan:\n")

        for loan in self.loans:
          print(f"{loan['book'].get('title')} is loaned to {loan['user'].get('first_name')} {loan['user'].get('last_name')}.")

      else:
        print("\nThere are no books on loan.")

    except:
      print("\nFailed to show books on loans!")


  def show_borrower_details(self, user_list:object) -> None:
    """Show book borrower details."""

    try:
      user = user_list.find("username", "username", "user")

      if user:
        user_loans = list()

        for loan in self.loans:
          if loan['user'].get('id') == user.get('id'):
            user_loans.append(loan)

        if len(user_loans) > 0:
          print(f"\n{user.get('first_name')} {user.get('last_name')} has {len(user_loans)} active loan{'s' if len(user_loans) > 1 else ''}:\n")

          for loan in user_loans:
            print(f"{loan['book'].get('title')}")

        else:
          print(f"\n{user.get('first_name')} {user.get('last_name')} has 0 active loans.")

      else:
        print(f"\nUser doesn't exists!")

    except:
      print("\nCouldn't find the borrower!")


  def count(self) -> int:
    """Return total number of loans."""
    return len(self.loans)