#!/usr/bin/env python3

from student import Student

# Creates an instance of the Student class, it will be separate from all other objects created with the Student class:
student1 = Student('John', '013454900')

print(student1.name)
print(student1.number)
print(student1.courses)
student1.displayStudent()

student2 = Student('Jessica', '023384103')

print(student2.name)
print(student2.number)
print(student2.courses)
student2.displayStudent()

# Add new courses for student1
student1.addGrade('uli101', 4.0)
student1.addGrade('ops235', 3.5)
student1.addGrade('ops435', 3.0)

# Add new courses for student2
student2.addGrade('ipc144', 4.0)
student2.addGrade('cpp244', 4.0)

print(student1.name)
print(student1.courses)
print(student2.name)
print(student2.courses)

# student1.name is a string like any other
print(student1.name)
student1.name = 'Jack'
print(student1.name)
len(student1.name)

# student3 is the object, Student is the class name, 'Jen' is the first argument passed to __init__, '034686901' is the second argument passed to init.
student3 = Student('Jen', '034686901')

print(student3.name)
print(student3.number)
print(student3.courses)
student3.displayStudent()