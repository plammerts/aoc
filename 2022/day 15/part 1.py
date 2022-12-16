import re


file = open("data.txt")
lines = file.read().split('\n')

beacons = []
sensors = []

for line in lines:
    [groups] = re.findall(
        r'Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)', line)
    groups = [int(x) for x in groups]
    sensors.append([groups[0], groups[1]])
    beacons.append([groups[2], groups[3]])

y_vals = [coord[1] for coord in sensors] + [coord[1] for coord in beacons]
x_vals = [coord[0] for coord in sensors] + [coord[0] for coord in beacons]
min_y = min(y_vals)
max_y = max(y_vals)
min_x = min(x_vals)
max_x = max(x_vals)
grid = {}
# grid = {(x, y): '.' for y in range(min_y, max_y + 1)
#         for x in range(min_x, max_x + 1)}
# grid = {(x, y): '.' for y in range(0, 100) for x in range(0, 100)}


def manhattan_distance(x1, y1, x2, y2):
    return abs(y2 - y1) + abs(x2 - x1)


# def draw(grid):
#     y_values = set([tup[1] for tup in sorted(grid, key=lambda tup: tup[1])])
#     x_values = set([tup[0] for tup in sorted(grid, key=lambda tup: tup[0])])
#     for y in y_values:
#         row = ''
#         for x in x_values:
#             if (x, y) in grid:
#                 row += grid[x, y]
#         print(row)

Y = 2000000
occupied = set()
for sensor, beacon in zip(sensors, beacons):
    dist = manhattan_distance(sensor[0], sensor[1], beacon[0], beacon[1])
    if Y in range(sensor[1] - dist, sensor[1] + dist):
        distx = dist - abs(Y - sensor[1])
        for x in range(sensor[0] - distx, sensor[0] + distx):
            occupied.add(x)

print("Answer: ", len(occupied))