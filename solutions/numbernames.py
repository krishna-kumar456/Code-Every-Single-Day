""" Number names
"""

from num2words import num2words
from random import randint

numbers = []

def generate_input():
	for i in range(99):
		numbers.append(i)

generate_input()

for item in numbers:
	print(num2words(item))