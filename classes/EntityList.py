class EntityList:


  def __init__(self) -> None:
    """EntityList class constructor."""
    self.entities = list()


  def find(self, prop:str = "id", value = "id", label = None):
    """Public method to find the entity in the list of entities by their property name and return its property value or any other property value."""

    while True:
      try:
        # Define a list to store any found entities
        found_entities = list()

        # Prompt the user to enter a keyword
        keyword = str(input(f"Find {label if label != None else ''}'s {prop}: "))

        # Check if the keyword is not empty
        if keyword == "":
          # Print a message that the keyword cannot be empty
          print(f"{label if label != None else 'Input'} cannot be empty, please try again.")
          # Proceed to the next iteration (skips exectution of any code below this line)
          continue

        # Check if the user forced to cancel this procedure
        if keyword == 'q':
          # Print a message that the procedure has been cancelled
          print('Operation has been canceled!')
          # Break out of the loop
          break

        # Loop through each entity in the list of entities
        for entity in self.entities:
          # Check if the value of the property inside entity object is equal to user keyword
          if entity.get(prop).lower() == keyword.lower():
            # Append entity to the list of entities
            found_entities.append(entity)

      except:
        # Print a message that unexpected error occurred
        print("\nError occurred in EntityList, find method.")
        # Return False
        return False

      else:
        # Check if the list of found_entities is not empty
        if len(found_entities) > 0:
          # Return the list
          return found_entities

        else:
          # Return False
          return False


  def remove(self, prop:str, value:str) -> bool:
    """Public method to remove entity from the list of entities."""

    try:
      # Iterate through list of entities
      for idx, entity in enumerate(self.entities):
        # Check if entity's property value is equal to specified value
        if entity.get(prop).lower() == value.lower():
          # Delete entity from the list of entities
          del self.entities[idx]

    except:
      return False

    else:
      return True


  def show_all(self) -> list:
    """Return the list of entities."""
    return self.entities


  def count(self) -> int:
    """Return the number of entities."""
    return len(self.entities)


  def select_from_list(self, the_list:list, prop:str):
    """Method to print the list of entities stored in the list. Program should prompt the user to select one entity and return it back to the caller."""

    try:
      # Print a message that the search returned more than 1 result
      print(f"\nYour search returned more than 1 result:\n")

      # Iterate through the list of entities
      for idx, entity in enumerate(the_list):
        # Print entity basic details
        print(f"{idx+1}. {entity.get(prop)}")

      while True:
        # Prompt the user to select an entity from the list
        selection = int(input("\nPlease select [1,2,3...]: "))

        # Check if the selection is within the list
        if selection in range(1, len(the_list) + 1):
          # Return the item from the list
          return the_list[selection - 1]

        else:
          # Print a message that the user selection was out of range.
          # The iteration will repeat itself
          print("\nSelection out of range, please try again.")

    except:
      # Print a message that unexpected error occurred
      print("Error occurred in select_from_list method.")
      # Return False
      return False