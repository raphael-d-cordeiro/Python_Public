"""
class Person
    __init__
        name str
        lastname str
        data_received bool (init False)

    API:
        get_all_data -> method
            OK
            404
            (data_received turn True if received data)

"""

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '..\\src'
            )
        )
    )

except:
    raise

import unittest
from unittest.mock import patch
from person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('Raphael', 'Cordeiro')

    def test_person_attr_name_have_correct_value(self):
        self.assertEqual((self.p1.name), 'Raphael')

    def test_person_attr_name_is_str(self):
        self.assertIsInstance((self.p1.name), str)

    def test_person_attr_lastname_have_correct_value(self):
        self.assertEqual((self.p1.lastname), 'Cordeiro')

    def test_person_attr_lastname_is_str(self):
        self.assertIsInstance((self.p1.lastname), str)

    def test_person_attr_data_received_init_false(self):
        self.assertFalse(self.p1.data_received)

    def test_get_all_data_succesfuly_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'Connected!')
            self.assertTrue(self.p1.data_received)

    def test_get_all_data_error_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), 'Error 404')
            self.assertFalse(self.p1.data_received)

    def test_get_all_data_succesfuly_and_error_sequential(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'Connected!')
            self.assertTrue(self.p1.data_received)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), 'Error 404')
            self.assertFalse(self.p1.data_received)


if __name__ == '__main__':
    unittest.main(verbosity=2)
