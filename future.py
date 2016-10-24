# from inspect import *
from .finish import finish

def future(coro, finish_instance = None, traceback = None):
	# s = stack()
	# if not finish_instance:
	# 	for frame in s:
	# 		for name, obj in frame[0].f_locals.items():
	# 			if isinstance(obj, finish):
	# 				if __debug__:
	# 					assert finish_instance is None or finish_instance is obj
	# 				finish_instance = obj
	# 				if not __debug__:
	# 					break
	# 		if finish_instance:
	# 			break
	# if not finish_instance:
	# 	for frame in s:
	# 		print('{:<20}'.format(frame[3]), [(name, isinstance(obj, finish))for name, obj in frame[0].f_locals.items()])
	if finish_instance == None:
		finish_instance = finish._finishes[-1]
	assert finish_instance != None

	finish_instance.future(coro)
