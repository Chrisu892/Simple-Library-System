# Import required modules
from .Entity import Entity


# Define Book class
class Book(Entity):


  def __init__(self) -> None:
    """Book class constructor."""

    # Initialise parent class
    Entity.__init__(self)

    # Define class properties
    self.title:str = ""
    self.author:str = ""
    self.year:int = 0
    self.publisher_name:str = ""
    self.publication_date:str = ""
    self.num_copies:int = 0


  def create(self) -> bool:
    """Public method to create a new book."""

    try:
      # For each property in the book class
      for prop in self.__dict__.items():

        # Skip the class ID
        if prop[0] == "id":
          continue

        # If property is a year, prompt the user to enter an integer
        if prop[0] == "year":
          self.set(prop[0], self.prompt(f"{prop[0]}", "int"))

        # If any other class property, prompt the user to enter a string
        else:
          self.set(prop[0], self.prompt(f"{prop[0]}"))

    except:
      # If error occurrs, show a message and return False
      print("\nFailed to create a new book!")
      return False

    else:
      # If the code executed without problems, show a message and return True
      print(f"\nBook '{self.get('title')}' has been created!")
      return True