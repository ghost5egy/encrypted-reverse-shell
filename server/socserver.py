import sys,os
from core.connect import connect
from core.crypter import cryptMsg
from core.file import filestream

def main():
	ip = '127.0.0.1'
	port = 8080
	key = 'this is my key b'
	deli = '<end_of_data>'
	con = connect(ip , port)
	crypter = cryptMsg(key)
	data = crypter.decrypt(con.recv_serv())
	data = data[:data.find(deli)].split(":")
	for n in data :
		print(n)

	while True :
		data =''
		cmd = input('enter command : ')
		if cmd == '' :
			continue
		elif cmd.find('upload', 0 , 6) != -1 :
			comp = cmd.split(' ')
			if os.path.exists(comp[1]) is False:
				print('Please enter correct path')
				continue
			if os.path.isfile(comp[1]) is False:
				print('it\'s not a file it\'s directory')
				continue
			if os.path.getsize(comp[1]) <= 0:
				print('File is empty')
				continue
			con.send_serv(crypter.encrypt(cmd))
			fs = filestream(comp[1], 'rb')
			data = fs.read()
			while len(data) > 0:
				data = fs.read()
				con.send_serv(data)
			con.send_serv(data + deli.encode())
			fs.close()
			del fs
			continue
		elif cmd.find('download', 0 , 8) != -1 :
			con.send_serv(crypter.encrypt(cmd))
			comp = cmd.split(' ')
			fs = filestream(comp[1], 'wb+')
			while True:
				data = con.recv_serv()
				if data.rfind(deli) != -1 :
					fs.write(data[:data.rfind(deli)])
					break
				fs.write(data)
			fs.close()
			del fs
			print('Completed successfully')
		else:
			con.send_serv(crypter.encrypt(cmd))
			data = crypter.decrypt(con.recv_serv())
			while data.rfind(deli) == -1 :
				data = crypter.decrypt(con.recv_serv())
			print(data[:data.rfind(deli)])
		if cmd == 'exit':
			break

	con.close_serv()

if __name__ == '__main__' :
	main()
