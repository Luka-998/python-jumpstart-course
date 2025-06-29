
# same code as in .ipynb

print('-'*60)
string= 'JOURNAL_APP'
print(f'{string:^60}')
print('-'*60)

previous_entries = []
while True:
    print('What do you want to do? [L]ist, [A]dd or E[x]it ?')
    user_entry = input().strip().upper()
    if user_entry == 'L':
        if not previous_entries:
            print('There is no previous entries!\n Please enter your #1 Journal entry!')
        else:
            for i,entry in enumerate(previous_entries,start = 1):
                print(f'{i}.{entry}')
    elif user_entry == 'A':
        print('Please write the Journal entry below.')
        entry = input()
        previous_entries.append(entry)
    elif user_entry == 'X':
         print('That''s it for today')
         break
    else:
        print('Invalid option, please choose [L], [A] or [X] !')