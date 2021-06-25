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

      # Create new book
      if book.create():
        self.entities.append(book)
      else:
        raise Exception

    except Exception:
      print("\nFailed to add a new book!")
      return False

    finally:
      print(f"\nBook {book.get('title')} has been created!")
      return True


  def remove_book(self) -> bool:
    """Public method to remove a book from the collection."""

    try:
      books = self.find("title", "title", "book")

      if len(books) > 1:
        print("\nYour search returned more than 1 book:\n")

        for idx, book in enumerate(books):
          print(f"{idx+1}. {book.get('title')} (author: {book.get('author')})")

        while True:
          selection = int(input(f"\nPlease select a book [1,2,3...]: "))

          if selection in range(1, len(books) + 1):
            if self.remove("id", books[selection - 1].get('id')) == False:
              print("\nFailed to remove book from the collection.")
            else:
              break

      else:
        if self.remove("title", books[0].get('title')) == False:
          print("\nFailed to remove book from the collection.")

    except:
      print(f"\nProblem occurred while removing the book from the collection.")
      return False

    else:
      print(f"Book '{books[0].get('title')}' has been removed from the collection.")
      return True


  def find_book(self) -> None:
    """Public method to find a book in the collection."""

    # Define empty list to store all books that match the search_by criteria
    found_books = []
    # Define a list of book properties are that search should look at
    searchable = ["title", "author", "publisher_name", "publication_date"]
    # Prompt the user to choose the search_by
    search_by = str(input("\nEnter search by: [title, author, publisher_name, publication_date]: "))

    # If user chosen one of the allowed search_by options
    if search_by in searchable:
      # Prompt the user to enter the search keyword
      keyword = str(input(f"Find book by {search_by}: "))

      # Iterate through the list of books and append book that matches
      # search criteria to the list of found books
      for book in self.entities:
        if search_by == "title" and book.get("title").lower() == keyword.lower():
          found_books.append(book)
        elif search_by == "author" and book.get("author").lower() == keyword.lower():
          found_books.append(book)
        elif search_by == "publisher_name" and book.get("publisher_name").lower() == keyword.lower():
          found_books.append(book)
        elif search_by == "publication_date" and book.get("publication_date").lower() == keyword.lower():
          found_books.append(book)

      if len(found_books) > 0:
        # Print the results back to the user
        print(f"\nYour search for '{keyword}' returned {len(found_books)} result{'s' if len(found_books) > 1 else ''}:\n")

        # Create table header
        self.UI.create_table_row("ID", "Title", "Author", "Copies")

        for book in found_books:
          self.UI.create_table_row(book.get('id'), book.get('title'), book.get('author'), book.get('num_copies'))
          self.UI.create_table_border(4)

      else:
        # Otherwise, show the message that search returned 0 results
        print(f"\nYour search for '{keyword}' in book {search_by} returned 0 results.")


  def num_books(self):
    """Public method to print the message to inform the program user
    about how many books exists in the collection."""

    print(f"\nThere {'are' if self.count() > 1 else 'is'} {self.count()} book{'s' if self.count() > 1 else ''} in the collection.")