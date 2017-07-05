""" Alarm Clock. 
"""
import datetime

def ring():
	print('Beep')

user_input_hour = int(input('Enter Hour'))
user_input_minutes = int(input('Enter minutes'))

beep = True
while beep:
	now = datetime.datetime.now()
	print(now.hour, now.minute, now.second)
	if user_input_hour == now.hour and user_input_minutes == now.minute:
		
		ring()
		beep = False
	


