#!/usr/bin/env python3
# Author ID: 1000

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        result = (int(number1) + int(number2))
        return result
    except:
        result = 'error: could not add numbers'
        return result
        #print('error: could not add numbers')

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        read_file = open(filename, 'r')
        result = read_file.readlines()
        read_file.close()
        return result
    except:
        result = 'error: could not read file'
        return result

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception