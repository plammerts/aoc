file = open("data.txt")
lines = file.read().split('\n')


class Rope:
    def __init__(self) -> None:
        self.parts = [[0, 0] for _ in range(10)]
        self.visited = {(0, 0)}

    def left(self):
        self.parts[0][0] -= 1
        for index in range(1, 10):
            self.fix(index)
        self.update_visited()

    def right(self):
        self.parts[0][0] += 1
        for index in range(1, 10):
            self.fix(index)
        self.update_visited()

    def up(self):
        self.parts[0][1] += 1
        for index in range(1, 10):
            self.fix(index)
        self.update_visited()

    def down(self):
        self.parts[0][1] -= 1
        for index in range(1, 10):
            self.fix(index)
        self.update_visited()

    def same_x(self, index):
        return self.parts[index - 1][0] == self.parts[index][0]

    def same_y(self, index):
        return self.parts[index - 1][1] == self.parts[index][1]

    def fix(self, index):
        if self.parts[index] == self.parts[index - 1]:
            pass
        elif self.max_distance(index) <= 1:
            pass
        elif self.same_y(index):
            self.parts[index][0] = round(
                (self.parts[index][0] + self.parts[index - 1][0]) / 2)
        elif self.same_x(index):
            self.parts[index][1] = round(
                (self.parts[index][1] + self.parts[index - 1][1]) / 2)
        elif self.max_distance(index) > 1:
            dir = self.direction(index)
            self.parts[index] = [self.parts[index][0] +
                                 dir[0], self.parts[index][1] + dir[1]]
        else:
            pass

    def max_distance(self, index):
        b = self.parts[index]
        a = self.parts[index - 1]
        return max([abs(a[0] - b[0]), abs(a[1] - b[1])])

    def direction(self, index):
        b = self.parts[index]
        a = self.parts[index - 1]
        xdiff = a[0] - b[0]
        ydiff = a[1] - b[1]

        return ((xdiff > 0) - (xdiff < 0), (ydiff > 0) - (ydiff < 0))

    def update_visited(self):
        self.visited.add(tuple(self.parts[len(self.parts) - 1]))


rope = Rope()
for line in lines:
    dir, num = line.split(' ')
    for _ in range(int(num)):
        if dir == 'R':
            rope.right()
        elif dir == 'L':
            rope.left()
        elif dir == 'U':
            rope.up()
        elif dir == 'D':
            rope.down()

print("Answer: ", len(rope.visited))
