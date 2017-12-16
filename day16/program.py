def spin(param, input_str):
    spin_of_size = -1 * int(param)
    str_size = len(input_str)
    return [input_str[(i + spin_of_size) % str_size] for i in range(str_size)]


def exchange(params):
    def do_action(input_str):
        arr = [input_str[i] for i in range(len(input_str))]

        p = "".join(params).split("/")

        pos_a = int(p[0])
        pos_b = int(p[1])

        val_a = arr[pos_a]
        val_b = arr[pos_b]

        arr[pos_a] = val_b
        arr[pos_b] = val_a

        return arr


def partner(params, input_str):
    arr = [input_str[i] for i in range(len(input_str))]

    p = "".join(params).split("/")

    val_a = p[0]
    val_b = p[1]

    pos_a = arr.index(val_a)
    pos_b = arr.index(val_b)

    arr[pos_a] = val_b
    arr[pos_b] = val_a

    return arr


def process(action, input_str):
    arr = [input_str[i] for i in range(len(input_str))]
    action_case, *params = action
    if action_case == "s":
        return spin("".join(params), input_str)
    if action_case == "x":
        return exchange("".join(params), input_str)
    if action_case == "p":
        return partner("".join(params), input_str)


def task1(actions, input_str):

    while len(actions) != 0:
        first_action, *other_actions = actions
        next_input_str = process(first_action, input_str)
        input_str = next_input_str
        actions = other_actions

    return input_str


def task2(actions, input_str, dances):

    for i in range(dances):
        input_str = task1(actions, input_str)

    return input_str
