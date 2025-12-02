import math


def part_1(data):
    total = 0

    for L, R in data:
        if len(str(L)) % 2 != 0: b = str(pow(10, math.ceil(math.log10(L)))) if L != 1 else '10'
        else: b = str(L)

        b = b[:(len(b) // 2)]

        while (n := int(b) * int('1' + '0' * (len(b) - 1) + '1')) <= R:
            if L <= n <= R: total += n      
            b = str(int(b) + 1)

    return total


def part_2(data):
    total = 0
    nums = set()

    for L, R in data:
        for f in factors(len(str(L))):
            for i in range(pow(10, f - 1), pow(10, f)):
                n = int(str(i) * (len(str(L)) // f))
                if L <= n <= R: nums.add(n)

        for f in factors(len(str(R))):
            for i in range(pow(10, f - 1), pow(10, f)):
                n = int(str(i) * (len(str(R)) // f))
                if L <= n <= R: nums.add(n)

    total += sum(nums)

    return total


def factors(n):
    fs = []

    for i in range(1, n):
        if n % i == 0:
            fs.append(i)
    
    return fs


def main():
    with open('in.txt', 'r') as file:
        line = file.read().strip()
        data = [[int(L), int(R)] for r in line.split(',') for L, R in [r.strip().split('-')]]

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()