import os, sys

FILENAME = "day1_p2.txt"

path = os.path.join(sys.path[0], FILENAME)
file = open(path)

most_calories = [0, 0, 0]
current_sum = 0

def update(sum):
    for index, mc in enumerate(most_calories):
        if sum > mc:
            most_calories[index] = sum
            sum = 0
    most_calories.sort()

for line in file:
    if line.strip():
        current_sum += int(line)
    else:
        update(current_sum)
        current_sum = 0
        
update(current_sum)
print("Answer: ", sum(most_calories))