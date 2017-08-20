""" FizzBuzz

	1. Check if only divisible by 3
	2. Check if only divisible by 5
	3. Check if divisible by 3 and 5.
"""


if __name__ == '__main__':

	for number in range(1,101):

		if number % 3 == 0 and not number % 5 == 0:
			print('Fizz')

		elif not number % 3 == 0 and number % 5 == 0:
			print('Buzz')

		elif number % 3 == 0 and number % 5 == 0:
			print('FizzBuzz')

		else:
			print(number)