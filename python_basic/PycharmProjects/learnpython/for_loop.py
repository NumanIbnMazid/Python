
friends = ["Jim", "karen", "Kevin"]
for friend in friends:
    print(friend)
#print the position of array items
for index in range(len(friends)):
    print(index)
#another
for index in range(len(friends)):
    print(friends[index])

print("\n")

#print all numbers between 10, will not print 10
for index in range(10):
    print(index)
print("\n")
#print all numbers between 3 to 10, will not print 10
for index in range(3, 10):
    print(index)

print("\n")

# print out all letters in words
for letter in "Numan Ibn Mazid":
    print(letter)

print("\n")

# special iteration loop
for index in range(5):
    if index == 0:
        print("First Iteration")
    elif index == 1:
        print("Second Iteration")
    else:
        print(str(index + 1) + " no. Iteration")