import sqlite3


# print(time.asctime(clock))

def addTuple(datensatz):
	# get clock somehow
	
	# data = [b,p,t, clock]
	sql = ''' INSERT INTO measurements(brightness, pressure, temperature) VALUES(?,?,?)  '''

	cur = con.cursor()
	cur.execute(sql, datensatz)

	con.commit()
	con.close()

con = sqlite3.connect("measurements.db")


cur = con.cursor()
try:
	cur.execute("CREATE TABLE measurements(brightness TEXT, pressure REAL, temperature REAL, timestamp TEXT DEFAULT CURRENT_TIMESTAMP)")
except Exception:
        pass


res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()

res1 = cur.execute("SELECT temperature FROM measurements")
res1.fetchall()

datensatz = ('hell', 932.9, 22.1)
datensatzID = addTuple(datensatz)

# def readTuple
# def deleteTuple
# def highest.temperature{}
# highest and lowest values as well as the average of each attribute