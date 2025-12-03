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
    nums = set()

    for L, R in data:
        strL, strR = str(L), str(R)

        for f in factors(len(strL)):
            for i in range(int(strL[:f]), pow(10, f)):
                n = int(str(i) * (len(strL) // f))
                if L <= n <= R: nums.add(n)

        for f in factors(len(strR)):
            for i in range(pow(10, f - 1), int(strR[:f]) + 1):
                n = int(str(i) * (len(strR) // f))
                if L <= n <= R: nums.add(n)

    return sum(nums)


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