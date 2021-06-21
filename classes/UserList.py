# Import super class EntityList
from .EntityList import EntityList
from .User import User


# Define subclass UserList
class UserList(EntityList):


  # Class constructor
  def __init__(self) -> None:
    # Instantiate super class
    EntityList.__init__(self)


  def create_user(self) -> bool:
    try:
      user = User()
      self.entities.append(user)
      print(f"\nUser {user.get_first_name()} has been added!\n")
      return True

    except:
      print("\nSomething went wrong, please try again.\n")
      return False


  # Method to show all users from the list of users
  def show(self) -> list:
    # SHOW * FROM self.entities
    return self.entities