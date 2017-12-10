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


def task1(elements_size, input_lengths):
    elements = [i for i in range(elements_size)]

    current_pos = 0
    skip_size = 0
    for length in input_lengths:
        reversable = take(skip(elements, current_pos), length)
        changable = reverse(reversable)
        elements = change(elements, changable, current_pos)

        current_pos = index(elements, current_pos + skip_size + length)

        skip_size = skip_size + 1

    return elements[0] * elements[1]



def to_ascii(text):
    return [int(ord(n)) for n in text]


def to_dense(sparse_hash):
    from functools import reduce
    return [reduce((lambda x, y: x ^ y), sparse_hash[(i * 16):((i+1) * 16)]) for i in range(16)]

def task2(input_text):

    one_round_input_lengths = to_ascii(input_text) + [17, 31, 73, 47, 23]

    input_lengths = []
    for i in range(64):
        input_lengths = input_lengths + one_round_input_lengths

    sparse_hash = task1(256, input_lengths)

    dense_hash = to_dense(sparse_hash)

    return ""

