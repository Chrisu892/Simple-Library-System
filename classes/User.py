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


  def create_user(self, details = dict()) -> bool:
    """Method to create a new user."""
    return self.create("user", details)


  def update_user(self, details = dict()) -> bool:
    """Method to update existing user."""
    return self.update("user", details)


  def get_full_name(self) -> str:
    """Method to return user's full name, if possible."""
    return (self.first_name + ' ' + self.last_name) if self.first_name and self.last_name else "undefined"