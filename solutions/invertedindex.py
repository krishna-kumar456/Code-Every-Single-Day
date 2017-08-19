""" Invertex Index Implementation.
"""
from collections import defaultdict



def create_index(data):
	""" Creates the Invertex index using the
		default dictionary data structure
		within the python collections.
	"""	
	sIndex = defaultdict(list)
	for i, tokens in enumerate(data):
		for token in tokens:
			for t in token:
				sIndex[t].append(i)
	return sIndex		



def read_file(files):
	""" Helper function to read text from a
		file and then use the contents of 
		the file to create an inverted index.
	"""
	try:
		content = []
		for file in files:
			print(file)
			with open(file) as f:
				content.append(f.readlines())

		result = []
		for c in content:
			result.append([x.split() for x in c])
	
	except e:
		print('Something went wrong with opening the file', e)

	return result


def search_text(files, query):
	""" Searches the user inputed text 
		within the Invertex Index.
	"""
	index = create_index(read_file(files))
	return index[query]



if __name__ == '__main__':

	number_of_files = input('Please enter the number of files: ')
	
	files = []

	for number in range(int(number_of_files)):
		file_name = input('Please enter the file name for file: ')
		files.append(file_name)


	query = input('Please enter the search query: ')
	print('The search query is present in the following files: ', search_text(files, query))

	