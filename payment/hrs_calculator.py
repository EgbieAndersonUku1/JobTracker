from datetime import datetime

from utils.date_stripper import Date


class HoursCalculator(object):

    @classmethod
    def calculate_hrs(cls, start_date, start_time, end_date, finish_time):
        """calculate_hrs(str, str, str, str) -> return hrs in float"""

        start_date, end_date = cls.get_start_and_end_dates_dict(start_date, end_date)
        start_time, end_time = cls._get_start_and_end_times_dict(start_time, finish_time)

        new_date = cls._calculate_diff_between_two_date_times(start_date, start_time, end_date, end_time)

        if new_date.days:
            return new_date.days + cls._secs_to_hrs(secs=new_date.seconds)
        return cls._secs_to_hrs(secs=new_date.seconds)

    @classmethod
    def _get_start_and_end_times_dict(cls, start_time, end_time):

        start_time_dict = Date.Strip.hour_and_minute_from_time_str(start_time)
        end_time_dict = Date.Strip.hour_and_minute_from_time_str(end_time)

        return start_time_dict, end_time_dict

    @classmethod
    def get_start_and_end_dates_dict(cls, start_date, end_date):
        """"""

        start_date_dict = Date.Strip.year_month_and_day_from_date_str(start_date)
        end_date_dict = Date.Strip.year_month_and_day_from_date_str(end_date)

        return start_date_dict, end_date_dict

    @classmethod
    def _calculate_diff_between_two_date_times(cls, start_date, start_time, end_date, end_time):
        """_calculate_diff_between_two_date_times(dict, dict, dict, dict) -> time obj
        """

        date_one = datetime(start_date['year'], start_date['month'], start_date['day'], start_time['hrs'], start_time['mins'])
        date_two = datetime(end_date['year'], end_date['month'], end_date['day'], end_time['hrs'], end_time['mins'])

        return date_two - date_one

    @classmethod
    def _secs_to_hrs(cls, secs):
        return secs / 3600