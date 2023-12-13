from django.utils.deprecation import MiddlewareMixin

class AnonymousSessions(MiddlewareMixin):
	sessionName = [
		"name 1",
		"name 2",
		"name 3",
		"name 4",
		"name 5",
		"name 6",
		"name 7",
		"name 8",
		"name 9",
		"name 10"
		]

	def __init__(self, get_response):
		self.get_response = get_response
		# One-time configuration and initialization.

	def __call__(self, request):
		# Code to be executed for each request before
		# the view (and later middleware) are called.

		response = self.get_response(request)

		# Code to be executed for each request/response after
		# the view is called.

		return response
