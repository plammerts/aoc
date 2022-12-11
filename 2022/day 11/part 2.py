import math
file = open("data.txt")
monkeys = []
lines = file.read().split('\n')
current_monkey = None


class Monkey():
    def __init__(self, index) -> None:
        self.index = index
        self.items = []
        self.operation = None
        self.operation_number = None
        self.test_number = None
        self.monkey_true = None
        self.monkey_false = None
        self.inspects = 0

    def run(self, lcm):
        while len(self.items) > 0:
            self.run_next_item(lcm)

    def run_next_item(self, lcm):
        self.inspects += 1
        item = self.items.pop()
        if self.operation == "*" and self.operation_number == None:
            item *= item
        elif self.operation == "*" and self.operation_number != None:
            item *= self.operation_number
        elif self.operation == "+":
            item += self.operation_number
        item = item % lcm

        if item % self.test_number == 0:
            self.monkey_true.add_item(item)
        else:
            self.monkey_false.add_item(item)
    



    def add_item(self, item):
        self.items.append(item)


for line in lines:
    line = line.strip()
    if line.startswith("Monkey"):
        current_monkey = Monkey(index=len(monkeys))
    elif line.startswith("Starting"):
        items = line.strip("Starting items: ").split(", ")
        items = [int(item) for item in items]
        current_monkey.items = items
    elif line.startswith("Operation"):
        line = line.strip("Operation: new = ")
        operation_numbers = [int(s) for s in line.split() if s.isdigit()]
        if "*" in line:
            current_monkey.operation = "*"
        elif "+" in line:
            current_monkey.operation = "+"
        if len(operation_numbers) == 1:
            current_monkey.operation_number = operation_numbers[0]
    elif line.startswith("Test"):
        current_monkey.test_number = int(line.strip("Test: divisble by "))
    elif line.startswith("If true"):
        current_monkey.monkey_true = int(
            line.strip("If true: throw to monkey "))
    elif line.startswith("If false"):
        current_monkey.monkey_false = int(
            line.strip("If false: throw to monkey "))
        monkeys.append(current_monkey)

for monkey in monkeys:
    monkey.monkey_true = monkeys[monkey.monkey_true]
    monkey.monkey_false = monkeys[monkey.monkey_false]

lcm = math.lcm(*[monkey.test_number for monkey in monkeys])

rounds = 10000
for _ in range(rounds):
    for monkey in monkeys:
        monkey.run(lcm)

top_two = sorted([monkey.inspects for monkey in monkeys], reverse=True)[:2]
print(top_two[0] * top_two[1])