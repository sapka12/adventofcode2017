def read_input():
    with open("input.txt") as f:
        return [x.strip() for x in f.readlines()]


def task1():
    data = read_input()
    return sum([1 for pw in data if is_valid(pw)])


def is_valid_wo_anagrams(pw):
    words = pw.split(" ")

    def count_word(word):
        return len([w for w in words if are_anagrams(w, word)])

    return all(count_word(word) == 1 for word in words)


def is_valid(pw):
    words = pw.split(" ")

    def count_word(word):
        return len([w for w in words if w == word])

    return all(count_word(word) == 1 for word in words)


def task2():
    data = read_input()
    return sum([1 for pw in data if is_valid_wo_anagrams(pw)])


def are_anagrams(str0, str1):
    return sorted(list(str0)) == sorted(list(str1))


print(task1())
print(task2())
