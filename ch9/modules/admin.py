from user import User
from privilege import Privilege


class Admin(User):
    """Admin user - instance of User class"""

    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privilege = Privilege()

