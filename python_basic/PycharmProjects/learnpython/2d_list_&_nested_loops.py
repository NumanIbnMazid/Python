
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][2])

print("\n")

# nested for loop
for row in number_grid:
    for col in row:
        print(col)
    print(row)