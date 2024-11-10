import unittest
from math_quiz import random_int, random_operator, get_problem_answer


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if the random operator function returns one of the expected operators
        for _ in range(1000):
            operator = random_operator()
            self.assertIn(operator, ['+', '-', '*'])  # Check if the operator is valid
        pass

    def test_get_problem_answer(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 4, '-', '3 - 4', -1),
                (7, 8, '*', '7 * 8', 56),
                (9, 5, '-', '9 - 5', 4),
                (6, 3, '+', '6 + 3', 9),
                (10, 2, '*', '10 * 2', 20),
                (1, 1, '-', '1 - 1', 0),
                (4, 6, '+', '4 + 6', 10)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # get answer for function
                problem, answer = get_problem_answer(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
