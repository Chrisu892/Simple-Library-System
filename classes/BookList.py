# Import super class EntityList
from .TableGenerator import TableGenerator
from .EntityList import EntityList
from .Book import Book


# Define subclass BookList
class BookList(EntityList):


  def __init__(self):
    """BookList class constructor."""

    EntityList.__init__(self)
    self.Table = TableGenerator()


  def add_book(self) -> bool:
    """Public method to add a new book to the collection."""

    try:
      # Create new instance of the Book class
      book = Book()

      # Create new book (create method returns bool)
      if book.create_book():

        # Append new book to the list of books
        self.entities.append(book)

      else:
        # If failed to create a book, raise an exception
        raise Exception

    # Catch an exception and return False
    except Exception:
      return False

    # If program executed without problems, return True
    else:
      return True


  def update_book_details(self) -> bool:
    """Public method to find a book by the title in the Library system. If the book exists, invoke a method to update user details."""

    try:
      # Prompt the user to enter the book's title to find:
      books = self.find("title", "title", "book")

      # Check if the search returned moe than 1 result
      if len(books) > 1:
        # Prompt the user to select 1 of the books from the list and set the_book
        the_book = self.select_from_list(books, "title")

      # Alternatively, if the search returned 1 result
      elif len(books) == 1:
        # Set the_book variable to be the first element from the book list
        the_book = books[0]

      else:
        # Print a message that the program couldn't find the book
        print("\nBook not found!")

      if the_book.update_book():
        return True

      else:
        return False

    except:
      print("\nError occurred in BookList, update_user method.")


  def remove_book(self) -> bool:
    """Public method to remove a book from the list of books."""

    try:
      # Prompt the user to find a book by its title
      books = self.find("title", "title", "book")

      if books == False:
        print("\nThis book doesn't exists!")
        return False

      # If the list has more than one book
      if len(books) > 1:
        # Prompt the user to select one of the books
        the_book = self.select_from_list(books, "title")

      # If the list has only one book
      elif len(books) == 1:
        # Pick the only book in the list
        the_book = books[0]

      # Otherwise, the list is empty
      else:
        print("\nBook not found!")
        return False

      # Try to remove the book from the list by it's ID
      if self.remove("id", the_book.get('id')):
        # If book has been removed, show a message and return True
        print(f"Book '{the_book.get('title')}' has been removed from the collection.")
        return True

      # Otherwise, show a message that book does not exists, and return False
      else:
        print(f"\nFailed to remove book from the collection. {the_book.get('title')} does not exists.")
        return False

    # Catch any problems and return False
    except:
      print("\nProblem occurred in the remove_book method.")
      return False


  def find_book(self) -> None:
    """Public method to find a book in the collection by it's title, author, publisher_name or publication_date."""

    # Define empty list to store all books that match the search_by criteria
    found_books = []

    # Define a list of book attributes that the program should look at
    searchable = ["title", "author", "publisher_name", "publication_date"]

    while True:
      # Prompt the user to select the book attribute to look at
      search_by = str(input("\nEnter search by: [title, author, publisher_name, publication_date]: "))

      # If user chosen one of the allowed search_by options
      if search_by in searchable:

        # Prompt the user to enter the search keyword
        keyword = str(input(f"Find book by {search_by}: "))

        # Iterate through the list of books and append book that matches
        # search criteria to the list of found books
        for book in self.entities:

          # If the program should look at the book title, and the book title is equal to the user defined keyword
          if search_by == "title" and book.get("title").lower() == keyword.lower():
            # Append the book into the list of found books
            found_books.append(book)

          # If the program should look at the book author, and the book author is equal to the user defined keyword
          elif search_by == "author" and book.get("author").lower() == keyword.lower():
            # Append the book into the list of found books
            found_books.append(book)
          
          # If the program should look at the book's publisher name, and the book's publisher name is equal to the user defined keyword
          elif search_by == "publisher_name" and book.get("publisher_name").lower() == keyword.lower():
            # Append the book into the list of found books
            found_books.append(book)

          # If the program should look at the book's publication data, and the book's publication date is equal to the user defined keyword
          elif search_by == "publication_date" and book.get("publication_date").lower() == keyword.lower():
            # Append the book into the list of found books
            found_books.append(book)

        # Check if the list of found books is not empty
        if len(found_books) > 0:

          # Print the results back to the user
          print(f"\nYour search for '{keyword}' returned {len(found_books)} result{'s' if len(found_books) > 1 else ''}:\n")

          # Create a table of found books
          self.Table.create_table(found_books)

        else:
          # Otherwise, show the message that search returned 0 results
          print(f"\nYour search for '{keyword}' in book {search_by} returned 0 results.")

        # Break out of the while loop
        break

      else:
        print("Selection out of range, please try again.")


  def num_books(self) -> None:
    """Public method to print the message to inform the program user about how many books exists in the collection."""
    print(f"\nThere {'are' if self.count() > 1 else 'is'} {self.count()} book{'s' if self.count() > 1 else ''} in the collection.")