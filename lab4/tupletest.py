#!/usr/bin/env python3

t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
t2 = (1, 2, 3, 4, 5, 6)

print(t1[0])
print(t2[2:4])

print('Ix' in t1)
print('Geidi' in t1)

list2 = [ 'uli101', 'ops235', 'ops335', 'ops435', 'ops535', 'ops635' ]

list2[0]= 'ica100'
print(list2[0])
print(list2)

t3 = t2[2:3]

for item in t1:
    print('item: ' + item)