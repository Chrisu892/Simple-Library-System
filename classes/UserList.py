# Import super class EntityList
from .EntityList import EntityList
from .User import User


# Define subclass UserList
class UserList(EntityList):


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


  def remove_user(self) -> bool:
    """Public method to remove a user from the library system."""

    try:
      firstname = str(input("Enter user first name: "))
      self.remove("first_name", firstname)
      return True

    except:
      print("Problem occurred while removing user from the library system.")
    
    return False


  def find_user(self):
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
          print(f"ID: {user.get('id')}")
          print(f"Username: {user.get('username')}")
          print(f"First name: {user.get('first_name')}")
          print(f"Last name: {user.get('last_name')}")
          print(f"Date of birth: {user.get('dob')}")
          print(f"House/Flat number: {user.get('house_no')}")
          print(f"Street name: {user.get('street_name')}")
          print(f"Postcode: {user.get('postcode')}")
          print(f"Email address: {user.get('email_address')}")

          break

      except ValueError:
        print("\nInvalid input, please type alphanumerical username.\n")


  def show_users(self):
    """Public method to show all users of the Library system."""
    
    if self.count() > 0:
      print(f"\nThe library system have {self.count()} user{'s' if self.count() > 1 else ''}:\n")

      for user in self.show_all():
        print(f"{user.get('first_name')} {user.get('last_name')} ({user.get('username')})")

    else:
      print(f"\nThe library system have 0 users.")
