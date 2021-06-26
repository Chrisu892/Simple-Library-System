# Import required modules
from .Entity import Entity


# Define class User
class User(Entity):


  def __init__(self):
    """User class constructor."""

    # Initialise parent class
    Entity.__init__(self)

    # Define user properties
    self.username:str = ""
    self.first_name:str = ""
    self.last_name:str = ""
    self.dob:str = ""
    self.house_no:int = 0
    self.street_name:str = ""
    self.postcode:str = ""
    self.email_address:str = ""


  def create_user(self) -> bool:
    """Method to create a new user."""
    return self.create("user")


  def update_user(self) -> bool:
    """Method to update existing user."""
    return self.update("user")


  def get_full_name(self) -> str:
    if self.first_name and self.last_name:
      return (self.first_name + ' ' + self.last_name)
    else:
      return "UNDEFINED"