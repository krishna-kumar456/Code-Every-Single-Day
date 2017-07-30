""" Limit Calculator

1. Accept numerator and denominator and limit
2. Apply the limit class
3. Display results
"""


from sympy import Limit



user_input_numerator = input('Please enter numerator')
user_input_denominator = input('Please enter denominator')
user_input_limit = input('Please enter the limit')

expr = user_input_numerator+'/'+user_input_denominator

result = Limit(expr, x, user_input_limit)

print('Resultant expression', result)
print('Final Result', result.doit())








