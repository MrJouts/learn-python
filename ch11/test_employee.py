import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for the employee"""

    def setUp(self):
        """Create an Employee and set his/her salary"""
        self.salary = 40000
        self.custom_rise = 7500
        self.employee = Employee("Carlos", "Zapata", self.salary)

    def test_default_rise(self):
        """Test if the salary increments in 5000"""
        self.employee.give_raise()
        self.assertEqual(self.employee.anual_salary, self.salary + 5000)

    def test_custom_rise(self):
        """Test if the salary increments the value given"""
        self.employee.give_raise(self.custom_rise)
        self.assertEqual(self.employee.anual_salary, self.salary + self.custom_rise)


unittest.main()
