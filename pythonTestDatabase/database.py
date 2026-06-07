import sqlite3

class database:

	def __init__(self):
		self.con = sqlite3.connect("measurements.db")
		self.cur = self.con.cursor()
		self.table_create()

	def table_create(self):
		try:
			cur.execute("CREATE TABLE measurements(brightness TEXT, pressure REAL, temperature REAL, timestamp TEXT DEFAULT CURRENT_TIMESTAMP)")
		except Exception:
			pass

	def add_measurement(self, datensatz):
		sql = ''' INSERT INTO measurements(brightness, pressure, temperature) VALUES(?,?,?)  '''

		self.cur = self.con.cursor()
		self.cur.execute(sql, datensatz)
		self.con.commit()
		
	def __del__(self):
		self.con.close()
