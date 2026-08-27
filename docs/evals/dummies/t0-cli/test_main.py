import unittest

from main import greet


class TestGreet(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(greet(), "hello")


if __name__ == "__main__":
    unittest.main()
