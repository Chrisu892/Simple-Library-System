from .User import User
from .UserList import UserList


class Test_UserList:


  def test_add_new_user(self):

    first_user_list = UserList()
    first_user = User()

    first_user.create_user({
      "username": "James123",
      "first_name": "James",
      "last_name": "Smith",
      "dob": "22/10/1992",
      "house_no": 10,
      "street_name": "Trafalgar Street",
      "postcode": "NE1 2LA",
      "email_address": "james.smith@email.com"
    })

    assert first_user_list.add_new_user(first_user) == True
    assert first_user_list.show_all_users() == True
    assert first_user_list.show_user_details("James123")


  def test_update_user_details(self):

    first_user_list = UserList()
    first_user = User()

    first_user.create_user({
      "username": "James123",
      "first_name": "James",
      "last_name": "Smith",
      "dob": "22/10/1992",
      "house_no": 10,
      "street_name": "Trafalgar Street",
      "postcode": "NE1 2LA",
      "email_address": "james.smith@email.com"
    })

    first_user_list.add_new_user(first_user)

    assert first_user_list.show_all_users()
    assert first_user_list.show_user_details("James123")

    new_user_details = {
      "username": "James123",
      "first_name": "James",
      "last_name": "Anderson",
      "dob": "22/10/1992",
      "house_no": 12,
      "street_name": "Northumberland Street",
      "postcode": "NE1",
      "email_address": "james.anderson@email.com"
    }

    assert first_user_list.update_user_details(new_user_details) == True
    assert first_user_list.show_all_users() == True
    assert first_user_list.show_user_details("James123") == True