#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: 1000

def sum_numbers(number1, number2):
    # Make this function add number1 and number2 and return the value
    sum = int(number1) + int(number2)
    return sum

def subtract_numbers(number1, number2):
    # Make this function subtract number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    sum = int(number1) - int(number2)
    return sum

def multiply_numbers(number1, number2):
    # Make this function multiply number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    product = int(number1) * int(number2)
    return product

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))