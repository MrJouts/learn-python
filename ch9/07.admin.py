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


class Admin(User):
    """Admin user - instance of User class"""

    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges of " + self.get_full_name() + ":")
        for privilege in self.privileges:
            print(" - " + privilege)


admin = Admin("Carlos", "Quinto", "masculino", 43)
admin.show_privileges()
