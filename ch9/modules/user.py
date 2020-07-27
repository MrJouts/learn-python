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

