def start_with_(pico_sec, input_map):

    def get_from_dict(i):
        if i in input_map.keys():
            return input_map[i]
        else:
            return 0

    def actual_position(_step, _max_position):
        down = [i for i in range(_max_position - 1)]
        up = [_max_position - i for i in range(_max_position - 1)]
        circle = down + up
        return circle[_step % len(circle)]

    max_key = max(input_map.keys())
    _dict = dict({i: get_from_dict(i) for i in range(max_key + 1)})

    _sum = 0
    catched = False
    for step, max_position in _dict.items():
        if max_position > 0:
            actual_pos = actual_position(step + pico_sec, max_position)
            if actual_pos == 0:
                catched = True
                _sum = _sum + step * max_position

    return _sum, catched


def task1(input_map):
    return start_with_(0, input_map)[0]


def task2(input_map):
    picos = 0
    while start_with_(picos, input_map)[1]:
        picos = picos + 1

    return picos
