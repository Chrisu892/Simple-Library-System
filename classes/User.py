# Define class User
from typing import AnyStr


class User:


  # Class contructor
  def __init__(self):
    self.__id = 0
    self.__first_name = None
    self.__last_name = None
    self.__house_number = None
    self.__street_name = None
    self.__postcode = None
    self.__email_address = None
    self.__dob = None


  def create(self) -> bool:
    # IF user IS created RETURN True ELSE False
    pass


  # Method to get property of the class User
  def get(self, prop):
    try:
      # Get class property
      return self[prop]
    except KeyError:
      # Class property not found
      return False


  def set(self, prop, val) -> bool:
    try:
      # Set class property to the new value
      self[prop] = val
    except KeyError:
      # Class property not found
      return False