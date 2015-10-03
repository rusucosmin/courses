import time
from datetime import date

today = date.today();

# ivlad@cs.ubbcluj.ro

bday, bmonth, byear = map(int, input("Please enter the date, the month and the year in one line separated by a space").split())

birthday = date(byear, bmonth, bday)

time_to_bday = today - birthday;

print("yay, you lived ", time_to_bday.days, " days! Long live!");
