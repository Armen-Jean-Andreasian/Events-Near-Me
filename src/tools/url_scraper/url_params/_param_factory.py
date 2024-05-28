from typing import Type, Any, Union, TYPE_CHECKING


if TYPE_CHECKING:
	from .event_categories import EventCategory
	from .dates_fixed import FixedDate
	from .entrance_fee import EntranceFee

	ParentCategory = Union[EventCategory, FixedDate, EntranceFee]


class ParamFactory:
	@staticmethod
	def create_param(
			parent_class: "ParentCategory",
			metaclass: type,
			category_key: str,
			property_name: str,
			representation: str,
	) -> Type[Any]:
		"""
		Returns an object that:
		 1. inherits from parent_class
		 2. uses the given metaclass
		 3. has a property with the name `property_name` that returns the value associated with `category_key`

		:param parent_class: The parent class to inherit from
		:param metaclass: The metaclass to use for the created class
		:param representation: The representation string for the class
		:param category_key: The key to retrieve the category value from
		:param property_name: The name of the property to create
		:return: The dynamically created class
		"""

		class Parameter(parent_class, metaclass=metaclass):
			__repr__ = representation

		# dynamically creating the property with the given name
		setattr(Parameter, property_name, property(lambda self: self._categories.get(category_key)))

		return Parameter
