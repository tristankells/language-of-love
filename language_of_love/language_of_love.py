from language_of_love.response import Response
from language_of_love.slots import AreaEnum
from language_of_love.alexa_talk_translator import Translator


class LanguageOfLove:
    """
    Main skill class. Defines game logic and supplies the appropriate response
    based on game state
    """

    speech_text = None

    @staticmethod
    def launch(session_variables):
        """
        Replies with a response on game launch. Longer response for the first time the Alexa
        user is playing the skill
        """
        if session_variables.first_time:
            LanguageOfLove.speech_text = Translator.launch_first_time
        if not session_variables.first_time:
            LanguageOfLove.speech_text = Translator.launch

        return Response(LanguageOfLove.speech_text)

    class Answers:
        """
        Store all the handlers for when the player has answered a question
        """
        @staticmethod
        def my_name_is(session_variables):
            """
            Handlers when the player responds with there name
            """
            LanguageOfLove.speech_text = None
            if session_variables.area == AreaEnum.tutorial:
                LanguageOfLove.speech_text = Translator.Tutorial.answer_to_your_name

            if LanguageOfLove.speech_text is None:
                LanguageOfLove.speech_text = Translator.Testing.error

            return Response(LanguageOfLove.speech_text)

    class Questions:
        """
        Store all the handlers for when the player has asked a question
        """
        @staticmethod
        def where_are_you_from(session_variables):
            """
            Handler when the player ask's their date where they are from
            """
            if session_variables.area == AreaEnum.tutorial:
                LanguageOfLove.speech_text = Translator.Tutorial.answer_to_question_where_are_you_from

            if LanguageOfLove.speech_text is None:
                LanguageOfLove.speech_text = Translator.Testing.error
            return Response(LanguageOfLove.speech_text)
