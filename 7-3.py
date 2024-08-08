class ExceptA(Exception):
    def __str__(self):
        return "例外Aが発生しました"

try:
    raise ExceptA()
except ExceptA as ea
    print(ea)
except:
    print('Unexpected Error:', sys.exc_info())

import sys

class MyValueLimitError(Exception):
    def __init__(self, x1, x2, limit_number):
        self.x1 = x1
        self.x2 = x2
        self.limit_number = limit_number

    def __str__(self):
        return '値の取りうる範囲を超えています{0} {1} {2} '.format
