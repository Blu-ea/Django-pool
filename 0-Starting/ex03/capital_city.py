import sys


def capital_city():
	states = {
		"Oregon": "OR",
		"Alabama": "AL",
		"New Jersey": "NJ",
		"Colorado": "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	if (len(sys.argv) != 2):
		exit()
	arg = sys.argv[1]
	state_id = states.get(arg)
	if (state_id):
		print(capital_cities[state_id])
	else:
		print("Unknow state")


if __name__ == '__main__':
	capital_city()
