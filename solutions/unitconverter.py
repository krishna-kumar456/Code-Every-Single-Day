""" Unit Converter. 
"""



class UnitConverterFormulae:
	def temp_fahr_cel(self, user_input):
		return (user_input - 32) * 0.5556

	def temp_cel_fahr(self, user_input):
		return (user_input * 1.8) + 32

ucf = UnitConverterFormulae()

unit_store = {
				'ftoc': ucf.temp_fahr_cel,
				'ctof': ucf.temp_cel_fahr
}

user_input_type = input('Enter unit type')
user_input_value = int(input('Enter value to be converted'))



for item in unit_store.keys():
	
	if user_input_type == item:	
		result = unit_store[item](user_input_value)
	else:
		result = 'Couldnt evalutate'
		


print('Resultant Conversion', result)




