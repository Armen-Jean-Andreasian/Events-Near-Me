from typing import Union
from src.tools.url_scraper.url_params import (
	BusinessCategory,
	FoodDrinkCategory,
	HealthCategory,
	MusicCategory,
	AutoBoatAirCategory,
	CharityCausesCategory,
	CommunityCategory,
	FamilyEducationCategory,
	FashionCategory,
	FilmMediaCategory,
	HobbiesCategory,
	HomeLifestyleCategory,
	PerformingVisualArtsCategory,
	GovernmentCategory,
	SpiritualityCategory,
	SchoolActivitiesCategory,
	ScienceTechCategory,
	HolidaysCategory,
	SportsFitnessCategory,
	TravelOutdoorCategory,
	OtherCategory
)
from src.tools.url_scraper.url_params import FreeEntrance, PaidEntrance
from src.tools.url_scraper.url_params import Today, Tomorrow, ThisWeekend

__all__ = ["EventCategory", "EntranceFee", "FixedDate"]

EventCategory = Union[
	BusinessCategory,
	FoodDrinkCategory,
	HealthCategory,
	MusicCategory,
	AutoBoatAirCategory,
	CharityCausesCategory,
	CommunityCategory,
	FamilyEducationCategory,
	FashionCategory,
	FilmMediaCategory,
	HobbiesCategory,
	HomeLifestyleCategory,
	PerformingVisualArtsCategory,
	GovernmentCategory,
	SpiritualityCategory,
	SchoolActivitiesCategory,
	ScienceTechCategory,
	HolidaysCategory,
	SportsFitnessCategory,
	TravelOutdoorCategory,
	OtherCategory
]

EntranceFee = Union[
	PaidEntrance,
	FreeEntrance
]

FixedDate = Union[
	Today,
	Tomorrow,
	ThisWeekend
]