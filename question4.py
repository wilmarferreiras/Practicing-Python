###
# Write a python program that:
# 1. Asks the user to enter a list of numbers (separated by spaces).
# 2. Asks for a single number to search for.
# 3. Tells the user **how many times** that number appears in the list.
# ###

empt = []
list_num = input("enter a list of numbers seperated by spaces: ").split()
search = int(input("What is the number you are looking for: "))
counter = 0
for i in list_num:
    empt.append(int(i))
for x in empt:
    if search== x:
        counter += 1
print(counter)
