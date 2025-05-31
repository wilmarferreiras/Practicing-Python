#Wilmar Ferreiras
#03/12/2025

#assignment 1
income = float(input("Enter annual income: $"))
if income < 85528:
    result = income * 0.18 - 556.2
    tax = round(result)
    print(f"The tax is: ${tax} thalers")
else:
    result = 14839.2
    if income - result > 85528:
        r1 = (income - result)* 0.32
        result2 = result + r1
        print(f"The tax is: ${result2} thalers")
    else:
        print("no")
        quit 



#Assignmetn 2
year = int(input("Enter a year: "))
if year % 4 != 0:
    print("Common Year")
elif year % 100 != 0:
    print("Leap Year")
elif year % 400 != 0:
    print("Common Year")
else:
    print("leap Year")

    

#Assignment 3
secret_number = 777
print("Welcome to my game! Guess teh secret number")
while True:
    guess = int(input("Eneter your guess: "))
    if guess != secret_number:
        print("Ha ha! You're stuck in my loop!")
        continue
    else:
        break
print(secret_number)
print("Well done, muggle! You are free now.")



#Assignment 4
userWord = input("Enter a word: ").upper()
for letter in userWord:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        print(letter) 
