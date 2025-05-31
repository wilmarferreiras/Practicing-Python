#Wilmar Ferreiras
#03/06/2025

#sets Examples
set_0 = {100, 200, 300}
print(set_0)
set_1 = {1, 2, 3, 4, 5, 6}
print("First Set:",set_1)
set_2 = {2, 3, 4, 5, 6, 7, 9}
print("Second Set: ",set_2)
set_1.add(9)
print("Set One: ", set_1)
set_2.discard(10)
print("Set Two: ", set_2)
set_1.remove(1)
print("Set One: ",set_1)
set_1.pop()
print("Set One: ",set_1)
set_0.clear()
print(set_0)
result = set_1.difference(set_2)
print(result)
#dictionary Examples 
students = {"John":100, "Stew":101, "Randy":102, "Josh":103}
print(students)
print(students.keys())
print(students.values())
print(students.items())
print(students["Randy"])
print(students["Josh"])
print(students["John"])
print(students["Stew"])
students.setdefault("John", 100)
students.pop("Stew")
print(students)
students.clear()
print(students)
students["John"] = 100

print(students)
