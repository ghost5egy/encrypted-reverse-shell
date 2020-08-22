import socket , sys ,time ,errno

class connect:

	def __init__(self,serip, serport):
		self.ser_ip = serip
		self.ser_port = serport
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.connect()
		except NameError as e :
			print('connection error : ',e.args[0])

	def connect(self):
		while True:
			try:
				self.sock.connect((self.ser_ip , self.ser_port))
				break
			except:
    				pass
			time.sleep(10)

	def send_serv(self,sercmd):
		try:
			self.sock.send(sercmd)
		except NameError as e:
			print('sending error : ',e.args[0])

	def recv_serv(self):
		try:
			rcvmsg = self.sock.recv(1024)
			return rcvmsg
		except NameError as e :
			print('sending error : ',e.args[0])

	def close_serv(self):
		self.sock.close()

