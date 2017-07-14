""" Income Tax calculator.
"""


def tax_on_income(amount, tax_rate):
	net_income = amount - ((tax_rate/100)*amount)
	return net_income


user_income = int(input('Please enter income'))

tax_rate = 0

if user_income <= 250000:
	tax_rate = 0

elif user_income >=250001 and user_income <= 500000:
	tax_rate = 5

elif user_income >=500001 and user_income <= 1000000:
	tax_rate = 20

elif user_income >=100001: 
	tax_rate = 30

final_income = tax_on_income(user_income, tax_rate)

print('Income after tax deductions', final_income)
