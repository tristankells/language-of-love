from custom_collections.intents import Intents
from custom_collections.slots import AreaEnum
from areas.area import Area
from custom_collections.practice_phrases import PracticePhrases


class Menu(Area):
    """
    Maps the intent of to the appropriate tutorial response
    :param intent_name: The name of the intent. 'AnswerNameIntent' or 'QuestionWhereYouFromIntent' for example
    :param session_variables: The SessionVariables object passed from the lambda function
    :return: a Response
    """
    speech_text = Area.translator.Menu.fallback

    def start_practice(self):
        self.session_variables.area = AreaEnum.practice
        self.session_variables.current_practice_phrase = PracticePhrases.WHAT_IS_YOUR_NAME
        self.speech_text = self.translator.Practice.begin + self.translator.Practice.what_is_your_name

    def start_speed_date(self):
        self.session_variables.area = AreaEnum.date
        self.speech_text = self.translator.Date.begin

    def help(self):
        self.speech_text = Area.translator.Menu.fallback

    intent_dictionary = {
        Intents.START_PRACTICE: start_practice,
        Intents.START_SPEED_DATE: start_speed_date,
        Intents.HELP: help
    }
