# Import required modules
from random import randint


# Entity class definition
class Entity:


  def __init__(self) -> None:
    """Entity class constructor."""
    self.id = self.__random_id()


  def set(self, prop, value):
    """Public method to set the property of the class."""
    try:
      setattr(self, prop, value)
    except:
      print(f"Error occurred, can't add {prop} to the class.")


  def get(self, prop):
    """Public method to get the property of the class."""
    try:
      return getattr(self, prop)
    except:
      print(f"Error occurred, can't find {prop} in the class.")


  def prompt(self, label, input_type = "str"):
    """Method to prompt the user to type some data into the program."""

    if input_type == "int":
      return int(input(f"{label}: "))
    else:
      return str(input(f"{label}: "))


  def __random_id(self) -> str:
    """Private method to generate and return the ID of the entity. For example: 123-456-768"""
    return str(randint(100, 1000)) + "-" + str(randint(100, 1000)) + "-" + str(randint(100, 1000))