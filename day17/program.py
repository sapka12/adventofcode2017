from collections import deque


def gen_deque(num_of_steps, rounds):
    q = deque([0])
    for actual_round in range(1, rounds + 1):
        q.rotate(-num_of_steps)
        q.append(actual_round)
    return q


def task1(num_of_steps, rounds):
    return gen_deque(num_of_steps, rounds)[0]


def task2(num_of_steps, rounds):
    q = list(gen_deque(num_of_steps, rounds))
    return q[(q.index(0) + 1) % len(q)]
