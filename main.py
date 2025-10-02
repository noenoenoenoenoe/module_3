# Module 3: String Manipulation and Loops

# Practice working with string methods and loops in Python.

"""
# Exercise 1: String Methods

# Explore various string methods in Python.

# TODO: Create a string variable with a sentence
phrase = " carla va voir nico au parloir "

# TODO: Convert the string to uppercase
print(phrase.upper())

# TODO: Convert the string to lowercase
print(phrase.lower())

# TODO: Capitalize the first letter of each word
print(phrase.title())

# TODO: Replace a word in the string
nouvelle_phrase = phrase.replace("carla", "louis")
print(nouvelle_phrase)

# TODO: Split the string into a list of words
mots = phrase.split()
print(mots)

# TODO: Join the list of words back into a string using a different separator
phrase_séparée = "-".join(mots)
print(phrase_séparée)

# TODO: Find the position of a specific word in the string
position = phrase.find("parloir")
print(position)

# TODO: Check if the string starts with a specific word
début = phrase.startswith("mdr")
print(début)
fin = phrase.endswith("parloir")
print(fin)

# TODO: Remove leading and trailing whitespace from a string
tout_propre = phrase.strip()
print(tout_propre)
"""
# Print the results of each operation -->ok

# Exercise 2: String Formatting

# Practice different ways of formatting strings.

# TODO: Create variables for name, age, and height
name = "Wemby"
age = "21"
height = "345"

# TODO: Use the .format() method to create a sentence with these variables
phrase = "coucou c'est {}, j'ai {} ans, je fais {}, personne peut me test".format(name, age, height)
print(phrase)

# TODO: Use f-strings to create the same sentence

# TODO: Use the % operator for string formatting

# TODO: Format a float number to display only two decimal places

# TODO: Create a table-like output using string formatting

# Print all formatted strings

## Exercise 3: For Loops

#Practice using for loops with different data structures.
# TODO: Create a list of numbers
#numbers = []

# TODO: Use a for loop to print each number in the list

# TODO: Use a for loop with enumerate() to print both index and value

# TODO: Create a dictionary and use a for loop to print all keys and values

# TODO: Use a for loop with range() to print numbers from 1 to 10

# TODO: Use list comprehension to create a new list of squares of numbers

# TODO: Use a nested for loop to create a multiplication table (up to 5x5)

## Exercise 4: While Loops

#Practice using while loops for different scenarios.
# TODO: Use a while loop to print numbers from 1 to 10

# TODO: Create a guessing game using a while loop
# (generate a random number and let the user guess until correct)

# TODO: Use a while loop to calculate the factorial of a number

# TODO: Implement a simple calculator using a while loop
# (continue calculating until the user chooses to exit)

# Exercise 5: Combining Strings and Loops

#Solve problems that involve both string manipulation and loops.
# TODO: Create a function that counts the occurrence of each vowel in a string

# TODO: Implement a simple Caesar cipher (shift each letter by a fixed amount)

# TODO: Create a function that generates the NATO phonetic alphabet representation of a word

# TODO: Implement a function that checks if a string is a palindrome

# Test each function with sample inputs and print the results
