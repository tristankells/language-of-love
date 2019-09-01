from custom_collections.intents import Intents
from custom_collections.slots import AreaEnum
import random
from custom_collections.practice_phrases import PracticePhrases
from areas.area import Area


class Practice(Area):
    """
    While in the practice area of the game, maps the intents to appropriate response
    """
    speech_text = Area.translator.Practice.fallback

    @staticmethod
    def get_new_phrase(current_phrase_key):
        """
        Return a new random tutorial phrase key not the same as the last phrase key
        """

        # TODO: Make it so that player gets a couple more unique messages before they might get a repeat

        phrase_dictionary = {
            1: PracticePhrases.WHAT_IS_YOUR_NAME,
            2: PracticePhrases.DO_YOU_LIKE_TO_TRAVEL,
            3: PracticePhrases.WHAT_IS_YOUR_JOB,
            4: PracticePhrases.WHERE_ARE_YOU_FROM,
            5: PracticePhrases.WHAT_IS_YOUR_FAVOURITE_ANIMAL,
            6: PracticePhrases.WHAT_IS_YOUR_FAVOURITE_COLOUR,
            7: PracticePhrases.HOW_IS_YOUR_DAY,
            8: PracticePhrases.HOW_OLD_ARE_YOU,
            9: PracticePhrases.WHAT_IS_YOUR_FAVOURITE_BOOK
        }

        new_phrase_key = None

        # Keep looking for a unique key
        while (new_phrase_key == None or new_phrase_key == current_phrase_key):
            random_number = random.randint(1, 3)
            new_phrase_key = phrase_dictionary[random_number]

        return new_phrase_key

    def new_phrase(self):
        """
        Handle when the player asks for a new phrase in the "repeat or new" practice loop
        """
        current_phrase_key = self.session_variables.current_practice_phrase
        new_phrase_key = self.get_new_phrase(current_phrase_key)
        self.speech_text = PracticePhrases.get_speech_text(new_phrase_key)
        self.session_variables.current_practice_phrase = new_phrase_key

    def repeat_phrase(self):
        """
        Handle when the player asks for phrase to be repeated in the "repeat or new" practice loop
        """
        phrase_key = self.session_variables.current_practice_phrase
        self.speech_text = PracticePhrases.get_speech_text(phrase_key)

    def end_tutorial(self):
        self.session_variables.area = AreaEnum.menu
        self.speech_text = self.translator.Practice.end + " " + self.translator.Menu.options

    def start_speed_date(self):
        self.session_variables.area = AreaEnum.date
        self.speech_text = self.translator.Date.begin

    intent_dictionary = {
        Intents.NEW_PRACTICE_PHRASE: new_phrase,
        Intents.REPEAT_PRACTICE_PHRASE: repeat_phrase,
        Intents.CANCEL: end_tutorial,
        Intents.LEAVE_AREA: end_tutorial,
        Intents.START_SPEED_DATE: start_speed_date
    }
