from payment.hrs_calculator import HoursCalculator


class Pay(object):
    """Calculates the wages of a given user"""

    def __init__(self, start_date, start_time, end_date, end_time):
        self._start_date = start_date
        self._start_time = start_time
        self._end_date = end_date
        self._end_time = end_time
        self._wages = 0.0

    def set_new_start_date(self, start_date):
        """set_new_start_date(str) -> None

        Allows the user to set a new start date without having to create a new object.
        The start date must be entered in the form of (YYYY-MM-DD)
        """
        self._start_date = start_date

    def set_start_time(self, start_time):
        """set_start_time(str) -> None

        Allows the user to set a new start time without having to create new object
        The start time must be entered in form (HH:MM) and in 24 hrs mode
        """
        self._start_time = start_time

    def set_end_date(self, end_date):
        """set_end_date(str) -> None

        Allows the user to set a new end date without having to create a new object.
        The end date must be entered in the form of (YYYY-MM-DD)
        """
        self._end_date = end_date

    def set_end_time(self, end_time):
        """set_start_time(str) -> None

        Allows the user to set a new end time without having to create new object
        The end time must be entered in form (HH:MM) and in 24 hrs mode
        """
        self._end_time = end_time

    def calculate_rate(self, hourly_rate):
        """calculate_rate(int) -> None

        Calculates the daily rate of particular job/shift
        The daily rate is calculated based on units

        :param
            hourly_rate: The hourly rate pay

        >>> start_date = "2019-01-17"
        >>> start_time = "12:00"
        >>> end_date = "2019-01-17"
        >>> end_time = "20:00"
        >>> my_pay = Pay(start_time, start_time, end_date, end_time)
        >>> my_pay.calculate_rate(hourly_rate=8)
        >>> my_pay.get_daily_rate
        80.0
        """
        total_hrs = HoursCalculator.calculate_hrs(self._start_date, self._start_time, self._end_date, self._end_time)
        self._wages = float(hourly_rate) * Pay._hrs_to_units(total_hrs)

    @property
    def get_daily_rate(self):
        """Returns the daily pay rate. Note the calculate_rate must be called first
           or after anytime a new date or new time has been set
        """
        return self._wages

    @staticmethod
    def _hrs_to_units(total_hrs):
        """_hrs_to_units(float) -> returns float

        Takes the total hours worked and converts into units.

        For example:

        1 min is equal to 0.02 units
        30 mins is equal to 0.5 units
        """
        mins = total_hrs * 60
        return round(mins/60, ndigits=2)