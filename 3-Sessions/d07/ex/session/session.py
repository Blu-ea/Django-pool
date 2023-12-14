from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest
from d07 import settings
import time
import random

class AnonymousSessions(MiddlewareMixin):
	def process_view(self, request: HttpRequest, view_func, *view_args, **view_kwargs):
		if request.user.is_authenticated:
			return
		
		init_time = request.session.setdefault("_session_anonmymous_timestamp_", time.time())
		session_is_expired = time.time() - init_time > 42

		if session_is_expired:
			request.session.flush()

		request.session.setdefault('anonymous_name', random.choice(
			settings.ANONYMOUS_NAMES))

		request.user.username = request.session.get('anonymous_name')
