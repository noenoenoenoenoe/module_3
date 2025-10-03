import random

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
"""
# Practice different ways of formatting strings.

# TODO: Create variables for name, age, and height
name = "Wemby"
age = 21
height = 345

# TODO: Use the .format() method to create a sentence with these variables
phrase = "coucou c'est {}, j'ai {} ans, je fais {}cm, personne peut me test".format(name, age, height)
print(phrase)

# TODO: Use f-strings to create the same sentence = permet d'éviter le .format
phrase_2 = f"coucou c'est {name}, j'ai {age} ans, je fais {height}cm, personne peut me test"
print(phrase_2)

# TODO: Use the % operator for string formatting
phrase_3 = "coucou c'est %s, j'ai %d ans, je fais %dcm, personne peut me test" % (name, age, int(height))
print(phrase_3)

# TODO: Format a float number to display only two decimal places
pi = 3.1415926535
formaté = f"{pi:1f}"
print(formaté)

# TODO: Create a table-like output using string formatting
# méthode1 avec variables :
name, age, height = "Wemby", 21, 345
name1, age1, height1 = "Lebron", 62, 200
name2, age2, height2 = "tp", 108, 150
print(f"{'Nom':<15} {'Âge':<10} {'Taille':<10}")
print("-" * 35)
print(f"{name1:<15} {age1:<10} {height1:<10}")
print(f"{name2:<15} {age2:<10} {height2:<10}")
print(f"{name:<15} {age:<10} {height:<10}")

# méthode2 avec boucle :
nba_tailles = [
    ("Wemby", 21, 345),
    ("Lebron", 62, 200),
    ("tp", 108, 150)
]
print(f"{'Nom':<15} {'Âge':<10} {'Taille':<10}")
print("." * 35)

for name, age, height in nba_tailles:
    print(f"{name:<15} {age:<10} {height:<10}")

# Print all formatted strings
"""
# Exercise 3: For Loops
"""
# Practice using for loops with different data structures.
# TODO: Create a list of numbers
nombres = [10, 11, 12, 13]

# TODO: Use a for loop to print each number in the list
for nombre in nombres:
    print(nombre)

# TODO: Use a for loop with enumerate() to print both index and value
Nombres = [10, 11, 12, 13,14, 15, 16]
print(Nombres)

for Index, Valeur in enumerate(Nombres):
    print(f"Index {Index} - Valeur {Valeur}")

# TODO: Create a dictionary and use a for loop to print all keys and values
books = {"title": "1984", "author": "George Orwell", "year": 1949}
print(type(books))
for key, value in books.items():
    print(key, "-", value)

# TODO: Use a for loop with range() to print numbers from 1 to 10
for i in range(1, 10):
    print(i)

# TODO: Use list comprehension to create a new list of squares of numbers
carrés = [n**2 for n in Nombres]
print(carrés)

# TODO: Use a nested for loop to create a multiplication table (up to 5x5)
for ligne in range(1, 6):
    for colonne in range(1, 6):
        print(f"{ligne*colonne:4}", end="")
    print()

for ligne in range(1, 6):
    for colonne in range(1, 6):
        print(f"{ligne*colonne:4}", end=" |")
    print()
"""
# Exercise 4: While Loops
# Practice using while loops for different scenarios.
"""
# TODO: Use a while loop to print numbers from 1 to 10
i = 0
while i <= 10:
    print(i)
    i += 2

# TODO: Create a guessing game using a while loop
# (generate a random number and let the user guess until correct)
secret = random.randint(1, 10)
guess = None
print()
while guess != secret:
    guess = int(input("ok bienvenue notre jeu c'est : devine le chiffre entre 1 et 10 ou on te pète les genoux"))

    if guess < secret:
        print("trop petit tu vas prendre un taquet")
    elif guess > secret:
        print("trop petit tu vas prendre un taquet")
    else:
        print("ok t'as de la chance tu gardes tes 2 jambes")

# TODO: Use a while loop to calculate the factorial of a number
Nombre = 5
fact = 1
i = 1
while i <= Nombre:
    fact = fact * i
    i += 1
print(f"Factorielle de {Nombre} = {fact} ma belle")

# TODO: Implement a simple calculator using a while loop
# (continue calculating until the user chooses to exit)
print("ptite calculette oklm")
print("mon gars ici tu peux utiliser du + du - du * du / régale toi")
print("si tu dois y aller y a 0 galère appuie sur q")

while True:
    op = input("mets toi bien choisis +, -, *, / ou q pour quitter\n")
    if op == "q":
        print("bises")
        exit(0)
    a = float(input("choisis ton 1er chiffre\n"))
    b = float(input("choisis ton 1er chiffre nan jdec c le 2ème\n"))
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        if b == 0:
            print("tu peux pas diviser par 0 ducon\n")
        else:
            print(a/b)
    else:
        print("g pas capté là")

"""
# Exercise 5: Combining Strings and Loops

# Solve problems that involve both string manipulation and loops.
# TODO: Create a function that counts the occurrence of each vowel in a string
def comptage_voyelles(text):
    vowels = "aeiouy"
    count = {}
    for char in text.lower():
        if char in vowels:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count
print(comptage_voyelles("Carla va voir Nico au parloir"))
print(f"{'Voyelle':<10}{'Occurence':<10}")
print("-"*22)
resultats = comptage_voyelles("Carla va voir Nico au parloir")
for voyelle, occ in resultats.items():
    print(f"{voyelle:<10} {occ:<10}")

# TODO: Implement a simple Caesar cipher (shift each letter by a fixed amount)

# TODO: Create a function that generates the NATO phonetic alphabet representation of a word

# TODO: Implement a function that checks if a string is a palindrome

# Test each function with sample inputs and print the results
# TODO: Create variables for name, age, and height


# TODO: Use the .format() method to create a sentence with these variables