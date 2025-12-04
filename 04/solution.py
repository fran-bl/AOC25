def part_1(data):
    cnt = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '@': continue

            adj = 0

            if i > 0:
                if data[i - 1][j] == '@': adj += 1
                if j > 0 and data[i - 1][j - 1] == '@': adj += 1
                if j < len(data[i]) - 1 and data[i - 1][j + 1] == '@': adj += 1

            if i < len(data) - 1:
                if data[i + 1][j] == '@': adj += 1
                if j > 0 and data[i + 1][j - 1] == '@': adj += 1
                if j < len(data[i]) - 1 and data[i + 1][j + 1] == '@': adj += 1

            if j > 0 and data[i][j - 1] == '@': adj += 1
            if j < len(data[i]) - 1 and data[i][j + 1] == '@': adj += 1

            cnt += not adj // 4

    return cnt


def part_2(data):
    cnt, removed = 0, 1

    while removed > 0:
        removed = 0

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] != '@': continue

                adj = 0

                if i > 0:
                    if data[i - 1][j] == '@': adj += 1
                    if j > 0 and data[i - 1][j - 1] == '@': adj += 1
                    if j < len(data[i]) - 1 and data[i - 1][j + 1] == '@': adj += 1

                if i < len(data) - 1:
                    if data[i + 1][j] == '@': adj += 1
                    if j > 0 and data[i + 1][j - 1] == '@': adj += 1
                    if j < len(data[i]) - 1 and data[i + 1][j + 1] == '@': adj += 1

                if j > 0 and data[i][j - 1] == '@': adj += 1
                if j < len(data[i]) - 1 and data[i][j + 1] == '@': adj += 1

                if adj < 4:
                    data[i][j] = '.'
                    cnt += 1
                    removed += 1

    return cnt


def main():
    with open('in.txt', 'r') as file:
        data = [list(line.strip()) for line in file.readlines()]

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()