from heapq import heappush, heappop


def part_1(data):
    ids = {k: None for k in data}
    pairs = []

    [heappush(pairs, (dist(data[i], data[j]), data[i], data[j])) for i in range(len(data) - 1) for j in range(i + 1, len(data))]

    c = 0

    for _ in range(1000):
        _, a, b = heappop(pairs)

        if ids[a] == ids[b] != None: continue
        elif ids[a] == ids[b] == None:
            ids[a] = ids[b] = c
            c += 1

        elif ids[a] == None: ids[a] = ids[b]
        elif ids[b] == None: ids[b] = ids[a]
        else:
            points = [k for k, v in ids.items() if v == ids[b]]
            for k in points:
                ids[k] = ids[a]

    sizes = sorted([sum([v == i for v in ids.values()]) for i in range(c)], reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def part_2(data):
    ids = {k: None for k in data}
    pairs = []

    [heappush(pairs, (dist(data[i], data[j]), data[i], data[j])) for i in range(len(data) - 1) for j in range(i + 1, len(data))]

    c = 0

    while True:
        _, a, b = heappop(pairs)

        if ids[a] == ids[b] != None: continue
        elif ids[a] == ids[b] == None:
            ids[a] = ids[b] = c
            c += 1

        elif ids[a] == None: ids[a] = ids[b]
        elif ids[b] == None: ids[b] = ids[a]
        else:
            points = [k for k, v in ids.items() if v == ids[b]]
            for k in points:
                ids[k] = ids[a]

        if len(set(ids.values())) == 1: return a[0] * b[0]


def dist(a, b):
    return sum([(a[i] - b[i])**2 for i in range(len(a))])


def main():
    with open('in.txt', 'r') as file:
        data = [tuple(map(int, line.strip().split(','))) for line in file.readlines()]

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()