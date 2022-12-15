file = open("data.txt")
lines = file.read().split('\n')


def draw(grid):
    y_values = set([tup[1] for tup in sorted(grid, key=lambda tup: tup[1])])
    x_values = set([tup[0] for tup in sorted(grid, key=lambda tup: tup[0])])
    for y in y_values:
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


min_x = min([tup[0] for tup in grid] + [500]) - 5
max_x = max([tup[0] for tup in grid] + [500]) + 5
min_y = min([tup[1] for tup in grid] + [0]) - 5
max_y = max([tup[1] for tup in grid] + [0]) + 5
grid = {(x, y): '.' if (x, y) not in grid else '#' for y in range(
    min_y, max_y) for x in range(min_x, max_x)}
grid[500, 0] = '+'


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
    # elif (y - max_y) < 5:
    #     return drop_sand(grid, x, y+1)
    else:
        return "inf"


found = False
num = 0

while found == False:
    if drop_sand(grid, 500, 0) == "inf":
        found = True
    else:
        num += 1

print("Answer: ", num)
draw(grid)
