#!/usr/bin/env python3
import ipdb
def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 0
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    numbers = [num ** 2 for num in int_list]
    return numbers

def fizzbuzz(i):
    # code goes here!
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i 
