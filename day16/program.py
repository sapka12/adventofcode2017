def spin(arr, move):
    spin_of_size = -1 * move
    str_size = len(arr)
    return [arr[(i + spin_of_size) % str_size] for i in range(str_size)]


def exchange(arr, pos_a, pos_b):
    val_a = arr[pos_a]
    val_b = arr[pos_b]

    arr[pos_a] = val_b
    arr[pos_b] = val_a

    return arr


def partner(arr, val_a, val_b):
    pos_a = arr.index(val_a)
    pos_b = arr.index(val_b)

    arr[pos_a] = val_b
    arr[pos_b] = val_a

    return arr


def to_dance_step(action):
    action_case, params = action[0], action[1:].split("/")

    def fun_spin(arr):
        return spin(arr, int(params[0]))

    def fun_exchange(arr):
        return exchange(arr, int(params[0]), int(params[1]))

    def fun_partner(arr):
        return partner(arr, params[0], params[1])

    if action_case == "s":
        return fun_spin
    if action_case == "x":
        return fun_exchange
    if action_case == "p":
        return fun_partner


def task1(actions, char_arr):
    functions = [to_dance_step(action) for action in actions]

    while functions:
        first_fun, other_funs = functions[0], functions[1:]

        char_arr = first_fun(char_arr)
        functions = other_funs

    return char_arr


def two_dances_permutation(actions, arr):
    after_2_dances = task1(actions, task1(actions, arr))
    result = [None] * len(arr)
    for idx, val in enumerate(arr):
        result[idx] = arr.index(after_2_dances[idx])
    return result


def two_dances_permutation_without_partner(actions, arr):
    print("before", len(actions))

    actions = [a for a in actions if a[0] != "p"]
    print("after", len(actions))

    after_2_dances = task1(actions, task1(actions, arr))
    result = [None] * len(arr)
    for idx, val in enumerate(arr):
        result[idx] = arr.index(after_2_dances[idx])
    return result


def do_permutation(arr, permutation):
    result = [None] * len(arr)
    for idx, val in enumerate(permutation):
        result[idx] = arr[val]
    return result


def to_str(arr):
    return "".join(arr)


def action_to_permutation(action, array_size):
    default_perm = [i for i in range(array_size)]

    if action[0] == "x":
        idx_0 = int(action[1:].split("/")[0])
        idx_1 = int(action[1:].split("/")[1])
        temp = default_perm[idx_0]
        default_perm[idx_0] = default_perm[idx_1]
        default_perm[idx_1] = temp
        return default_perm

    if action[0] == "s":
        s = int(action[1:])
        return [default_perm[(i - s) % array_size] for i in range(array_size)]

    return []


def sum_permutations(perm1, perm2):
    print(perm1)
    print(perm2)
    return [perm1[perm2[i]] for i in range(len(perm1))]


def actions_to_permutation(actions, array_size):
    actions = [a for a in actions if a[0] != "p"]

    permutation = action_to_permutation(actions[0], array_size)
    if len(actions) > 1:
        for i in range(len(actions) - 1):
            idx = i + 1
            p = action_to_permutation(actions[idx], array_size)
            permutation = sum_permutations(permutation, p)

    return permutation


def task2(actions, arr, dances):
    permutation = two_dances_permutation_without_partner(actions, arr)

    permutations = dances // 2
    i = 0
    visited = [arr]

    while i < permutations:
        i = i + 1
        next_arr = do_permutation(arr, permutation)
        if next_arr in visited:
            return visited[(permutations % i)]

        visited.append(next_arr)
        arr = next_arr

    return arr
