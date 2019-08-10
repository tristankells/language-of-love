import unittest
from areas.introduction import Introduction
from session_variables import SessionVariables
from collections import slots
from collections.intents import Intents
from translators.test_translator import TestTranslator


class TestIntroduction(unittest.TestCase):
    # Introduction -> MyNameIsIntent
    def test_my_name_is_returns_the_correct_speech_text(self):
        session_variables = {
            SessionVariables.AREA: slots.AreaEnum.introduction
        }
        response = Introduction(Intents.ANSWER_NAME, session_variables).get_response()

        self.assertEqual(response.speech_text, TestTranslator.Introduction.answer_to_your_name)

    # Introduction -> Anything else
    def test_non_introduction_intent_receives_fallback_message(self):
        session_variables = {
            SessionVariables.AREA: slots.AreaEnum.introduction
        }

        response = Introduction(Intents.ANIMAL_IS, session_variables).get_response()

        self.assertEqual(response.speech_text, TestTranslator.Introduction.fallback)


if __name__ == '__main__':
    unittest.main()
