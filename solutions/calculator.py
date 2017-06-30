""" A simple calculator.
"""
def calculator_processing(a,b, choice):
	if choice == 'add':
		return a + b

	if choice == 'subtract':
		return a - b

	if choice == 'multiply':
		return a * b

	if choice == 'divide':
		return a / b


user_input_choice = input('list basic operations')
user_input_a = int(input('a'))
user_input_b = int(input('b'))
result = calculator_processing(user_input_a, user_input_b, user_input_choice)
print(result)