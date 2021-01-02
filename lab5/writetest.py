#!/usr/bin/env python3

my_number = 1000
my_list = [1,2,3,4,5]
f = open('file3.txt', 'w')
f.write(str(my_number) + '\n')
for num in my_list:
    f.write(str(num) + '\n')
f.close()

f = open('file1.txt', 'w')
f.write('Line 1\nLine 2 is a little longer\nLine 3 is too\n')
f.close()

f = open('file2.txt', 'w')
f.write('Line 1\nLine 2 is a little longer\nLine 3 is as well\n')
f.close()

f = open('file1.txt', 'a')
f.write('This is the 4th line\n')
f.write('Last line in file\n')
f.close()
