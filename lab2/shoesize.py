#!/usr/bin/env python3

while True:
    try:
        shoeSize = int(input('What is your shoe size?'))
        if shoeSize < 1 or shoeSize > 20:
            print('Please enter a valid shoe size(1 to 20)')
            continue
    except ValueError:
        raise ValueError('Please enter a valid shoe size(1 to 20)')
        continue
    break
print('Your shoe size is: ' + shoeSize)