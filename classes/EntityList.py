class EntityList:


  # Class constructor
  def __init__(self) -> None:
    self.entities = list()


  # # Add entity to the list of entities
  # def add(self, entity:object) -> bool:
  #   print("Add Entity to the Entity List")
  #   return self.entities.append(entity)

  
  # # Remove entity from the list of entities
  # def remove(self, string:str) -> bool:
  #   print("Remove entity from entities where entity[key] == value")
  #   # Search self.entities and remove specified entity
  #   # For example:
  #   # DELETE entity FROM self.entities WHERE entitity[key] == value
  #   pass


  # Count number of entities in the list
  def count(self) -> int:
    return len(self.entities)