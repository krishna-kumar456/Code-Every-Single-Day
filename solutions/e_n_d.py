""" Program to find e to the power nth.
"""
import math

def get_e_to_nth(n):
	if n <= 1000:
		return round(math.e,n) 

user_input = int(input("Please enter n"))
result = get_e_to_nth(user_input)
print("e to the power n:", result)
