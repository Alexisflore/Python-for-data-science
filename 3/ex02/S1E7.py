from abc import ABCMeta
from S1E9 import Character, Stark

class Baratheon(Character):
	"""Representing the Baratheon family"""
	def __init__(self, name, is_alive=True):
		"""Initialize the Baratheon"""
		self.first_name = name
		self.is_alive = is_alive
		self.family_name = "Baratheon"
		self.eyes = "brown"
		self.hairs = "dark"

	def die(self):
		"""Kill the Baratheon"""
		super().die()

	def __str__(self):
		"""Return the name of the character"""
		return f"{self.first_name} Baratheon"

	def __repr__(self):
		"""Return the bound method representation"""
		return f"<bound method Baratheon.__str__ of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

class Lannister(Character):
	"""Lannister class"""
	def __init__(self, name, is_alive=True):
		"""Initialize the Lannister"""
		self.first_name = name
		self.is_alive = is_alive
		self.family_name = "Lannister"
		self.eyes = "blue"
		self.hairs = "light"

	def die(self):
		"""Kill the Lannister"""
		super().die()

	def __str__(self):
		"""Return the name of the character"""
		return f"{self.first_name} Lannister"

	def __repr__(self):
		"""Return the bound method representation"""
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

	@staticmethod
	def create_lannister(name, is_alive=True):
		"""Create a Lannister"""
		return Lannister(name, is_alive)
