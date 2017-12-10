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
        print("length: " + str(length))
        print("current_pos: " + str(current_pos))
        print("skip_size: " + str(skip_size))
        print(elements)
        reversable = take(skip(elements, current_pos), length)
        changable = reverse(reversable)
        elements = change(elements, changable, current_pos)

        current_pos = index(elements, current_pos + skip_size + length)

        skip_size = skip_size + 1
        print(elements)
        print()

    return elements[0] * elements[1]
