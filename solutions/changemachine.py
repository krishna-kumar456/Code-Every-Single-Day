""" Change machine - Returns change as per user entered cost and money given.
"""
def change_calculation(cost, amount):

	half_dollar = 0
	quarter = 0
	dime = 0
	nickel = 0
	penny = 0

	diff = amount - cost

	print(diff)

	if diff < 0 :
		return -1

	if diff == 0:
		return -2

	

	if diff > 0:
		if diff >= 0.50:
			half_dollar += 1
			diff = diff - 0.50
			
		if diff >= 0.25:
			quarter += 1
			diff = diff - 0.25

		if diff >= 0.10:
			dime += 1
			diff = diff - 0.10

		if diff >= 0.5:
			nickel += 1
			diff = diff - 0.5
		penny = int(diff)
	return half_dollar, quarter, dime, nickel, penny


user_input_cost = int(input('Enter cost'))
user_input_amount = float(input('Enter Amount'))

result = []
result = change_calculation(user_input_cost, user_input_amount)

if result[0] == -1:
	print('Please gif required cost')

if result[0] == -2:
	print('No change required')
if len(result) > 0:
	print('Change to be provided')
	print('Half dollars', result[0])
	print('Quarters', result[1])
	print('Dimes', result[2])
	print('Nickel', result[3])
	print('Pennies', result[4])


