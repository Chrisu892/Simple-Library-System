class EntityList:


  # Class constructor
  def __init__(self) -> None:
    self.entities = list()


  def find_id_by(self, prop) -> str:
    while True:
      try:
        keyword = str(input(f"Find entity ID by {prop}: "))

        for entity in self.entities:
          if entity.get(prop) == keyword:
            print(f"Found '{prop}' ID: {entity.get('id')}")
            return entity.get("id")

        print(f"Entity with property '{prop}' does not exist.")

      except ValueError:
        print(f"Could not find entity ID, '{prop}' is not defined.")



  def count(self) -> int:
    """Return the number of entities."""
    return len(self.entities)


  def show_all(self) -> list:
    """Return the list of entities."""
    return self.entities