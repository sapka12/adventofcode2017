

def task1(input_map):

    def get_from_dict(i):
        if i in input_map.keys():
            return 0, input_map[i], True
        else:
            return 0, 0, True

    max_key = max(input_map.keys())
    dict = {i: get_from_dict(i) for i in range(max_key + 1)}

    print input_map, max_key, dict
    return 24


def task2(input_file):
    return 0