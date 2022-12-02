def shape_score(shape1, shape2):
    if shape1 == 'A':
        if shape2 == 'X':
            return 3
        elif shape2 == 'Y':
            return 1
        elif shape2 == 'Z':
            return 2
    elif shape1 == 'B':
        if shape2 == 'X':
            return 1
        elif shape2 == 'Y':
            return 2
        elif shape2 == 'Z':
            return 3
    elif shape1 == 'C':
        if shape2 == 'X':
            return 2
        elif shape2 == 'Y':
            return 3
        elif shape2 == 'Z':
            return 1

def game_score(shape):
    if shape == 'X':
        return 0
    elif shape == 'Y':
        return 3
    elif shape == 'Z':
        return  6
            

file = open("data.txt", "r")
lines = file.read().split("\n")
lines = [line.split(" ") for line in lines]
lines = [game_score(line[1]) + shape_score(line[0], line[1]) for line in lines]
print("Answer: ", sum(lines))
