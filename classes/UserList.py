# Import super class EntityList
from .TableGenerator import TableGenerator
from .EntityList import EntityList
from .User import User


# Define subclass UserList
class UserList(EntityList):


  def __init__(self) -> None:
    """UserList class constructor."""

    EntityList.__init__(self)
    self.Table = TableGenerator()


  def add_new_user(self, user:object = None) -> bool:
    """Public method to create a new instance of the user. If the user has been successfully created, append new user to the list of entities."""

    try:
      if user == None:
        # Create new instance of the user
        user = User()
        # Create user details
        user.create_user()

      # Append instance of the user to the list of entities
      self.entities.append(user)

    except:
      # Error occurred
      return False

    else:
      # Everything should be fine
      return True


  def remove_existing_user(self) -> bool:
    """Public method to prompt the user to enter the user's first name and invoke a function to remove entity from the list of entities."""

    try:
      # Prompt the administrator to enter the user's first name and try to find it
      users = self.find("first_name", "user")

      # If search returned more than 1 result
      if len(users) > 1:
        # Prompt the administrator to select 1 user from the list
        the_user = self.select_from_list(users, "username")

      # Alternatively, if the search returned 1 result
      elif len(users) == 1:
        # Assign the first element from the list of found results to the_user
        the_user = users[0]

      else:
        # Print a message that the system couldn't find the user
        print("\nUser not found!")

        # Return False to stop execution of the code below this line
        return False

      # If removal of the user from the list of users was successful
      if self.remove("id", the_user.get('id')):
        # Print a message that the user has been deleted
        print(f"\nUser {the_user.get('first_name')} has been removed from the system.")
        # Success, return True
        return True

      else:
        # Print a message to notify administrator that user doesn't exists
        print(f"\nFailed to remove the user. User does not exists!")
        # Failure, return Falses
        return False

    # Catch exception
    except Exception as ex:
      # Print exception message
      print(f"\nException in UserList, remove_user: {ex}")

      # Failure, return False
      return False


  def show_user_details(self, username = None) -> bool:
    """Method to find the Library user by their username and show their full information back to the administrator."""

    try:
      if username == None:
        # Prompt the administrator to type the username to find
        users = self.find("username", "username", "user")
      else:
        users = self.find("username", username, "user")

      # If the search returned any results
      if len(users) > 0:

        # Print a message that the system found x number of users with the same username
        print(f"\nYour search returned {len(users)} user{'s' if len(users) > 1 else ''}:\n")

        # Create table of users
        self.Table.create_table(users)

      else:
        # Print a message that the search returned 0 results
        print("\nYour search returned 0 results.")

    except:
      # Print a message that unexpected error occurred
      print("\nError occurred in UserList, find_user method.")
      return False

    else:
      # Everything seems OK. return True
      return True


  def update_user_details(self, details = dict()) -> None:
    """Public function to find a user by their username in the Library system. If the user exists, invoke a method to update user details."""

    try:
      if len(details.items()) > 0:
        # Find user in the list of entities
        users = self.find("username", "user", details['username'])
      else:
        # Prompt the user to enter user's username to find
        users = self.find("username", "user")

      # Check if search returned more than 1 result
      if (len(users) > 1):
        # Prompt the user to select 1 of the users from the list and set the_user
        the_user = self.select_from_list(users, "username")

      # Alternatively, if the search returned 1 result
      elif len(users) == 1:
        # Set the_user variable to be the first element from the users list
        the_user = users[0]

      else:
        # Print a message that the program couldn't find the user
        print("\nUser not found!")

        # Return False to stop the execution of the code below this line
        return False

      # If the user was found and update method returned True
      if the_user.update_user(details):
        # The execution of this method was successfull, return True
        return True

      else:
        # Couldn't update the user's details, return False
        return False

    except:
      # Print a message that unexpected error occurred
      print("\nError occurred in the update_user method.")
      return False


  def show_all_users(self) -> None:
    """Public method to show all users of the Library system."""
    
    # Check if the list of library users is not empty
    if self.count() > 0:

      # Print a message stating how many library users is in the system
      print(f"\nThe library system have {self.count()} user{'s' if self.count() > 1 else ''}:\n")

      # Show table of users
      self.Table.create_table(self.show_all())
      return True

    else:
      # Print the message that the library system doesn't have any users
      print(f"\nThe library system have 0 users.")
      return False