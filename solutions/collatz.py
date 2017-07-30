"""
Collatz Conjecture

1. Take any Positive integer.
2. If even, divide by 2
3. If odd, multiply by 3 and add by 1
4. Count each turn while reaching towards 1
"""


user_input = int(input('Please enter input '))
number_of_turns = 0

while user_input != 1 :
	if user_input % 2 == 0:
		user_input = user_input // 2
	elif user_input % 2 == 1:
		user_input = 3*user_input + 1
	number_of_turns += 1

print('Number of turns to reach 1', number_of_turns)
