#!/usr/bin/env python3

import os
import sys

'''
OPS435 Assignment 2P - Fall 2020
Program: a1_[student_id].py (replace student_id with your Seneca User name)
Author: 1000
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''

class Date:

    global month_name
    global days_in_month
    month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                'Jul','Aug','Sep','Oct','Nov','Dec']
    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        global days_in_month

        #Take a year in "YYYY" format, and return True if the given year is a leap year, otherwise return False.
        
        if (self.year % 4) == 0:
            if (self.year % 100) == 0:
                if (self.year % 400) == 0:
                    status = True
                else:
                    status = False
            else:
                status = True
        else:
            status = False
        
        if status == True:
            days_in_month[2] = 29

    def __repr__(self):
        return '%.4d-%.2d-%.2d' % (self.year, self.month, self.day)

    def __str__(self):
        return '%.4d/%.2d/%.2d' % (self.year, self.month, self.day)
    
    def __add__(self, day_increase):
        self.day = self.day + day_increase
        if self.day > days_in_month[self.month]:
            self.month = self.month + 1
            self.day = 1
            new_day = self.day - days_in_month[self.month] 
            if self.month == 13:
                self.month == 1
                self.year = self.year + 1
        
        return self
    
    def __sub__(self, yesterday):

        return self.yesterday

    def tomorrow():

        return tomorrow
    
    def yesterday():

        return yesterday
    
    def day_of_week():

        return day_of_week
