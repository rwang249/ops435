#!/usr/bin/env python3

def square(number):
    return number ** 2

def sum_numbers(number1, number2):
    return int(number1) + int(number2)

print(square(5))
print(square(10))
print(square(12))
print(square(square(2)))
print(square(int('2')))

print(sum_numbers(5, 10))
print(sum_numbers(5, 100))
print(square(sum_numbers(5, 5)))
