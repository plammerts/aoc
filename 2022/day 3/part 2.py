import string

file = open("data.txt")
lines = file.read().split('\n')
sum = 0
alphabet = list(string.ascii_letters)

for index, line in enumerate(lines[::3]):
    index *= 3

    elf1 = lines[index]
    elf2 = lines[index + 1]
    elf3 = lines[index + 2]

    badge = list(set(elf1) & set(elf2) & set(elf3))[0]
    sum += alphabet.index(badge) + 1

print("Answer: ", sum)