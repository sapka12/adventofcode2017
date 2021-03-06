def maximum(arr):
    return max([max(a) for a in arr])


def next_layer(arr):
    orig_size = len(arr)
    size = orig_size + 2

    result = [[None] * size for i in range(size)]

    for x in range(orig_size):
        for y in range(orig_size):
            result[x + 1][y + 1] = arr[x][y]

    actual_max = maximum(arr)
    right = [actual_max + 1 + i for i in range(orig_size + 1)]

    actual_max = max(right)
    top = [actual_max + 1 + i for i in range(orig_size + 1)]

    actual_max = max(top)
    left = [actual_max + 1 + i for i in range(orig_size + 1)]

    actual_max = max(left)
    bottom = [actual_max + 1 + i for i in range(orig_size + 1)]

    for i in range(len(right)):
        result[len(result) - 1][len(result) - 2 - i] = right[i]

    for i in range(len(top)):
        result[len(result) - 2 - i][0] = top[i]

    for i in range(len(left)):
        result[0][1 + i] = left[i]

    for i in range(len(bottom)):
        result[1 + i][len(result) - 1] = bottom[i]

    return result


def generate_square_which_contains(x):
    result = [[1]]

    while maximum(result) < x:
        result = next_layer(result)

    return result


def manhattan_disatance(pos1, pos2):
    (pos1x, pos1y) = pos1
    (pos2x, pos2y) = pos2
    return abs(pos1x - pos2x) + abs(pos1y - pos2y)


def pos_of_val(arr, value):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == value:
                return (x, y)


def get_distance_from_1(arr, value):
    pos_1 = pos_of_val(arr, 1)
    pos_val = pos_of_val(arr, value)
    return manhattan_disatance(pos_1, pos_val)


def manhattan_disatance_from_1(num):
    arr = generate_square_which_contains(num)
    return get_distance_from_1(arr, num)


def in_arr(arr, idx):
    return idx >= 0 and idx < len(arr)


def part2(input):

    counter = 1

    while True:

        counter = counter + 1

        arr = generate_square_which_contains(counter)
        max_val = maximum(arr)

        zeros = [[0] * len(arr[x]) for x in range(len(arr))]

        for num in [i + 1 for i in range(max_val)]:
            x, y = pos_of_val(arr, num)

            next_val = 1
            if num == 1:
                zeros[x][y] = next_val
            else:
                next_val = sum(
                    [sum(
                        [
                            zeros[xx][yy]
                            for yy in range(y - 1, y + 2)
                            if in_arr(zeros[xx], yy)
                        ]
                    )
                        for xx in range(x - 1, x + 2)
                        if in_arr(zeros, xx)
                    ]
                )
                zeros[x][y] = next_val

            if next_val > input:
                return next_val


# print(manhattan_disatance_from_1(361527))
# print(part2(361527))