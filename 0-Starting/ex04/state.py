import sys


def state():
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
	for city_key, city_value in capital_cities.items():
		if city_value == arg:
			for state_key, state_value in states.items():
				if city_key == state_value:
					print(state_key)
					exit()
	print("Unknow capital city")


if __name__ == '__main__':
	state()
