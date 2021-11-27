import time
import RPi.GPIO as GPIO #Import GPIO library
GPIO.setmode(GPIO.BOARD) #Set Board
GPIO.setup(7,GPIO.OUT) #Select Pin for Output
GPIO.setup(5,GPIO.IN) #Select Pin for Input through
while 1:
	if(GPIO.input(5)==0):
		print('light is on')
		GPIO.output(7,1)
	else:
		print('light is off')
		GPIO.output(7,0)
