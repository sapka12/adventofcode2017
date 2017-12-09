garbage_start = "<"
garbage_end = ">"

group_start = "{"
group_end = "}"

ignore = "!"


def task1(text):
    result = ""

    in_garbage = False
    need_ignore = False
    group_level = 0

    counter = 0

    for i in range(len(text)):
        actual_char = text[i]

        if in_garbage and actual_char != garbage_end and not need_ignore and actual_char != ignore:
            result = result + actual_char

        if need_ignore:
            need_ignore = False
        elif actual_char == ignore:
            need_ignore = True
        elif in_garbage and actual_char == garbage_end:
            in_garbage = False
        elif not in_garbage and actual_char == group_end:
            counter = counter + group_level
            group_level = group_level - 1
        elif not in_garbage and actual_char == group_start:
            group_level = group_level + 1
        elif not in_garbage and actual_char == garbage_start:
            in_garbage = True

    return (len(result), counter)
