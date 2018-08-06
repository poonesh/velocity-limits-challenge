from collections import deque
from vlc_date import Date


class Client():
    """
    Creates a Client object with all the features of an account.
    """
    def __init__(self, client_ID):
        self.client_id = client_ID
        self.max_daily_load = 5000
        self.max_weekly_load = 20000
        self.max_num_load_daily = 3
        self.num_loads_currentday = 0
        self.last_load_date = Date()
        self.loadamount_currentday = 0
        self.loadamount_currentweek = 0

    def initiate_new_day_load(self, load_date):
        """
        Initiates the client object daily load properties if the laod_date is a new date 
        compare to the last_load_date and also if this is the very first time loading for 
        the client. It also initiates the client weekly load properties if the load_date is
        in the same week.
        """
        date = Date()
        date.set_from_string(load_date)
        if self.last_load_date.is_different_date(date):
            self.loadamount_currentday = 0
            self.num_loads_currentday = 0
            if self.last_load_date.is_different_week(date):
                self.loadamount_currentweek = 0 
            self.last_load_date = date

    def check_daily_load_exceeded(self, load_amount):
        """
        Checks if the new load meets the limits for a daily load. 
        """
        if load_amount > self.max_daily_load:
            return True
        if self.max_daily_load - self.loadamount_currentday < load_amount:
            return True
        if self.num_loads_currentday >= self.max_num_load_daily:
            return True
        return False

    def update_daily_load(self, load_amount):
        """
        Updates object daily load properties.
        """
        self.loadamount_currentday += load_amount
        self.num_loads_currentday += 1       

    def check_weekly_load_exceeded(self, load_amount):
        """
        Checks if the new load meets the limits for a weekly load. 
        """
        if load_amount > self.max_weekly_load:
            return True
        if self.max_weekly_load - self.loadamount_currentweek < load_amount:
            return True
        return False

    def update_weekly_load(self, load_amount):
        """
        Updates object weekly load property.
        """
        self.loadamount_currentweek += load_amount


    def load(self, load_amount, load_date):
        """
        Checks for daily and weekly limits and if a new load can be registered.
        """
        self.initiate_new_day_load(load_date)
        A = self.check_daily_load_exceeded(load_amount)
        B = self.check_weekly_load_exceeded(load_amount)
        if not A and not B:
            self.update_daily_load(load_amount)
            self.update_weekly_load(load_amount)
            return True
        return False


