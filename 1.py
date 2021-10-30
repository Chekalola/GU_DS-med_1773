class Date:
    def __init__(self, data):
        if self.validate(data):
            self.day, self.month,self.year = map(int, data.split('-'))

    @staticmethod
    def validate(data):
        try:
            day, month, year = map(int, data.split('-'))
        except ValueError:
            return False
        if not 0 < month < 13:
            return False
        if not 0 < day < 30:
            return False
        if not 0 < year < 99:
            return False
        return True

    @classmethod
    def explode(cls, data):
        date = cls(data)
        return date.day, date.month, date.year

data = input('Введите дату:')
obj = Date.validate(data)
print(obj)
