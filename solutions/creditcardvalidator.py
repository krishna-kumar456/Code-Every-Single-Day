""" Credit Card Validator - Based on Luhn's Algorithm
"""
import math

def check_dig_num(n):
	if n > 0:
		digits = int(math.log10(n))+1
	
	elif n == 0:
		digits = 1

	return digits

def sum_digit(n):
 	r = 0
 	while n:
 		r,n = r + n % 10, n // 10

 	return r




card_number = list(input('Enter Card Number '))
card_number_int = [int(x) for x in card_number]
last_digit = card_number_int[-1]
del(card_number_int[-1])



for index, value in enumerate(card_number_int):
	if index % 2 == 1:
		card_number_int[index] = value*2


sum_of_card_number = 0

for index, value in enumerate(card_number_int):
	
	if check_dig_num(value) > 1:
		sum_of_card_number = sum_of_card_number + sum_digit(value)
	else:
		sum_of_card_number += value


multiplier = sum_of_card_number * 9
check_digit = multiplier % 10

if check_digit == last_digit:
	print('Valid Card Number')

else:
	print('Invalid')





