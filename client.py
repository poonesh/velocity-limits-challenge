from collections import deque
from vlc_date import Date


class Client():
    """
    This class creates a Client object with all the features of an account.
    """
    def __init__(self, client_ID):
        self.client_id = client_ID
        self.max_daily_load = 5000
        self.max_weekly_load = 20000
        self.max_num_load_daily = 3
        self.num_loads_currentday = 0
        self.last_load_date = None
        self.loadamount_currentday = 0
        self.loadamount_currentweek = 0

    def initiate_daily_load(self, load_date):
        date = Date()
        date.set_from_string(load_date)
        if self.last_load_date is None or self.last_load_date.is_different_date(date):
            self.last_load_date = date
            self.loadamount_currentday = 0
            self.num_loads_currentday = 0

    def check_daily_load_exceeded(self, load_amount):
        if load_amount > self.max_daily_load:
            return True
        if self.max_daily_load - self.loadamount_currentday < load_amount:
            return True
        if self.num_loads_currentday > self.max_num_load_daily:
            return True
        return False

    def update_daily_load(self, load_amount):
        self.loadamount_currentday += load_amount
        self.num_loads_currentday += 1

    def initiate_weekly_load(self, load_amount, load_date):
        date = Date()
        date.set_from_string(load_date)
        if date.is_different_week(load_date):
            self.loadamount_currentweek = 0         

    def check_weekly_load_exceeded(self, load_amount):
        if load_amount > self.max_weekly_load:
            return False
        if self.max_weekly_load - self.loadamount_currentweek < load_amount:
            return False
        return True

    def update_weekly_load(self, load_amount, load_date):
        self.loadamount_currentweek += load_amount



    def load(self, load_amount, load_date):
        A = self.check_daily_load_exceeded(load_amount)
        B = self.check_weekly_load_exceeded(load_amount)
        if not A and not B:
            self.initiate_daily_load(load_amount, load_date)
            self.update_daily_load(load_amount, load_date)
            self.initate_weekly_load(load_amount, load_date)
            self.update_weekly_load(load_amount, load_date)
            return True
        return False
