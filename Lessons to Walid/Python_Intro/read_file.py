employee_file = open("my_doc.txt", "r+")

# first check if the file is readable
# print(employee_file.readable())

employee_file.write("\n This line has been aded.")

print("\n")

print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())