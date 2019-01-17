from unittest import TestCase

from payment.hrs_calculator import HoursCalculator


class HoursCalculatorTest(TestCase):

    def test_calculate_the_hours_when_the_start_and_end_time_are_the_same__Should_return_zero(self):

        expected_hrs = 0

        start_date = "2019-01-17"
        start_time = "10:00"

        end_date = "2019-01-17"
        end_time = "10:00"

        hrs = HoursCalculator.calculate_hrs(start_date, start_time, end_date, end_time)
        self.assertEqual(hrs, expected_hrs)

    def test_calculate_the_hours_between_two_different_times_on_the_same_day__Should_return_the_hours(self):
        """"""

        expected_hrs = 10

        start_date = "2019-01-17"
        start_time = "10:00"

        end_date = "2019-01-17"
        end_time = "20:00"

        hrs = HoursCalculator.calculate_hrs(start_date, start_time, end_date, end_time)
        self.assertEqual(hrs, expected_hrs)

    def test_the_hours_when_start_time_starts_on_one_day_and_finish_time_ends_on_another_day_Should_return_the_hours(self):
        """"""

        expected_hrs = 15

        start_date = "2019-01-17"
        start_time = "10:00"

        end_date = "2019-01-18"
        end_time = "01:00"

        hrs = HoursCalculator.calculate_hrs(start_date, start_time, end_date, end_time)
        self.assertEqual(hrs, expected_hrs)



