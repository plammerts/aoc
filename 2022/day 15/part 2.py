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

def manhattan_distance(x1, y1, x2, y2):
    return abs(y2 - y1) + abs(x2 - x1)



for Y in range(0, 20):
    print(Y)
    occupied = set()
    for sensor, beacon in zip(sensors, beacons):
        dist = manhattan_distance(sensor[0], sensor[1], beacon[0], beacon[1])
        miny = sensor[1] - dist
        miny = miny if miny > 0 else 0
        maxy = sensor[1] + dist
        maxy = maxy if maxy < 20 else 20
        if Y >= miny and Y <= maxy:
            distx = dist - abs(Y - sensor[1])
            minx = sensor[0] - distx
            minx = minx if minx > 0 else 0
            maxx = sensor[0] + distx
            maxx = maxx if maxx < 20 else 20
            # for x in range(minx, maxx):
            #     occupied.add(x) 
            occupied.update(range(minx, maxx))
    if len(occupied) > 0 and len(occupied) != len(range(min(occupied), max(occupied) + 1)):
        print(len(occupied))
        print(len(range(min(occupied), max(occupied))))
        print("Fuock")

print("Answer: ", len(occupied))