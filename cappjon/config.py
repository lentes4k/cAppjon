import os
from dotenv import load_dotenv

class Config: 

	def __init__(self):
		load_dotenv()
		if os.getenv('LOG_DIR'):
			self.log_dir = os.getenv('LOG_DIR')
		else:
			self.log_dir = '/logs/'
			if not os.path.exists(self.log_dir):
				os.mkdir(self.log_dir)

		if os.getenv('LOG_FILE'):
			self.log_file = os.getenv('LOG_FILE')
		else:
			self.log_file = 'notas.log'


	def get_directorio(self):
		return self.log_dir

	def get_archivo(self):
		return self.log_file

