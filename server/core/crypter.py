from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad ,unpad
import hashlib , base64 , urllib3

class cryptMsg :
	def __init__(self, key):
		self.key = hashlib.md5(key.encode())

	def encrypt(self, message):
		iv = Random.new().read(AES.block_size)
		self.obj = AES.new(self.key.digest(), AES.MODE_CBC, iv)
		return base64.b64encode(iv + self.obj.encrypt(pad(message.encode('ascii') ,AES.block_size)))

	def decrypt(self, message):
		encrcv = base64.b64decode(message)
		iv = encrcv[:AES.block_size]
		self.obj = AES.new(self.key.digest(), AES.MODE_CBC, iv)
		return unpad(self.obj.decrypt(encrcv[AES.block_size:]) , AES.block_size).decode('utf-8')

	def get_key(self):
		return self.key
