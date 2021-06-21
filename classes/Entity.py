# Import required modules
from random import randint


# Entity class definition
class Entity:


  # Class constructor
  def __init__(self) -> None:
    self.__id = self.__set_random_id()


  # Public method to return the entity ID
  def get_id(self):
    try:
      return self.__id
    except KeyError:
      print("Book ID is undefined.")
      return False


  # Private method to create random ID
  def __set_random_id(self) -> str:
    # Return, for example: 123-456-789
    return str(randint(100, 1000)) + "-" + str(randint(100, 1000)) + "-" + str(randint(100, 1000))