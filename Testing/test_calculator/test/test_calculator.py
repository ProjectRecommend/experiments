import unittest

# importing calculator from app directory
from app.calculator import Calculator

class TddInPythonExample(unittest.TestCase):
    # to keep the computer ready for all the TestCases
    def setUp(self):
        self.calc = Calculator()

    # addition using Calculator
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        # method assertEqual checks whether the value in result is equal
        # to the number given as argument i.e 4
        self.assertEqual(4, result)


    # subraction using Calculator
    def test_calculator_sub_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.sub(2,2)
        self.assertEqual(0, result)


    # multiplication using Calculator
    def test_calculator_mul_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.mul(2,2)
        self.assertEqual(4, result)


    # division using Calculator
    def test_calculator_div_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.div(2,2)
        self.assertEqual(1, result)



    # raising error message while addition
    # this method raises exception if wrong inputs such as
    # words are given instead of numbers
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    # adding a testcase where one might be a number and other may not be
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)

    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')


    # raising error message while subraction
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.sub, 'two', 'three')

    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.sub, 'two', 3)

    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.sub, 2, 'three')


    # raising error message while multiplication
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.mul, 'two', 'three')

    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.mul, 'two', 3)

    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.mul, 2, 'three')


    # raising error message while division
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.div, 'two', 'three')

    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.div, 'two', 3)

    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.div, 2, 'three')

if __name__ == '__main__':
    unittest.main()
