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
      for prop in self.__dict__.items():

        if prop[0] == "id":
          continue

        if type(prop[0]) == "int":
          self.set(prop[0], self.prompt(f"{prop[0]}", "int"))
        else:
          self.set(prop[0], self.prompt(f"{prop[0]}"))

    except:
      print(f"\nFailed to create a new {entity_type if entity_type != None else 'entity'}!")
      return False

    else:
      print(f"\nA new {entity_type if entity_type != None else 'entity'} has been created!")
      return True


  def update(self, entity_type:str = None) -> bool:
    """Method to update entity details."""

    try:
      for prop, value in self.__dict__.items():

        if prop[0] == "id":
          continue

        resp = self.prompt(f"Set {prop} from {value} to")

        if resp != "":
          self.set(prop, resp)
          print(f"{entity_type if entity_type != None else 'Entity'}'s {prop} has been updated!\n")

        else:
          print(f"{entity_type if entity_type != None else 'Entity'}'s {prop} has been skipped!\n")

    except:
      return False

    else:
      return True


  def prompt(self, label, input_type = "str"):
    """Method to prompt the user to type some data into the program."""

    # Prompt the user to enter an integer
    if input_type == "int":
      return int(input(f"{label}: "))

    # Prompt the user to enter a string
    else:
      return str(input(f"{label}: "))


  def __random_id(self) -> str:
    """Private method to generate and return the ID of the entity.
    For example: 123-456-768 would be generated and set as the ID."""

    return str(randint(100, 1000)) + "-" + str(randint(100, 1000)) + "-" + str(randint(100, 1000))