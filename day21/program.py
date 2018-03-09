import numpy as np


def read(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()]


f = read("input.txt")

all_variations = {}


def key(mx):
    return mx.tostring()


def variations(mx):
    return [
        np.fliplr(mx),
        np.flipud(mx),
        np.rot90(mx, 1),
        np.rot90(mx, 2),
        np.rot90(mx, 3),
        mx
    ]


def to_mx(text):

    def to_bool(x):
        if x == "#":
            return 1
        else:
            return 0

    return np.vectorize(to_bool)(np.array([list(row) for row in text.split("/")]))


for line in f:
    arr = line.split(" => ")
    _from = to_mx(arr[0])
    _to = to_mx(arr[1])

    for v in variations(_from):
        all_variations[key(_from)] = _to


print(len(all_variations.values()))