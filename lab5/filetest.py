#!/usr/bin/env python3

f = open('data.txt', 'r')

#f.read()            # read the entire contents and return a single string object
#f.readlines()       # read the entire contents and return each line in the file as a list
#f.readline()        # return the first line, if run a second time it will return the second line, then third

read_data = f.read()
print(read_data)

#read_lines = f.readlines()
#print(read_lines)

read_data.split('\n')                       # Returns a list
list_of_lines = read_data.split('\n')       # name the returned list object as list_of_lines
print(list_of_lines)

# METHOD 1:

# f = open('data.txt', 'r')
# method1 = list(f)
# f.close()
# print(method1)

# METHOD 2:

# f = open('data.txt', 'r')
# method2 = f.readlines()
# f.close()
# print(method2)


f.close()           # close the opened file