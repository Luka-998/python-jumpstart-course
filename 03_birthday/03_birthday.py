
"""
print('-'*60)
print(f'{'BIRTHDAY_APP':^60}')
print('-'*60)

# from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

current_date = datetime.now()
year = current_date.year
month = current_date.month
day = current_date.day
print(year)
print(month)
print(day)
print(current_date)

birth_date = datetime(year=1998,month=7,day=30)
birth_year=birth_date.year
birth_month= birth_date.month
birth_day = birth_date.day
print(birth_date)
"""

"""




""
print('What year were you born [YYYY]? ')
year= int(input())
print('What month were you born [MM]? ')
month = int(input())
print('What day were you born [DD]? ')
day = int(input())


print(f'It looks like you were born on {day}/{month}/{year}')
print(f"Looks like your birthday is in {diff.days} days")
"""
# i need to parse current_date to only months and days and subtract from my birt date .
