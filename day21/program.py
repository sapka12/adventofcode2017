import numpy as np


def to_mx(text):
    def to_bool(x):
        if x == "#":
            return 1
        else:
            return 0

    return np.vectorize(to_bool)(np.array([list(row) for row in text.split("/")]))


start_image = to_mx(".#./..#/###")


def read(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()]


f = read("input.txt")

all_variations = {}


def key(mx):
    return mx.tostring()


def variations(mx):
    rotations = [np.rot90(mx, 1) for i in range(4)]
    _all_variations = [[mx, np.fliplr(mx), np.flipud(mx)] for mx in rotations]

    return [item for sublist in _all_variations for item in sublist]


for line in f:
    arr = line.split(" => ")
    _from = to_mx(arr[0])
    _to = to_mx(arr[1])

    for v in variations(_from):
        all_variations[key(_from)] = _to


def change_mx(mx, _variations):
    return _variations[key(mx)]


def sub_mx(_mx, x_range, y_range):
    return _mx[np.ix_(list(x_range), list(y_range))]


def reshape_tiles(_mx, tile_size, _variations):
    _size = len(_mx)
    out = np.zeros(_size * _size).reshape((_size, _size))

    for x in range(_size // tile_size):
        for y in range(_size // tile_size):
            r_x = [i + tile_size * x for i in range(tile_size)]
            r_y = [i + tile_size * y for i in range(tile_size)]

            tile = sub_mx(_mx, r_x, r_y)
            out[x, y] = change_mx(tile, _variations)
    return out


def reassembly(_mx, tile_size):
    pass


def iterate(_mx, _variations):
    tile_size = 2
    if len(_mx) % tile_size == 0:
        return reassembly(reshape_tiles(_mx, tile_size, _variations), 3)
    else:
        tile_size = 3
        return reassembly(reshape_tiles(_mx, tile_size, _variations), 4)
