def part_1(data):
    total = 0

    for row in data:
        op = row[-1]
        nums = [int(x) for x in row[:-1]]
        
        if op == '+': total += sum(nums)
        else:
            res = 1
            for num in nums: res *= num
            total += res

    return total


def part_2(split, raw):
    total = 0
    seg_lengths = [len(max(col[:-1], key=len)) for col in split]
    ops = raw[-1].strip().split()

    data = []
    start = 0
    
    for seg, op in zip(seg_lengths, ops):
        args = [raw[i][start:start + seg] for i in range(len(raw) - 1)]
        data.append((args, op, seg))
        start += seg + 1

    for args, op, seg in data:
        answer = 0 if op == '+' else 1

        for i in range(seg):
            num = int(''.join(arg[i] for arg in args))
            
            if op == '+': answer += num
            else: answer *= num

        total += answer

    return total


def main():
    with open('in.txt', 'r') as file:
        raw = file.readlines()
        data = [line.strip().split() for line in raw]
        data = list(map(list, zip(*data)))

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data, raw))


if __name__ == '__main__':
    main()