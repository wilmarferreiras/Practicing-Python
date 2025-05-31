###
# Write a Python program that:
# 1. Asks the user to enter a sentence.
# 2. Reverses **each word** in the sentence **individually**, but keeps the word order the same.
# 3. Prints the transformed sentence.
###

sentence = input("Enter a sentence: ").lower().split()
sentence2 = []
for i in sentence:
    sentence2.append(i[::-1])
print(' '.join(sentence2))