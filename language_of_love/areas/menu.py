from intents import Intents
from translators.alexa_talk_translator import Translator
from response import Response
from response_handler import response_handler
from slots import AreaEnum


def Menu(intent_name, session_variables):
    """
    Maps the intent of to the appropriate tutorial response
    :param intent_name: The name of the intent. 'AnswerNameIntent' or 'QuestionWhereYouFromIntent' for example
    :param session_variables: The SessionVariables object passed from the lambda function
    :return: a Response
    """
    def start_practice(session_variables):
        session_variables.area = AreaEnum.practice
        return Response(Translator.Practice.start, session_variables=session_variables)

    def start_speed_date(session_variables):
        session_variables.area = AreaEnum.speed_date
        return Response(Translator.SpeedDate.begin, reprompt=Translator.Reprompt.menu,
                        session_variables=session_variables)

    def error(session_variables):
        return Response(Translator.Error.bad_option, reprompt=Translator.Reprompt.menu,
                        session_variables=session_variables)

    intent_dictionary = {
        Intents.START_PRACTICE: start_practice,
        Intents.START_SPEED_DATE: start_speed_date
    }

    return response_handler(intent_name, intent_dictionary, session_variables, error)
