import sys


def all_in():
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

	lst_word = sys.argv[1].title().split(',')
	for word in lst_word:
		word = " ".join(word.split())
		if (word == ''):
			continue
		if (check_state(states, capital_cities, word)):
			continue
		if (check_capital(states, capital_cities, word)):
			continue
		print("%s is neither a capital nor a state" % (word))


def check_state(states: {str: str}, capital_cities: {str: str}, word: str):
	state_id = states.get(word)
	if (state_id):
		print("%s is the capital of %s" % (capital_cities[state_id], word))
		return True
	return False


def check_capital(states: {str: str}, capital_cities: {str: str}, word: str):
	for city_key, city_value in capital_cities.items():
		if city_value == word:
			for state_key, state_value in states.items():
				if city_key == state_value:
					print("%s is the capital of %s" % (word, state_key))
					return True
	return False


if __name__ == '__main__':
	all_in()
