
# read mode 'r',
# write mode 'w',
# append mode 'a' - only can add new information
# read and write 'r+' - all the power

employee_file = open("employee.txt", "r")

# first check if the file is readable
print(employee_file.readable())

print("\n")

# print specific line of the file
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())

print("\n")

# print the whole contents of the file and put in an array
print(employee_file.readlines())

print("\n")

# access specific content from that array
# print(employee_file.readlines()[0])

# print("\n")

# for employee in employee_file.readlines():
#     print(employee)
#
# print("\n")

# print the whole contents of the file
print(employee_file.read())

employee_file.close()