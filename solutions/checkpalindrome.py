

if __name__ == '__main__':

	word = input('Please enter the word')
	rev_word = word[::-1]
	print(rev_word)

	if word == rev_word:
		print('Palindrome')
	else:
		print('NOT')
