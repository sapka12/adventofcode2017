from collections import deque


def task1(sounds):
    commands = sounds.split("\n")

    command_id = 0

    diction = {}

    def val_of(data):
        if 'a' <= data <= 'z':
            if data in diction.keys():
                return diction[data]
            else:
                return 0
        else:
            return int(data)

    played = deque([])

    def get_command(_id):
        return commands[_id].split(" ")

    while True:
        command_desc = get_command(command_id)

        command = command_desc[0]

        if command == "set":
            x = command_desc[1]
            y = val_of(command_desc[2])
            diction[x] = y
            command_id = command_id + 1

        if command == "snd":
            x = command_desc[1]
            played.append(diction[x])
            command_id = command_id + 1

        if command == "add":
            x = command_desc[1]
            y = val_of(command_desc[2])
            diction[x] = diction[x] + y
            command_id = command_id + 1

        if command == "mul":
            x = command_desc[1]
            y = val_of(command_desc[2])

            diction[x] = val_of(x) * y
            command_id = command_id + 1

        if command == "mod":
            x = command_desc[1]
            y = val_of(command_desc[2])
            diction[x] = diction[x] % y
            command_id = command_id + 1

        if command == "rcv":
            x = command_desc[1]
            val_of_x = val_of(x)
            if val_of_x != 0:
                return played.pop()
            command_id = command_id + 1

        if command == "jgz":
            x = val_of(command_desc[1])
            y = val_of(command_desc[2])

            if x > 0:
                command_id = command_id + y
            else:
                command_id = command_id + 1
