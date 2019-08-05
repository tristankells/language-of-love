from response import Response
from slots import AreaEnum
from translators.production_translator import Translator
import random

class LanguageOfLove:
    """
    Main skill class. Defines game logic and supplies the appropriate response
    based on game state
    """

    speech_text = []

    @staticmethod
    def launch(session_variables):
        """
        Replies with a response on game launch. Longer response for the first time the Alexa
        user is playing the skill
        """
        if session_variables.first_time:
            LanguageOfLove.speech_text = Translator.launch_first_time

        elif not session_variables.first_time:
            LanguageOfLove.speech_text = Translator.launch

        return Response(Translator.launch)

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
            if session_variables.area == AreaEnum.introduction:
                LanguageOfLove.speech_text = Translator.Introduction.answer_to_your_name

            return Response(LanguageOfLove.speech_text, session_variables=session_variables)

    class Questions:
        """
        Store all the handlers for when the player has asked a question
        """
        @staticmethod
        def where_are_you_from(session_variables):
            """
            Handler when the player ask's their date where they are from
            """
            if session_variables.area == AreaEnum.introduction:
                LanguageOfLove.speech_text = Translator.Introduction.answer_to_question_where_are_you_from

            return Response(LanguageOfLove.speech_text)

    class Practice:
        """
        Store all the response handler for starting practice
        """

        @staticmethod
        def start(session_variables):
            """
            Handler when the player launches the start practice intent
            """

            LanguageOfLove.speech_text.append(Translator.Practice.begin)
            LanguageOfLove.speech_text.append(get_rand_practice_phrase())

            return Response(LanguageOfLove.speech_text)


def get_rand_practice_phrase():
    """
    Returns a random practice phrase to use an a response
    """
    x = random.randint(1, 3)
    dict = {
        1: Translator.Practice.what_is_your_name,
        2: Translator.Practice.where_are_you_from,
        3: Translator.Practice.what_is_your_job,
    }
    return dict[x]
