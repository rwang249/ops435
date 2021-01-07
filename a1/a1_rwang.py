#!/usr/bin/env python3
''' template for ops435 assignment 1 script
-----------------------------------------------------------------------
OPS435 Assignment 1 - Fall 2020
Program: a1_rwang.py 
Author: Raphael Wang
Done for personal learning. Only os and sys modules were allowed
'''
import os
import sys

def leap_year(obj):
    '''
    The leap_year() function will take a year in "YYYY" format, and return True 
    if the given year is a leap year, otherwise return False.
    '''
    if (obj % 4) == 0:
        if (obj % 100) == 0:
            if (obj % 400) == 0:
                status = True
            else:
                status = False
        else:
            status = True
    else:
        status = False

    return status

def sanitize(obj1,obj2):
    '''
    The sanitize() function will take two string objects, the first string object is the object to be sanitized, 
    and the 2nd string object contains letters that are allowed. This function will return the first object with 
    letters not in the 2nd string object removed.
    '''
    results = ''
    for char in obj1:
        if char in obj2:
            results = results + results.join(char)

    return results

def size_check(obj, intobj):
    '''
    The size_check() function will take an collection data type object and expected number of items as an integer and will return either 'True' or 'False'. 
    If the number of items in the data object match the integer value given, return 'True', otherwise return 'False'
    '''
    length = len(obj)
    if length == intobj:
        status = True
    else:
        status = False
    
    return status

def range_check(obj1, obj2):
    '''
    The range_check() function will take an integer object and a tuple with two integer values, 
    the first value indicates the lower bound and the second one 
    indicates the upper bound of a integer range. 
    If the integer object falls in between the range given in the tuple, 
    return 'True', otherwise return 'False'.
    '''
    if obj1 >= obj2[0] and obj1 <= obj2[1]:
        status = True
    else:
        status = False

    return status
    
def usage():    
    '''
    The usage() function will take no argument and return a string describing the usage of the script.
    '''
    scriptName = sys.argv[0]
    status = 'Usage: ' + scriptName + ' YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD'

    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   #print('Sanitized user data:', dob)
   # step 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong data entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: Wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   #print("Your date of birth is:", new_dob)  
   print(new_dob)