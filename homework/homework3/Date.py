class Date:
    def __init__(self):
        self._day = 0
        self._month = 0
        self._year = 0

    def __str__(self):
        return str(self._day) + "/" + str(self._month) + "/" + str(self._year)

    def __eq__(self, other):
        return self._day == other.day and self._month == other.month and self._year == other.year

    def validate_day(self, day):
        if day < 1 or day > 31:
            raise ValueError("Please enter a valid day.")

    def validate_month(self, month):
        if month < 1 or month > 12:
            raise ValueError("Please enter a valid month.")

    def set_date(self, day, month, year):
        self.validate_day(day)
        self._day = day
        self.validate_month(month)
        self._month = month
        self._year = year

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    @day.setter
    def day(self, day):
        self.validate_day(day)
        self._day = day

    @month.setter
    def month(self, month):
        self.validate_day(month)
        self._month = month

    @year.setter
    def year(self, year):
        self._year = year
