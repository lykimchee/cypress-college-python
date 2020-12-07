class Event:
    def validate_hour(self, hour):
        if hour < 0 or hour > 23:
            raise ValueError("Please enter a valid time.")

    def __init__(self, name, start, end, date):
        self._event_date = date
        self._event_name = str(name)

        self.validate_hour(start)
        self._start_hour = start

        self.validate_hour(end)
        self._end_hour = end

    def __str__(self):
        result = self._event_name + " is scheduled for " + str(self._event_date)
        result += " from " + str(self._start_hour) + ":00 to " + str(self._end_hour) + ":00."
        return result

    @property
    def event_date(self):
        return self._event_date

    @property
    def event_name(self):
        return self._event_name

    @property
    def start_hour(self):
        return self._start_hour

    @property
    def end_hour(self):
        return self._end_hour

    @event_date.setter
    def event_date(self, date):
        self._event_date = date

    @event_name.setter
    def event_name(self, name):
        self._event_name = name

    @start_hour.setter
    def start_hour(self, start):
        self.validate_hour(start)
        self._start_hour = start

    @end_hour.setter
    def end_hour(self, end):
        self.validate_hour(end)
        self._end_hour = end
