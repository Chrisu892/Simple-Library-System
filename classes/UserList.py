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

    # Create new instance of the User
    user = User()

    # Create new user
    # @todo: Could add a check if the username is already taken by someone else
    if user.create():
      self.entities.append(user)


  def remove_user(self) -> None:
    """Public method to prompt the user to enter the user's first name
    and invoke a function to remove entity from the list of entities."""

    try:
      users = self.find("first_name", "first_name", "First name")

      if len(users) > 1:
        print(f"\nYour search returned more than 1 user:\n")

        for idx, user in enumerate(users):
          print(f"{idx+1}. {user.get('first_name')} {user.get('last_name')} ({user.get('username')})")

        while True:
          selection = int(input(f"\nPlease select user {enumerate(users).keys()}: "))

          if selection in range(1, len(users) + 1):
            if self.remove("id", users[idx].get('id')) == False:
              print("\nFailed to remove user from list of multiple users.")
            else:
              break

      else:
        if self.remove("first_name", users[0].get('first_name')) == False:
          print("\nFailed to remove user from list of 1 users.")

    except:
      print("\nProblem occurred while removing user from the library system.")
      return False

    else:
      print(f"User {users[0].get('first_name')} has been removed from the system.")
      return True


  def find_user(self) -> None:
    """Public method to find the Library users by their username."""

    while True:
      try:
        username = str(input("Please type username to find: "))

        if username == 'q':
          print("\nOperation has been cancelled!")
          break

        results = self.show("username", username)

        if len(results) > 0:
          print(f"\nYour search for '{username}' returned {len(results)} result{'s' if len(results) > 1 else ''}:")

          for user in results:
            print()
            for item in user.__dict__.items():
              print(f"{item[0]}: {item[1]}")

          break

      except:
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
      self.create_table_header("ID","Username","First Name","Last Name")

      for user in self.show_all():
        print(f"| {user.get('id')}{' ' * (14 - len(user.get('id')))}| {user.get('username')}{' ' * (14 - len(user.get('username')))}| {user.get('first_name')}{' ' * (14 - len(user.get('first_name')))}| {user.get('last_name')}{' ' * (14 - len(user.get('last_name')))}|")
        self.create_table_border()

    else:
      print(f"\nThe library system have 0 users.")