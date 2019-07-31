import unittest
from tutorial import Tutorial
from session_variables import SessionVariables
import slots
from intents import Intents
from alexa_talk_translator import Translator
from practice_phrase import PracticePhrases


class TestSessionVariables(unittest.TestCase):
    def test_session_variables_does_not_contain_None_values(self):
        variables = {

        }
        session_variables = SessionVariables(variables)

        self.assertIsNotNone(session_variables.area, msg="Area should never be null")
        self.assertIsNotNone(session_variables.name, msg="Name should never be null")
        self.assertIsNotNone(session_variables.first_time, msg="First should never be null")
        self.assertIsNotNone(session_variables.tutorial_repeat_or_new,
                             msg="Tutorial repeat or null should never be null")
        self.assertIsNotNone(session_variables.current_tutorial_phrase, msg="Tutorial phrases should never be null")
        self.assertIsNotNone(session_variables.gender_preference, msg="Gender preferences should never be null")

    def test_get_function_does_not_return_None_values(self):
        session_variables = SessionVariables({

        })

        session_variables = session_variables.get()
        self.assertIsNotNone(session_variables['area'], msg="Area should never be null")
        self.assertIsNotNone(session_variables['name'], msg="Name should never be null")
        self.assertIsNotNone(session_variables['first_time'], msg="First should never be null")
        self.assertIsNotNone(session_variables['tutorial_repeat_or_new'],
                             msg="Tutorial repeat or null should never be null")
        self.assertIsNotNone(session_variables['current_tutorial_phrase'], msg="Tutorial phrases should never be null")
        self.assertIsNotNone(session_variables['gender_preference'], msg="Gender preferences should never be null")

    def test_get_function_returns_same_as_passed_values(self):
        original_variables = {
            SessionVariables.AREA: slots.AreaEnum.speed_date,
            SessionVariables.NAME: "Test Name",
            SessionVariables.FIRST_TIME: False,
            SessionVariables.TUTORIAL_REPEAT_OR_NEW: False,
            SessionVariables.CURRENT_TUTORIAL_PHRASE: PracticePhrases.WHAT_IS_YOUR_NAME,
            SessionVariables.GENDER_PREFERENCE: slots.GenderPreferenceEnum.both
        }

        session_variables = SessionVariables(original_variables)

        get_session_variables = session_variables.get()
        self.assertEqual(original_variables['area'], get_session_variables['area'])
        self.assertEqual(original_variables['name'], get_session_variables['name'])
        self.assertEqual(original_variables['first_time'], get_session_variables['first_time'])
        self.assertEqual(original_variables['tutorial_repeat_or_new'], get_session_variables['tutorial_repeat_or_new'])
        self.assertEqual(original_variables['current_tutorial_phrase'],
                         get_session_variables['current_tutorial_phrase'])
        self.assertEqual(original_variables['gender_preference'], get_session_variables['gender_preference'])

    def test_get_initial_returns_default_values(self):
        # TODO: Add test for the get_init function
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
