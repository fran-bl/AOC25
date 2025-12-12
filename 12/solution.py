def part_1(shapes, grids):
    return sum(sum(reqs[i] * len(shapes[i]) for i in range(len(reqs))) <= grid[0] * grid[1] for grid, reqs in grids)


def part_2(shapes, grids):
    return\
    """
            *
           /.\\
          / o \\
         / .  o\\
         -------
           | |
    
      Merry Christmas!
    """


def main():
    with open('in.txt', 'r') as file:
        blocks = file.read().strip().split('\n\n')

        grids = []

        for line in blocks[-1].split('\n'):
            args = line.strip().split()
            reqs = list(map(int, args[1:]))
            grid = tuple(int(c) for c in args[0][:-1].split('x'))

            grids.append((grid, reqs))

        shapes = {}

        for block in blocks[:-1]:
            lines = block.split('\n')
            mapping = []

            for i in range(len(lines[1:])):
                line = lines[i + 1].strip()

                for j in range(len(line)):
                    if line[j] == '#': mapping.append((i, j))

            shapes[int(lines[0].strip()[:-1])] = mapping


    print('Part 1:', part_1(shapes, grids))
    print('Part 2:', part_2(shapes, grids))


if __name__ == '__main__':
    main()