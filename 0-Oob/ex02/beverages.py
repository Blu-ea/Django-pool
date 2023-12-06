class HotBeverage:
	def __init__(self) -> None:
		self.price = 0.30
		self.name = "hot beverage"

	def description(self) -> str:
		return 'Just some hot water in a cup.'
	
	def __str__(self) -> str:
		return("name: {}\nprice: {:.2f}\ndescription: {}".format(self.name, self.price, self.description()))



class Coffee(HotBeverage):
	def __init__(self) -> None:
		self.price = 0.40
		self.name = "coffee"

	def description(self) -> str:
		return 'A coffee, to stay awake.'



class Tea(HotBeverage):
	def __init__(self) -> None:
		super().__init__()
		self.name = "tea"



class Chocolate(HotBeverage):
	def __init__(self) -> None:
		self.price = 0.50
		self.name = "chocolate"

	def description(self) -> str:
		return 'Chocolate, sweet chocolate...'



class Cappuccino(HotBeverage):
	def __init__(self) -> None:
		self.price = 0.45
		self.name = "cappuccino"

	def description(self) -> str:
		return 'un po\' di Italia nella sua tazza!'




if __name__ == "__main__":
	print("=======")
	hotbeverage = HotBeverage()
	print (hotbeverage)

	print("=======")
	coffee = Coffee()
	print (coffee)

	print("=======")
	tea = Tea()
	print (tea)

	print("=======")
	chocolate = Chocolate()
	print (chocolate)

	print("=======")
	cappuccino = Cappuccino()
	print (cappuccino)