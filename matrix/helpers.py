# print matrix

# Lets say we have an arry called grid
l = len(grid[0])
dp = [[0] * l for i in range(l)]

# to print
for row in grid:
    for col in row:
        print col

# one more
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        print (grid[i][j])
