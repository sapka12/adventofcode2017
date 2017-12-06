def next_idx(arr, actual_idx):
    return (actual_idx + 1) % len(arr)


def next_state(arr, left, idx):
    if left == 0:
        return arr
    else:
        arr[idx] = arr[idx] + 1
        return next_state(arr, left - 1, next_idx(arr, idx))


def go(arr, strategy):
    visited = []

    while not (arr in visited):
        visited.append([elem for elem in arr])
        maximum = max(arr)
        max_index = arr.index(max(arr))
        arr[max_index] = 0
        arr = next_state(arr, maximum, next_idx(arr, max_index))

    return strategy(visited, arr)


def task1(arr):
    return go(arr, lambda visited, arr: len(visited))


def task2(arr):
    return go(arr, lambda visited, arr: len(visited) - visited.index(arr))