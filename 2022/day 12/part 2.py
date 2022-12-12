from heapq import heappush, heappop

file = open("data.txt")
lines = file.read().split('\n')


def bfs(grid, root, goal):
    queue = []
    visited = {}

    for cell in grid:
        for l in grid[cell]:
            if l in root:
                heappush(queue, (0, cell[0], cell[1]))
                visited = {(cell[0], cell[1])}

    while len(queue) > 0:
        d, x, y = heappop(queue)

        for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            cx = x + dx
            cy = y + dy
            if (cx, cy) not in visited and (cx, cy) in grid:
                current = grid[x, y] if grid[x, y] != root else 'a'
                next = grid[cx, cy] if grid[cx, cy] != goal else 'z'
                if ord(next) - ord(current) > 1:
                    continue
                if grid[cx, cy] == goal:
                    return d + 1
                visited.add((cx, cy))
                heappush(queue, (d + 1, cx, cy))


grid = {(x, y): l for y, line in enumerate(lines) for x, l in enumerate(line)}
distance = bfs(grid, 'aS', 'E')
print("Answer: ", distance)
