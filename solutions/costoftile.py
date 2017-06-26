""" Calculate the cost of title for floor plan
"""
def cost_floor_plan(cost):
	height_floor = 25
	width_floor = 25
	height_of_tile = 5
	width_of_tile = 5

	area_tile = height_of_tile * width_of_tile
	area_floor = height_floor * width_floor
	no_of_tiles = area_floor // area_tile

	total_cost = no_of_tiles * cost

	return total_cost


user_input = int(input('Enter the cost for 1 tile'))
result = cost_floor_plan(user_input)
print(result)