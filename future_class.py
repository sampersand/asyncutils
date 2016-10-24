from . import ensure_future
class Future():
	def __init__(self, finish_instance, coro):
		self.finish_instance = finish_instance
		self.future = ensure_future(coro)
	def __await__(self):
		if self in self.finish_instance:
			self.finish_instance.remove(self)
		return self.future.__await__()
	def result(self):
		return self.future.result()