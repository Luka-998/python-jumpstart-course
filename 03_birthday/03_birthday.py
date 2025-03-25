print("-"*60)
print(f" "*20,'BIRTHDAY_APP'," "*20)
print('-'*60)

from datetime import date,datetime,timedelta

def user_input(): # ova funkcija ce biti bd
    print('What year you were born?: ')
    year = int(input())
    print('Month??:__')
    month = int(input())
    print('What day? __')
    day = int(input())
    birthday=datetime(year,month,day)
    return birthday # 1998/7/30

def time_to_birthday(my_birthday): #definisan parametar my_birthday koji je zapravo return iz prve funkcije
    current_date = datetime.now() # object datetime vraca yyyy mm dd hhmmss / od cega mi treba samo DD
    next_birthday = my_birthday.replace(current_date.year) # ovo obezbedjuje varijablu 'next_birthday', koriscenjem replace i current_date.year omoguci ce ispravan objekat za oduzimanje
    # ovaj deo petlje treba da definise uslov ukoliko je rodjendan vec prosao ove godine:
    # razmisli dobro ovde, ovo je najbitniji deo celog koda
    if current_date < next_birthday: # ovde ne radi jer on my birthday gleda kao 1998 7 30 :D
        days_to_birthday = (next_birthday-current_date).days  # .days obezbedjuje da se vrate samo dani, jer zelimo da izracunamo u danima koliko je ostalo
        print(f"You have {days_to_birthday} days to your Birthday!")
        return days_to_birthday
    else:
        next_birthday = my_birthday.replace(current_date.year+1)
        days_to_birthday = (next_birthday-current_date).days
        print(f"Your birthday is coming in {days_to_birthday} days! (It has already passed in this year)")

bd = user_input()
time_to_birthday(bd)






