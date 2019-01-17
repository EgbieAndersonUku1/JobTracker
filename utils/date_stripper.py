

class Date(object):

    class Strip(object):

        @staticmethod
        def year_month_and_day_from_date_str(date_str):
            """get_year_month_and_day_from_date_str(str) -> return tuple in the form of (year, month, day)"""

            year, month, day = date_str.split("-")

            return {"year": int(year), "month": int(month), "day": int(day)}

        @staticmethod
        def hour_and_minute_from_time_str(time_str):
            """get_hour_and_minute_from_time_str> return tuple in the form of (hr, sec)"""

            hrs, mins = time_str.split(":")
            return {"hrs": int(hrs), "mins": int(mins)}