age = 21

name = "Numan"

is_male = True

# Execute code in terminal : 'python python_basic.py' and hit enter

print("Hellow my name is {} and I am {} years old".format("Numan", 27))
if age > 18 and is_male:
    print("Yes you are adult male.")
else:
    print("You are not adult or mot male.")

# Function
def hellow():
    print("Hellow World !")
hellow()

def add_parameter(name, age=35):
    return "Hellow {} you are {}".format(name, age)
stored = add_parameter("Mark")
print(stored)

# Lists
names = ["Mark", "Nil", "Abraham", 2023, False, 20.83]
names.insert(0, "Neymar")
del(names[3])
names[1] = "Ronaldo"
print(names[2])
print(names)
print(len(names))

# Loops
for name in names:
    print(name)

for x in range(1,4):
    print(x)

print("\n")

age = 0
while age < 5:
    print(age)
    age += 1

# Dictionary
persons = {"Dany":21, "Silva":23, "Luiz":19, "Rooney":False, "Abraham":17.67}
del(persons["Dany"])
persons["Randy"] = 15
persons["Silva"] = 16
print(persons)
print(persons["Silva"])

# class
class Dog:
    dogInfo = "Dogs are cool !"
    def bark(self, extra):
        print("Buuuuuuuh {} !!!".format(extra))
myDog = Dog()
myDog.bark("Man")
myDog.name = "Bondhon"
myDog.age = 45
print(myDog.name)
print(myDog.age)
print(Dog.dogInfo)
print(myDog.dogInfo)

print("\n")

class Cats:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
myCat = Cats("Persian", 5, "white")
print(myCat.name)
print(myCat.age)
print(myCat.color)
