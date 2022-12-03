import string

file = open("data.txt")
lines = file.read().split('\n')
sum = 0
alphabet = list(string.ascii_letters)

for line in lines:
    mid = int(len(line) / 2)
    fh = line[:mid]
    sh = line[mid:]
    mistake = list(set(fh) & set(sh))[0]
    sum += alphabet.index(mistake) + 1

print("Answer: ", sum)