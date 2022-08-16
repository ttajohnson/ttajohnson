first_choice = input('Enter the first word: ')
first_word = list(first_choice)
second_choice = input('Enter the second word: ')
second_word = list(second_choice)

first_word.sort() 
second_word.sort()

if first_word == second_word:
    print(f'{first_choice} and {second_choice} are anagrams! ')
else:
    print(f'{first_choice} and {second_choice} are not anagrams... ')