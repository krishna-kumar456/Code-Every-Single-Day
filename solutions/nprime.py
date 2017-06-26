""" Find next prime number 
"""

def is_prime(n):

	if n == 2:
		return True

	if not n & 1:
		return False

	for x in range(3, int(n**0.5), 2):
		if n%x == 0:
			return False

	return True




quit = False
start = 2
prev = []
while not quit:

	user_input = input('n for next prime, q for quit')
	
	if user_input == 'q':
		
		quit = True
		break

	if user_input == 'n':
		
		for i in range(start, 1000):
			if is_prime(i) and i not in prev:
				print(i)
				prev.append(i)
				break



