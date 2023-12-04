import unittest

from my_classes.dog import Dog


class DogTest(unittest.TestCase):

    def test_speak(self):
        fido = Dog()
        fido.speak()


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
