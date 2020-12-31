#!/usr/bin/env python3

#Author: Raphael Wang   
#Author ID: 1000
#Date Created: 2020/12/28

import sys

argument = len(sys.argv)

if argument == 1:
    timer = 3
elif argument == 2:
    timer = int(sys.argv[1])

while timer != 0:
    print(str(timer))
    timer = timer - 1
print('blast off!')
