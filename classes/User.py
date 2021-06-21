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
      self.set("fname", str(input("First name: ")))
      self.set("lname", str(input("Last name: ")))
      self.set("dob", str(input("Date of birth: ")))
      self.set("house_no", str(input("House/Flat number: ")))
      self.set("street_name", str(input("Street name: ")))
      self.set("postcode", str(input("Postcode: ")))
      self.set("email_address", str(input("Email address: ")))

    except:
      print("\nFailed to create new user!\n")

    finally:
      print(f"\nUser '{self.get('fname')}' has been created!\n")