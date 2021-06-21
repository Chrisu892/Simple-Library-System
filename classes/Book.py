# Import required modules
from .Entity import Entity


# Define Book class
class Book(Entity):


  def __init__(self) -> None:
    """Book class constructor."""
    Entity.__init__(self)


  def create(self):
    """Public method to create a new book."""

    try:
      self.set("title", str(input("Book title: ")))
      self.set("author", str(input("Author name: ")))
      self.set("year", int(input("Book year: ")))
      self.set("publisher_name", str(input("Publisher name: ")))
      self.set("publication_date", str(input("Publication date: ")))
      self.set("num_copies", int(input("Number of copies: ")))

    except:
      print("\nFailed to create a new book!\n")
      return False

    finally:
      print(f"\nBook {self.get('title')} has been created!\n")
      return True