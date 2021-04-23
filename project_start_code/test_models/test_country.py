import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.france = Country("France", 1)


    def test_country_has_name(self):
        self.assertEqual("France", self.france.name)