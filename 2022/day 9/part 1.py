file = open("data.txt")
lines = file.read().split('\n')
visited = set()
H = [0, 0]
T = [0, 0]


class Rope:
    def __init__(self) -> None:
        self.H = [0, 0]
        self.T = [0, 0]
        self.visited = {(0, 0)}

    def left(self):
        self.H[0] -= 1
        if self.uncoupled_x():
            if self.same_y():
                self.T[0] -= 1
            else:
                self.T = [self.H[0] + 1, self.H[1]]
        self.update_visited()

    def right(self):
        self.H[0] += 1
        if self.uncoupled_x():
            if self.same_y():
                self.T[0] += 1
            else:
                self.T = [self.H[0] - 1, self.H[1]]
        self.update_visited()

    def up(self):
        self.H[1] += 1
        if self.uncoupled_y():
            if self.same_x():
                self.T[1] += 1
            else:
                self.T = [self.H[0], self.H[1] - 1]
        self.update_visited()

    def down(self):
        self.H[1] -= 1
        if self.uncoupled_y():
            if self.same_x():
                self.T[1] -= 1
            else:
                self.T = [self.H[0], self.H[1] + 1]
        self.update_visited()

    def same_x(self):
        return self.T[0] == self.H[0]

    def same_y(self):
        return self.T[1] == self.H[1]

    def uncoupled_y(self):
        return abs(self.H[1] - self.T[1]) > 1

    def uncoupled_x(self):
        return abs(self.H[0] - self.T[0]) > 1

    def update_visited(self):
        self.visited.add(tuple(self.T))

    def print(self):
        print("H", rope.H)
        print("T", rope.T)


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
