def content(filepath):
	with open(filepath, 'r') as content_file:
		return open(filepath, 'r').read()


def nth_pair(char_list, n0, find_n_plus1_idx):
	size = len(char_list)
	n0 = int(n0) % size
	n1 = find_n_plus1_idx(size, n0)
	return (char_list[n0], char_list[n1])


def nth_sum_of_pair(chars, n, strategy):
	(a, b) = nth_pair(chars, n, strategy)
	if (a == b):
		return int(a)
	else:
		return 0


def captcha(input_str, strategy):
	chars = list(input_str)
	sums = [ nth_sum_of_pair(chars, idx, strategy) for idx in range(len(chars))]
	return sum(sums)


def find_n_plus1_next(size, n):
	return (int(n) + 1) % size


def find_n_plus1_halfway(size, n):
	return (n + int(size / 2)) % size


def captcha_part_one(input_str):
	return captcha(input_str, find_n_plus1_next)


def captcha_part_two(input_str):
	return captcha(input_str, find_n_plus1_halfway)


print(captcha_part_one(content('input.txt')))
print(captcha_part_two(content('input.txt')))
