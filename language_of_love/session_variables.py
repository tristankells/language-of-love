from language_of_love.slots import AreaEnum
from language_of_love.slots import GenderPreferenceEnum


class SessionVariables:
    """
    Contains all the variables stored in the Alexa input handler 
    """
    FIRST_TIME = "first_time"
    NAME = "name"
    AREA = "area"
    GENDER_PREFERENCE = "gender_preference"

    def __init__(self, state_variables):
        self.first_time = state_variables[self.FIRST_TIME] if self.FIRST_TIME in state_variables else True
        self.name = state_variables[self.NAME] if self.NAME in state_variables else "default"
        self.area = AreaEnum(state_variables[self.AREA]) if self.AREA in state_variables else AreaEnum.tutorial
        self.gender_preference = GenderPreferenceEnum(state_variables[
                                                          self.GENDER_PREFERENCE]) if self.GENDER_PREFERENCE in state_variables else GenderPreferenceEnum.both

    @staticmethod
    def get_initial():
        session_variables = {
            SessionVariables.FIRST_TIME: True,
            SessionVariables.NAME: "default",
            SessionVariables.AREA: AreaEnum.tutorial,
            SessionVariables.GENDER_PREFERENCE: GenderPreferenceEnum.both
        }
        return session_variables
