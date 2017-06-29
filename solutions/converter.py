""" Convert binary to decimal or reverse.
"""
def decimal_to_binary(n):
	
	binary_form = []
	
	while n > 0:
		binary_form.append(n%2)
		n = n//2
		

	return reversed(binary_form)


def binary_to_decimal(n):
	
	r_arr = reversed(n)
	f_sum = 0
	for index, item in enumerate(r_arr):
		print(index, item)
		if item == '1':
			f_sum += 2**index
			
	return f_sum

user_input = int(input('Enter Decimal number'))
user_input_bin = list(input('Enter binary number'))
result = decimal_to_binary(user_input)
for item in result:
	print(item, end=' ')

result_bin = binary_to_decimal(user_input_bin)
print(result_bin)

