""" Coin Flip Simulation.

1. Accept number of turns
2. For each turn, get random of Heads or Tails.
3. Store result in list.
4. Print Count of both outcomes.
"""

from random import randint

user_input = int(input('Please enter number of coin flips'))

HEADS = 0
TAILS = 1

result = [0,0]

for i in range(user_input):
	outcome = randint(0,1)

	if outcome:
		result[1] += 1
	else:
		result[0] += 1

print('Number of heads ', result[0])
print('Number of tails ', result[1])


