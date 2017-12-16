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


def task2(actions, arr, dances):
    for i in range(dances):
        arr = task1(actions, arr)

    return arr
