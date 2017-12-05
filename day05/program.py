def is_out_of_maze(arr, pointer):
    return pointer < 0 or len(arr) <= pointer


def solve(arr, idx, num_of_changes, diff_by_offset):

    while not is_out_of_maze(arr, idx):
        offset = arr[idx]
        arr[idx] = offset + diff_by_offset(offset)
        idx = idx + offset
        num_of_changes = num_of_changes + 1

    return num_of_changes


def task1(arr):
    return solve(arr, 0, 0, lambda x: 1)


def offset_by_2(offset):
    if offset > 2:
        return -1
    return 1


def task2(arr):
    return solve(arr, 0, 0, offset_by_2)