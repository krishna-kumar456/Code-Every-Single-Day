""" Mortgage calculator
Monthly payments m = r/(1-(1+r)**-N)*P
"""
def calculate_fixed_n(p,r,n):
	m = (r//(1-(1+r)**-n))*p
	return m

user_input_p = int(input('Enter principal'))
user_input_r = int(input('Enter rate'))
user_input_n = int(input('Enter loan term n'))
result = calculate_fixed_n(user_input_p, user_input_r, user_input_n)
print('No of monthly installments ', result)