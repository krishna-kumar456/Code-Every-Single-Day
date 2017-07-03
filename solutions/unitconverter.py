""" Unit Converter. 
"""
unit_col = {}

class UnitConverterStore:
	def __init__(self, unit, formula):
		self.unit = unit 
		self.formula = formula

	if self.unit not in unit_col:
		unit_col[self.unit] = self.formula



class UnitConverterFormulae:
	def temp_fahr_cel(self, user_input):
		return (user_input - 32) * 0.5556

	def temp_cel_fahr(self, user_input):
		return (user_input * 1.8) + 32





