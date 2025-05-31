#Wilmar Ferreiras
#Date: 02/28/2025

#Assingment 1
hatList = [100, 200, 300, 400, 500]
print("Replace the middle number of the list with a number of your liking")
replace_prompt = input("New Number: ")
hatList.insert(2, int(replace_prompt))
hatList.pop(3)
hatList.pop(-1)
print(len(hatList))
print(hatList)
#Assingment 2
Beatles = []
Beatles.append("Paul McCartney")
Beatles.append("Pete Best")
Beatles.append("George Harrison")
Beatles.append("Stu Sutcliffe")
Beatles.append("John Lennon")
print(Beatles)
Beatles.insert(1, "John Lennon")
print(Beatles)
Beatles.pop(-1)
print(Beatles)
Beatles.pop(-1)
print(Beatles)
Beatles.insert(0, "Ringo Starr")
print(Beatles)
#Assignment 3
studentList = []

print("Please Add 5 Students")
stu1 = input("First Student Name: ")
stu2 = input("Second Student Name: ")
stu3 = input("Third Student Name: ")
stu4 = input("Fourth Student Name: ")
stu5 = input("Fifth Student Name: ")

studentList. append(stu1)
studentList. append(stu2)
studentList. append(stu3)
studentList. append(stu4)
studentList. append(stu5)

print(studentList)
studentList.sort()
print(studentList)
studentList.reverse()
print(studentList)
print("middle student is " + studentList[2])

newList = []
newList.append("John Smith")
newList.append("Mary Miller")
print(newList)
