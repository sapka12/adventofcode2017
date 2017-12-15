import math

factor_a = 16807
factor_b = 48271


def one_round(seed, factor, divider=1):
    r = (seed * factor) % 2147483647
    if r % divider == 0:
        return r
    else:
        return one_round(r, factor, divider)


def to_binary(num):
    return "{0:b}".format(num)


def last16bits(num):
    return to_binary(num)[-16:]


_16bit = math.pow(2, 16)


def last_16_bits_match(num1, num2):
    res = num1 ^ num2
    return res % _16bit == 0


def go(seed_a, seed_b, rounds, divider_a, divider_b):
    counter = 0
    for a_round in range(rounds):

        seed_a = one_round(seed_a, factor_a, divider_a)
        seed_b = one_round(seed_b, factor_b, divider_b)

        if last_16_bits_match(seed_a, seed_b):
            counter = counter + 1
    return counter


def task1(seed_a, seed_b, rounds):
    return go(seed_a, seed_b, rounds, 1, 1)


def task2(seed_a, seed_b, rounds):
    return go(seed_a, seed_b, rounds, 4, 8)
