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

            # Print notification
            print(f"Found '{prop}' ID: {entity.get(value)}")

            # Return the entity
            found_entities.append(entity)

      except:
        # Catch any unexpected errors and notify the user
        print(f"Could not find entity ID, property '{prop}' is not defined.")
        return False

      else:
        print(f"Found {len(found_entities)} entities.")
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


  def create_table_row(self, col1:str, col2:str, col3:str, col4:str) -> None:
    """Method to create a table row with four columns."""
    print(f"| {col1}{' ' * (14 - len(col1))}| {col2}{' ' * (14 - len(col2))}| {col3}{' ' * (14 - len(col3))}| {col4}{' ' * (14 - len(col4))}|")

  def create_table_border(self) -> None:
    """Private method to create table bottom or top border."""
    print(f"+{'-' * 15}+{'-' * 15}+{'-' * 15}+{'-' * 15}+")