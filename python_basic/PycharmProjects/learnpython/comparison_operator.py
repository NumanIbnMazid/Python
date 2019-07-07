
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(32, 40, 5))

print("\n")


def max_res(animal1, animal2, animal3):
    if animal1 >= animal2 and animal1 >= animal3:
        return animal1
    elif animal2 >= animal1 and num2 >= animal3:
        return animal2
    else:
        return animal3


print(max_res("dog", "crow", "zebra"))
