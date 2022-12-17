"""
OOP class for today date processing
"""

from datetime import datetime


class Today:

    def __init__(self):
        self.y = str(datetime.now().year)
        self.m = str(datetime.now().month)
        self.d = str(datetime.now().day)
        self.h = str(datetime.now().hour)
        self.mn = str(datetime.now().minute)

    def transform(self, x:str):
        """
        transforms a number into a two-digit number

        :param x: an number
        :return: an two-digit-number

        example:
            >>>self.transform("5")
            05
        """
        return "0" + str(x) if 0 <= int(x) <= 9 else x

    def __str__(self):
        month_correspondances = {
            '1': 'January',
            '2': 'February',
            '3': 'March',
            '4': 'April',
            '5': 'May',
            '6': 'June',
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December'
        }

        string = f"We are the {self.d} {month_correspondances[self.m]} {self.y}; it's {self.transform(self.h)} : {self.transform(self.m)}"

        return string

