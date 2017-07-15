""" Find the factorial
"""

def get_factorial(n):

	if n == 1:
		return 1
	else:
		return n * get_factorial(n-1)


user_input = int(input('Enter number whose factorial needs to be found '))
print(get_factorial(user_input))
