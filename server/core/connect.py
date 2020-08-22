import socket , sys

class connect:

	def __init__(self,serip, serport):
		self.ser_ip = serip
		self.ser_port = serport

		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.bind((self.ser_ip , self.ser_port))
			self.sock.listen(20)
			self.cli_sock, self.cli_address = self.sock.accept()
			print('connected with : ', self.cli_address)
		except NameError as e :
			print('connection error : ',e.args[0])
			sys.exit(1)

	def send_serv(self,sercmd):
		try:
			self.cli_sock.send(sercmd)
		except NameError as e:
			print('sending error : ',e.args[0])

	def recv_serv(self):
		try:
			rcvmsg = self.cli_sock.recv(4 * 1024).decode('utf-8')
			return rcvmsg
		except NameError as e :
			print('sending error : ',e.args[0])

	def close_serv(self):
		self.cli_sock.close()
		self.sock.close()

