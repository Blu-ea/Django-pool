def print_file():
	file = open('numbers.txt', 'r')
	line = file.readline()
	if line[-1:] == '\n':
		line = line[:-1]
	lines = line.split(sep=',')
	for nb in lines:
		print(nb)


if __name__ == '__main__':
	print_file()
