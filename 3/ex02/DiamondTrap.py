from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	def __init__(self, name):
		Baratheon.__init__(self, name)

	def set_eyes(self, color):
		self.eyes = color
	
	def set_hairs(self, color):
		self.hairs = color
	
	def get_hairs(self):
		return self.hairs
	
	def get_eyes(self):
		return self.eyes