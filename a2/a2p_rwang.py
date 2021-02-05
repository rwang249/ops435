#!/usr/bin/env python3

import os
import sys

'''
OPS435 Assignment 2P - Fall 2020
Program: a2p_rwang.py
Author: 1000
Used for personal learning.

Only os and sys modules were allowed for this assignment
'''

class Date:

    # init
    def __init__(self, year=1970, month=1, day=1):
        # set dictionary to refer for each month
        global days_in_month
        days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        # set class attributes
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        # return self if called
        return '%.4d-%.2d-%.2d' % (self.year, self.month, self.day)

    def __str__(self):
        # return self if called as string
        return '%.4d/%.2d/%.2d' % (self.year, self.month, self.day)
    
    def __add__(self, day_increase):
        # use the date_to_days() function to convert date to # of days, add days, and then convert back into date
        addition_day = self.date_to_days() + day_increase
        addition = self.days_to_time(addition_day)
        return addition
    
    def __sub__(self, day_decrease):
        # use the date_to_days() function to convert date to # of days, subtract days, and then convert back into date
        subtraction_day = self.date_to_days() - day_decrease
        subtraction = self.days_to_time(subtraction_day)
        return subtraction

    def tomorrow(self):
        # similar to __add__, but only adding 1 day instead of adding a dynamic number
        tomorrow_day = self.date_to_days() + 1
        tomorrow = self.days_to_time(tomorrow_day)
        return tomorrow
    
    def yesterday(self):
        # similar to __sub__, but only subtracting 1 day instead of subtracting a dynamic number
        yesterday_day = self.date_to_days() - 1
        yesterday = self.days_to_time(yesterday_day)
        return yesterday
    
    def day_of_week(self):
        #calculate day of week using algorithm from Tomohiko Sakamoto
        t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ] 
        self.year -= self.month < 3
        return (( self.year + int(self.year / 4) - int(self.year / 100) 
                + int(self.year / 400) + t[self.month - 1] + self.day) % 7) 
    
    def date_to_days(self):
        # initialize variables used for calculation
        seconds = 0
        count = 1
        year_difference = self.year - 1970
        year_calculation = 1970

        # iterate through years from 1970 up to self.year but not including. add number of seconds depending on if leap year
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

        # Start going through current year by first determining if it is a leap year. 
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
        
        # Then convert current days to date and add to seconds variable. First going through by month and then by days   
        while True:
            if count == self.month:
                seconds += self.day * 86400
                break
            else:
                seconds += days_in_month[count] * 86400
            count += 1
        
        # convert seconds to days and return
        date_in_days = (seconds / 86400)
        return date_in_days

    def days_to_time(self, days):
        # initialize Date object to return
        date = Date(self.year, self.month, self.day)
        count = 1
        # start year calculation from epoch year
        year_calculation = 1970
        
        # iterate through each year up to current year. subtract days in year from number of days passed into function
        while True:
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
        
        # Check status of current year, number of days in february will reflect type of year
        if status == True:
            days_in_month[2] = 29
        else:
            days_in_month[2] = 28
     
        # initialize variables for month + day calculation
        month_count = 1
        overflow_month = 0
        overflow_year = 0
        overflow_trigger = False

        # iterate through remaining days 
        while days >= 0:

            # if month exceeds 13, reset to 1 and increment overflow_year to be added to final year value
            if month_count > 12:
                overflow_trigger = True
                month_count = 1
                overflow_year += 1

            # in the special condition that the variables read january 0, reset to december 31st
            if days == 0 and month_count == 1:
                days = days_in_month[12]
                month_count = 12
                break
            elif days <= days_in_month[month_count] and days != 0:
                break
            else:
                # if flag was triggered, increment to overflow month to be added to final month value
                days -= days_in_month[month_count]
                month_count += 1
                if overflow_trigger == True:
                    overflow_month += 1

        # set object attributes, adding overflow
        date.year = year_calculation + overflow_year
        date.month = month_count + overflow_month
        date.day = days
        
        # final check. if any attribute is over or under accepted values, increment/decrement next value.
        if date.day > days_in_month[date.month]:
            date.month += 1
            date.day = 1
            if date.month > 12:
                date.month == 1
                date_year += 1
        elif date.day < 1:
            date.month +- 1
            date.day = days_in_month[date.month]
            if date.month < 1:
                date.month == 12
                date.year -= 1
        return date