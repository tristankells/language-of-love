from slots import AreaEnum
from slots import GenderPreferenceEnum
from practice_phrases import PracticePhrases
from player import Player


class SessionVariables:
    """
    Contains all the variables stored in the Alexa input handler 
    """
    CONVERSATION = "conversation"
    PLACE = "place"
    FIRST_TIME = "first_time"
    NAME = "name"
    AREA = "area"
    GENDER_PREFERENCE = "gender_preference"
    CURRENT_PRACTICE_PHRASE = "current_practice_phrase"
    PRACTICE_REPEAT_OR_NEW = "practice_repeat_or_new"
    PLAYER_VARIABLES = "player_variables"

    conversation = None
    place = None
    first_time = None
    name = None
    area = None
    gender_preference = None
    current_practice_phrase = None
    tutorial_repeat_or_new = None
    player_variables = None

    def __init__(self, state_variables):
        self.first_time = state_variables[self.FIRST_TIME] if self.FIRST_TIME in state_variables else True
        self.name = state_variables[self.NAME] if self.NAME in state_variables else "default"
        self.area = AreaEnum(state_variables[self.AREA]) if self.AREA in state_variables else AreaEnum.speed_date
        self.gender_preference = GenderPreferenceEnum(state_variables[
                                                          self.GENDER_PREFERENCE]) if self.GENDER_PREFERENCE in state_variables else GenderPreferenceEnum.both
        self.current_practice_phrase = state_variables[
            self.CURRENT_PRACTICE_PHRASE] if self.CURRENT_PRACTICE_PHRASE in state_variables else PracticePhrases.EMPTY
        self.tutorial_repeat_or_new = state_variables[
            self.PRACTICE_REPEAT_OR_NEW] if self.PRACTICE_REPEAT_OR_NEW in state_variables else False
        self.conversation = state_variables[self.CONVERSATION] if self.CONVERSATION in state_variables else 1000
        self.place = state_variables[self.PLACE] if self.PLACE in state_variables else 0


    @staticmethod
    def get_initial():
        return {
            SessionVariables.FIRST_TIME: True,
            SessionVariables.NAME: "default",
            SessionVariables.AREA: AreaEnum.introduction,
            SessionVariables.GENDER_PREFERENCE: GenderPreferenceEnum.both,
            SessionVariables.CURRENT_PRACTICE_PHRASE: PracticePhrases.EMPTY,
            SessionVariables.PRACTICE_REPEAT_OR_NEW: False,
            SessionVariables.CONVERSATION: 1000,
            SessionVariables.PLACE: 0
        }

    def get(self):
        return {
            SessionVariables.FIRST_TIME: self.first_time,
            SessionVariables.NAME: self.name,
            SessionVariables.AREA: self.area,
            SessionVariables.GENDER_PREFERENCE: self.gender_preference,
            SessionVariables.CURRENT_PRACTICE_PHRASE: self.current_practice_phrase,
            SessionVariables.PRACTICE_REPEAT_OR_NEW: self.tutorial_repeat_or_new,
            SessionVariables.CONVERSATION: self.conversation,
            SessionVariables.PLACE: self.place
        }
