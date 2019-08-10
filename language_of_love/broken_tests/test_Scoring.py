import unittest
from areas.menu import Menu
from session_variables import SessionVariables
from enums import slots
from enums.intents import Intents
from translators.test_translator import TestTranslator


class TestMenu(unittest.TestCase):

    def test_player_score_goes_up(self):
        session_variables = {
            SessionVariables.AREA: slots.AreaEnum.speed_date,

        }
        response = Menu(Intents.START_PRACTICE, session_variables).get_response()

        # Check the player is in the practice area now
        self.assertEqual(slots.AreaEnum.practice, response.session_variables.area)
        # Check the correct speech text has been received
        self.assertEqual(TestTranslator.Practice.begin, response.speech_text, )


if __name__ == '__main__':
    unittest.main()
