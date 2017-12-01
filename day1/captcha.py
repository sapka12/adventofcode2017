def content(filepath):
	with open(filepath, 'r') as content_file:
		return content_file.read()


def eq(n0, n1):
	return int(n0) == int(n1)


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
	sums = [ nth_sum_of_pair(chars, idx, strategy) for idx, digit in enumerate(chars)]
	return sum(sums)


def run(inputs, strategy):
	for input_captcha in inputs:
		print(input_captcha + " : " + str(captcha(input_captcha, strategy)))


def main():	
	
	def find_n_plus1_next(size, n):
		return (int(n) + 1) % size


	def find_n_plus1_halfway(size, n):
		return (n + int(size / 2)) % size
	
	
	run([
		"1122", 
		"1111", 
		"1234", 
		"91212129",
		content('input.txt')
	], find_n_plus1_next)
	
	run([
		"1212", 
		"1221", 
		"123425", 
		"123123",
		"12131415",
		content('input.txt')
	], find_n_plus1_halfway)


main()


