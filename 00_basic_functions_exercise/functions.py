
# 1 Sum digits
def sum_numbers(x,y):
    return x+y

sum_numbers(5,6)

# 2 Count vowels in the string 

def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

print(count_vowels('lukajasovic'))


import math
def fact_calc(number):
    return math.factorial(number)

print(fact_calc(4))  # Output: 24


# 4 Palindrome Checker


def palindrome_check(string):
    # it is the word that is same if read/written from start and from the end
    if string == string[::-1]:
        print(string)
    else:
        print("No a palindrome string!")

palindrome_check('ASDASD123')

# 5️⃣ Reverse a String

# Write a function that takes a string and returns it reversed.

def reverse_string(string):
    reverse = string[::-1]
    print(reverse)
    return reverse

reverse_string('ReverseString:)')

# 6️⃣ Find the Largest Number in a List
# Write a function that takes a list of numbers and returns the largest one.
 # TypeError: 'list' object cannot be interpreted as an integer
def pick_largest(l):
    largest = max(l)
    print(largest)
    return largest
    
l = [1660,11,1]
largest = pick_largest(l)
pick_largest(l)

#7️⃣ Fibonacci Sequence
#Write a function that returns the first n numbers of the Fibonacci sequence.

# f0 = 0
# f1 = fn-1 + fn-2 where n=1

def fibbonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n>1:
        f = fibbonachi(n-1)+fibbonachi(n-2)
        print(f)
        return f
fibbonachi(7)

# 8️⃣ Check if a Number is Prime

# Write a function that checks if a given number is prime.
import math
def is_prime(number):
    if number < 2:  # Handles negative numbers and 0, 1
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for num in range(3, int(math.sqrt(number)) + 1, 2):  #  Convert sqrt to int - This part is important because i was missing it
        if number % num == 0: 
            return False
    return True  #
# We are checking if the given number is divisible by any odd number from 3 up to its square root.
print(is_prime(19))  
print(is_prime(22))  

#9️⃣ Find the Most Frequent Element in a List

# Write a function that takes a list and returns the most frequently occurring element.

from collections import Counter

def count_frequent():
    g = Counter([1,2,3,4,5])
    print(g)


# Counter({'B': 4, 'o': 1, 'n': 1}) [B - Key : 4 - Value] -> need the most frequently occuring element

# so the counter here acts as a dictionary 

# i noticed that always the most frequent one is at position 0. 
# what about .most_common() method?
from collections import Counter

def get_frequency_new(list):
    values = Counter(list)
    most_freq = values.most_common(1)
    print(most_freq)
    print(f"Value {most_freq[0][0]} appeared {most_freq[0][1]} times")
    return most_freq

check_this_V3 = [1,1,2,2,2,2,3,3,4,4,5,6,7]

get_frequency_new(check_this_V3)

# 🔟 Convert Seconds to Hours, Minutes, and Seconds
# Write a function that converts seconds into hours:minutes:seconds format.

def time_convert(input):
    seconds = input
    hours = seconds // 3600 # leftover seconds
    remained_seconds = hours % 3600
    minutes = remained_seconds//60
    final_seconds = remained_seconds % 60
    print(f"{hours}:{minutes}:{remained_seconds}:{final_seconds}")
sec = 871
time_convert(sec)

# time object is not good aproach in this case because it represents only specific time of the day while,
# my input hours could be much bigger than 24h