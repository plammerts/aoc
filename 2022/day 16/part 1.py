from __future__ import annotations
import re

file = open("data.txt")
lines = file.read().split('\n')
valves = {}

class Valve:
    def __init__(self, index, id, flow, to) -> None:
        self.index = index
        self.id = id
        self.flow = flow
        self.to = to

for index, line in enumerate(lines):
    [groups] = re.findall(
        r'Valve (\w*) has flow rate=(\d*); tunnels? leads? to valves? (.*)', line)
    to = groups[2].split(', ')

    valve = Valve(index=index, id=groups[0], flow=int(groups[1]), to=to)
    valves[valve.id] = valve

def shortest_paths(valves):
    dist = [[10000 for _ in range(len(valves))] for _ in range(len(valves))]
    next = [[None for _ in range(len(valves))] for _ in range(len(valves))]
    shortest_paths = [[[] for _ in range(len(valves))] for _ in range(len(valves))]
    for v in valves:
        valve = valves[v]
        for to in valve.to:
            to_valve = valves[to]
            dist[valve.index][to_valve.index] = 1
            next[valve.index][to_valve.index] = to_valve.id
        
        dist[valve.index][valve.index] = 0
        next[valve.index][valve.index] = valve.id
    
    for k in range(len(valves)):
        for i in range(len(valves)):
            for j in range(len(valves)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]
    
    for u in valves:
        u = valves[u]
        for v in valves:
            v = valves[v]
            if next[u.index][v.index] != None:
                path = [u.id]
                check_index = u.index
                to_index = v.index
                while check_index != to_index:
                    id = next[check_index][to_index]
                    check_index = valves[id].index
                    path.append(id)
                shortest_paths[u.index][v.index] = path

    return shortest_paths

def order(current_valve, valves, shortest_paths, to_visit, visit_order, total_cost):
    current_valve = valves[current_valve]
    for to in to_visit:
        to = valves[to]
        cost = len(shortest_paths[current_valve.index][to.index])
        if cost < total_cost:
            tv = to_visit.copy()
            tv.remove(to.id)
            yield from order(to.id, valves, shortest_paths, tv, visit_order + [to.id], total_cost - cost)
    yield visit_order


def calc_vented(valves, shortest_paths, visit_order, time_remaining: int) -> int:
    current = "AA"
    pressure = 0

    for to in visit_order:
        current = valves[current]
        to = valves[to]
        cost = len(shortest_paths[current.index][to.index])
        time_remaining -= cost + 1
        pressure += to.flow * time_remaining
        current = to.id

    return pressure

shortest_paths = shortest_paths(valves)
unjammed_valves = [v for v in valves if valves[v].flow > 0]
for v in valves:
    valve = valves[v]
    print(valve.id)
    print(shortest_paths[valve.index])

visit_order = order("AA", valves, shortest_paths, unjammed_valves, [], 30)

max_pressure = 0
for visit_order in visit_order:
    pressure = calc_vented(valves, shortest_paths, visit_order, 30)

    if pressure > max_pressure:
        max_pressure = pressure

print(max_pressure)