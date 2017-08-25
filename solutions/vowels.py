from collections import Counter






if __name__ == '__main__':

	vowels = ['a', 'e', 'i', 'o', 'u']
	vowel_count = Counter()

	word = list(input('Please enter the word'))

	for char in word:
		if char in vowels:
			vowel_count[char] += 1


	print(vowel_count)

