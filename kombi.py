import time
import Helligkeitsensor as hell
import Temperatursensor as temp
import drivers

hell.start_hellSensor()
temp.start_tempDruSensor()
display = drivers.Lcd()

try: 
    print("Press CTRL + C to quit program")
    while True:
        with open("hellig.txt") as f, open("temper.txt") as x, open("druck.txt") as k:
            temperatur = x.readline()
            temperatur = temperatur.strip() + " \xDFC"
            druck = k.readline()
            druck = druck.strip() + " hPa"
            hellig = f.readline()
            hellig = hellig.strip()
            
            display.lcd_clear()
            display.lcd_display_string("Es ist " + hellig, 1)
            time.sleep(2)
            display.lcd_clear()
            display.lcd_display_string("Temperatur:", 1)
            display.lcd_display_string(temperatur, 2)
            time.sleep(2)
            display.lcd_clear()
            display.lcd_display_string("Druck:", 1)
            display.lcd_display_string(druck, 2)
            time.sleep(2)

except KeyboardInterrupt:
    display.lcd_clear()
    display.lcd_backlight(1)
    
