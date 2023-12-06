from beverages import Coffee, Tea, Cappuccino, Chocolate , HotBeverage
import random

class CoffeeMachine:
	def __init__(self) -> None:
		self._usage = 10
		
	class EmptyCup(HotBeverage):
		def __init__(self) -> None:
			self.name = "empty cup"
			self.price = 0.90

		def description(self) -> str:
			return "\033[95mAn empty cup?! Gimme my money back!\033[00m"
		
	class BrokenMachinException(Exception):
		def __init__(self) -> None:
			super().__init__('\033[91mthis coffee machine has to be repaired.')

	def repaire(self):
			print("\033[92mThe machine is being repaired\033[00m")
			self._usage = 10

	def serve(self, Parameteres: HotBeverage) -> HotBeverage:
		if (self._usage == 0):
			raise CoffeeMachine.BrokenMachinException()
		self._usage -= 1
		if (random.randint(0,1)):
			return Parameteres()
		else:
			return CoffeeMachine.EmptyCup()
		

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(23):
		try :
			beverage_id =random.randint(0,3)
			match beverage_id:
				case 0:
					beverage_wanted = Coffee
				case 1:
					beverage_wanted = Tea
				case 2:
					beverage_wanted = Cappuccino
				case 3:
					beverage_wanted = Chocolate
			print (f"\n\033[94m---- Service {i+1} ---- {beverage_wanted().name} \033[00m")
			cup_served = machine.serve(beverage_wanted)
			print (cup_served)

		except CoffeeMachine.BrokenMachinException as err:
			print(err)
			machine.repaire()


