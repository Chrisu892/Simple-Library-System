# Import super class EntityList
from .EntityList import EntityList
from .User import User


# Define subclass UserList
class UserList(EntityList):


  # Class constructor
  def __init__(self) -> None:
    """UserList class constructor."""
    EntityList.__init__(self)


  def add_user(self):
    """Public method to add a new user to the Library system."""

    # Create new instance of the User
    user = User()

    # Create new user
    if user.create():
      self.entities.append(user)


  def remove_user(self):
    """Public method to remove a user from the Library system."""
    pass


  def find_user(self):
    """Public method to find user of the Library."""
    pass