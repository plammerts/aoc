file = open("data.txt")
line = file.read()
index = 0
found = False
while found == False:
    sequence = line[index:index+4]
    if len(set(sequence)) == 4:
        found = True
        index = index + 4
    else: 
        index += 1

print("Answer: ", index)