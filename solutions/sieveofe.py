"""
Sieve of Eratosthenes.

1. Generate numbers to the limit.
2. Start with 2, eliminate multiples of 2.
3. Proceed to next number (3), eliminate multiples of 3
4. Keep looping until p2 > n.
"""


userInput = int(input('Please enter the upper limit'))

numbersGeneratedFromLimit = [True for x in range(userInput)]
finalPrimes = []

for i in range(2,userInput):
	if numbersGeneratedFromLimit[i] == True:
		j = i**2
		for j in range(1, userInput):
			


