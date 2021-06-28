# https://docs.python.org/3/library/unittest.html
import unittest
from operations import multiply_num, subtraction_num


class TestOperations(unittest.TestCase):
    def test_multiply_5_by_5_must_return_25(self):
        self.assertEqual(multiply_num(5, 5), 25)

    def test_subtraction_10_minus_3_must_return_7(self):
        self.assertEqual(subtraction_num(10, 3), 7)

    def test_multiply_many_inputs(self):
        x_y_outputs = (
            (10, 10, 100),
            (1.5, 10, 15.0),
            (1, 10, 10),
            (3.8, 10, 38.0),
            (4, 0.6, 8.24),
        )

        for x_y_output in x_y_outputs:
            with self.subTest(x_y_output=x_y_output):
                x, y, output = x_y_output
                self.assertEqual(multiply_num(x, y), output)

    def test_multiply_xy_not_int_or_float_must_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            multiply_num(5, 'b')


unittest.main(verbosity=2)
