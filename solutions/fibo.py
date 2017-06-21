def print_fibonacci(n):
	if n <= 1:
		return 1
	else:
		return print_fibonacci(n-1) + print_fibonacci(n-2)

user_input = int(input("Enter number whose fibonacci needs to be found"))
result = print_fibonacci(user_input)
print(result)
