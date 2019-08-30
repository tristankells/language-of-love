from custom_collections.slots import AreaEnum
from custom_collections.slots import GenderPreferenceEnum
from custom_collections.slots import DateEnum
from custom_collections.slots import ConversationEnum
from custom_collections.practice_phrases import PracticePhrases


class SessionVariables:
    """
    Contains all the variables stored in the Alexa input handler 
    """
    # Variable string constants
    CONVERSATION = "conversation"
    FIRST_TIME = "first_time"
    NAME = "name"
    AREA = "area"
    GENDER_PREFERENCE = "gender_preference"
    CURRENT_PRACTICE_PHRASE = "current_practice_phrase"
    DATE_SCORE = "date_score"
    TOTAL_SCORE = "total_score"
    DATE_BAD_RESPONSE_COUNT = "date_bad_response_count"
    DATE_ROUND = 'date_round'
    NUMBER_OF_DATES = "number_of_dates"
    DATE = "date"

    # Variables
    conversation = None
    first_time = None
    name = None
    area = None
    gender_preference = None
    current_practice_phrase = None
    date_score = None
    total_score = None
    date_bad_response_count = None
    date_round = None
    number_of_dates = None
    date = None

    def __init__(self, state_variables):
        """
        Takes a dictionary of session variables and turns it into SessionVariables object (with default values, linting and enum transformation)
        """
        self.first_time = state_variables[self.FIRST_TIME] if self.FIRST_TIME in state_variables else True

        self.name = state_variables[self.NAME] if self.NAME in state_variables else "default"

        self.area = AreaEnum(state_variables[self.AREA]) if self.AREA in state_variables else AreaEnum.date

        self.gender_preference = GenderPreferenceEnum(state_variables[
                                                          self.GENDER_PREFERENCE]) if self.GENDER_PREFERENCE in state_variables else GenderPreferenceEnum.both

        self.current_practice_phrase = state_variables[
            self.CURRENT_PRACTICE_PHRASE] if self.CURRENT_PRACTICE_PHRASE in state_variables else PracticePhrases.EMPTY

        self.conversation = ConversationEnum(state_variables[self.CONVERSATION]) if self.CONVERSATION in state_variables else ConversationEnum.nothing

        self.date_score = state_variables[self.DATE_SCORE] if self.DATE_SCORE in state_variables else 0

        self.total_score = state_variables[self.TOTAL_SCORE] if self.TOTAL_SCORE in state_variables else 0

        self.date_bad_response_count = state_variables[
            self.DATE_BAD_RESPONSE_COUNT] if self.DATE_BAD_RESPONSE_COUNT in state_variables else 0

        self.date_round = state_variables[self.DATE_ROUND] if self.DATE_ROUND in state_variables else 0

        self.number_of_dates = state_variables[self.NUMBER_OF_DATES] if self.NUMBER_OF_DATES in state_variables else 0

        self.date = DateEnum(state_variables[self.DATE]) if self.DATE in state_variables else DateEnum.enrique


    @staticmethod
    def get_initial_dict():
        """
        Gets the initial state of the game variables as
        """
        return {
            SessionVariables.FIRST_TIME: True,
            SessionVariables.NAME: "default",
            SessionVariables.AREA: AreaEnum.introduction,
            SessionVariables.GENDER_PREFERENCE: GenderPreferenceEnum.both,
            SessionVariables.CURRENT_PRACTICE_PHRASE: PracticePhrases.EMPTY,
            SessionVariables.CONVERSATION: ConversationEnum.nothing,
            SessionVariables.DATE_SCORE: 0,
            SessionVariables.TOTAL_SCORE: 0,
            SessionVariables.DATE_BAD_RESPONSE_COUNT: 0,
            SessionVariables.DATE_ROUND: 0,
            SessionVariables.NUMBER_OF_DATES: 0,
            SessionVariables.DATE: DateEnum.conchita
        }

    def get_dict(self):
        return {
            SessionVariables.FIRST_TIME: self.first_time,
            SessionVariables.NAME: self.name,
            SessionVariables.AREA: self.area,
            SessionVariables.GENDER_PREFERENCE: self.gender_preference,
            SessionVariables.CURRENT_PRACTICE_PHRASE: self.current_practice_phrase,
            SessionVariables.CONVERSATION: self.conversation,
            SessionVariables.DATE_SCORE: self.date_score,
            SessionVariables.TOTAL_SCORE: self.total_score,
            SessionVariables.DATE_BAD_RESPONSE_COUNT: self.date_bad_response_count,
            SessionVariables.DATE_ROUND: self.date_round,
            SessionVariables.NUMBER_OF_DATES: self.number_of_dates,
            SessionVariables.DATE: self.date
        }
