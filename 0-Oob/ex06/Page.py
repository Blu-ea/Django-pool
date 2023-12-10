from element import *
from elem import *

class Page:
	def __init__(self, param: Elem) -> None:
		self.__page = param


	""" A function that check is the page a either a class Html has Head or Body inside"""
	def is_valid(self) -> bool:
		if (self.__page.tag != "html"):
			return False
		return False
	

if __name__ == '__main__':


	page = Page(
		Html()
	)


	if (page.is_valid()):
		print (f"\033[96mPass !\033[00m")
	else:
		print (f"\033[91mFail !\033[00m")