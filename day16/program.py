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


def do_actual_permutation(arr, the_permutation):
    return [arr[the_permutation[idx]] for idx in range(len(arr))]


def perm(actions, input_arr):
    perm_length = len(input_arr)

    def to_perm(action_case, params):
        arr = list(range(perm_length))

        if action_case == "s":
            _rotation = int(params[0])
            arr = [arr[(x - _rotation) % perm_length] for x in arr]
        elif action_case == "x":
            x = int(params[0])
            y = int(params[1])
            arr[x], arr[y] = arr[y], arr[x]
        return arr

    permutations = [to_perm(a[0], a[1:].split("/")) for a in actions]

    p = range(perm_length)

    for _perm in permutations:
        p = do_actual_permutation(p, _perm)

    return p


def task1_arr(actions, dancers):
    one_round_permutation = perm(actions, dancers)

    dancers = do_actual_permutation(dancers, one_round_permutation)

    for a in actions:
        if a[0] == "p":
            params = a[1:].split("/")

            x = params[0]
            y = params[1]
            x_idx = dancers.index(x)
            y_idx = dancers.index(y)

            dancers[x_idx] = y
            dancers[y_idx] = x

    return dancers


def task2_arr(actions, dancers, dances):
    found_dances = []

    for i in range(dances):
        found_dances.append(dancers)
        dancers = task1_arr(actions, dancers)
        if dancers in found_dances:
            return found_dances[dances % (i+1)]

    return dancers


def to_str(arr):
    return "".join(arr)



def task1(actions, dancers):
    return to_str(task1_arr(actions, dancers))


def task2(actions, dancers, dances):
    return to_str(task2_arr(actions, dancers, dances))