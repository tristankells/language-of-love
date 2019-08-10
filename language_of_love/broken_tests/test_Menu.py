import unittest
from areas.menu import Menu
from session_variables import SessionVariables
from enums import slots
from enums.intents import Intents
from translators.test_translator import TestTranslator


class TestMenu(unittest.TestCase):

    def test_begin_practice_give_correct_response(self):
        session_variables = {
            SessionVariables.AREA: slots.AreaEnum.menu
        }
        response = Menu(Intents.START_PRACTICE, session_variables).get_response()

        # Check the player is in the practice area now
        self.assertEqual(slots.AreaEnum.practice, response.session_variables.area)
        # Check the correct speech text has been received
        self.assertEqual(TestTranslator.Practice.begin, response.speech_text, )

    def test_begin_speed_date_give_correct_response(self):
        session_variables = {
            SessionVariables.AREA: slots.AreaEnum.menu
        }
        response = Menu(Intents.START_SPEED_DATE, session_variables).get_response()

        # Check the player is in the speed date area now
        self.assertEqual(slots.AreaEnum.speed_date, response.session_variables.area)
        # Check the correct speech text has been received
        self.assertEqual(TestTranslator.SpeedDate.begin, response.speech_text)

    def test_bad_intent_give_correct_response(self):
        session_variables = {
            SessionVariables.AREA: slots.AreaEnum.menu
        }
        response = Menu(Intents.ANIMAL_IS, session_variables).get_response()

        # Check the player is in the speed date area now
        self.assertEqual(slots.AreaEnum.menu, response.session_variables.area)
        # Check the correct speech text has been received
        self.assertEqual(TestTranslator.Menu.fallback, response.speech_text)

if __name__ == '__main__':
    unittest.main()
