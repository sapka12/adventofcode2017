def read_file(file_path):
    with open(file_path) as f:
        return [[c for c in list(x) if c != '\n'] for x in f.readlines()]


def start_position(data):
    return 0, data[0].index('|')


def sign_in_pos(line, pos, data):
    return data[line][pos]


def next_pos(direction, line, pos, sign, word, data):
    pass
    # if direction == 'v':
    #     return direction, line, pos, sign, word


def task1(file_path):
    data = read_file(file_path)

    # v ^ < >
    direction = "v"
    line, pos = start_position(data)
    word = ""

    sign = sign_in_pos(line, pos, data)

    while sign != ' ':
        direction, line, pos, sign, word = next_pos(direction, line, pos, sign, word, data)

    return word


def task2(file_path):
    pass
