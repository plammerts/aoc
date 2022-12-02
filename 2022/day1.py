# Number of calories each elf is carrying
# 
import os, sys

FILENAME = "day1.txt"

path = os.path.join(sys.path[0], FILENAME)
file = open(path)

most_calories = 0
current_sum = 0

for line in file:
    if line.strip():
        current_sum += int(line)
    else:
        if current_sum > most_calories:
            most_calories = current_sum
        current_sum = 0

print("Answer: ", most_calories)