#!/usr/bin/env python3

s1 = {'Prime', 'Ix', 'Secundus', 'Caladan'}
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}

print('Ix' in s1)
print('Geidi' in s1)

print(s2)
print(s3)

print(s2 | s3)         # returns a set containing all values from both sets
print(s2.union(s3))    # same as s2 | s3

print(s2 & s3)             # returns a set containing all values that s2 and s3 share
print(s2.intersection(s3)) # same as s2 & s3

print(s2 - s3)             # returns a set containing all values in s2 that are not found in s3
print(s2.difference(s3))   # same as s2 - s3

print(s2 ^ s3)                     # returns a set containing all values that both sets DO NOT share
print(s2.symmetric_difference(s3)) # same as s2 ^ s3

l2 = [1, 2, 3, 4, 5]
l3 = [4, 5, 6, 7, 8]
temporary_set = set(l2).intersection(set(l3))
new_list = list(temporary_set)  # '''set()''' can make lists into sets. '''list()''' can make sets into lists.
print(new_list)