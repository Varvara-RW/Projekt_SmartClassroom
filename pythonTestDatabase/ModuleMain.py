from database import database

datebase = database()
datensatz = ('hell', 19,31)
datebase.add_measurement(datensatz)

del database