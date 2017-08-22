""" Pig Lating Conversion
"""


def convert_to_pig_latin(word):
	""" Returns the converted string based on the
		rules defined for Pig Latin.
	"""

	vowels = ['a', 'e', 'i', 'o', 'u']

	char_list = list(word)


	""" Vowel Rule.
	"""
	if char_list[0] in vowels:
		resultant_word = word + 'way'




	return resultant_word



if __name__ == '__main__':

	word = input('Please enter the word for conversion ')
	print('Post conversion ', convert_to_pig_latin(word))