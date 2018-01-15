def read_file(file_path):
    with open(file_path) as f:
        return [[c for c in list(x) if c != '\n'] for x in f.readlines()]


def start_position(data):
    return 0, data[0].index('|')


def sign_in_pos(line, pos, data):
    if 0 <= line < len(data) and 0 <= pos < len(data[line]):
        return data[line][pos]
    else:
        return " "


def next_pos(direction, line, pos, word, data, counter):
    sign = sign_in_pos(line, pos, data)
    print(direction, line, pos, word, "<", sign, ">", counter)

    if 'A' <= sign <= 'Z':
        word = word + sign

    if direction == 'v':
        next_line = line
        next_p = pos

        if sign == '+':
            if sign_in_pos(line, pos - 1, data) == ' ':
                direction = '>'
                next_p = pos + 1
            else:
                direction = '<'
                next_p = pos - 1
        else:
            next_line = line + 1

    elif direction == '^':
        next_line = line
        next_p = pos

        if sign == '+':
            if sign_in_pos(line, pos - 1, data) == ' ':
                direction = '>'
                next_p = pos + 1
            else:
                direction = '<'
                next_p = pos - 1
        else:
            next_line = line - 1

    elif direction == '>':
        next_line = line
        next_p = pos

        if sign == '+':
            if sign_in_pos(line + 1, pos, data) == ' ':
                direction = '^'
                next_line = line - 1
            else:
                direction = 'v'
                next_line = line + 1
        else:
            next_p = pos + 1

    elif direction == '<':
        next_line = line
        next_p = pos

        if sign == '+':
            if sign_in_pos(line + 1, pos, data) == ' ':
                direction = '^'
                next_line = line - 1
            else:
                direction = 'v'
                next_line = line + 1
        else:
            next_p = pos - 1

    return direction, next_line, next_p, word, sign, counter + 1


def task1(file_path):
    data = read_file(file_path)

    counter = -1

    # v ^ < >
    direction = "v"
    line, pos = start_position(data)
    word = ""

    sign = sign_in_pos(line, pos, data)

    while sign != ' ':
        direction, line, pos, word, sign, counter = next_pos(direction, line, pos, word, data, counter)

    return word, counter


