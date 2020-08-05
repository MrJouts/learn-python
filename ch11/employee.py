class Employee:
    """Define an employee class"""

    def __init__(self, first_name, last_name, anual_salary):
        """Store first name, last name and anual salary of the employee"""
        self.last_name = last_name
        self.first_name = first_name
        self.anual_salary = anual_salary

    def give_raise(self, amout=5000):
        """Add $5000 or a custom amount to the salary"""
        self.anual_salary += amout
        # print("Salary uptated, new salary is: " + str(self.anual_salary))


# carlos = Employee("Carlos", "Quinto", 20000)
# print(carlos.anual_salary)
# carlos.give_raise()
# print(carlos.anual_salary)
# carlos.give_raise(70000)
# print(carlos.anual_salary)
