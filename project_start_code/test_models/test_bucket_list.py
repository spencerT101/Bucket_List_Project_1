import unittest
from models.bucket_list import Bucket_list
from models.country import Country
from models.destination import Destination


class TestBucketList(unittest.TestCase):
    def setUp(self):
        self.bucket_list1 = Bucket_list("Paris")
    

    def test_list_has_destination(self):
        self.assertEqual("Paris", self.bucket_list1.destination)