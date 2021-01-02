#!/usr/bin/env python3

# try:
#     print(5 + 'ten')
# except TypeError:
#     print('At least one of the values is NOT an integer')

try:
    f = open('filethatdoesnotexist', 'r')
    f.write('hello world\n')
    f.close()
except (FileNotFoundError, PermissionError, IsADirectoryError): 
    print('failed to open file')