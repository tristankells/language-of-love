import unittest
from menu import Menu
from session_variables import SessionVariables
import slots
from intents import Intents
from alexa_talk_translator import Translator
from practice import Practice
from practice_phrase import PracticePhrases


class TestPractice(unittest.TestCase):

    def test_practice_if_player_ask_to_repeat_they_get_the_same_message(self):
        session_variables = SessionVariables({
            SessionVariables.CURRENT_TUTORIAL_PHRASE: PracticePhrases.WHAT_IS_YOUR_NAME,
            SessionVariables.TUTORIAL_REPEAT_OR_NEW: True,
            SessionVariables.AREA: slots.AreaEnum.practice
        })
        response = Practice(Intents.REPEAT, session_variables)

        # Confirm player still in tutorial
        self.assertEqual(response.session_variables.area, slots.AreaEnum.practice)
        # Confirm player out of repeat loop
        self.assertEqual(response.session_variables.tutorial_repeat_or_new, False)
        # Confirm player gets the same message
        self.assertEqual(response.speech_text, PracticePhrases.get_speech_text(PracticePhrases.WHAT_IS_YOUR_NAME))

    def test_practice_if_player_ask_to_repeat_they_get_a_different_message(self):
        session_variables = SessionVariables({
            SessionVariables.CURRENT_TUTORIAL_PHRASE: PracticePhrases.WHAT_IS_YOUR_NAME,
            SessionVariables.TUTORIAL_REPEAT_OR_NEW: True,
            SessionVariables.AREA: slots.AreaEnum.practice
        })
        response = Practice(Intents.NEW_PHRASE, session_variables)

        # Confirm player still in tutorial
        self.assertEqual(response.session_variables.area, slots.AreaEnum.practice)
        # Confirm player out of repeat loop
        self.assertEqual(response.session_variables.tutorial_repeat_or_new, False)
        # Confirm player gets a different message
        self.assertNotEqual(response.speech_text, PracticePhrases.get_speech_text(PracticePhrases.WHAT_IS_YOUR_NAME))

    def test_practice_player_leaves_loop_if_they_cancel_practice(self):
        session_variables = SessionVariables({
            SessionVariables.CURRENT_TUTORIAL_PHRASE: PracticePhrases.WHAT_IS_YOUR_NAME,
            SessionVariables.TUTORIAL_REPEAT_OR_NEW: True,
            SessionVariables.AREA: slots.AreaEnum.practice
        })

        response = Practice(Intents.CANCEL, session_variables)
        # Confirm player is in the menu area
        self.assertEqual(response.session_variables.area, slots.AreaEnum.menu)
        # Confirm player out of repeat loop
        self.assertEqual(response.session_variables.tutorial_repeat_or_new, False)
        # Confirm player gets the cancel tutorial message
        self.assertEqual(response.speech_text, Translator.Practice.end)


if __name__ == '__main__':
    unittest.main()
