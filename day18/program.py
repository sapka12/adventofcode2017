from collections import deque


def val_of(data, _dict):
    if 'a' <= data <= 'z':
        if data in _dict.keys():
            return _dict[data]
        else:
            return 0
    else:
        return int(data)


def task1(sounds):
    commands = sounds.split("\n")

    command_id = 0

    diction = {}

    played = deque([])

    def get_command(_id):
        return commands[_id].split(" ")

    while True:
        command_desc = get_command(command_id)

        command = command_desc[0]

        if command == "set":
            x = command_desc[1]
            y = val_of(command_desc[2], diction)
            diction[x] = y
            command_id = command_id + 1

        if command == "add":
            x = command_desc[1]
            y = val_of(command_desc[2], diction)
            diction[x] = diction[x] + y
            command_id = command_id + 1

        if command == "mul":
            x = command_desc[1]
            y = val_of(command_desc[2], diction)

            diction[x] = val_of(x, diction) * y
            command_id = command_id + 1

        if command == "mod":
            x = command_desc[1]
            y = val_of(command_desc[2], diction)
            diction[x] = diction[x] % y
            command_id = command_id + 1

        if command == "jgz":
            x = val_of(command_desc[1], diction)
            y = val_of(command_desc[2], diction)

            if x > 0:
                command_id = command_id + y
            else:
                command_id = command_id + 1

        if command == "rcv":
            x = command_desc[1]
            val_of_x = val_of(x, diction)
            if val_of_x != 0:
                return played.pop()
            command_id = command_id + 1

        if command == "snd":
            x = command_desc[1]
            played.append(diction[x])
            command_id = command_id + 1


def task2(instructions):
    commands = instructions.split("\n")

    def get_command(_id):
        return commands[_id].split(" ")

    p0_idx = 0
    p1_idx = 0

    p1_sends_value = 0

    p0_blocked = False
    p1_blocked = False

    p0_dict = {'p': 0}
    p1_dict = {'p': 1}

    p0_buffer = deque([])
    p1_buffer = deque([])

    def do_a_command(program, command_id, diction, own_buffer, other_buffer, own_blocked, other_blocked,
                     p1_sends_value):
        command_desc = get_command(command_id)

        command = command_desc[0]

        if command == "set":
            x = command_desc[1]
            y = val_of(command_desc[2], diction)
            diction[x] = y
            command_id = command_id + 1

        if command == "add":
            x = command_desc[1]
            y = val_of(command_desc[2], diction)
            diction[x] = diction[x] + y
            command_id = command_id + 1

        if command == "mul":
            x = command_desc[1]
            y = val_of(command_desc[2], diction)

            diction[x] = val_of(x, diction) * y
            command_id = command_id + 1

        if command == "mod":
            x = command_desc[1]
            y = val_of(command_desc[2], diction)
            diction[x] = diction[x] % y
            command_id = command_id + 1

        if command == "jgz":
            x = val_of(command_desc[1], diction)
            y = val_of(command_desc[2], diction)

            if x > 0:
                command_id = command_id + y
            else:
                command_id = command_id + 1

        if command == "snd":
            x = command_desc[1]
            other_buffer.append(diction[x])
            command_id = command_id + 1
            other_blocked = False
            if program == 1:
                p1_sends_value = p1_sends_value + 1

        if command == "rcv":
            x = command_desc[1]
            if own_buffer:
                command_id = command_id + 1
                diction[x] = own_buffer.popleft()
            else:
                own_blocked = True

        return command_id, diction, own_buffer, other_buffer, own_blocked, other_blocked, p1_sends_value

    while True:
        if p0_blocked and p1_blocked:
            return p1_sends_value
        elif not p0_blocked:
            p0_idx, p0_dict, p0_buffer, p1_buffer, p0_blocked, p1_blocked, p1_sends_value = \
                do_a_command(0, p0_idx, p0_dict, p0_buffer, p1_buffer, p0_blocked, p1_blocked, p1_sends_value)
        else:
            p1_idx, p1_dict, p1_buffer, p0_buffer, p1_blocked, p0_blocked, p1_sends_value = \
                do_a_command(1, p1_idx, p1_dict, p1_buffer, p0_buffer, p1_blocked, p0_blocked, p1_sends_value)
