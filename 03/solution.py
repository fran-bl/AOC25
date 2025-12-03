def part_1(data):
    total = 0

    for line in data:
        bats = list(map(int, list(line.strip())))
        a = max(bats[:-1])
        b = max(bats[bats.index(a) + 1:])

        total += a * 10 + b

    return total


def part_2(data):
    total = 0

    for line in data:
        bats = list(map(int, list(line.strip())))

        for i in range(11, -1, -1):
            d = max(bats[:-i] if i != 0 else bats)
            bats = bats[bats.index(d) + 1:]
            total += d * pow(10, i)

    return total


def main():
    with open('in.txt', 'r') as file:
        data = file.readlines()

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()