import unittest

from my_classes.person import Person


class PersonTest(unittest.TestCase):

    def test_person(self):
        person1 = Person("John", 21)
        self.assertEqual(person1.name, "John")
        self.assertEqual(person1.age, 21)

    def test_age_setter(self):
        person2 = Person("John", 21)
        self.assertEqual(person2.name, "John")
        self.assertEqual(person2.age, 21)

        person2.age = 50
        self.assertEqual(person2.age, 50)

        # Now validate an exception is thrown
        with self.assertRaises(Exception):
            person2.age = -1

        with self.assertRaises(Exception):
            person2.age = 130

        with self.assertRaises(Exception):
            person2.age = "one"


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
