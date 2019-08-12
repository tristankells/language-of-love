import unittest
from session_variables import SessionVariables
from custom_collections import slots
from custom_collections.intents import Intents
from translators.test_translator import TestTranslator

from areas.practice import Practice
from custom_collections.practice_phrases import PracticePhrases


class TestDateHandler(unittest.TestCase):

    def test_if(self):
        session_variables = {
            SessionVariables.CURRENT_PRACTICE_PHRASE: PracticePhrases.WHAT_IS_YOUR_NAME,
            SessionVariables.PRACTICE_REPEAT_OR_NEW: True,
            SessionVariables.AREA: slots.AreaEnum.practice
        }
        response = Practice(Intents.REPEAT_PRACTICE_PHRASE, session_variables).get_response()

        # Confirm player still in tutorial
        self.assertEqual(response.session_variables.area, slots.AreaEnum.practice)
        # Confirm player out of repeat loop
        self.assertEqual(response.session_variables.tutorial_repeat_or_new, False)
        # Confirm player gets the same message
        self.assertEqual(response.speech_text, PracticePhrases.get_speech_text(PracticePhrases.WHAT_IS_YOUR_NAME))


if __name__ == '__main__':
    unittest.main()
