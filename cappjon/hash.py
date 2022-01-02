class Hash

	def __init__(self):
		key = 0

	def hashing(self, valor):
		for i in range(0, len(valor)):
			key+= ord(valor[i])
		return key % 127 
