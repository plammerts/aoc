file = open("data.txt")
lines = file.read().split('\n')

num_stacks = int((len(lines[0]) + 1) / 4)
initialize = True
stacks = [[] for _ in range(num_stacks)]
crate_lines = []

for line in lines:
    if line.strip().startswith('1'):
        initialize = False
        crate_lines.reverse()

        for crate_line in crate_lines:
            for index, crate in enumerate(crate_line):
                if crate != '':
                    stacks[index].append(crate)
            
    if initialize:
        crates_line = [line[i:i+4] for i in range(0, len(line), 4)]
        crates_line = [crate.replace('[', '').replace(']', '').strip() for crate in crates_line]
        crate_lines.append(crates_line)        

    if line.startswith('move'):
        line = line.replace('move ', '').replace(' from', '').replace(' to', '').split(' ')
        commands = [int(command) for command in line]
        for i in range(commands[0]):
            crate = stacks[commands[1] - 1].pop()
            stacks[commands[2] - 1].append(crate)

answer = ''
for stack in stacks:
    answer += stack.pop()

print("Answer: ", answer)