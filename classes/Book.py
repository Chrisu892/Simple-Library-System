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
      self.set("title", self.prompt("Book title"))
      self.set("author", self.prompt("Author name"))
      self.set("year", self.prompt("Book year", "int"))
      self.set("publisher_name", self.prompt("Publisher name"))
      self.set("publication_date", self.prompt("Publication date"))
      self.set("num_copies", self.prompt("Number of copies"))

    except:
      print("\nFailed to create a new book!")
      return False

    finally:
      print(f"\nBook {self.get('title')} has been created!")
      return True