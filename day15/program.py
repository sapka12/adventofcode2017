factor_a = 16807
factor_b = 48271


def one_round(seed, factor):
    return (seed * factor) % 2147483647


def to_binary(num):
    return "{0:b}".format(num)


def last16bits(num):
    return to_binary(num)[-16:]


def last_16_bits_match(num1, num2):
    return last16bits(num1) == last16bits(num2)


def task1(seed_a, seed_b, rounds):
    counter = 0
    for a_round in range(rounds):

        seed_a = one_round(seed_a, factor_a)
        seed_b = one_round(seed_b, factor_b)

        if last_16_bits_match(seed_a, seed_b):
            counter = counter + 1
    return counter
