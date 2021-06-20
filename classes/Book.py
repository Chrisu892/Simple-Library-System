# Import required modules
from random import randint
from typing import AnyStr


# Define Book class
class Book:


  # Class constructor
  def __init__(self) -> None:
    self.__id = self.__set_random_id()
    self.__title = str(input("Book title: "))
    self.__author = str(input("Author name: "))
    self.__year = int(input("Book year: "))
    self.__publisher_name = str(input("Publisher name: "))
    self.__publication_date = str(input("Publication date: "))
    self.__num_copies = int(input("Number of copies: "))


  # Method to return the book ID
  def get_id(self):
    try:
      return self.__id
    except KeyError:
      print("Book ID is undefined.")
      return False


  # Method to return the book title
  def get_title(self) -> str:
    try:
      return self.__title
    except KeyError:
      print("Book title is undefined.")
      return False


  # Method to get the book author
  def get_author(self):
    try:
      return self.__author
    except KeyError:
      print("Book author is undefined.")
      return False


  # Method to return the book year
  def get_year(self):
    try:
      return self.__year
    except:
      print("Book year is undefined.")
      return False


  # Method to return the publisher name
  def get_publisher_name(self):
    try:
      return self.__publisher_name
    except:
      print("Book publisher name is undefined.")
      return False


  # Method to return the publication date
  def get_publication_date(self):
    try:
      return self.__publication_date
    except:
      print("Book publication date is undefined.")
      return False


  # Method to return the number of copies
  def get_num_copies(self) -> str:
    try:
      return self.__num_copies
    except:
      print("Book number of copies in undefined.")
      return False


  # Method to return the book year
  def get_publication_date(self) -> str:
    try:
      return self.__publication_date
    except:
      print("Book publication date is undefined.")
      return False


  # Method to create random ID
  def __set_random_id(self) -> str:
    # Return, for example: 123-456-789
    return str(randint(100, 1000)) + "-" + str(randint(100, 1000)) + "-" + str(randint(100, 1000))