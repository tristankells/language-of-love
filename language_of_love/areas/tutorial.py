from slots import AreaEnum
from alexa_talk_translator import Translator
from response import Response
from intents import Intents

class Tutorial:

    @staticmethod
    def my_name_is(session_variables):
        """
        Handlers when the player responds with there name
        """
        speech_text = Translator.Intro.answer_to_your_name

        return Response(speech_text, session_variables=session_variables)

    @staticmethod
    def where_are_you_from(session_variables):
        """
        Handler when the player ask's their date where they are from
        """
        # TODO: No longer needed after the tutorial / intro.py rework
        session_variables.area = AreaEnum.menu
        speech_text = Translator.Intro.answer_to_question_where_are_you_from

        return Response(speech_text, session_variables=session_variables)

    @staticmethod
    def error(session_variables):
        """
        Handler when the player ask's their date where they are from
        """

        speech_text = Translator.Intro.error

        return Response(speech_text, session_variables=session_variables)

    @staticmethod
    def request_handler(intent_name, session_variables):
        """
        Maps the intent of to a the appropriate tutorial response
        :param intent_name: The name of the intent. 'AnswerNameIntent' or 'QuestionWhereYouFromIntent' for example
        :param session_variables: The SessionVariables object passed from the lambda function
        :return: a Response
        """
        intent_dictionary = {
            Intents.ANSWER_NAME: Tutorial.my_name_is,
            Intents.QUESTION_WHERE_YOU_FROM: Tutorial.where_are_you_from
        }

        if intent_name in intent_dictionary:
            return intent_dictionary[intent_name](session_variables)

        else:
            return Tutorial.error(session_variables)
