def part_1(data):
    cnt = 0
    total_shift = 50

    for line in data:
        shift = int(line[1:])

        if line.startswith('L'):
            shift = -shift

        total_shift += shift

        if total_shift % 100 == 0:
            cnt += 1

    return cnt


def part_2(data):
    cnt = 0
    curr = 50

    for line in data:
        shift = int(line[1:])

        cnt += shift // 100
        rem = shift % 100

        if line.startswith('L'):
            cnt += (curr != 0 and rem >= curr)  
            curr = (curr - rem) % 100 
        
        else:
            cnt += (curr + rem) >= 100
            curr = (curr + rem) % 100

    return cnt


def main():
    with open('in.txt', 'r') as file:
        data = file.readlines()

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()