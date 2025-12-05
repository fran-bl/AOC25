from heapq import heappop, heappush


def part_1(bounds, ids):
    stack, final = [], []

    for _ in range(len(bounds)):
        b = heappop(bounds)

        if b[1] == 'L': stack.append(b)
        elif len(stack) == 1: final.append([stack.pop()[0], b[0]])
        else: stack.pop()

    cnt = 0

    for id in ids:
        for r in final:
            L, R = r
            cnt += (L <= id <= R)

    return cnt


def part_2(bounds):
    stack, final = [], []

    for _ in range(len(bounds)):
        b = heappop(bounds)

        if b[1] == 'L': stack.append(b)
        elif len(stack) == 1: final.append([stack.pop()[0], b[0]])
        else: stack.pop()

    return sum([r[1] - r[0] + 1 for r in final])


def main():
    with open('in.txt', 'r') as file:
        ranges, ids = file.read().strip().split('\n\n')
        
        h = []
        for line in ranges.split('\n'):
            bounds = line.strip().split('-')
            heappush(h, (int(bounds[0]), 'L'))
            heappush(h, (int(bounds[1]), 'R'))

        ids = [int(l) for l in ids.strip().split('\n')]

    print('Part 1:', part_1(h.copy(), ids))
    print('Part 2:', part_2(h.copy()))


if __name__ == '__main__':
    main()