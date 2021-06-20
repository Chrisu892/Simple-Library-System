# Import super class EntityList
from .EntityList import EntityList


# Define subclass BookList
class UserList(EntityList):


  # Class constructor
  def __init__(self) -> None:
    # Instantiate super class
    EntityList.__init__(self)


  # Method to show all users from the list of users
  def show(self) -> list:
    # SHOW * FROM self.entities
    return self.entities