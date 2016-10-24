from .complete import complete
from . import ensure_future, END_QUEUE
from .aiter import aiter
from asyncio import Queue
class finish(Queue):
	_finishes = []
	def __enter__(self):
		finish._finishes.append(self)
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		complete(self._empty())
		del finish._finishes[finish._finishes.index(self)]
		if exc_val:
			raise exc_val
	
	async def _empty(self):
		while not self.empty():
			f = await self.get()
			if f is END_QUEUE:
				return
			await f

	async def __aenter__(self):
		finish._finishes.append(self)
		return self

	async def __aexit__(self, exc_type, exc_val, exc_tb):
		await self._empty()
		del finish._finishes[finish._finishes.index(self)]
		if exc_val:
			raise exc_val

	def future(self, coro):
		self.put_nowait(ensure_future(coro))

	def __repr__(self):
		return str(self)
	def __str__(self):
		return '<finish at 0x{:x} size={}>'.format(id(self), self.qsize())