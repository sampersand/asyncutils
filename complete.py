from asyncio import get_event_loop, new_event_loop, iscoroutine, iscoroutinefunction
def complete(coro, use_new_loop = False, loop = None):
	if use_new_loop:
		loop = new_event_loop()
	if loop == None:
		try:
			loop = get_event_loop()
		except RuntimeError:
			loop = new_event_loop()
	if iscoroutinefunction(coro):
		coro = coro()
	assert iscoroutine(coro), type(coro)

	return loop.run_until_complete(coro)