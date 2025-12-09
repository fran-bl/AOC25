def part_1(data):
    return max([(abs(data[i][0] - data[j][0]) + 1) * (abs(data[i][1] - data[j][1]) + 1) for i in range(len(data) - 1) for j in range(i + 1, len(data))])


def part_2(data):
    vertices = set(data)
    h_edges = {}
    v_edges = {}

    for i in range(len(data)):
        a, b = data[i], data[(i + 1) % len(data)]
        
        if a[1] == b[1]:
            edge = (a[0], b[0]) if a[0] < b[0] else (b[0], a[0])

            if a[1] not in h_edges: h_edges[a[1]] = [edge]
            else: h_edges[a[1]].append(edge)

        elif a[0] == b[0]:
            edge = (a[1], b[1]) if a[1] < b[1] else (b[1], a[1])

            if a[0] not in v_edges: v_edges[a[0]] = [edge]
            else: v_edges[a[0]].append(edge)

    pairs = [(data[i], data[j]) for i in range(len(data) - 1) for j in range(i + 1, len(data))]

    return max([(abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1) for a, b in pairs if check_rect(a, b, h_edges, v_edges, vertices)])


def check_rect(p1, p2, h_edges, v_edges, vertices):
    p3, p4 = (p1[0], p2[1]), (p2[0], p1[1])

    if not (check_point(p3, h_edges, vertices) and check_point(p4, h_edges, vertices)): return False

    edge = (p1[0], p2[0]) if p1[0] < p2[0] else (p2[0], p1[0])
    
    for x in [x for x in v_edges.keys() if edge[0] < x < edge[1]]:
        for y1, y2 in v_edges[x]:
            if p1[1] < p2[1]:
                if y1 <= p1[1] < y2 or y1 < p2[1] <= y2: return False
            elif y1 < p1[1] <= y2 or y1 <= p2[1] < y2: return False

    edge = (p1[1], p2[1]) if p1[1] < p2[1] else (p2[1], p1[1])

    for y in [y for y in h_edges.keys() if edge[0] < y < edge[1]]:
        for x1, x2 in h_edges[y]:
            if p1[0] < p2[0]:
                if x1 <= p1[0] < x2 or x1 < p2[0] <= x2: return False
            elif x1 < p1[0] <= x2 or x1 <= p2[0] < x2: return False

    return True


def check_point(p, edges, vertices):
    if p in vertices: return True

    y_below = [y for y in edges.keys() if y > p[1]]
    
    c = 0
    for y in y_below:
       for x1, x2 in edges[y]:
           if x1 <= p[0] < x2: c += 1

    if c == 0:
        for y in y_below:
            for _ ,x2 in edges[y]:
                if p[0] == x2: c += 1

    return c % 2 != 0


def main():
    with open('in.txt', 'r') as file:
        data = [tuple(map(int, line.strip().split(','))) for line in file.readlines()]

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()