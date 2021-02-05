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

    # init
    def __init__(self, year=1970, month=1, day=1):
        # set dictionary to refer for each month
        global days_in_month
        days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
                    
        global date_in_days
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return '%.4d-%.2d-%.2d' % (self.year, self.month, self.day)

    def __str__(self):
        return '%.4d/%.2d/%.2d' % (self.year, self.month, self.day)
    
    def __add__(self, day_increase):
        addition_day = self.date_to_days() + day_increase
        addition = self.days_to_time(addition_day)
        return addition
    
    def __sub__(self, day_decrease):
        subtraction_day = self.date_to_days() - day_decrease
        subtraction = self.days_to_time(subtraction_day)
        return subtraction

    def tomorrow(self):
        tomorrow_day = self.date_to_days() + 1
        tomorrow = self.days_to_time(tomorrow_day)
        return tomorrow
    
    def yesterday(self):
        yesterday_day = self.date_to_days() - 1
        yesterday = self.days_to_time(yesterday_day)
        return yesterday
    
    def day_of_week(self):
        day_of_week = days_in_month[self.month] - self.day
        return day_of_week
    
    def date_to_days(self):
        global date_in_days
        seconds = 0
        count = 1
        year_difference = self.year - 1970
        year_calculation = 1970

        #print('year difference:' + str(year_difference))
        while year_difference != 0:
            #print(year_calculation)
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
        
        date_in_days = (seconds / 86400)
        return date_in_days

    def days_to_time(self, days):
        date = Date(self.year, self.month, self.day)
        count = 1
        #Start year calculation from epoch year
        year_calculation = 1970
        
        while True:
            #print(days)
            if days < 0:
                break
            else:
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
                    days_in_year = 366
                    if days < days_in_year:
                        break
                    else:    
                        days -= days_in_year
                else:
                    days_in_year = 365
                    if days < days_in_year:
                        break
                    else:    
                        days -= days_in_year
                
                if days != 0:
                    year_calculation += 1

        if status == True:
            days_in_month[2] = 29
        else:
            days_in_month[2] = 28
##################FIX CALCULATION###############        
        month_count = 1
        overflow_month = 0
        overflow_year = 0
        overflow_trigger = False
        while days >= 0:
            #print('days before calculation:' + str(days))
            if month_count > 12:
                overflow_trigger = True
                month_count = 1
                overflow_year += 1
           # print('month:' + str(month_count))
           # print('days in month: ' + str(days_in_month[month_count]))

            if days == 0 and month_count == 1:
                days = days_in_month[12]
                month_count = 12
                break
            elif days <= days_in_month[month_count] and days != 0:
               # print('break - after calculation:' + str(days))
                break
            else:
                days -= days_in_month[month_count]
              #  print('after calculation:' + str(days))
                month_count += 1
                if overflow_trigger == True:
                    overflow_month += 1

        print(year_calculation)
        #print(month_count)
        #print('overflow info:' + str(overflow_month) + str(overflow_year) + str(overflow_trigger))
        date.year = year_calculation + overflow_year
        date.month = month_count + overflow_month
        date.day = days
        
       # print('info' + str(date.year) + ' ' +  str(date.month) + ' ' + str(date.day))
        if date.day > days_in_month[date.month]:
            date.month += 1
            date.day = 1
           # print(date.month)
            if date.month > 12:
                date.month == 1
                date_year += 1
        elif date.day < 1:
           # print(date.month)
            date.month +- 1
            date.day = days_in_month[date.month]
           # print(date.day)
            if date.month < 1:
                date.month == 12
                date.year -= 1
        return date