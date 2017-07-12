""" Finding distance between two cities 
"""
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

geolocater = Nominatim()

city_A = geolocater.geocode(input('Enter city A'))
city_B = geolocater.geocode(input('Enter city B'))

choice_of_measure = input('Please enter choice of measure')

city_A_coor = (city_A.latitude, city_A.longitude)
city_B_coor = (city_B.latitude, city_B.longitude)

if choice_of_measure == 'miles':
	print(vincenty(city_A_coor, city_B_coor).miles)

if choice_of_measure == 'meters':
	print(vincenty(city_A_coor, city_B_coor).meters)

