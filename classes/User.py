# Import required modules
from .Entity import Entity


# Define class User
class User(Entity):


  def __init__(self):
    """User class constructor."""
    Entity.__init__(self)


  def create(self) -> bool:
    """Method to create a new user."""
    try:
      self.set("username", str(input("Username: ")))
      self.set("first_name", str(input("First name: ")))
      self.set("last_name", str(input("Last name: ")))
      self.set("dob", str(input("Date of birth: ")))
      self.set("house_no", str(input("House/Flat number: ")))
      self.set("street_name", str(input("Street name: ")))
      self.set("postcode", str(input("Postcode: ")))
      self.set("email_address", str(input("Email address: ")))

    except:
      print("\nFailed to create new user!\n")
      return False

    finally:
      print(f"\nUser '{self.get('first_name')} {self.get('last_name')}' has been created!")
      return True