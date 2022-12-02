def game_score(shape1, shape2):
    if shape1 == 'A':
        if shape2 == 'X':
            return 3
        elif shape2 == 'Y':
            return 6
        elif shape2 == 'Z':
            return 0
    elif shape1 == 'B':
        if shape2 == 'X':
            return 0
        elif shape2 == 'Y':
            return 3
        elif shape2 == 'Z':
            return 6
    elif shape1 == 'C':
        if shape2 == 'X':
            return 6
        elif shape2 == 'Y':
            return 0
        elif shape2 == 'Z':
            return 3

def shape_score(shape):
    if shape == 'X':
        return 1
    elif shape == 'Y':
        return 2
    elif shape == 'Z':
        return  3
            

file = open("data.txt", "r")
lines = file.read().split("\n")
lines = [line.split(" ") for line in lines]
lines = [(shape_score(line[1]) + game_score(line[0], line[1])) for line in lines]
print("Answer: ", sum(lines))
