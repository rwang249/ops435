#!/usr/bin/env python3

import sys

mark = int(sys.argv[1])

if mark < 60:
    grade = 'D'
elif mark >= 60 and mark < 70:
    grade = 'C'
elif mark >= 70 and mark < 80:
    grade = 'B'
else:
    grade = 'A'

print('Your grade is: ' + grade)
