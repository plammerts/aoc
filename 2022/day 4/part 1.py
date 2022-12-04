file = open("data.txt")
lines = file.read().split('\n')
lines = [line.split(',') for line in lines]
lines = [[elf1.split('-'), elf2.split('-')] for [elf1, elf2] in lines]
lines = [[[int(num) for num in elf] for elf in line] for line in lines]

count = 0
for [[start1, end1], [start2, end2]] in lines:
    range1 = set(range(start1, end1 + 1))
    range2 = set(range(start2, end2 + 1))
    intersection = range1 & range2
    if range1 == intersection or range2 == intersection:
        count += 1

print("Answer: ", count)

