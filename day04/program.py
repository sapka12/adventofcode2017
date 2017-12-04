def read_input():
    with open("input.txt") as f:
        return [x.strip() for x in f.readlines()]


def validate(pw, validator_fn):
    words = pw.split(" ")

    def count_word(word):
        return len([w for w in words if validator_fn(w, word)])

    return all(count_word(word) == 1 for word in words)


def are_anagrams(str0, str1):
    return sorted(list(str0)) == sorted(list(str1))


def task(password_match_fn):
    data = read_input()
    return sum([1 for pw in data if validate(pw, password_match_fn)])


def task1():
    return task(lambda x, y: x == y)


def task2():
    return task(are_anagrams)
