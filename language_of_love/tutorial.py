from slots import AreaEnum
from alexa_talk_translator import Translator
from response import Response

class Tutorial:

    @staticmethod
    def begin():
        """
        Get the begin tutorial Response
        :return: Response
        """
        speech_text = Translator.Tutorial.begin
        return Response(speech_text)

    @staticmethod
    def my_name_is(session_variables):
        """
        Handlers when the player responds with there name
        """
        speech_text = None
        if session_variables.area == AreaEnum.tutorial:
            speech_text = Translator.Tutorial.answer_to_your_name

        return Response(speech_text, session_variables=session_variables)

    @staticmethod
    def where_are_you_from(session_variables):
        """
        Handler when the player ask's their date where they are from
        """
        if session_variables.area == AreaEnum.tutorial:
            speech_text = Translator.Tutorial.answer_to_question_where_are_you_from

        return Response(speech_text)
