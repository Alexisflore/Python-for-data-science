from abc import ABC, abstractmethod

class Character(ABC):
	"""Character class"""
	def __init__(self, name, is_alive=True):
		self.first_name = name
		self.is_alive = is_alive

	@abstractmethod
	def die(self):
		"""Kill the character"""
		self.is_alive = False

class Stark(Character):
	"""Stark class"""
	def __init__(self, name, is_alive=True):
		"""Initialize the Stark"""
		super().__init__(name, is_alive)

	def die(self):
		"""Kill the Stark"""
		super().die()
