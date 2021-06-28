"""
TDD - Test Driven development

Red
Step 1 - Build the test and look the failure

Green
Step 2 - Build the code and look the test finish succesfuly

Refactor
Step 3 - Improve my code

"""

import unittest
from baconwitheggs import bacon_with_eggs


class TestBaconWithEggs(unittest.TestCase):
    def test_if_not_integer_must_raise_assertionerror(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs('')

    def test_bacon_with_eggs_must_return_baconwitheggs_if_multiple_3and5(self):
        inputs = (15, 30, 45, 60)
        output = 'Bacon with eggs'

        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(
                    bacon_with_eggs(i=input),
                    output,
                    msg=f'Input "{input}" does not return "{output}"'
                )

    def test_bacon_with_eggs_must_return_hungry_if_not_multiple_3and5(self):
        inputs = (26, 32, 11, 19)
        output = 'Hungry'

        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(
                    bacon_with_eggs(i=input),
                    output,
                    msg=f'Input "{input}" does not return "{output}"'
                )

    def test_bacon_with_eggs_must_return_bacon_if_multiple_3(self):
        inputs = (3, 6, 9, 12)
        output = 'Bacon'

        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(
                    bacon_with_eggs(i=input),
                    output,
                    msg=f'Input "{input}" does not return "{output}"'
                )

    def test_bacon_with_eggs_must_return_bacon_if_multiple_3(self):
        inputs = (5, 10, 20, 25)
        output = 'Eggs'

        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(
                    bacon_with_eggs(i=input),
                    output,
                    msg=f'Input "{input}" does not return "{output}"'
                )


unittest.main(verbosity=2)
