file = open("data.txt")
lines = file.read().split('\n')
grid_size = len(lines[0])


class Forest:
    def __init__(self, grid_size) -> None:
        self.grid_size = grid_size
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    def visible(self, x, y):
        return self.visible_up(x, y) * self.visible_down(x, y) * \
            self.visible_left(x, y) * self.visible_right(x, y)

    def visible_up(self, x, y):
        up = 0
        for index in range(y - 1, -1, -1):
            if self.grid[index][x] < self.grid[y][x]:
                up += 1
            else:
                up += 1
                break

        return 1 if up == 0 else up

    def visible_down(self, x, y):
        down = 0
        for index in range(y + 1, self.grid_size):
            if self.grid[index][x] < self.grid[y][x]:
                down += 1
            else:
                down += 1
                break

        return 1 if down == 0 else down

    def visible_left(self, x, y):
        left = 0
        for index in range(x - 1, -1, -1):
            if self.grid[y][index] < self.grid[y][x]:
                left += 1
            else:
                left += 1
                break

        return 1 if left == 0 else left

    def visible_right(self, x, y):
        right = 0
        for index in range(x + 1, self.grid_size):
            if self.grid[y][index] < self.grid[y][x]:
                right += 1
            else:
                right += 1
                break

        return 1 if right == 0 else right


forest = Forest(grid_size=grid_size)

for index1, line in enumerate(lines):
    for index2, tree in enumerate(line):
        forest.grid[index1][index2] = int(tree)

best = 0
for y in range(0, grid_size):
    for x in range(0, grid_size):
        total = forest.visible(x, y)
        if total > best:
            best = total

print("Answer: ", best)
