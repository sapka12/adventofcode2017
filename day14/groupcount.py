def next_visited_layer(connection_map, all_visited):
    next_layer = set([])

    for visited in all_visited:
        for elem, connections in connection_map.items():
            if visited == elem:
                next_layer = next_layer | set(connections)

    return next_layer - all_visited

    return 0


def group_of_(x, input_map):
    visited = {x}
    next_layer = next_visited_layer(input_map, visited)

    while len(next_layer) > 0:

        next_layer = next_visited_layer(input_map, visited)
        visited = visited | next_layer

    return visited


def task1(input_map):
    return len(group_of_(0, input_map))


def count_group(input_map):
    keys = set(input_map.keys())
    print("keys:", len(keys))

    groups = []
    while len(keys) > 0:
        key = list(keys)[0]
        group = group_of_(key, input_map)
        keys = keys - group
        groups.append(group)

    return len(groups)