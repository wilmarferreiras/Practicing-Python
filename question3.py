###
# Write a Python program that asks the user to enter a number, and then tells the user whether the number is **even** or **odd**.
###

def is_Even_or_Odd(num):
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")
while True:
    num = int(input("Enter your number: "))
    is_Even_or_Odd(num)