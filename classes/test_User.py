from .User import User


class Test_User:


  def test_create_user(self):
    """Method to test creation of a new user."""

    first_user = User()

    details = {
      "username": "Ayesha123",
      "first_name": "Ayesha",
      "last_name": "Bahadur",
      "dob": "22/10/1994",
      "house_no": 12,
      "street_name": "Trafalgar Street",
      "postcode": "NE1 2LA",
      "email_address": "ayesha@email.com"
    }

    assert first_user.create_user(details) == True
    assert first_user.get("username") == "Ayesha123"
    assert first_user.get_full_name() == "Ayesha Bahadur"


  def test_update_user(self):
    """Method to test updating the user."""

    first_user = User()

    details = {
      "username": "James123",
      "first_name": "James",
      "last_name": "Smith",
      "dob": "22/10/1992",
      "house_no": 10,
      "street_name": "Trafalgar Street",
      "postcode": "NE1 2LA",
      "email_address": "james.smith@email.com"
    }

    first_user.create_user(details)

    assert first_user.update_user(details) == True
    assert first_user.get_full_name() == "James Smith"
    assert first_user.set("first_name", "Tim") == True
    assert first_user.get("first_name") == "Tim"
    assert first_user.get("last_name") == "Smith"
    assert first_user.get_full_name() == "Tim Smith"