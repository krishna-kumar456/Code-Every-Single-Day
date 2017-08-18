""" Invertex Index Implementation.
"""
from collections import defaultdict

def create_index (data):
	""" Creates the Invertex index using the
		default dictionary data structure
		within the python collections.
	"""

	index = defaultdict(list)
	for i, tokens in enumerate(data):
		print('i', i, 'tokens', tokens)
		index[tokens].append(i)
	return index



def read_file(file):
	""" Helper function to read text from a
		file and then use the contents of 
		the file to create an inverted index.
	"""
	try:
		text_file = open(file, 'r')
	
	except e:
		print('Something went wrong with opening the file', e)

	return text_file.split()


def search_text(file, query):
	""" Searches the user inputed text 
		within the Invertex Index.
	"""

	index = create_index(read_file(file))   ##Modifiy this to accept more than 1 file.

	return index[query]



if __name__ == '__main__':

	number_of_files = int('Please enter the number of files: ')
	files = []

	for number in range(number_of_files):
		file_name = input('Please enter the file name for file ' +number+ ': ')
		files.append(file_name)


	query = input('Please enter the search query: ')
	print('The search query is present in the following files: ', search_text(files, query))

	