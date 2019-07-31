from slots import AreaEnum
from alexa_talk_translator import Translator
from response import Response
from intents import Intents
from response_handler import response_handler


def Introduction(intent_name, session_variables):
    def my_name_is(session_variables):
        """
        Handlers when the player responds with there name
        """
        speech_text = Translator.Tutorial.answer_to_your_name

        # Break the intro loop and enter menu loop
        session_variables.area = AreaEnum.menu
        return Response(speech_text, session_variables=session_variables)

    def fallback(session_variables):
        """
        Handler when the player ask's their date where they are from
        """

        speech_text = Translator.Tutorial.error

        return Response(speech_text, session_variables=session_variables)

    intent_dictionary = {
        Intents.ANSWER_NAME: my_name_is
    }

    return response_handler(intent_name, intent_dictionary, session_variables, fallback)
