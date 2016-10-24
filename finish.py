from .complete import complete
from . import ensure_future
from .aiter import aiter
from .future_class import Future

_finishes = []
class Finish(set):
	def add_nowait(self, ele):
		super().add(ele)

	async def add(self, ele):
		return self.add_nowait(ele)

	async def __aiter__(self):
		return self

	async def __anext__(self):
		if not self:
			raise StopAsyncIteration
		return self.pop()

	async def clear(self):
		async for fut in self:
			await fut

	async def __aenter__(self):
		_finishes.append(self)
		return self

	async def __aexit__(self, exc_type, exc_val, exc_tb):
		await self.clear()
		assert not self
		assert _finishes[-1] is self
		_finishes.pop()
		if exc_val:
			raise exc_val

	def __enter__(self):
		_finishes.append(self)
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		complete(self.clear())
		del _finishes[_finishes.index(self)]
		if exc_val:
			raise exc_val

	def future(self, coro):
		fut = Future(self, coro)
		self.add_nowait(fut)
		return fut

	def __repr__(self):
		return str(self)

	def __str__(self):
		return '<Finish at 0x{:x} size={}>'.format(id(self), self.qsize())




