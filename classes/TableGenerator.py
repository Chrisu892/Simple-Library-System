class TableGenerator:

  def create_table(self, rows:list):
    """Method to create a table with X number of columns."""

    border = self.create_table_border(len(rows[0].__dict__.items()))
    table = border + "\n|"

    for col in rows[0].__dict__.items():
      table += f" {col[0]}{' ' * (19 - len(str(col[0])))}|"

    table += "\n" + border

    for row in rows:
      table += "\n|"

      for col in row.__dict__.items():
        table += f" {col[1]}{' ' * (19 - len(str(col[1])))}|"

      table += "\n" + border

    print(table)


  def create_table_row(self, col1:str, col2:str, col3:str = None, col4:str = None) -> None:
    """Method to create a table row with four columns."""

    string = f"+{'-' * 20}+{'-' * 20}+"

    if col3 != None:
      string += f"{'-' * 20}+"

    if col4 != None:
      string += f"{'-' * 20}+"

    string += f"\n| {col1}{' ' * (19 - len(str(col1)))}| {col2}{' ' * (19 - len(str(col2)))}|"

    if col3 != None:
      string += f" {col3}{' ' * (19 - len(str(col3)))}|"

    if col4 != None:
      string += f" {col4}{' ' * (19 - len(str(col4)))}|"

    print(string)


  def create_table_border(self, cols:int = 2) -> str:
    """Method to create table bottom or top border."""

    string = f"+{'-' * 20}"
    string = string * cols
    string += "+"

    return string