file = open("data.txt")
line = file.read()
index = 0
found = False
while found == False:
    sequence = line[index:index+14]
    if len(set(sequence)) == 14:
        found = True
        index = index + 14
    else: 
        index += 1

print("Answer: ", index)