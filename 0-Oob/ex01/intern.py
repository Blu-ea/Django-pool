class Intern:
	def __init__(self, name: str = "My name? I'm nobody, an intern, I have no name.") -> None:
		self._name = name

	def __str__(self) -> str:
		return self._name

	class Coffee:
		def __str__(self) -> str:
			return "This is the worst coffee you ever tasted."
		def __init__(self) -> None:
			pass

	def work(self):
		raise Exception("I'm just an intern, I can't do that...")
	
	def make_coffee(self) -> Coffee:
		return self.Coffee()



if (__name__ == '__main__'):
	mark = Intern("Mark")
	no_name = Intern()

	print(mark)
	print(no_name)
	print ('=====')

	print(mark.make_coffee())
	print ('=====')

	try:
		no_name.work()
	except Exception as err:
		print(err)