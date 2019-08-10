import unittest
from session_variables import SessionVariables
from collections import slots
from collections.intents import Intents
from translators.test_translator import TestTranslator
from areas.practice import Practice
from collections.practice_phrases import PracticePhrases


class TestPractice(unittest.TestCase):

    def test_practice_if_player_ask_to_repeat_they_get_the_same_message(self):
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

    def test_practice_if_player_ask_for_new_phrase_they_get_a_different_message(self):
        session_variables = {
            SessionVariables.CURRENT_PRACTICE_PHRASE: PracticePhrases.WHAT_IS_YOUR_NAME,
            SessionVariables.PRACTICE_REPEAT_OR_NEW: True,
            SessionVariables.AREA: slots.AreaEnum.practice
        }
        response = Practice(Intents.NEW_PRACTICE_PHRASE, session_variables).get_response()

        # Confirm player still in tutorial
        self.assertEqual(slots.AreaEnum.practice, response.session_variables.area)
        # Confirm player out of repeat loop
        self.assertEqual(False, response.session_variables.tutorial_repeat_or_new)
        # Confirm player gets a different message
        self.assertNotEqual(PracticePhrases.get_speech_text(PracticePhrases.WHAT_IS_YOUR_NAME), response.speech_text)

    def test_practice_player_leaves_loop_if_they_cancel_practice(self):
        session_variables = {
            SessionVariables.CURRENT_PRACTICE_PHRASE: PracticePhrases.WHAT_IS_YOUR_NAME,
            SessionVariables.PRACTICE_REPEAT_OR_NEW: True,
            SessionVariables.AREA: slots.AreaEnum.practice
        }

        response = Practice(Intents.CANCEL, session_variables).get_response()
        # Confirm player is in the menu area
        self.assertEqual(response.session_variables.area, slots.AreaEnum.menu)
        # Confirm player out of repeat loop
        self.assertEqual(response.session_variables.tutorial_repeat_or_new, False)
        # Confirm player gets the cancel tutorial message
        self.assertEqual(response.speech_text, TestTranslator.Practice.end + " " + TestTranslator.Menu.options)


if __name__ == '__main__':
    unittest.main()
