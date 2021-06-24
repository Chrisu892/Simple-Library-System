# Import super class EntityList
from .EntityList import EntityList
from .Book import Book


# Define subclass BookList
class BookList(EntityList):


  def __init__(self):
    """BookList class constructor."""
    EntityList.__init__(self)


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


  # @todo: if there are 2 or more books with the same title, prompt the user to select correct book
  def remove_book(self) -> bool:
    """Public method to remove a book from the collection."""

    try:
      # Prompt the user to enter the title of the book to remove
      title = str(input("Book title to remove: "))

      # Iterate through the list of books
      for idx, book in enumerate(self.entities):
        # Find a matching book title
        if book.get('title').lower() == title.lower():
          # Delete matching book from the list
          del self.entities[idx]
          # Notify the user about the change
          print(f"\nBook {title} has been removed.")

    except:
      # Notify user that something went wrong
      print("\nBook not found.")
      return False

    else:
      # Notify the program user about success
      print(f"\nBook {title} has been removed from the collection.")
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
        for book in found_books:
          for item in book.__dict__.items():
            print(f"{item[0]}: {item[1]}")

      else:
        # Otherwise, show the message that search returned 0 results
        print(f"\nYour search for '{keyword}' in book {search_by} returned 0 results.")


  def num_books(self):
    """Public method to print the message to inform the program user
    about how many books exists in the collection."""

    print(f"\nThere {'are' if self.count() > 1 else 'is'} {self.count()} book{'s' if self.count() > 1 else ''} in the collection.")