class filestream:

	def __init__(self, filename, fmode):
		self.fileob = open(filename, fmode)
		self.chunk = 1024

	def read(self):
		return self.fileob.read(self.chunk)

	def write(self, data):
		try:
			self.fileob.write(data.encode())
		except:
			print('bad data')

	def close(self):
		self.fileob.close()
