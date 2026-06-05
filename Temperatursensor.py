import board
import busio
import adafruit_bmp280
import time

def start_tempDruSensor ():
	i2c = busio.I2C(board.SCL, board.SDA)
	sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

	try:
		while True:
			with open("temper.txt", "w") as f, open("druck.txt", "w") as k:
				f.write(f"{sensor.temperature:.1f}")
				k.write(f"{sensor.pressure:.1f}")
			print("\nTemperatur: %0.1f *C" % sensor.temperature)
			print("Luftdruck: %0.1f hPa" % sensor.pressure)
			time.sleep(2)
	
	except KeyboardInterrupt:
		print("Interrupt")


