class Task:
    # b inc 580 if bkd > -1
    #       Task(      'b',   580,    'bkd',     '>',  -1)
    def __init__(self, label, inc_val, variable, sign, value):
        self.label = label
        self.inc_val = inc_val
        self.variable = variable
        self.sign = sign
        self.value = value

    def from_(line):
        arr = line.split(" ")
        inc = int(arr[1].replace("inc", "1").replace("dec", "-1")) * int(arr[2])

        s = arr[5]
        op = (lambda x, y: x == y)
        if s == "!=":
            op = (lambda x, y: x != y)
        elif s == "<":
            op = (lambda x, y: x < y)
        elif s == "<=":
            op = (lambda x, y: x <= y)
        elif s == ">":
            op = (lambda x, y: x > y)
        elif s == ">=":
            op = (lambda x, y: x >= y)

        return Task(
            label=arr[0],
            inc_val=inc,
            variable=arr[4],
            sign=op,
            value=int(arr[6])
        )

    def change_val(self, values_map):
        if self.sign(values_map[self.variable], self.value):
            values_map[self.label] = values_map[self.label] + self.inc_val


def tasks(input_file):
    with open(input_file) as f:
        all_tasks = [Task.from_(line) for line in [x.strip() for x in f.readlines()]]
        values = {label: 0 for label in set([task.label for task in all_tasks])}
        return all_tasks, values


def task1(input_file):
    all_tasks, values = tasks(input_file)

    for task in all_tasks:
        task.change_val(values)
    return max(values.values())


def task2(input_file):
    all_tasks, values = tasks(input_file)

    actual_max = 0
    for task in all_tasks:
        task.change_val(values)
        actual_max = max(actual_max, max(values.values()))
    return actual_max
