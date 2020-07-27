from user import User
from admin import Admin

user = User("Maria", "Vasualdo", "femenino", 38)
user.describe_user()
user.greet_user()

admin = Admin("Carlos", "Quinto", "masculino", 43)
admin.privilege.show_privileges()
