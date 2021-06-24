# Import required modules
from .Entity import Entity


# Define class User
class User(Entity):


  def __init__(self):
    """User class constructor."""

    Entity.__init__(self)

    self.username = ""
    self.first_name = ""
    self.last_name = ""
    self.dob = ""
    self.house_no = ""
    self.street_name = ""
    self.postcode = ""
    self.email_address = ""


  def create(self) -> bool:
    """Method to create a new user."""

    try:
      for prop in self.__dict__.items():
        if prop[0] != 'id':
          self.set(prop[0], self.prompt(f"{prop[0]}"))

    except:
      print("\nFailed to create new user!")
      return False

    else:
      print(f"\nUser '{self.get('first_name')} {self.get('last_name')}' has been created!")
      return True


  def update(self) -> bool:
    """Method to update user details."""

    try:
      for prop, value in self.__dict__.items():
        resp = self.prompt(f"Set {prop} from {value} to")

        if resp != "":
          self.set(prop, resp)
          print(f"User {prop} has been updated!\n")
        else:
          print(f"User {prop} has not been updated.\n")

    except:
      print("\nCouldn't update user details!")
      return False

    else:
      print("\nUser details have been updated!")
      return True
