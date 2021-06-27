# Import required modules
from .Entity import Entity


# Define Book class
class Book(Entity):


  def __init__(self) -> None:
    """Book class constructor."""

    # Initialise parent class
    Entity.__init__(self)

    # Define book properties
    self.title:str = ""
    self.author:str = ""
    self.year:int = 0
    self.publisher_name:str = ""
    self.publication_date:str = ""
    self.num_copies:int = 0


  def create_book(self, details = dict()) -> bool:
    """Method to create a new book."""
    return self.create("book", details)


  def update_book(self, details = dict()) -> bool:
    """Method to update existing book."""
    return self.update("book", details)