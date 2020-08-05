import unittest

from city_functions import get_full_city


class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like Santiago, Chile works?"""
        formatted_city = get_full_city("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago, Chile")

    def test_city_country_population(self):
        """DO cities like Buenos Aires, Argentina - population: 40000000"""
        formatted_city = get_full_city("buenos aires", "argentina", 40000000)
        self.assertEqual(
            formatted_city, "Buenos Aires, Argentina - population 40000000"
        )


unittest.main()
