import itertools


file = open("data.txt")
lines = file.read().split('\n')
pairs = []
current_pair = []
for line in lines:
    if line == "":
        pairs.append(current_pair)
        current_pair = []
    else:
        line = eval(line)
        current_pair.append(line)


def is_right_order(left, right):
    if right == None:
        return False
    elif left == None:
        return True
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in list(itertools.zip_longest(left, right)):
            res = is_right_order(l, r)
            if res == None:
                continue
            else:
                return res
    elif isinstance(left, list) and isinstance(right, int):
        return is_right_order(left, [right])
    elif isinstance(right, list) and isinstance(left, int):
        return is_right_order([left], right)
    elif left > right:
        return False
    elif left < right:
        return True
    elif left == right:
        return None
    else:
        return None


sum = 0
for index, (left, right) in enumerate(pairs):
    if is_right_order(left, right):
        print("Correct: ", index + 1)
        sum += index + 1
print("Answer: ", sum)
