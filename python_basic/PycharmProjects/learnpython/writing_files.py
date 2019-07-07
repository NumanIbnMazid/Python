
employee_file = open("employee.txt", "a")
employee_file.write("Toby - Human Resources")

# write files with a new line with escape characters
employee_file.write("\nKelly - Customer Service")

# writing files : This will overwrite files and remove all the past contents
employee_file = open("employee.txt", "w")

employee_file.write("Kelly- Customer Service")

employee_file.close()


#creating new file
employee_file = open("employee1.txt", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

