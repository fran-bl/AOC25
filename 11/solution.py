def part_1(data):
    return search(data, 'you', 'out', {})


def part_2(data):
    return search(data, 'svr', 'fft', {}) * search(data, 'fft', 'dac', {}) * search(data, 'dac', 'out', {}) +\
           search(data, 'svr', 'dac', {}) * search(data, 'dac', 'fft', {}) * search(data, 'fft', 'out', {})


def search(data, curr, goal, memo):
    if curr == goal: return 1
    if curr == 'out': return 0
    if curr in memo: return memo[curr]

    cnt = sum(search(data, n, goal, memo) for n in data[curr])
    memo[curr] = cnt

    return cnt


def main():
    with open('in.txt', 'r') as file:
        data = {args[0][:-1]: args[1:] for line in file.readlines() if (args := line.strip().split())}

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()