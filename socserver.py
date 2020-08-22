import sys
from core.connect import connect
from core.crypter import cryptMsg

def main():
	con = connect('127.0.0.1' , 8080)
	crypter = cryptMsg('this is my key b')
	data = crypter.decrypt(con.recv_serv())
	print(data[:data.find('<end_of_data>')])
	while True :
		data =''
		cmd = input('enter command : ')
		if cmd == '' :
			continue
		con.send_serv(crypter.encrypt(cmd))
		data = crypter.decrypt(con.recv_serv())
		while data.find('<end_of_data>') == -1 :
			data = crypter.decrypt(con.recv_serv())
		print(data[:data.find('<end_of_data>')])
		if cmd == 'exit':
			break

	con.close_serv()

if __name__ == '__main__' :
	main()
