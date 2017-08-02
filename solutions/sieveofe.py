"""
Sieve of Eratosthenes.

1. Generate numbers to the limit.
2. Start with 2, eliminate multiples of 2.
3. Proceed to next number (3), eliminate multiples of 3
4. Keep looping until p2 > n.
"""


userInput = int(input('Please enter the upper limit'))

def primes_sieve2(limit):
    a = [False] * 2 + [True] * (limit-2)                        # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


result = primes_sieve2(userInput)

for items in result:
	print(items)
			


