import random

consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
vowels = ("a", "e", "i", "o", "u")

syllables = []
for consonant in consonants:
    for vowel in vowels:
        syllables.append(consonant + vowel)

for i in range(100):
    username = ""
    for i in range(4):
        username = username + random.choice(syllables)
    print(username)
