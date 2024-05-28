class ReprMeta(type):
	"""
	Defines a class-level `__repr__` method, which returns a .__repr__ class level attribute.
	In other words you can print a custom text without class initialization (usage of the instance-level __repr__).
	"""

	def __repr__(cls):
		"""
		Equivalent to `ClassName.__repr__` access.
		"""
		# Important: this will not work if the class level attribute will have another name but __repr__
		return getattr(cls, '__repr__')
