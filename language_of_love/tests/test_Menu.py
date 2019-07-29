import unittest
from menu import Menu
from session_variables import SessionVariables
import slots
from intents import Intents
from alexa_talk_translator import Translator


class TestMenu(unittest.TestCase):

    def test_begin_practice_give_correct_response(self):
        session_variables = SessionVariables({
            SessionVariables.AREA: slots.AreaEnum.menu
        })
        response = Menu.request_handler(Intents.START_PRACTICE, session_variables)

        # Check the player is in the practice area now
        self.assertTrue(response.session_variables.area is slots.AreaEnum.practice)
        # Check the correct speech text has been received
        self.assertTrue(response.speech_text is Translator.Practice.begin)

    def test_begin_speed_date_give_correct_response(self):
        session_variables = SessionVariables({
            SessionVariables.AREA: slots.AreaEnum.menu
        })
        response = Menu.request_handler(Intents.START_SPEED_DATE, session_variables)

        # Check the player is in the speed date area now
        self.assertTrue(response.session_variables.area is slots.AreaEnum.speed_date)
        # Check the correct speech text has been received
        self.assertTrue(response.speech_text is Translator.SpeedDate.begin)

    def test_bad_intent_give_correct_response(self):
        session_variables = SessionVariables({
            SessionVariables.AREA: slots.AreaEnum.menu
        })
        response = Menu.request_handler(Intents.ANIMAL_IS, session_variables)

        # Check the player is in the speed date area now
        self.assertTrue(response.session_variables.area is slots.AreaEnum.menu)
        # Check the correct speech text has been received
        self.assertTrue(response.speech_text is Translator.Error.bad_option)


if __name__ == '__main__':
    unittest.main()
