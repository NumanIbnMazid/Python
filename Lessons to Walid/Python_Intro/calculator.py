number1 = input("Please enter first number: ")
operator = input("Please choose your desired operator: ")
number2 = input("Please second first number: ")
valid_operators = ["+", "-", "*", "/"]

if number1.isdigit() == False or number2.isdigit() == False:
	print("Please enter a valid number!")
elif not operator in valid_operators:
	print("Please enter a valid operator!")
else:
	number1 = float(number1)
	number2 = float(number2)
	if operator == "+":
		result = number1 + number2
	if operator == "-":
		result = number1 - number2
	if operator == "*":
		result = number1 * number2
	if operator == "/":
		result = number1 / number2
	print(result)