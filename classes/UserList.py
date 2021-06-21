# Import super class EntityList
from .EntityList import EntityList
from .User import User


# Define subclass UserList
class UserList(EntityList):


  # Class constructor
  def __init__(self) -> None:
    # Instantiate super class
    EntityList.__init__(self)


  def add(self) -> bool:
    try:
      user = User()
      user.create()
      self.entities.append(user)
      return True

    except:
      print("\nSomething went wrong, please try again.\n")
      return False


  # Method to show all users from the list of users
  def show(self) -> list:
    # SHOW * FROM self.entities
    return self.entities