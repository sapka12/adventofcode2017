from hash import hash_knot
from groupcount import count_group


def hexa_to_binary(hexa):
    return "".join(["{0:4b}".format(int(c, 16)).replace(" ", "0") for c in hexa])


def square(input_txt):
    xxx = [hexa_to_binary(hash_knot(input_txt + "-" + str(i))) for i in range(128)]
    return [[int(i) for i in s] for s in xxx]


def task1(input_txt):
    return sum([sum(arr) for arr in square(input_txt)])


def neighbours_with_1(x, y, mx):
    ns = [
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1)
    ]
    return [n for n in ns if 0 <= n[0] < 128 and 0 <= n[1] < 128 and mx[n[0]][n[1]] == 1]


def task2(input_txt):
    mx = square(input_txt)
    sum_map = {}

    print("matrix ready")

    for x in range(128):
        for y in range(128):
            if mx[x][y] == 1:
                neighbours = neighbours_with_1(x, y, mx)
                sum_map.update({(x, y): neighbours})

    print("group map ready")

    return count_group(sum_map)
