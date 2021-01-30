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

    global days_in_month
    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    def __init__(self, year, month, day):
        global days_in_month
        global date_in_days
        self.year = year
        self.month = month
        self.day = day
        seconds = 0
        count = 1
        year_difference = self.year - 1970
        year_calculation = self.year

        while year_difference != 0:
            if (year_calculation % 4) == 0:
                if (year_calculation % 100) == 0:
                    if (year_calculation % 400) == 0:
                        status = True
                    else:
                        status = False
                else:
                    status = True
            else:
                status = False
            
            if status == True:
                seconds += 31622400
            else:
                seconds += 31536000
            
            days_in_month[2] = 28
            year_calculation += 1
            year_difference -= 1

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
        
        while True:
            if count == self.month:
                seconds += self.day * 86400
                break
            else:
                seconds += days_in_month[count] * 86400
            count += 1
        
        date_in_days = seconds / 86400


    def __repr__(self):
        return '%.4d-%.2d-%.2d' % (self.year, self.month, self.day)

    def __str__(self):
        return '%.4d/%.2d/%.2d' % (self.year, self.month, self.day)
    
    def __add__(day_increase):
        # self.day = self.day + day_increase
        # if self.day > days_in_month[self.month]:
        #     self.month = self.month + 1
        #     self.day = 1
        #     if self.month > 12:
        #         self.month == 1
        #         self.year = self.year + 1

        date_in_days += day_increase
        
        return self
    
    def __sub__(day_decrease):
        # self.day = self.day - day_decrease
        # if self.day < 1:
        #     self.month = self.month - 1
        #     self.day = days_in_month[self.month]
        #     if self.month < 1:
        #         self.month == 12
        #         self.year = self.year - 1

        return self

    def tomorrow():

        return tomorrow
    
    def yesterday():

        return yesterday
    
    def day_of_week():

        return day_of_week

    def days_to_time(self, days):
        count = 1

        #calculate number of years to add to epoch
        num_of_years = days / 365

        #calculate number of months to add to epoch
        days_left = (days % 365)
        while True:
            if count == self.month and days_left > 0 and days_left < 31:
                days_left = (days % 365) - days_in_month[count]
                break
            else:
                days_left -= days_in_month[count]
            count += 1

        year_from_epoch
        if 
        month_from_epoch
        days_from_epoch

        date = year_from_epoch + " - " + month_from_epoch + " - " + days_from_epoch
        return date