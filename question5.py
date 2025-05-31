###
# Write a Python program that:
# 1. Asks the user to enter a word.
# 2. Counts how many **vowels** are in that word.
# 3. Prints the number of vowels.
# > Vowels are: `a`, `e`, `i`, `o`, `u` (both uppercase and lowercase should count!)
###

vowels = ["a", "e", "i", "o", "u"]
word = input("Enter a word: ").lower()
counter = 0

for i in word:
    for x in vowels:
        if x == i:
            counter += 1

print(counter)