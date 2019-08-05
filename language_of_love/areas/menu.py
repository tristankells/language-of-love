from intents import Intents
from slots import AreaEnum
from areas.area import Area


class Menu(Area):
    """
    Maps the intent of to the appropriate tutorial response
    :param intent_name: The name of the intent. 'AnswerNameIntent' or 'QuestionWhereYouFromIntent' for example
    :param session_variables: The SessionVariables object passed from the lambda function
    :return: a Response
    """
    Area.speech_text = Area.translator.Menu.fallback

    def start_practice(self):
        self.session_variables.area = AreaEnum.practice
        self.speech_text = self.translator.Practice.begin

    def start_speed_date(self):
        self.session_variables.area = AreaEnum.speed_date
        self.speech_text = self.translator.SpeedDate.begin

    Area.intent_dictionary = {
        Intents.START_PRACTICE: start_practice,
        Intents.START_SPEED_DATE: start_speed_date
    }
