class EntityList:


  def __init__(self) -> None:
    """EntityList class constructor."""
    self.entities = list()


  def find(self, prop:str = "id", value = "id", label = None):
    """Public method to find the entity in the list of entities by their property name
    and return its property value or any other property value."""

    while True:
      try:
        # Prompt the user to enter a keyword
        keyword = str(input(f"Find {label if label != None else ''} {prop} by {value}: "))

        # Check if user forced to cancel the search operation
        if keyword == 'q':
          print('Operation has been canceled!')
          break

        # Loop through each entity in the list of entities
        for entity in self.entities:
          # Check if the value of the property inside entity object is equal to user keyword
          if entity.get(prop) == keyword:
            # Print notification
            print(f"Found '{prop}' ID: {entity.get(value)}")
            # Return the entity
            return entity

        # Notify program user that the property is undefined
        print(f"Entity with property '{prop}' set to '{keyword}' does not exist.")

      except:
        # Catch any unexpected errors and notify the user
        print(f"Could not find entity ID, property '{prop}' is not defined.")

    return False


  def remove(self, prop:str, value:str) -> bool:
    """Public method to remove entity from the list of entities."""

    # Iterate through list of entities
    for idx, entity in enumerate(self.entities):
      # Check if entity's property value is equal to specified value
      if entity.get(prop) == value:
        # Delete entity from the list of entities
        del self.entities[idx]
        # Notify the user about successful operation
        print(f"\nEntity '{value}' has been removed.")
        # Return True
        return True

    # Notify the user that the entity could not be found and operation failed
    print(f"\nEntity '{value}' could not be removed. '{value}' does not exists!")
    return False


  def show(self, prop:str, value:str):
    """Public method to show entity details from the list of entities."""

    # Iterate through list of entities
    for entity in self.entities:
      # Check if entity's property value is equal to specified value
      if entity.get(prop) == value.lower():
        # Return the entity object back to the caller
        return entity

    # If entity wasn't found, then return True
    return False


  def show_all(self) -> list:
    """Return the list of entities."""
    return self.entities


  def count(self) -> int:
    """Return the number of entities."""
    return len(self.entities)