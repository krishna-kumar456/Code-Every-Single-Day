""" Complex Number Algebra.
"""


def addition(number_1, number_2):
	result = []

	result.append(number_1[0]+number_2[0])
	result.append(number_1[1]+number_2[1])
	return result


def subtraction(number_1, number_2):
	result = []

	result.append(number_1[0]-number_2[0])
	result.append(number_1[1]-number_2[1])
	return result

def multiplication(number_1, number_2):
	result = []

	first_half = number_1[0]*number_2[0] 
	second_half =  number_1[0]*number_2[1]
	third_half = number_1[1]*number_2[0]
	fourth_half = (number_1[1]* number_2[1])*-1

	result.append(first_half+fourth_half)
	result.append(second_half+third_half)
	return result


def division(number_1, number_2):
	result = []

	first_half = number_1[0]*number_2[0] 
	second_half =  number_1[0]*(number_2[1])*-1
	third_half = number_1[1]*number_2[0]
	fourth_half = (number_1[1]* (number_2[1])*-1)*-1
	fifth_half = number_2[0]**2 + number_2[1]**2

	result.append((first_half+fourth_half)/fifth_half)
	result.append((second_half+third_half)/fifth_half)
	
	return result



user_input_real_1 = int(input('Enter the real component for 1'))
user_input_complex_1 = int(input('Enter the complex component 1'))


user_input_real_2 = int(input('Enter the real component for 2'))
user_input_complex_2 = int(input('Enter the complex component 2'))



user_input_operation = input('Select Opertion ')

number_1 = [user_input_real_1, user_input_complex_1]
number_2 = [user_input_real_2, user_input_complex_2]

final_result = []

if user_input_operation == 'addition':
	final_result = addition(number_1, number_2)

elif user_input_operation == 'subtraction':
	final_result = subtraction(number_1, number_2)

elif user_input_operation == 'multiplication':
	final_result = multiplication(number_1, number_2)

elif user_input_operation == 'subtraction':
	final_result = division(number_1, number_2)

if len(final_result) < 1:
	print('Invalid Operation selected')

else:

	print(str(final_result[0]) + '+' + str(final_result[1]) + 'i')

