class User:
    """My first user class"""

    def __init__(self, first_name, last_name, gender, age):
        """Initialize first_name an last_name atributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def get_full_name(self):
        """Make full name"""
        return self.first_name.title() + " " + self.last_name.title()

    def describe_user(self):
        """Describes user attributes"""
        print("User details:")
        print(" - Nombre: " + self.first_name.title())
        print(" - Apellido: " + self.last_name.title())
        print(" - Genero: " + self.gender.title())
        print(" - Edad: " + str(self.age))

    def greet_user(self):
        """Greeting the user"""
        print("Hello " + self.get_full_name())


class Privilege:
    """List of user privileges"""

    def __init__(self, privileges=[]):
        """Define user privileges"""
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Show user privileges"""
        print("Privileges :")
        for privilege in self.privileges:
            print(" - " + privilege)


class Admin(User):
    """Admin user - instance of User class"""

    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privilege = Privilege()


admin = Admin("Carlos", "Quinto", "masculino", 43)
admin.privilege.show_privileges()
