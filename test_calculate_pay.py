from unittest import TestCase

from calculate_pay import calculate_pay


class TestCalculatePay(TestCase):
    def test_calculate_pay_lowest_regular_hour(self):
        self.assertEqual(20, calculate_pay(1, 20))

    def test_calculate_pay_middle_regular_hour(self):
        self.assertEqual(400, calculate_pay(20, 20))

    def test_calculate_pay_highest_regular_hour(self):
        self.assertEqual(800, calculate_pay(40, 20))

    def test_calculate_pay_overtime(self):
        self.assertEqual(840, calculate_pay(41, 20))

    def test_calculate_pay_zero_hour(self):
        self.assertEqual(0, calculate_pay(0, 20))

    def test_calculate_pay_zero_wage(self):
        self.assertEqual(0, calculate_pay(40, 0))

    def test_calculate_pay_lower_than_zero_hour(self):
        self.assertEqual(0, calculate_pay(-1, 20))

    def test_calculate_pay_lower_than_zero_wage(self):
        self.assertEqual(0, calculate_pay(20, -1))
