# ....Lab 09 (COMPLETE)

import re
import math
with open('C:/users/johns/desktop/gettysburg_address.txt') as f:
    contents = f.read()
# print(contents)

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

words = re.split(r'\s', contents)
words.sort()
words = words[9::]
word_count = len(words)
# print(words)
# print(word_count)

characters = ''.join(words)
character_count = len(characters)
# print(characters)
# print(character_count)

sentences = re.split(r'[.?!]', contents)
sentences.sort()
sentences = sentences[1::]
sentence_count = len(sentences)
# print(sentences)
# print(sentence_count)


ari_score = 4.71*(character_count/word_count) + .5*(word_count/sentence_count) - 21.43
ari_score = math.ceil(ari_score)
print(f'The ARI for gettysburg_address.txt is {ari_score}.')
grade_level = ari_scale[13]['grade_level']
ages = ari_scale[13]['ages']
print(f'This corresponds to a {grade_level} level of difficulty that is suitable for an average person {ages} years old.')

