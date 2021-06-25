class EntityList:


  def __init__(self) -> None:
    """EntityList class constructor."""
    self.entities = list()


  def find(self, prop:str = "id", value = "id", label = None):
    """Public method to find the entity in the list of entities by their property name
    and return its property value or any other property value."""

    while True:
      try:
        # Define a variable to store a list of found entities
        found_entities = list()

        # Prompt the user to enter a keyword
        keyword = str(input(f"Find {label if label != None else ''} {prop}: "))

        # Check if user forced to cancel the search operation
        if keyword == 'q':
          print('Operation has been canceled!')
          break

        # Loop through each entity in the list of entities
        for entity in self.entities:

          # Check if the value of the property inside entity object is equal to user keyword
          if entity.get(prop).lower() == keyword.lower():

            # Show message that entity has been found
            print(f"{label if label != None else 'Entity'} has been found!\n")

            # Return the entity
            found_entities.append(entity)

      except:
        return False

      else:
        return found_entities


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


  def show(self, prop:str, value:str):
    """Public method to show entity details from the list of entities."""

    # Define a variable to store a list of found entities
    found_entities = list()

    # Iterate through list of entities
    for entity in self.entities:
      # Check if entity's property value is equal to specified value
      if entity.get(prop).lower() == value.lower():
        # Return the entity object back to the caller
        found_entities.append(entity)

    # If entity wasn't found, then return True
    return found_entities


  def show_all(self) -> list:
    """Return the list of entities."""
    return self.entities


  def count(self) -> int:
    """Return the number of entities."""
    return len(self.entities)