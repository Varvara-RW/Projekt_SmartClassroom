import RPi.GPIO as GPIO
import time

def start_hellSensor ():
	value = 0

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.IN)
	try:
		while True:
			value=GPIO.input(4)
			if value == 0:
				with open("hellig.txt", "w") as f:
					f.write("Hell")
				print("Hell")
			else:
				with open("hellig.txt", "w") as f:
					f.write("Dunkel")
				print("Dunkel")
			time.sleep(2)
		
	except KeyboardInterrupt:
		print("interrupt")
