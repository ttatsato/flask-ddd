from enum import Enum, unique


@unique
class Cuisine(Enum):
    Japanese = ('japanese', '和食')
    Western = ('western', '洋食')
    Chinese = ('chinese', '中華')

    def __new__(cls, value, *arg):
        obj = object.__new__(cls)
        obj._value = value
        return obj

    def __init__(self, *args):
        self.values = args

    def to_label(self):
        return self.values[1]