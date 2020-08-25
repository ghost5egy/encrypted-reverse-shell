import subprocess , sys , os

class command:
	def __init__(self):
		osinfo = os.uname()
		self.data = osinfo.machine + ":" + osinfo.sysname + ":" + osinfo.release + ":" + osinfo.version + ":" + os.getlogin() + ":" + os.path.expanduser('~') + ":" + os.getcwd()

	def run_cmd(self,cmd):
		data = subprocess.run([cmd], shell=True , capture_output=True)
		if data.stderr.decode('utf-8') == '' :
			self.data = self.data + data.stdout.decode('utf-8')
		else:
			self.data = self.data + data.stderr.decode('utf-8')

		self.data = self.data + '\nCompleted sucessfully'

	def get_data(self,cmd=''):
		if cmd != '':
			self.run_cmd(cmd)
		return self.data

	def flush_cmd(self):
		self.data = ''

	def download(self, filep):
		if os.path.exists(filep) :
			if os.path.isfile(filep):
				return 'downloading'
			else:
				return 'not a file'
		return False

	def change_dir(self, gdir):
		try:
			if os.path.exists(gdir) :
				os.chdir(gdir)
			else:
				self.data = 'path not found'
		except OSError as e:
			self.data = e
