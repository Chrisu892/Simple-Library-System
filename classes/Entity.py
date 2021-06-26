# Import required modules
from random import randint


# Entity class definition
class Entity:


  def __init__(self) -> None:
    """Entity class constructor."""

    # Assign random ID to the entity (could be book or user)
    self.id = self.__random_id()


  def set(self, prop, value) -> bool:
    """Public method to set the property of the class."""

    try:
      # Try to set the attribute of the class
      setattr(self, prop, value)

    except:
      # Show an error message if setting the attribute failed
      print(f"Error occurred, can't add {prop} to the class.")
      return False

    else:
      # Return True if all is OK
      return True


  def get(self, prop):
    """Public method to get the property of the class."""

    try:
      # Try to set the attribute of the class
      return getattr(self, prop)

    except:
      # Show an error message if setting the attribute failed
      print(f"Error occurred, can't find {prop} in the class.")
      return False


  def create(self, entity_type:str = None) -> bool:
    """Method to create a new entity."""

    try:
      self.__set__properties(entity_type)

    except:
      print(f"\nFailed to create a new {entity_type if entity_type != None else 'entity'}!")
      return False

    else:
      print(f"\nA new {entity_type if entity_type != None else 'entity'} has been created!")
      return True


  def update(self, entity_type:str = None) -> bool:
    """Method to update entity details."""

    try:
      self.__set__properties(entity_type)

    except:
      # If errors occurred, return False
      return False

    else:
      # If everything is OK, then return True
      return True


  def prompt(self, label, input_type = "str"):
    """Method to prompt the user to type some data into the program."""

    # Prompt the user to enter an integer
    if input_type == "int":
      return int(input(f"{label}: "))

    # Prompt the user to enter a string
    else:
      return str(input(f"{label}: "))


  def __set__properties(self, entity_type:str = None) -> None:
    """Private method to set object properties."""

    # Iterate through the properties of the class
    for prop, value in self.__dict__.items():
        
      # Skip prompting user to change the ID
      if prop == "id":
        continue

      # Prompt the user to enter a new value for the object property
      resp = self.prompt(f"{prop}", type(prop))

      # Check if response is not empty
      if resp != "":
        # Set property to the new value
        self.set(prop, resp)

        # Print a confirmation message
        print(f"{entity_type if entity_type != None else 'Entity'}'s {prop} has been updated!\n")

      else:
        # Print message that updating this property has been skipped
        print(f"{entity_type if entity_type != None else 'Entity'}'s {prop} has been skipped!\n")


  def __random_id(self) -> str:
    """Private method to generate and return the ID of the entity. For example: 123-456-768 would be generated and set as the ID."""
    return str(randint(100, 1000)) + "-" + str(randint(100, 1000)) + "-" + str(randint(100, 1000))