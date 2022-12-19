from __future__ import annotations
import re
import itertools

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

    return dist


def paths(current_valve, valves, distances, path, total_cost, to_visit):
    for next in to_visit:
        dist = distances[valves[current_valve].index][valves[next].index]
        if dist < total_cost:
            tv = to_visit.copy()
            tv.remove(next)
            yield from paths(next, valves, distances, path + [next], total_cost - dist, tv)
    yield path


def pressure(valves, distances, path) -> int:
    pressure = 0
    total_time = 26
    current = "AA"

    for to in path:
        current = valves[current]
        to = valves[to]
        distance = distances[current.index][to.index]
        total_time -= distance + 1
        pressure += to.flow * total_time
        current = to.id

    return pressure


distances = shortest_paths(valves)
to_visit = [v for v in valves if valves[v].flow > 0]
all_paths = paths("AA", valves, distances, [], 26, to_visit)
pressures = [(pressure(valves, distances, path), path) for path in all_paths]
max_pressure = 0
for index, (p1, path1) in enumerate(sorted(pressures, reverse=True, key=lambda x: x[0])):
    if p1 * 2 < max_pressure:
        break
    for p2, path2 in pressures[index+1:]:
        if len(set(path1) & set(path2)) == 0:
            p = p1 + p2
            if p > max_pressure:
                print(max_pressure)
                max_pressure = p


print("Answer: ", max_pressure)