import unittest
from app.main import add


class TransformTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2, add(1, 1))
