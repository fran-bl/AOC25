def part_1(data):
    S = (0, data[0].index('S'))
    end = len(data)
    visited = set()
    
    def check_below(row, col):
        for i in range(row, end):
            if data[i][col] == '^':
                if (i, col) not in visited:
                    visited.add((i, col))
                    check_below(i, col - 1)
                    check_below(i, col + 1)
                return

    check_below(*S)
    return len(visited)


def part_2(data):
    S = (0, data[0].index('S'))
    end = len(data)
    start_i = next(i for i in range(end) if data[i][S[1]] == '^')
    visited = {}
    
    def check_below(row, col):
        for i in range(row, end):
            if data[i][col] == '^':
                if (i, col) not in visited:
                    visited[(i, col)] = check_below(i, col - 1) + check_below(i, col + 1)
                return visited[(i, col)]

        return 1

    return check_below(start_i, S[1])
            

def main():
    with open('in.txt', 'r') as file:
        data = [list(line.strip()) for line in file.readlines()]

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()