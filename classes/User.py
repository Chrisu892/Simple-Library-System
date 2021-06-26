# Import required modules
from .Entity import Entity


# Define class User
class User(Entity):


  def __init__(self):
    """User class constructor."""

    Entity.__init__(self)

    self.username:str = ""
    self.first_name:str = ""
    self.last_name:str = ""
    self.dob:str = ""
    self.house_no:int = 0
    self.street_name:str = ""
    self.postcode:str = ""
    self.email_address:str = ""


  def create(self) -> bool:
    """Method to create a new user."""

    try:
      for prop in self.__dict__.items():

        if prop[0] == 'id':
          continue

        if prop[0] == "house_no":
          self.set(prop[0], self.prompt(f"{prop[0]}", "int"))
        else:
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

        if prop[0] == 'id':
          continue

        resp = self.prompt(f"Set {prop} from {value} to")

        if resp != "":
          self.set(prop, resp)
          print(f"User {prop} has been updated!\n")
        else:
          print(f"{prop} has been skipped.\n")

    except:
      return False

    else:
      return True


  def get_full_name(self) -> str:
    if self.first_name and self.last_name:
      return (self.first_name + ' ' + self.last_name)
    else:
      return "UNDEFINED FULL NAME"