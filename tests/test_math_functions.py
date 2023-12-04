import unittest

# What we are testing
import math_functions


class TestMathFunctions(unittest.TestCase):

    def test_add_two(self):
        result = math_functions.add_two(1, 2)
        self.assertEqual(result, 3)

    def test_add_many(self):
        result = math_functions.add_many(*[1, 2, 3, 4])
        self.assertEqual(result, 10)

    """
    We know that integers have to be passed in, so lets just test that 
    an exception is thrown when non integer arguments are passed in
    """
    def test_add_two_throws_exception(self):
        with self.assertRaises(ValueError):
            result = math_functions.add_two(1, "two")


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
