# Import required modules
from .Entity import Entity


# Define Book class
class Book(Entity):


  def __init__(self) -> None:
    """Book class constructor."""

    Entity.__init__(self)

    self.title:str = ""
    self.author:str = ""
    self.year:int = 0
    self.publisher_name:str = ""
    self.publication_date:str = ""
    self.num_copies:int = 0


  def create(self) -> bool:
    """Public method to create a new book."""

    try:
      for prop in self.__dict__.items():
        
        if prop[0] == "id":
          continue

        if prop[0] == "year":
          self.set(prop[0], self.prompt(f"{prop[0]}", "int"))
        else:
          self.set(prop[0], self.prompt(f"{prop[0]}"))

    except:
      print("\nFailed to create a new book!")
      return False

    else:
      print(f"\nBook '{self.get('title')}' has been created!")
      return True