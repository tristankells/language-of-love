import unittest
from session_variables import SessionVariables
import slots
from intents import Intents
from translators.test_translator import TestTranslator
from areas.practice import Practice
from practice_phrases import PracticePhrases


class TestPractice(unittest.TestCase):

    def test_practice_if_player_ask_to_repeat_they_get_the_same_message(self):
        session_variables = {
            SessionVariables.conversation: "None",
            SessionVariables.place: 0,
            SessionVariables.AREA: slots.AreaEnum.practice
        }
        response = Practice(Intents.REPEAT, session_variables).get_response()

        # Confirm player still in tutorial
        self.assertEqual(response.session_variables.area, slots.AreaEnum.practice)
        # Confirm player out of repeat loop
        self.assertEqual(response.session_variables.tutorial_repeat_or_new, False)
        # Confirm player gets the same message
        self.assertEqual(response.speech_text, PracticePhrases.get_speech_text(PracticePhrases.WHAT_IS_YOUR_NAME))


if __name__ == '__main__':
    unittest.main()
