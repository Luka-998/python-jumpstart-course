

print('-'*60)
print(f'{'BIRTHDAY_APP':^60}')
print('-'*60)

from datetime import datetime

def user_birthday():
    year = int(input('What year were you born [YYYY]? '))
    month = int(input('What month were you born [MM]? '))
    day = int(input('What day were you born [DD]? '))
    return month, day  # No need to return year

def time_to_birthday(birth_month, birth_day):
    today = datetime.today()
    current_year = today.year

    try:
        next_birthday = datetime(current_year, birth_month, birth_day)
    except ValueError:  # Handles Feb 29 in non-leap years
        next_birthday = datetime(current_year + 1, birth_month, birth_day)

    if next_birthday < today:
        next_birthday = datetime(current_year + 1, birth_month, birth_day)

    days_remaining = (next_birthday - today).days

    months_remaining = days_remaining // 30
    extra_days = days_remaining % 30

    print(f"Your next birthday is in {months_remaining} months and {extra_days} days.")

# Run: 
def main():
    birth_month, birth_day = user_birthday()
    time_to_birthday(birth_month, birth_day)

if __name__ == "__main__":
    main()
