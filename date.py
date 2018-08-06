import datetime


class Date():
	"""
	"""
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def set_from_string(self, string):
        self.year = date[0:4]
        self.month = date[5:7]
        self.day = date[8:10]

    def is_different_date(self, other):
        year = self.year == other.year
        month = self.month == other.month
        day = self.day == other.day
        if year and month and day:
            return True
        return False

    def is_different_week(self, other):
        day = datetime.datetime(self.year, self.month, self.day)
        other_day = datetime.datetime(other.year, other.month, other.day)
        delta = other_day - day
        if delta >= 7:
            return True
        if delta < 7 and other_day.weekday() < day.weekday():
            return True
        return False

        