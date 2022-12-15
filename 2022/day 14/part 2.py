file = open("data.txt")
lines = file.read().split('\n')


def draw(grid):
    y_values = set([tup[1] for tup in sorted(grid, key=lambda tup: tup[1])])
    x_values = set([tup[0] for tup in sorted(grid, key=lambda tup: tup[0])])
    for y in range(200):
        row = ''
        for x in x_values:
            if (x, y) in grid:
                row += grid[x, y]
        print(row)


grid = {}
for line in lines:
    coords = line.split(" -> ")
    coords = [coord.split(',') for coord in coords]
    coords = [(int(coord[0]), int(coord[1])) for coord in coords]

    for prev, next in zip(coords, coords[1:]):
        if prev[0] == next[0]:
            dir = -1 if prev[1] > next[1] else 1
            x = prev[0]
            for y in range(prev[1], next[1] + dir, dir):
                grid[x, y] = "#"
        if prev[1] == next[1]:
            dir = -1 if prev[0] > next[0] else 1
            y = prev[1]
            for x in range(prev[0], next[0] + dir, dir):
                grid[x, y] = "#"


min_x = 0
max_x = 1000
min_y = 0
max_y = 1000
floor = max([tup[1] for tup in grid]) + 2
grid = {(x, y): '.' if (x, y) not in grid else '#' for y in range(
    min_y, max_y + 2) for x in range(min_x, max_x)}
grid[500, 0] = '+'
for x in range(min_x, max_x):
    grid[x, floor] = "#"


def drop_sand(grid, x, y):
    if (x, y+1) in grid and grid[x, y+1] == '.':
        return drop_sand(grid, x, y+1)
    elif (x-1, y+1) in grid and grid[x-1, y+1] == '.':
        return drop_sand(grid, x-1, y+1)
    elif (x+1, y+1) in grid and grid[x+1, y+1] == '.':
        return drop_sand(grid, x+1, y+1)
    elif (x, y) in grid and grid[x, y] == '.' and (x, y+1) in grid:
        grid[x, y] = 'o'
        return grid
    else:
        return "inf"

found = False

while found == False:
    if drop_sand(grid, 500, 0) == "inf":
        found = True

num = 1
for x, y in grid:
    if grid[x, y] == 'o':
        num += 1

print("Answer: ", num)