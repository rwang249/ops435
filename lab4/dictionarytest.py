#!/usr/bin/env python3

dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Postal Code': 'M3J3M6'}

print(dict_york.values())

print(dict_york['Address'])
print(dict_york['Postal Code'])

dict_york['Country'] = 'Canada'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

dict_york['Province'] = 'BC'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())


dict_york['Province'] = 'ON'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

list_of_keys = list(dict_york.keys())
print(list_of_keys[0])

list_of_keys = list(dict_york.keys())
for key in list_of_keys:
    print(key)
for value in dict_york.values():
    print(value)