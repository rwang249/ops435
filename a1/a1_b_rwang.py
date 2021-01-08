#!/usr/bin/env python3
''' template for ops435 assignment 1 B script
-----------------------------------------------------------------------
OPS435 Assignment 1 B - Fall 2020
Program: a1_rwang.py 
Author: Raphael Wang
Done for personal learning. Only os, subprocess, and sys modules were allowed. For some reason dictionaries were not allowed
Alternate assignment option
'''
import os
import sys
import subprocess

dfcount = 0

def call_df():
    '''
    should take no arguments return a list of strings returned by the shell command.
    Output is filtered to omit any lines that contain loop or tmpfs. These are not proper file systems and should not be displayed.
    '''
    dfList = []
    process = subprocess.Popen(['df'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    communicate = process.communicate()
    output = communicate[0].decode('utf-8')
    listOutput = output.split('\n')

    # loop through listOutput and if file system is tmpfs or loop do not put into santized list for return
    for string in listOutput:
        fs = string.split()
        if len(string) == 0:
            continue
        else:
            if fs[0] == 'tmpfs' or fs[0] == 'loop' or fs[0] == 'Filesystem':
                continue
            else:
                dfList.append(fs[0])
                dfList.append(fs[4])
    
    return dfList

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
    # call subprocess to grab output of hostname, decode to utf-8 and split per line
    process = subprocess.Popen(['hostname'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    communicate = process.communicate()
    output = communicate[0].decode('utf-8').split('\n')
    
    #assign hostname and return
    hostname = output[0]

    return hostname

def call_release():
    '''
    should take no arguments, and should return strings from the shell.
    '''
    # call subprocess to grab output of uname -r in pretty format, decode to utf-8 and split per line
    process = subprocess.Popen(['uname -r'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    communicate = process.communicate()
    output = communicate[0].decode('utf-8').split('\n')

    #assign release and return
    release = output[0]

    return release

def call_uptime():
    '''
    should take no arguments, and should return strings from the shell.
    '''
    # call subprocess to grab output of uptime in pretty format, decode to utf-8 and split per line
    process = subprocess.Popen(['uptime -p'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    communicate = process.communicate()
    output = communicate[0].decode('utf-8').split('\n')

    #assign uptime and return
    uptime = output[0]

    return uptime

def percent_to_graph(percent):
    '''
    will take an integer 'percent' and return a bar graph that represents this percentage. 
    The bar graph should begin with '[', and end with ']'. Then contents inside should be 20 characters long.
    '''
    # initialize variables
    count = 0
    graphList = ['[']

    # calculate how many = characters will be in graph
    toFill = percent / 5

    # create graph list
    while count != 21:
        if int(toFill) != 0:
            graphList.append('=')
            count = count + 1
            toFill = int(toFill) - 1
        elif toFill == 0 and count != 20:
            graphList.append(' ')
            count = count + 1
        else:
            graphList.append(']')
            count = count + 1
    
    #reset count for subsequent use
    count = 0

    # append percentage
    while count != 4:
        if count == 3:
            graphList.append('%')
            count = count + 1
        elif count == 1:
            graphList.append(str(percent))
            count = count + 1 
        else:
            graphList.append(' ')
            count = count + 1

    # convert list to string and return
    graph = ''.join(graphList)

    return graph

def print_percent_line(name, percent):
    '''
    will print a properly formatted line
    '''

    line = "{0:<12}{1}".format(name,str(percent))
    print(line)


# assign output from modules for later use
df = call_df()
memory = call_free()
hostname = call_hostname()
release = call_release()
uptime = call_uptime()

# calculate number of pairs(fs and percentage used)
fsNum = len(df) / 2

# print output
print('Hostname: ' + hostname)
print('Kernel Release: ' + release)
print('Uptime: ' + uptime)
print('----------------------------------------')

while dfcount != fsNum:
    percent = df[1].replace('%', '')
    print_percent_line(df[0], percent_to_graph(int(percent)))
    del df[1]
    del df[0]
    dfcount = dfcount + 1

print('----------------------------------------')

print_percent_line('Mem', percent_to_graph(int(memory[0])))
print_percent_line('Swap', percent_to_graph(int(memory[1])))
