# Create a Mad Lib utilizing the .split() function, even though it wasn't taught yet.
adjective = input('Give me an adjective: ')
description = '55 years old, 6 feet tall, uglier than a hog.'
split = description.split(', ') # Will have to learn about what exactly goes within the parantheticals for .split
result = f'''
Wanted Dead or Alive
{adjective} Pete, for crimes against humanity.

Suspect is {split}'''
print(result)