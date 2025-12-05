def part_1(data):
    cnt = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '@': continue
            cnt += not check_area(data, i, j)[0] // 4

    return cnt


def part_2(data):
    cnt = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '@': continue
            cnt += rec_check(data, i, j)

    return cnt


def check_area(data, i, j):
    adj = 0
    mapping = {}

    if i > 0:
        if data[i - 1][j] == '@': adj += 1; mapping[(i - 1, j)] = True
        else: mapping[(i - 1, j)] = False
        if j > 0 and data[i - 1][j - 1] == '@': adj += 1; mapping[(i - 1, j - 1)] = True
        else: mapping[(i - 1, j - 1)] = False
        if j < len(data[i]) - 1 and data[i - 1][j + 1] == '@': adj += 1; mapping[(i - 1, j + 1)] = True
        else: mapping[(i - 1, j + 1)] = False

    if i < len(data) - 1:
        if data[i + 1][j] == '@': adj += 1; mapping[(i + 1, j)] = True
        else: mapping[(i + 1, j)] = False
        if j > 0 and data[i + 1][j - 1] == '@': adj += 1; mapping[(i + 1, j - 1)] = True
        else: mapping[(i + 1, j - 1)] = False
        if j < len(data[i]) - 1 and data[i + 1][j + 1] == '@': adj += 1; mapping[(i + 1, j + 1)] = True
        else: mapping[(i + 1, j + 1)] = False

    if j > 0 and data[i][j - 1] == '@': adj += 1; mapping[(i, j - 1)] = True
    else: mapping[(i, j - 1)] = False
    if j < len(data[i]) - 1 and data[i][j + 1] == '@': adj += 1; mapping[(i, j + 1)] = True
    else: mapping[(i, j + 1)] = False

    return adj, mapping


def rec_check(data, i, j):
    adj, mapping = check_area(data, i, j)

    if data[i][j] == '.' or adj >= 4: return 0

    data[i][j] = '.'
    cnt = 1

    for k, v in mapping.items():
        if v: cnt += rec_check(data, *k)

    return cnt


def main():
    with open('in.txt', 'r') as file:
        data = [list(line.strip()) for line in file.readlines()]

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()