from intents import Intents
from alexa_talk_translator import Translator
from response import Response
from slots import AreaEnum
import random
from practice_phrase import PracticePhrases
from response_handler import response_handler


def Practice(intent_name, session_variables):
    def get_new_phrase(current_phrase_key):
        """
        Return a new random tutorial phrase key not the same as the last phrase key
        """

        # TODO: Make it so that player gets a couple more unique messages before they might get a repeat

        phrase_dictionary = {
            1: PracticePhrases.WHAT_IS_YOUR_NAME,
            2: PracticePhrases.WHERE_ARE_YOU_FROM,
            3: PracticePhrases.WHAT_IS_YOUR_JOB
        }

        new_phrase_key = None

        # Keep looking for a unique key
        while (new_phrase_key is None or new_phrase_key is current_phrase_key):
            random_number = random.randint(1, 3)
            new_phrase_key = phrase_dictionary[random_number]

        return new_phrase_key

    def new_phrase(session_variables):
        """
        Handle when the player asks for a new phrase in the "repeat or new" practice loop
        """
        current_phrase_key = session_variables.current_tutorial_phrase
        new_phrase_key = get_new_phrase(current_phrase_key)
        speech_text = PracticePhrases.get_speech_text(new_phrase_key)

        session_variables.current_tutorial_phrase = new_phrase_key
        session_variables.tutorial_repeat_or_new = False

        return Response(speech_text, session_variables=session_variables)

    def repeat_phrase(session_variables):
        """
        Handle when the player asks for phrase to be repeated in the "repeat or new" practice loop
        """
        phrase_key = session_variables.current_tutorial_phrase
        speech_text = PracticePhrases.get_speech_text(phrase_key)

        session_variables.tutorial_repeat_or_new = False

        return Response(speech_text, session_variables=session_variables)

    def fallback(session_variables):
        # TODO: Idea: This could be used to display a message if they player says something not recognised at the 'new or repeat' loop

        return Response(Translator, session_variables)

    def end_tutorial(session_variables):
        session_variables.tutorial_repeat_or_new = False
        session_variables.area = AreaEnum.menu

        return Response(Translator.Practice.end, session_variables=session_variables)

    practice_intents = {
        Intents.NEW_PHRASE: new_phrase,
        Intents.REPEAT: repeat_phrase,
        Intents.CANCEL: end_tutorial
    }

    return response_handler(intent_name, practice_intents, session_variables, fallback)
