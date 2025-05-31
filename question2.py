###
# Write a Python program that asks the user to enter a word, and then checks whether the word is a **palindrome**.
# A palindrome is a word that reads the same forward and backward (like `racecar`, `level`, or `madam`).
###
is_true = False
user_word = input("What's the word: ")
empt = []
for i in user_word:
    empt.append(i)
result = []
for x in empt[::-1]:
    result.append(x)
if empt == result:
    is_true = True
    print(is_true)
else:
    print(is_true)