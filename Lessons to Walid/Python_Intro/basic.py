whole_number = 1
fraction = 1.5
chars = "ABC"
check = True
confusional_string = 'False'

print(type(whole_number))
print(type(fraction))
print(type(chars))
print(type(check))
print(type(confusional_string))

import array as walid

a = walid.array("I", [2, 3, 5])

print(type(a))

items = []
items = [1, "Walid", True, 4.6]
print(items[-3])
items[0] = 10
items.insert(2,"Numan")
print(items)

def my_name(first_name, last_name, age):
	full_name = first_name + " " + last_name
	# sentence = "My name is %s. I am %s years old." %(full_name, age)
	# sentence = "My name is {}. I am {} years old.".format(full_name, age)
	sentence = f"My name is {full_name}. I am {age} years old."
	print(sentence)

my_name("Hasan", "Walid", 20)

# for x in range(1, 5):
# 	print(x)

# print("/n")

# y = 1
# data_type = type(y)
# check = data_type.isdigit()
# print(check)


walid_books = {"book1":'Novels', "book2":'History', 'book3':'Other Articles'}
# del walid_books['book1']
print(walid_books)
print(walid_books['book2'])
print((walid_books.keys()))
print(len(walid_books.keys()))
print((walid_books.values()))

my_list = [1, 2, 56, 67]
my_name = "I am Walid"
print(len(my_list))
print(len(my_name))

# my_function(s, 5)

def add(v1,v2):
	result = v1 + v2 
	print("This is the result:", result)

add(10,5)