# Import super class EntityList
from .EntityList import EntityList
from .User import User


# Define subclass UserList
class UserList(EntityList):


  def __init__(self) -> None:
    """UserList class constructor."""
    EntityList.__init__(self)


  def add_user(self) -> bool:
    """Public method to create a new instance of the user. If the user
    has been successfully created, append new user to the list of entities."""

    try:
      # Create new instance of the User
      user = User()

      # Create new user
      if user.create():
        self.entities.append(user)
    
    except:
      print("\nFailed to add a new user!")
      return False

    else:
      print(f"\nUser {user.get('username')} has been added!")
      return True


  def remove_user(self) -> None:
    """Public method to prompt the user to enter the user's first name
    and invoke a function to remove entity from the list of entities."""

    try:
      firstname = str(input("Enter user first name: "))
      if self.remove("first_name", firstname) == False:
        raise Exception

    except:
      print("\nProblem occurred while removing user from the library system.")
      return False

    else:
      print(f"User {firstname} has been removed from the system.")
      return True



  def find_user(self) -> None:
    """Public method to find the Library users by their username."""

    while True:
      try:
        username = str(input("Please type username to find: "))

        if username == 'q':
          print("\nOperation has been cancelled!")
          break

        user = self.show("username", username)

        if user:
          print(f"\nYour search for '{username}' returned:\n")

          for item in user.__dict__.items():
            print(f"{item[0]}: {item[1]}")
          break

      except ValueError:
        print("\nInvalid input, please type alphanumerical username.\n")
        break


  def update_user(self) -> None:
    """Public function to find a user by their username in the Library system.
    If the user exists, invoke a method to update user details."""

    try:
      user = self.find("username", "username", "username")

      if user:
        user.update()

    except:
      print("\nCouldn't find the user!")


  def show_users(self) -> None:
    """Public method to show all users of the Library system."""
    
    if self.count() > 0:
      print(f"\nThe library system have {self.count()} user{'s' if self.count() > 1 else ''}:\n")

      for user in self.show_all():
        print(f"{user.get('first_name')} {user.get('last_name')} ({user.get('username')})")

    else:
      print(f"\nThe library system have 0 users.")