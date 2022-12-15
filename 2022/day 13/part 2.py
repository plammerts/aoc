import itertools
from functools import cmp_to_key

file = open("data.txt")
lines = file.read().split('\n')
pairs = []
for line in lines:
    if line != "":
        line = eval(line)
        pairs.append(line)


def compare(left, right):    
    if left == None:
        return -1
    elif right == None:
        return 1
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(right, list) and isinstance(left, int):
        return compare([left], right)
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    else:
        for l, r in itertools.zip_longest(left, right):
            res = compare(l, r)
            if res != 0:
                return res
    return 0

pairs.append([[2]])
pairs.append([[6]])
sorted = sorted(pairs, key=cmp_to_key(compare))
indices = []
for index, line in enumerate(sorted):
    if line in [[[2]], [[6]]]:
        indices.append(index + 1)
print("Answer: ", indices[0] * indices[1])