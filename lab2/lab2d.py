#!/usr/bin/env python3

import sys

script = sys.argv[0]
arguments = len(sys.argv)

if arguments != 3:
    print('Usage: ' + script + ' name age')
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]
print('Hi ' + name + ', you are ' + str(age) + ' years old.')
