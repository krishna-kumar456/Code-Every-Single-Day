""" Detect Happy Numbers.
"""




def split_square_sum(num):

	split_num = []

	if int(num)//10 != 0:
		split_num.append(int(num)//10)

	split_num.append(int(num)%10)

	sum_split = 0
	for item in split_num:
		sum_split += item**2

	return sum_split


def detect_happy(num):

	total = split_square_sum(num)
	unhappy_numbers = [4, 16, 37, 58, 89, 145, 42, 20]

	if total in unhappy_numbers:
		return False

	while total >=1:
		if total == 1:
			return True
		else:
			detect_happy(total)


user_input = input('Please enter a number for evaluation')
is_happy = detect_happy(user_input)
if is_happy:
	print('Found Happy Number')
else:
	print('Not a Happy Number')

