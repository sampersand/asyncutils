class _no_sentinel(): pass
_no_sentinel = _no_sentinel()
async def aiter(iterable_or_function, sentinel = _no_sentinel):
	if sentinel is _no_sentinel:
		for x in iter(iterable_or_function):
			yield x
	else:
		while True:
			future = iterable_or_function()
			if future is sentinel:
				break
			yield future

