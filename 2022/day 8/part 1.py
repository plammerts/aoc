file = open("data.txt")
lines = file.read().split('\n')
grid_size = len(lines[0])


class Forest:
    def __init__(self, grid_size) -> None:
        self.grid_size = grid_size
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    def visible(self, x, y):
        return self.visible_up(x, y) or self.visible_down(x, y) or \
            self.visible_left(x, y) or self.visible_right(x, y)

    def visible_up(self, x, y):
        up = [self.grid[index][x] for index in range(
            0, y) if self.grid[index][x] >= self.grid[y][x]]
        return len(up) == 0

    def visible_down(self, x, y):
        down = [self.grid[index][x] for index in range(
            y + 1, self.grid_size) if self.grid[index][x] >= self.grid[y][x]]
        return len(down) == 0

    def visible_left(self, x, y):
        left = [self.grid[y][index] for index in range(
            0, x) if self.grid[y][index] >= self.grid[y][x]]
        return len(left) == 0

    def visible_right(self, x, y):
        right = [self.grid[y][index] for index in range(
            x + 1, self.grid_size) if self.grid[y][index] >= self.grid[y][x]]
        return len(right) == 0


forest = Forest(grid_size=grid_size)

for index1, line in enumerate(lines):
    for index2, tree in enumerate(line):
        forest.grid[index1][index2] = int(tree)

total_visible = 0
for y in range(1, grid_size - 1):
    for x in range(1, grid_size - 1):
        if forest.visible(x, y):
            total_visible += 1

print("Answer: ", total_visible + (forest.grid_size * 4 - 4))