import datetime


class Date():
    """
    Creates a Date object.
    """
    def __init__(self, year=1970, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    def set_from_string(self, string):
        """
        Updates the year, month and day of the class object given a date in 
        the format of "year-month-day".
        """
        self.year = int(string[0:4])
        self.month = int(string[5:7])
        self.day = int(string[8:10])

    def is_different_date(self, other):
        """
        Checks if a given date(other) is different from the date object.
        """
        year = self.year == other.year
        month = self.month == other.month
        day = self.day == other.day
        if year and month and day:
            return False
        return True

    def is_different_week(self, other):
        """
        Checks if a given date(other) is in a different week of the object date.
        The parameter other passed to the method is assumed to be a future day.
        """
        day = datetime.datetime(self.year, self.month, self.day)
        other_day = datetime.datetime(other.year, other.month, other.day)
        delta = (other_day - day).days
        if delta >= 7:
            return True
        if delta < 7 and other_day.weekday() < day.weekday():
            return True
        return False

       