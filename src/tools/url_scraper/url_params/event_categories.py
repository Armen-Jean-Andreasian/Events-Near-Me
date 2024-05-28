from .error import BaseClassError
from ._param_factory import ParamFactory
from ._repr_metaclass import ReprMeta


class EventCategory:
	__repr__: str

	def __init__(self):
		self._categories = {
			"business": "business--events",
			"food_and_drink": "food-and-drink--events",
			"health": "health--events",
			"music": "music--events",
			"auto_boat_and_air": "auto-boat-and-air--events",
			"charity_and_causes": "charity-and-causes--events",
			"community": "community--events",
			"family_and_education": "family-and-education--events",
			"fashion": "fashion--events",
			"film_and_media": "film-and-media--events",
			"hobbies": "hobbies--events",
			"home_and_lifestyle": "home-and-lifestyle--events",
			"performing_and_visual_arts": "arts--events",
			"government": "government--events",
			"spirituality": "spirituality--events",
			"school_activities": "school-activities--events",
			"science_and_tech": "science-and-tech--events",
			"holidays": "holiday--events",
			"sports_and_fitness": "sports-and-fitness--events",
			"travel_and_outdoor": "travel-and-outdoor--events",
			"other": "other--events"
		}

	@property
	def category(self):
		raise BaseClassError(class_name=self.__class__.__name__, property_name='category')


class EventCategoryFactory:
	@staticmethod
	def create(representation: str, category_key: str):
		return ParamFactory.create_param(
			representation=representation,
			category_key=category_key,
			parent_class=EventCategory,
			metaclass=ReprMeta,
			property_name='category'
		)


BusinessCategory = EventCategoryFactory.create("Business", "business")
FoodDrinkCategory = EventCategoryFactory.create("Food & Drink", "food_and_drink")
HealthCategory = EventCategoryFactory.create("Health", "health")
MusicCategory = EventCategoryFactory.create("Music", "music")
AutoBoatAirCategory = EventCategoryFactory.create("Auto, Boat & Air", "auto_boat_and_air")
CharityCausesCategory = EventCategoryFactory.create("Charity & Causes", "charity_and_causes")
CommunityCategory = EventCategoryFactory.create("Community", "community")
FamilyEducationCategory = EventCategoryFactory.create("Family & Education", "family_and_education")
FashionCategory = EventCategoryFactory.create("Fashion", "fashion")
FilmMediaCategory = EventCategoryFactory.create("Film & Media", "film_and_media")
HobbiesCategory = EventCategoryFactory.create("Hobbies", "hobbies")
HomeLifestyleCategory = EventCategoryFactory.create("Home & Lifestyle", "home_and_lifestyle")
PerformingVisualArtsCategory = EventCategoryFactory.create("Performing & Visual Arts", "performing_and_visual_arts")
GovernmentCategory = EventCategoryFactory.create("Government", "government")
SpiritualityCategory = EventCategoryFactory.create("Spirituality", "spirituality")
SchoolActivitiesCategory = EventCategoryFactory.create("School Activities", "school_activities")
ScienceTechCategory = EventCategoryFactory.create("Science & Tech", "science_and_tech")
HolidaysCategory = EventCategoryFactory.create("Holidays", "holidays")
SportsFitnessCategory = EventCategoryFactory.create("Sports & Fitness", "sports_and_fitness")
TravelOutdoorCategory = EventCategoryFactory.create("Travel & Outdoor", "travel_and_outdoor")
OtherCategory = EventCategoryFactory.create("Other", "other")
