from unittest import TestCase

from payment.pay import Pay


class PayTest(TestCase):

    def setUp(self):

        start_date = "2019-01-17"
        start_time = "10:00"

        end_date = "2019-01-17"
        end_time = "10:00"

        self.pay = Pay(start_date, start_time, end_date, end_time)

    def test_if_zero_pay_is_returned_if_no_hours_are_worked__Should_return_zero_pay(self):

        expected_wage = 0.0

        self.pay.calculate_rate(hourly_rate=1)
        self.assertEqual(self.pay.get_daily_rate, expected_wage)

    def test_if_zero_pay_is_returned_if_hourly_rate_is_zero__Should_return_zero_pay(self):

        expected_wage = 0.0

        self.pay.set_end_time(end_time="16:00")
        self.pay.calculate_rate(hourly_rate=0.00)

        self.assertEqual(self.pay.get_daily_rate, expected_wage)

    def test_if_correct_pay_is_returned_if_user_works_one_hour__Should_return_correct_pay(self):

        expected_wage = 1.0

        self.pay.set_end_time(end_time="11:00")
        self.pay.calculate_rate(hourly_rate=1.00)

        self.assertEqual(self.pay.get_daily_rate, expected_wage)

    def test_if_correct_pay_is_returned_if_user_works_a_time_half__Should_return_correct_pay(self):

        expected_wage = 1.5

        self.pay.set_end_time(end_time="11:30")
        self.pay.calculate_rate(hourly_rate=1.00)

        self.assertEqual(self.pay.get_daily_rate, expected_wage)

