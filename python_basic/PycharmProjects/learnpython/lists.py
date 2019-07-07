friends = ["Bivan", "John", "Def", "Faal", "Gia", "Uie"]
print(friends)
print(friends[1])
print(friends[-1])

#modify value
friends[1] = "Mike"

# starts from defined
print(friends[1:])
print(friends[1:3])

print("\n")

lucky_numbers = [3, 4, 6, 8, 10, 6, 32, 23]
friends = ["Kevin", "Karan", "Jim" , "Karan", "Oscar", "Neymar" , "Karan", "Silva"]
print(friends)

#Extend function
friends.extend(lucky_numbers)
print(friends)

#append
friends.append("Creed")
print(friends)

#insert
friends.insert(1, "Metallica")
print(friends)

#delete item
friends.remove("Creed")
print(friends)

#pop - removes the last item
friends.pop()
print(friends)

#search by index
print(friends.index("Karan"))

#sorting
friends = ["Kevin", "Karan", "Jim" , "Karan", "Oscar", "Neymar" , "Karan", "Silva"]
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)

#reverse
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2, friends)

#counting item
print(friends.count("Karan"))

#remove all
friends.clear()
print(friends)