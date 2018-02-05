def read(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()]


def manhattan_distance(coordinate):
    return sum([abs(c) for c in coordinate])


def sum_coordinates(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1], c1[2] + c2[2]


def parse_line(line):
    p = ">, "

    def parse_coordinate(c):
        return [int(i) for i in c.split(",")]

    pva = [parse_coordinate(e[3:].replace(">", "")) for e in line.split(p)]

    return pva[0], pva[1], pva[2]


def pva_lines(file_path):
    return [parse_line(line) for line in read(file_path)]


def step_for_pva(pva):
    p = pva[0]
    v = pva[1]
    a = pva[2]

    new_v = sum_coordinates(v, a)
    new_p = sum_coordinates(p, v)

    return new_p, new_v, a


def task1(file_path):
    pva_list = pva_lines(file_path)

    for _ in range(100000):
        pva_list = [step_for_pva(pva) for pva in pva_list]

    distances = [manhattan_distance(p) for (p, v, a) in pva_list]
    return distances.index(min(distances))


# print(task1("example.txt"))
# print(task1("input.txt"))


def remove_collided(PVAs):

    coordinate_count = {}
    for pva in PVAs:
        pos = pva[0]
        if pos in coordinate_count.keys():
            coordinate_count[pos] += 1
        else:
            coordinate_count[pos] = 1

    return [pva for pva in PVAs if coordinate_count[pva[0]] == 1]


def task2(file_path):
    pva_list = pva_lines(file_path)
    print(len(pva_list))

    for i in range(1000000):

        if i % 10000 == 0:
            print(i, len(pva_list), pva_list[0])

        pva_list = [step_for_pva(pva) for pva in pva_list]
        pva_list = remove_collided(pva_list)

    return len(pva_list)


# print(task2("example2.txt"))
print(task2("input.txt"))
