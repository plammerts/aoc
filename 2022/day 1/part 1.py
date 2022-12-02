file = open("data.txt")

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