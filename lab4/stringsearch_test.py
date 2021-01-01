#!/usr/bin/env python3

text = 'Seneca'
offset = 0
length = len(text)
while offset < length:
    print(offset, text[offset])
    offset = offset + 1


text = "Seneca"
for letter in text:
    print(letter)

s1 = 'Seneca'
print(s1, 'contains letter s? ->', 's' in s1)
print(s1, 'contains letter S? ->', 'S' in s1)

def is_vowel(char):
    if char in 'aeiou':
        return True
    return False
      
if __name__ == '__main__':
    text = 'Seneca'
    vowel_count = 0
    for char in text:
        if is_vowel(char):
             vowel_count = vowel_count + 1
    print('There are',vowel_count,'vowel(s) in',text)