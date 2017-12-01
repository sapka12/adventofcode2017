def content(filepath):
	with open(filepath, 'r') as content_file:
		return content_file.read()


def eq(n0, n1):
	return int(n0) == int(n1)


def nthPair(char_list, n0):
	size = len(char_list)
	n0 = int(n0) % size
	n1 = (n0 + int(size / 2)) % size
	return (char_list[n0], char_list[n1])

def sumOfPair(chars, n):
	(a, b) = nthPair(chars, n)
	if (a == b):
		return int(a)
	else:
		return 0


def captcha(input_str):
	chars = list(input_str)
	sums = [ sumOfPair(chars, idx) for idx, digit in enumerate(chars)]
	return sum(sums)


def main():	
	inputs = [
		"1212", 
		"1221", 
		"123425", 
		"123123",
		"12131415",
		content('input.txt')
	]

	for input_captcha in inputs:
		print(input_captcha + " : " + str(captcha(input_captcha)))


main()

