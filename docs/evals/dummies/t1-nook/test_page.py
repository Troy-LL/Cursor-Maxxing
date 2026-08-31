import unittest

from page import EMPTY


class TestEmpty(unittest.TestCase):
    def test_shelves(self):
        self.assertEqual(EMPTY, "No shelves yet.")


if __name__ == "__main__":
    unittest.main()
