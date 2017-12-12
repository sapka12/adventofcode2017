from functools import reduce


def to_vector(text):
    if text == "n":
        return 1, 1
    if text == "ne":
        return 0, 1
    if text == "nw":
        return 1, 0
    if text == "s":
        return -1, -1
    if text == "se":
        return -1, 0
    if text == "sw":
        return 0, -1


vec = ["n", "ne", "se", "s", "sw", "nw"]
vec2 = [to_vector(i) for i in vec]


def invert(text):
    if text == "n":
        return "s"
    if text == "s":
        return "n"
    if text == "ne":
        return "sw"
    if text == "nw":
        return "se"
    if text == "se":
        return "nw"
    if text == "sw":
        return "ne"


def remove_one_pair_of_inverts(vector):
    for x in vector:
        inv = invert(x)
        if inv in vector:
            vector.remove(x)
            vector.remove(inv)
            return vector
    return vector


def vector_add(a, b):
    return a[0] + b[0], a[1] + b[1]


def create_next_layer(layer_id, new_layer, visited):
    print(layer_id)
    list_of_list = [[vector_add(v, outer_elem) for v in vec2] for outer_elem in new_layer]
    flatten = set([item for sublist in list_of_list for item in sublist])
    new_layer = set(filter(lambda x: x not in visited, flatten))
    visited = visited | new_layer
    return layer_id + 1, new_layer, visited


def end_pos(steps):
    return reduce(vector_add, [to_vector(step) for step in steps])


def task1(steps):
    x, y = end_pos(steps)
    print(x, y)

    visited = set([(0, 0)])
    new_layer = visited
    layer = 0
    while (x, y) not in visited:
        layer, new_layer, visited = create_next_layer(layer, new_layer, visited)
    return layer


def task2(vectors):
    all = len(vectors)

    visited = set([(0, 0)])
    new_layer = visited
    layer = 0

    for i in range(all):

        print("step: ", i, (100.0 * i) / all)

        path = vectors[0:i + 1]
        x, y = end_pos(path)
        while (x, y) not in visited:
            layer, new_layer, visited = create_next_layer(layer, new_layer, visited)

    return layer
