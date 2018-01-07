from collections import deque

def snd(dict):
    return lambda x: dict[x]


def set(dict):
    def f(x, y):
        dict[x] = dict[y]
    return f


def add(dict):
    def f(x, y):
        dict[x] = dict[x] + dict[y]
    return f


def mul(dict):
    def f(x, y):
        dict[x] = dict[x] * dict[y]
    return f




def task1(sounds):
    commands = sounds.split("\n")

    command_id = 0
    command = commands[command_id].split(" ")[0]

    diction = {}

    def val_of(data):
        if 'a' <= data <= 'z':
            return diction[data]
        else:
            return int(data)

    played = deque([])

    def get_command(id):
        return commands[id].split(" ")

    while command != "rcv":
        command_desc = get_command(command_id)
        print(command_desc)

        command = command_desc[0]

        if command == "set":
            x = command_desc[1]
            y = val_of(command_desc[2])
            diction[x] = y
            command_id = command_id + 1

        if command == "snd":
            x = command_desc[1]
            played.append(diction[x])
            print("played: ", diction[x])
            command_id = command_id + 1

        if command == "add":
            x = command_desc[1]
            y = val_of(command_desc[2])
            diction[x] = diction[x] + y
            command_id = command_id + 1

        if command == "mul":
            x = command_desc[1]
            y = val_of(command_desc[2])
            diction[x] = diction[x] * y
            command_id = command_id + 1

        if command == "mod":
            x = command_desc[1]
            y = val_of(command_desc[2])
            diction[x] = diction[x] % y
            command_id = command_id + 1

        if command == "rcv":
            x = command_desc[1]
            val_of_x = diction[x]
            if val_of_x != 0:
                return played.pop()
            command_id = command_id + 1

        if command == "jgz":
            x = command_desc[1]
            y = val_of(command_desc[2])
            val_of_x = diction[x]
            val_of_y = diction[y]
            if val_of_x > 0:
                command_id = command_id + val_of_y
            else:
                command_id = command_id + 1

    return commands

