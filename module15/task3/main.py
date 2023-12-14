class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        if cls.is_date_valid(date_string):
            return cls(day, month, year)
        else:
            raise ValueError("Invalid date format or values")

    @staticmethod
    def is_date_valid(date_string):
        try:
            day, month, year = map(int, date_string.split('-'))
            if day < 1 or month < 1 or month > 12 or year < 1:
                return False
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                days_in_month[1] = 29
            return day <= days_in_month[month - 1]
        except ValueError:
            return False

    def __str__(self):
        return f"День: {self.day}    Месяц: {self.month}    Год: {self.year}"

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
