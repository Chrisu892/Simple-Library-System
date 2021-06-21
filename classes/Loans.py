# Define Loan class
class Loans:


  # Define class constructor
  def __init__(self):
    self.__loans = list()


  # Method to lend a book to the borrower
  def lend_book(self, user_list, book_list) -> bool:
    print("INSERT INTO loans (user_id, book_id) VALUES (user_id, book_id)")
    pass


  # Method to return a book
  def return_book(self, user_id:int, book_id:int) -> bool:
    print("DELETE loan FROM loans WHERE loan[user_id] = user_id AND loan[book_id] = book_id")
    pass

  
  # Method to show the list of borrowed books
  def show_borrowed_books(self, user_id:int) -> list:
    print("SELECT books FROM loans WHERE loan[user_id] = user_id")
    pass


  # Method to return all loaned books back to the library
  def return_overdue_books(self, user_id:int) -> bool:
    print("DELETE loan FROM loans WHERE loan[user_id] = user_id")
    pass


  # Show the list of people who have a loan in the library
  def show_borrower_details(self, book_id:int) -> list:
    print("SELECT user.* FROM loans WHERE loan[book_id] = book_id")
    pass


  # Show the total count of all loans - Added by the author
  def count(self) -> int:
    return len(self.__loans)