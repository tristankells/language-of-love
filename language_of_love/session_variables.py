from slots import AreaEnum
from slots import GenderPreferenceEnum


class SessionVariables:
    """
    Contains all the variables stored in the Alexa input handler 
    """
    FIRST_TIME = "first_time"
    NAME = "name"
    AREA = "area"
    GENDER_PREFERENCE = "gender_preference"
    CURRENT_TUTORIAL_PHRASE = "current_tutorial_phrase"
    TUTORIAL_REPEAT_OR_NEW = "tutorial_repeat_or_new"

    first_time = None
    name = None
    area = None
    gender_preference = None
    current_tutorial_phrase = None
    tutorial_repeat_or_new = None

    def __init__(self, state_variables):
        self.first_time = state_variables[self.FIRST_TIME] if self.FIRST_TIME in state_variables else True
        self.name = state_variables[self.NAME] if self.NAME in state_variables else "default"
        self.area = AreaEnum(state_variables[self.AREA]) if self.AREA in state_variables else AreaEnum.tutorial
        self.gender_preference = GenderPreferenceEnum(state_variables[
                                                          self.GENDER_PREFERENCE]) if self.GENDER_PREFERENCE in state_variables else GenderPreferenceEnum.both
        self.current_tutorial_phrase = state_variables[
            self.CURRENT_TUTORIAL_PHRASE] if self.CURRENT_TUTORIAL_PHRASE in state_variables else None
        self.tutorial_repeat_or_new = state_variables[
            self.TUTORIAL_REPEAT_OR_NEW] if self.TUTORIAL_REPEAT_OR_NEW in state_variables else False

    @staticmethod
    def get_initial():
        session_variables = {
            SessionVariables.FIRST_TIME: True,
            SessionVariables.NAME: "default",
            SessionVariables.AREA: AreaEnum.tutorial,
            SessionVariables.GENDER_PREFERENCE: GenderPreferenceEnum.both,
            SessionVariables.CURRENT_TUTORIAL_PHRASE: None,
            SessionVariables.TUTORIAL_REPEAT_OR_NEW: False
        }
        return session_variables

    @staticmethod
    def get():
        return {
            SessionVariables.FIRST_TIME: SessionVariables.first_time,
            SessionVariables.NAME: SessionVariables.name,
            SessionVariables.AREA: SessionVariables.area,
            SessionVariables.GENDER_PREFERENCE: SessionVariables.gender_preference,
            SessionVariables.CURRENT_TUTORIAL_PHRASE: SessionVariables.current_tutorial_phrase,
            SessionVariables.TUTORIAL_REPEAT_OR_NEW: SessionVariables.tutorial_repeat_or_new,
        }
