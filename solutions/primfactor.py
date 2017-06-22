""" Find Prime factors of a number. 
"""
def check_prime(n):
	n = abs(int(n))

	if n < 2:
		return False

	if n == 2:
		return True

	if not n & 1:
		return False

	for x in range(3, int(n**0.5), 2):
		if n % x == 0:
			return False

	return True

def get_prime_factors(n):

	result = []

	i = 2
	while i < n:
		if check_prime(i):
			if n % i == 0:
				result.append(i)
		i = i + 1

	return result

user_input = int(input('Enter number whose prime factors need to be found'))
display_result = get_prime_factors(user_input)
for item in display_result:
	print(item)