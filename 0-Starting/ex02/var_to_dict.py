def var_to_dict():
	d = [
		('Hendrix', '1942'),
		('Allman', '1946'),
		('King', '1925'),
		('Clapton', '1945'),
		('Johnson', '1911'),
		('Berry', '1926'),
		('Vaughan', '1954'),
		('Cooder', '1947'),
		('Page', '1944'),
		('Richards', '1943'),
		('Hammett', '1962'),
		('Cobain', '1967'),
		('Garcia', '1942'),
		('Beck', '1944'),
		('Santana', '1947'),
		('Ramone', '1948'),
		('White', '1975'),
		('Frusciante', '1970'),
		('Thompson', '1949'),
		('Burton', '1939')
	]
	my_dict: dict[str, str] = {}
	for element, index in d:
		if (my_dict.get(index)):
			my_dict[index] += " " + element
		else:
			my_dict[index] = element
	for date in my_dict.keys():
		print("%s : %s" % (date, my_dict[date]))


if __name__ == "__main__":
	var_to_dict()
