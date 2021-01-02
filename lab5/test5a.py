#!/usr/bin/env python3

import lab5a        
file_name = 'data.txt'                             
print(lab5a.read_file_string(file_name))
# Will print 'Hello World\nThis is the second line\nThird line\nLast line\n'
print(lab5a.read_file_list(file_name))
# Will print ['Hello World', 'This is the second line', 'Third line', 'Last line']