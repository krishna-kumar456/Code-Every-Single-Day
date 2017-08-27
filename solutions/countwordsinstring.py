from collections import Counter

if __name__ == '__main__':

	word = list(input('Please enter a word'))
	c = Counter()

	for char in word:
		c[char] += 1


	print('Count of characters in ', word)
	for k,v in c.items():
		print(k, v)
