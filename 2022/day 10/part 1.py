file = open('data.txt')
lines = file.read().split('\n')
cycle = 1
X = 1
to_check = [20, 60, 100, 140, 180, 220]
SUM = 0


def check(X, cycle, SUM):
    if cycle in to_check:
        SUM += X * cycle
        return SUM
    else:
        return SUM


for line in lines:
    if line == "noop":
        SUM = check(X, cycle, SUM)
        cycle += 1
    else:
        SUM = check(X, cycle, SUM)

        cycle += 1
        SUM = check(X, cycle, SUM)

        num = int(line.strip("addx "))
        X += num
        cycle += 1

print("Answer: ", SUM)
