# Import super class EntityList
from .EntityList import EntityList
from .Book import Book


# Define subclass BookList
class BookList(EntityList):


  # Class constructor
  def __init__(self):
    # Instantiate super class
    EntityList.__init__(self)


  # Method to add a book to the collection
  def add_book(self) -> bool:
    try:
      # Create new instance of Book class
      book = Book()
      # Append book to the list of books (entities)
      self.entities.append(book)
      # Print the message back to user
      print(f"\nBook {book.get('title')} has been added!\n")
      # Return bool
      return True

    except:
      # Notify the user about a problem
      print("\nSomething went wrong, please try again.\n")
      # Return bool
      return False


  # Method to remove the book from the list of books
  # @todo: if there are 2 or more books with the same title, prompt the user to select correct book
  def remove_book(self) -> bool:
    try:
      # Prompt the user to enter the title of the book to remove
      title = str(input("Book title to remove: "))

      # Iterate through the list of books
      for idx, book in enumerate(self.entities):
        # Find a matching book title
        if book.get_title() == title:
          # Delete matching book from the list
          del self.entities[idx]
          # Notify the user about the change
          print(f"\nBook {title} has been removed.\n")
          # Return truthy bool
          return True

      # Notify the user that book has not been found
      print(f"\nBook {title} does not exist.\n")
      # Return falsy bool
      return False

    except ValueError:
      # Notify user that something went wrong
      print("Invalid book title, please try again.")
      # Return falsy bool
      return False


  # Method to search through the list of books and find those
  # that match one of the selected criteria
  def find_book(self) -> None:

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
        if search_by == "title" and book.get("title") == keyword:
          found_books.append(book)
        elif search_by == "author" and book.get("author") == keyword:
          found_books.append(book)
        elif search_by == "publisher_name" and book.get("publisher_name") == keyword:
          found_books.append(book)
        elif search_by == "publication_date" and book.get("publication_date") == keyword:
          found_books.append(book)

      # Print the results back to the user
      if len(found_books) > 0:
        print(f"\nYour search for '{keyword}' in book {search_by} returned {len(found_books)} result{'s' if len(found_books) > 1 else ''}:\n")
        for book in found_books:
          print(f"Title: {book.get('title')}")
          print(f"Author: {book.get('author')}")
          print(f"Year: {book.get('year')}")
          print(f"Publisher name: {book.get('publisher_name')}")
          print(f"Publication date: {book.get('publication_date')}")
          print(f"Number of copies: {book.get('num_copies')}\n")

      # Otherwise, show the message that search returned 0 results
      else:
        print(f"\nYour search for '{keyword}' in book {search_by} returned 0 results.\n")


  # Method to print the message stating how many books is in the collection
  def num_books(self):
    print(f"\nThere {'are' if self.count() > 1 else 'is'} {self.count()} book{'s' if self.count() > 1 else ''} in the collection.\n")