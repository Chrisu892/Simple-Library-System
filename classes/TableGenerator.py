class TableGenerator:

  def create_table(self, rows:list) -> None:
    """Dynamically create a table from the list of objects."""

    # Create a reusable table border
    border = self.create_table_border(len(rows[0].__dict__.items()))

    # Append border, new line and vertical line (left border) to the table
    table = border + "\n|"

    # Iterate through each attribute of the FIRST object in the list
    for col in rows[0].__dict__.items():
      # Create a table header from the attributes inside the first object in the lisst
      table += f" {col[0]}{' ' * (19 - len(str(col[0])))}|"

    # Append a new line and add a border between header and the first row inside the table
    table += "\n" + border

    # Iterate through each object in the list
    for row in rows:
      # Append a new line and vertical line (left border) to the table
      table += "\n|"

      # Iterate through each attribute of the object
      for col in row.__dict__.items():
        # Append cells to the table. Each cell has a value of the property
        table += f" {col[1]}{' ' * (19 - len(str(col[1])))}|"

      # Append a new line and add a bottom border to the table
      table += "\n" + border

    # Print the table
    print(table)


  def create_table_row(self, col1:str, col2:str, col3:str = None, col4:str = None) -> None:
    """Create a table row with up to 4 columns."""

    string = self.create_table_border(2)

    if col3 != None:
      string += f"{'-' * 20}+"

    if col4 != None:
      string += f"{'-' * 20}+"

    string += f"\n| {col1}{' ' * (19 - len(str(col1)))}| {col2}{' ' * (19 - len(str(col2)))}|"

    if col3 != None:
      string += f" {col3}{' ' * (19 - len(str(col3)))}|"

    if col4 != None:
      string += f" {col4}{' ' * (19 - len(str(col4)))}|"

    string += self.create_table_border(2)

    print(string)


  def create_table_border(self, cols:int = 2) -> str:
    """Method to create table bottom or top border."""

    string = f"+{'-' * 20}"
    string = string * cols
    string += "+"

    return string