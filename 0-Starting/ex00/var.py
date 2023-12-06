def print_my_var(var):
	print("%s has a type %s" % (var, type(var)))


def my_var():
	int_42 = 42
	str_42 = "42"
	quarante_deux = "quarante-deux"
	float_42 = 42.0
	bool_42 = True
	list_42 = [42]
	dict_42 = {42: 42}
	tuple_42 = (42, )
	set_42 = set()
	print_my_var(int_42)
	print_my_var(str_42)
	print_my_var(quarante_deux)
	print_my_var(float_42)
	print_my_var(bool_42)
	print_my_var(list_42)
	print_my_var(dict_42)
	print_my_var(tuple_42)
	print_my_var(set_42)


if __name__ == '__main__':
	my_var()
