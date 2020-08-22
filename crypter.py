from Crypto.Cipher import AES
from Crypto import Random
import hashlib , base64 ,sys

class cryptMsg :
	def __init__(self, key):
		self.key = hashlib.md5(key.encode())

	def encrypt(self, message):
		iv = Random.new().read(AES.block_size)
		self.obj = AES.new(self.key.digest(), AES.MODE_CBC, iv)
		return base64.b64encode(iv + self.obj.encrypt(self.pad(message).encode()))

	def decrypt(self, message):
		encrcv = base64.b64decode(message)
		iv = encrcv[:AES.block_size]
		self.obj = AES.new(self.key.digest(), AES.MODE_CBC, iv)
		return self.rmpad(self.obj.decrypt(encrcv[AES.block_size:]).decode('utf-8'))

	def get_key(self):
		return self.key

	def rmpad(self, s):
		return s.replace('`','')

	def pad(self, s):
		return s + ((16 - len(s) % 16) * '`')

