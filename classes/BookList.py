# Import super class EntityList
from .EntityList import EntityList
from .Book import Book
from .UI import UI


# Define subclass BookList
class BookList(EntityList):


  def __init__(self):
    """BookList class constructor."""

    EntityList.__init__(self)
    self.UI = UI()


  def add_book(self) -> bool:
    """Public method to add a new book to the collection."""

    try:
      # Create new instance of the Book class
      book = Book()

      # Create new book (create method returns bool)
      if book.create():

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


  def remove_book(self) -> bool:
    """Public method to remove a book from the list of books."""

    try:
      # Prompt the user to find a book by its title
      books = self.find("title", "title", "book")

      # If the returned list is greater than 1
      if len(books) > 1:

        # Show a message that the search returned more than 1 book
        print("\nYour search returned more than 1 book:\n")

        # Loop through all books in the list of found books
        for idx, book in enumerate(books):

          # Print option number and the book details
          print(f"{idx+1}. {book.get('title')} (author: {book.get('author')})")

        while True:
          # Prompt the user to select a book from the list
          selection = int(input(f"\nPlease select a book [1,2,3...]: "))

          # Check if the selection is within the range of found books
          if selection in range(1, len(books) + 1):

            # Try to remove the book by its ID
            if self.remove("id", books[selection - 1].get('id')) == False:
              raise Exception

            # Break out of the loop if the book has been removed
            else:
              break

      # If the list of found books has only 1 book
      else:
        # Try to remove the book by its title
        if self.remove("title", books[0].get('title')) == False:
          raise Exception

    except:
      # Show a message that program failed to remove the book from the list
      print("\nFailed to remove book from the collection.")
      return False

    else:
      # Show a message that the program successfully removed the book from the list
      print(f"Book '{books[0].get('title')}' has been removed from the collection.")
      return True


  def find_book(self) -> None:
    """Public method to find a book in the collection by its
    title, author, publisher_name or publication_date."""

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

          # Create table header
          self.UI.create_table_row("ID", "Title", "Author", "Copies")

          # Create table rows
          for book in found_books:
            self.UI.create_table_row(book.get('id'), book.get('title'), book.get('author'), book.get('num_copies'))
            self.UI.create_table_border(4)

        else:
          # Otherwise, show the message that search returned 0 results
          print(f"\nYour search for '{keyword}' in book {search_by} returned 0 results.")

        # Break out of the while loop
        break

      else:
        print("Selection out of range, please try again.")

  def num_books(self):
    """Public method to print the message to inform the program user
    about how many books exists in the collection."""

    print(f"\nThere {'are' if self.count() > 1 else 'is'} {self.count()} book{'s' if self.count() > 1 else ''} in the collection.")