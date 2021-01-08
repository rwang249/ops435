#!/usr/bin/env python3
''' template for ops435 assignment 1 B script
-----------------------------------------------------------------------
OPS435 Assignment 1 B - Fall 2020
Program: a1_rwang.py 
Author: Raphael Wang
Done for personal learning. Only os, subprocess, and sys modules were allowed.
Alternate assignment option
'''
import os
import sys
import subprocess

def call_df():
    '''
    should take no arguments return a list of strings returned by the shell command.
    Output is filtered to omit any lines that contain loop or tmpfs. These are not proper file systems and should not be displayed.
    '''
    process = subprocess.Popen(['df'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    communicate = process.communicate()
    output = communicate[0].decode('utf-8')
    listOutput = output.split('\n')
    count = 0

    # loop through listOutput and if file system is tmpfs or loop do not put into santized list for return
    for string in listOutput:
        fs = string.split(' ')
        if fs[0] == 'tmpfs' or fs[0] == 'loop':
            del listOutput[count]
        count = count + 1
    
    return listOutput

def call_free():
    '''
    should take no arguments, and should return a list of strings from the shell.
    Will also calculate a percent of memory used divided by total memory.
    '''
    # initialize list which will be returned by function
    cleanedOutput = []

    # call subprocess to grab output of free, decode to utf-8 and split per line
    process = subprocess.Popen(['free'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    communicate = process.communicate()
    output = communicate[0].decode('utf-8')
    listOutput = output.split('\n')
    memList = listOutput[1]
    swapList = listOutput[2]

    #split memory and swap lists per column and assign total and used ints for calculation
    formattedMem = memList.split()
    formattedSwap = swapList.split()
    totalMem = formattedMem[1]
    usedMem = formattedMem[2]
    totalSwap = formattedSwap[1]
    usedSwap = formattedSwap[2]

    # calculate rounded percentage of memory used 
    totalUsedMem = round((int(usedMem) / int(totalMem)) * 100)
    totalUsedSwap = round((int(usedSwap) / int(totalSwap)) * 100)

    # add rounded percentage to list for return
    cleanedOutput.append(totalUsedMem)
    cleanedOutput.append(totalUsedSwap)

    return cleanedOutput

def call_hostname():
    '''
    should take no arguments, and should return strings from the shell.
    '''

    return hostname

def call_uptime():
    '''
    should take no arguments, and should return strings from the shell.
    '''

    return uptime

def percent_to_graph(percent):
    '''
    will take an integer 'percent' and return a bar graph that represents this percentage. 
    The bar graph should begin with '[', and end with ']'. Then contents inside should be 20 characters long.
    '''

    return output

def print_percent_line(name, percent):
    '''
    will print a properly formatted line
    '''

    return output

#call_df()
#call_free()