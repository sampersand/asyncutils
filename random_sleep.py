from asyncio import sleep
from random import random

async def random_sleep(reductor = 0.1):
	await sleep(random() * reductor)
	return random()

