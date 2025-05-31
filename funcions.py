#Wilmar Ferreiras
#03/17/2025

#Assignment 1
def l100kmtompg(liters):
    convert = liters * 0.26
    return print(f" gallons: {convert}")
l100kmtompg(4)
def mpgtol100km(miles):
    convert = miles * 1.61
    return print(f"kilometer: {convert}")
mpgtol100km(10)

#Assignment 2
def Fahrenheit(Celsius):
    convert = (9/5 * Celsius) + 32
    return print(f"Fahrenheit: {convert }")
Fahrenheit(20)
def Celsius(Fahrenheit):
    convert = (5/9) * (Fahrenheit - 32)
    return print(f"Celsius: {convert}")
Celsius(20)

#Assignment 3
def contains_duplicate(a_list):
    temp = set()
    
    for x in a_list:
        if x in temp:
            return True  
        temp.add(x)
    
    return False  

result = contains_duplicate([1, 2, 2, 3, 4])
print(result)



            
