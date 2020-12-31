#!/usr/bin/env python3

def hello():
    print('Hello World')
    print('Inside a Function')
    return

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

my_stuff = hello()
print('Return stuff from hello():',my_stuff)
print('the object my_stuff is of type:',type(my_stuff))

text = return_text_value()
print(text)

number = return_number_value()
print('my number is ', number)
print('my number is ' + str(number))
print('my number is ' + str(return_number_value()))
print(number + 5)
print(return_number_value() + 10)
