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
    last_closest = [0 for _ in range(len(pva_list))]
    closest = [manhattan_distance(p) for (p, v, a) in pva_list]

    while closest != last_closest or 0 in closest:
        last_closest = closest
        next_pva_list = [step_for_pva(pva) for pva in pva_list]
        closest = [
            min(
                manhattan_distance(pva_list[idx][0]),
                manhattan_distance(next_pva_list[idx][0])
            ) for idx in range(len(pva_list))
        ]
        pva_list = next_pva_list

    return min(closest)


print(task1("example.txt"))
print(task1("input.txt"))


