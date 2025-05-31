### 
# Write a Python program that asks the user to enter a list of numbers (separated by spaces), then prints out the **largest** number from that list.
###

input = input("Enter A list of numbers: ").split()
output = []

for i in input:
    output.append(int(i))

output.sort()
result = output[-1]
print(result)