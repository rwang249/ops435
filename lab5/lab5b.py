#!/usr/bin/env python3
# Author ID: 1000

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    file = open(file_name, 'r')
    contents = file.read()
    file.close()
    return contents

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    file = open(file_name, 'r')
    contents = file.read().splitlines()
    file.close()
    return contents

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    file = open(file_name, 'a')
    contents = file.write(string_of_lines)
    file.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    file = open(file_name, 'w')
    for line in list_of_lines:
        file.write(line + '\n')
    file.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    file1 = open(file_name_read, 'r')
    file2 = open(file_name_write, 'w')
    l = 1
    read_file = file1.read().splitlines()
    #splitfile = read_file.split('\n') 
    for split in read_file:
        file2.write(str(l) + ':' + str(split) + '\n')
        l = l + 1

    file1.close
    file2.close

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))