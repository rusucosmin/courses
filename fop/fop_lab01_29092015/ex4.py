import datetime

year = int(input('input the year:'))
days = int(input('input the day:'))

data = datetime.datetime(year, 1, 1) + datetime.timedelta(days - 1)
print(data)
