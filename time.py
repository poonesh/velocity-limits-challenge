class Time():
	"""
	"""
    def __init__(self, hour=0, minute=0, sec=0):
        self.hour = hour
        self.minute = minute
        self.sec = sec

    def set_from_string(self, string):
        self.hour = time[0:2]
        self.minute = time[3:5]
        self.sec = time[6:9]