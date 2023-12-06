import sys


def periodic_table():
	file = open("periodic_table.txt")
	period_t: list[dict[str, int, str, str, float]] = []
	for line in file.readlines():
		split = line.split(' = ')
		name = split[0]
		other = split[1].split(', ')
		position = other[0].split(':')[1]
		number = other[1].split(':')[1]
		small = other[2].split(':')[1]
		molar = other[3].split(':')[1]
		period_t.append({
				"name": name,
				"position": position,
				"number": number,
				"small": small,
				"molar": molar,
			})
	file.close()
	print(period_t)
	do_html(period_t)

def do_html(period_t: list[dict[str, int, str, str, float]]):
	file = open("periodic_table.html", 'w')
	file.flush()
	file.write("<>")
	file.close()


if __name__ == "__main__":
	periodic_table()
