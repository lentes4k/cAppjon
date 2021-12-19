class Hash

	def __init__(self, valor):
		key = 0
		for i in range(0, len(valor)):
			key+= ord(valor[i])
		return key % 127 
