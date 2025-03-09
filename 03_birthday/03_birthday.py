print('-'*60)
print(f'{'BIRTHDAY_APP':^60}')
print('-'*60)

from datetime import datetime, timedelta

def user_input():
    print('Years?')
    year = int(input())
    print('Months?')
    month = int(input())
    print('Days?')
    day = int(input())
    birthday = datetime(year, month, day)
    return birthday  # Returns <class 'datetime.datetime'>

def time_to_birthday(my_birthday):
    current_date = datetime(year=2025, month=3, day=8)

    # Adjust my_birthday to this year birthday
    next_birthday = my_birthday.replace(year=current_date.year)

    # If birthday has already passed this year
    if next_birthday < current_date:
        next_birthday = next_birthday.replace(year=current_date.year + 1)

    days_remaining = (next_birthday - current_date).days  # This is an integer 
    print(f"Your next birthday is in {days_remaining} days.")
    return days_remaining  # Returning just the number of days

# Run the program
bd = user_input()
time_to_birthday(bd)
