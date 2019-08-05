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
