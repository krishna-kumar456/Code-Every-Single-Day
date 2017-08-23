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

	""" Consonant Rule.
	"""

	if char_list[0] not in vowels:
		resultant_word = ''.join(char_list[1:]) + str(char_list[0]) + 'a'

	""" Consonant Cluster Rule.
	"""

	if char_list[0] == 'c' and char_list[1] == 'h':
		resultant_word = ''.join(char_list[2:]) + char_list[0] + char_list[1] + 'ay'

	elif char_list[0] == 's' and char_list[1] == 'h' or char_list[1] =='t' or char_list[1] == 'm':
		resultant_word = ''.join(char_list[2:]) + char_list[0] + char_list[1] + 'ay'

	elif char_list[0] == 't' and char_list[1] == 'h':
		resultant_word = ''.join(char_list[2:]) + char_list[0] + char_list[1] + 'ay'





	return resultant_word



if __name__ == '__main__':

	word = input('Please enter the word for conversion ')
	print('Post conversion ', convert_to_pig_latin(word))