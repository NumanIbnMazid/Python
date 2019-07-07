# Differnce between list and touple

# it will be list
itlist = [(12, 23, 3, 4, 5, 65, 12), (23, 34, 44, 34), (23, 23, 3, 43)]
print(itlist[0])
itlist[0] = (12, 23, 23)
print(itlist)

print("\n")

#it will be tupple
#tuple is like list, It is a type of data structure. Not actually list\
#It cannot be changed or modified
coordinates = (12, 23, 3, 4, 5, 65, 12)
print(coordinates)
print(coordinates[2])

#after modifying tgis will give an error
coordinates[2] = 16
print(coordinates)

