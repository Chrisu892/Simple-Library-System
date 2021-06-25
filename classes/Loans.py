# Define Loan class
class Loans:


  def __init__(self):
    """Loans class constructor."""
    self.loans = list()


  def lend_book(self, user_list:object, book_list:object) -> bool:
    """Method to lend a book to the user."""

    try:
      users = user_list.find("username", "id", "user")
      books = book_list.find("title", "id", "book")

      self.loans.append({'user': users[0], 'book': books[0]})

    except:
      print(f"\nFailed to lend a book!\n")
      return False

    else:
      print(f"\nBook {books[0].get('title')} has been lended to user {users[0].get('first_name')} {users[0].get('last_name')}.")
      return True


  def return_book(self, user_list:object, book_list:object) -> bool:
    """Method to return a book back to the Library."""

    try:
      users = user_list.find("username", "username", "user")
      books = book_list.find("title", "title", "book")

      if users and books:
        if len(users) > 1:
          print(f"\nThere is more than 1 user with this username:\n")

          for idx, user in enumerate(users):
            print(f"{idx+1}. {user.get('first_name')} {user.get('last_name')} ({user.get('username')})")

          while True:
            selection = int(input("Please select a user [1,2,3...]: "))

            if selection in range(1, len(users) + 1):
              user_id = users[selection - 1].get('id')
              break

        else:
          user_id = users[0].get('id')

        if len(books) > 1:
          print(f"\nThere is more than 1 book with this title:\n")

          for idx, book in enumerate(books):
            print(f"\n{idx+1}. {book.get('title')} (author: {book.get('author')})")

          while True:
            book_selection = int(input("Please select a book [1,2,3...]: "))

            if book_selection in range(1, len(books) + 1):
              book_id = books[selection - 1].get('id')
              break

        else:
          book_id = books[0].get('id')

        for idx, loan in enumerate(self.loans):
          if loan['user'].get('id') == user_id and loan['book'].get('id') == book_id:
            del self.loans[idx]
            break

    except:
      print(f"\nFailed to return a book to the Library!\n")
      return False

    else:
      print(f"\nBook {book.get('title')} has been returned to the Library by {user.get('first_name')} {user.get('last_name')}.")
      return True


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

    # @todo: need to take into consideration multiple users
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