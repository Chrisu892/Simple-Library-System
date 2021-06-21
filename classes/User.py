# Import required modules
from .Entity import Entity


# Define class User
class User(Entity):


  # Class contructor
  def __init__(self):
    # Instantiate super class
    Entity.__init__(self)
    # Set User details
    self.__fname = str(input("First name: "))
    self.__lname = str(input("Last name: "))
    self.__house_num = str(input("House/Flat number: "))
    self.__street_name = str(input("Street name: "))
    self.__postcode = str(input("Postcode: "))
    self.__email_addr = str(input("Email address: "))
    self.__dob = str(input("Date of birth: "))


  # Create new user
  def create_user(self) -> bool:
    # IF user IS created RETURN True ELSE False
    pass


  # Get the user first name
  def get_first_name(self) -> str:
    try:
      return self.__fname
    except:
      print("\nFirst name is undefined.\n")
      return False


  # Get the user last name
  def get_last_name(self) -> str:
    try:
      return self.__lname
    except:
      print("\nLast name is undefined.\n")
      return False


  # Get the user last name
  def get_house_number(self) -> str:
    try:
      return self.__house_num
    except:
      print("\nHouse/Flat number is undefined.\n")
      return False


  # Get the user last name
  def get_street_name(self) -> str:
    try:
      return self.__street_name
    except:
      print("\nStreet name is undefined.\n")
      return False


  # Get the user last name
  def get_postcode(self) -> str:
    try:
      return self.__postcode
    except:
      print("\nPostcode is undefined.\n")
      return False


  # Get the user last name
  def get_email_address(self) -> str:
    try:
      return self.__email_addr
    except:
      print("\nEmail address is undefined.\n")
      return False


  # Get the user last name
  def get_dob(self) -> str:
    try:
      return self.__dob
    except:
      print("\nDate of birth is undefined.\n")
      return False