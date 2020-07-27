from user import User

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

