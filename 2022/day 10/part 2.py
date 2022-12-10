file = open('data.txt')
lines = file.read().split('\n')


class Drawing():
    def __init__(self) -> None:
        self.drawing = ["" for _ in range(6)]
        self.cycle = 0
        self.X = 1

    def draw(self):
        row = self.cycle // 40
        if self.cycle - (row * 40) in [self.X - 1, self.X, self.X + 1]:
            self.replace_str_index(row, self.cycle, '#')
        else:
            self.replace_str_index(row, self.cycle, '.')

    def replace_str_index(self, row, index, replacement):
        self.drawing[row] = '%s%s%s' % (
            self.drawing[row][:index], replacement, self.drawing[row][index+1:])


drawing = Drawing()

for line in lines:
    if line == "noop":
        drawing.draw()
        drawing.cycle += 1
    else:
        drawing.draw()

        drawing.cycle += 1
        drawing.draw()

        num = int(line.strip("addx "))
        drawing.X += num
        drawing.cycle += 1

for i in range(len(drawing.drawing)):
    print(drawing.drawing[i])