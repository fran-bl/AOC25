from heapq import heappush, heappop
from z3 import *


def part_1(data):
    total = 0

    for lights, btns, _ in data:
        q = [(0, len(lights), frozenset(lights))]
        visited = set()

        while q:
            d, n, curr = heappop(q)

            if curr in visited: continue

            visited.add(curr)

            if n == 0 and curr != lights: total += d; break

            for b in btns:
                new = frozenset(curr ^ b)
                heappush(q, (d + 1, len(new), new))
    
    return total


def part_2(data):
    total = 0

    for _, btns, joltage in data:
        solver = Optimize()

        x = [Int(f'b{i}') for i in range(len(btns))]

        for i in range(len(btns)):
            solver.add(x[i] >= 0)

        for i in range(len(joltage)):
            solver.add(Sum([x[j] for j in range(len(btns)) if i in btns[j]]) == joltage[i])

        solver.minimize(Sum(x))

        if solver.check() == sat: total += sum(solver.model()[x[i]].as_long() for i in range(len(btns)))
    
    return total


def main():
    with open('in.txt', 'r') as file:
        data = []
        for line in file.readlines():
            args = line.strip().split()
            config = args[0][1:-1]
            lights = set(i for i in range(len(config)) if config[i] == '#')
            buttons = [set(map(int, b[1:-1].split(','))) for b in args[1:-1]]
            joltage = tuple(map(int, args[-1][1:-1].split(',')))

            data.append((lights, buttons, joltage))

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()