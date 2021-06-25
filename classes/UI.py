class UI:

  def create_table_row(self, col1:str, col2:str, col3:str = None, col4:str = None) -> None:
    """Method to create a table row with four columns."""

    string = f"+{'-' * 16}+{'-' * 16}+"

    if col3 != None:
      string += f"{'-' * 16}+"

    if col4 != None:
      string += f"{'-' * 16}+"

    string += f"\n| {col1}{' ' * (15 - len(col1))}| {col2}{' ' * (15 - len(col2))}|"

    if col3 != None:
      string += f" {col3}{' ' * (15 - len(col3))}|"

    if col4 != None:
      string += f" {col4}{' ' * (15 - len(col4))}|"

    print(string)


  def create_table_border(self, cols:int = 2) -> None:
    """Private method to create table bottom or top border."""

    string = f"+{'-' * 16}"
    string = string * cols
    string += "+"

    print(string)