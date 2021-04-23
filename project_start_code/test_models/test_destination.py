import unittest
from models.destination import Destination

class TestDestination(unittest.TestCase):
    def setUp(self):
        self.paris = Destination("Paris", False, "France")
        self.madrid = Destination("Madrid", True, "Spain")
    
    def test_destination_has_city_name(self):
        self.assertEqual("Paris", self.paris.city_name)
    
    def test_destination_has_been_visted_False(self):
        self.assertEqual(False, self.paris.visited)
    
    def test_destination_has_been_visted_true(self):
        self.assertEqual(True, self.madrid.visited)
    
    # def test_destination_has_city_name(self):
    #     self.assertEqual("France", self.paris.country)
