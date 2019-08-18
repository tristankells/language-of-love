from enum import Enum


class AreaEnum(Enum):
    """
    Represents the area the player is currently playing in; tutorial, practice 
    or speed date
    """
    menu = 0
    introduction = 1
    practice = 2
    speed_date = 3


class GenderPreferenceEnum(Enum):
    """
    Represents the preferred gender of the player's romantic interests in the
    skill: both, male or female
    """
    both = 1
    male = 2
    female = 3


class Date(Enum):
    """
    Who the player is on a date with
    """

    tessa = 1
    enrique = 2
    conchita = 3
