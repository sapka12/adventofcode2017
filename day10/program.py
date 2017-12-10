def index(arr, n):
    return n % len(arr)


def skip(arr, n):
    return [arr[index(arr, n + i)] for i in range(len(arr))]


def take(arr, n):
    return arr[:n]


def reverse(arr):
    return list(reversed(arr))


def change(base_arr, change_arr, offset_start):
    for i in range(len(change_arr)):
        base_arr[index(base_arr, offset_start + i)] = change_arr[i]
    return base_arr


def common(elements, input_lengths, current_pos, skip_size):
    for length in input_lengths:
        reversable = take(skip(elements, current_pos), length)
        changable = reverse(reversable)
        elements = change(elements, changable, current_pos)

        current_pos = index(elements, current_pos + skip_size + length)

        skip_size = skip_size + 1

    return elements[0] * elements[1], current_pos, skip_size, elements


def task1(elements_size, input_lengths):
    return common([i for i in range(elements_size)], input_lengths, 0, 0)[0]


def to_ascii(text):
    return [int(ord(n)) for n in text]


def to_dense(sparse_hash):
    from functools import reduce
    return [reduce((lambda x, y: x ^ y), sparse_hash[(i * 16):((i + 1) * 16)]) for i in range(16)]


def to_hexa(i):
    return "{:02x}".format(i)


def task2(input_text):
    input_lengths = to_ascii(input_text) + [17, 31, 73, 47, 23]

    current_pos = 0
    skip_size = 0
    sparse_hash = [i for i in range(256)]
    for i in range(64):
        bits, current_pos, skip_size, sparse_hash = common(sparse_hash, input_lengths, current_pos, skip_size)

    return "".join([to_hexa(i) for i in to_dense(sparse_hash)])
