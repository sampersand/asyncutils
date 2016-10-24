# from inspect import *
from .finish import _finishes
from asyncio import iscoroutine
from .random_sleep import random_sleep
async def getval(non_coro_func, args, sleep):
	if sleep:
		await random_sleep(sleep)
	return non_coro_func(*args)
def future(func, *args_for_non_coro, sleep = False, finish_instance = None):
	if finish_instance == None:
		finish_instance = _finishes[-1]

	if not iscoroutine(func):
		func = getval(func, args_for_non_coro, sleep)
	else:
		assert not sleep, 'only can use random sleep on non-coroutine'
	return finish_instance.future(func)

def cont(func, *args_for_non_coro):
	return future(func, *args_for_non_coro)