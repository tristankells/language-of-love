import unittest
from session_variables import SessionVariables
from collections import slots
from collections.practice_phrases import PracticePhrases


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
        self.assertIsNotNone(session_variables.current_practice_phrase, msg="Tutorial phrases should never be null")
        self.assertIsNotNone(session_variables.gender_preference, msg="Gender preferences should never be null")

    def test_get_function_does_not_return_None_values(self):
        session_variables = SessionVariables({

        })

        session_variables = session_variables.get_json()
        self.assertIsNotNone(session_variables[SessionVariables.AREA], msg="Area should never be null")
        self.assertIsNotNone(session_variables[SessionVariables.NAME], msg="Name should never be null")
        self.assertIsNotNone(session_variables[SessionVariables.FIRST_TIME], msg="First should never be null")
        self.assertIsNotNone(session_variables[SessionVariables.PRACTICE_REPEAT_OR_NEW],
                             msg="Tutorial repeat or null should never be null")
        self.assertIsNotNone(session_variables[SessionVariables.CURRENT_PRACTICE_PHRASE],
                             msg="Tutorial phrases should never be null")
        self.assertIsNotNone(session_variables[SessionVariables.GENDER_PREFERENCE],
                             msg="Gender preferences should never be null")

    def test_get_function_returns_same_as_passed_values(self):
        original_variables = {
            SessionVariables.AREA: slots.AreaEnum.speed_date,
            SessionVariables.NAME: "Test Name",
            SessionVariables.FIRST_TIME: False,
            SessionVariables.PRACTICE_REPEAT_OR_NEW: False,
            SessionVariables.CURRENT_PRACTICE_PHRASE: PracticePhrases.WHAT_IS_YOUR_NAME,
            SessionVariables.GENDER_PREFERENCE: slots.GenderPreferenceEnum.both
        }

        session_variables = SessionVariables(original_variables)

        get_session_variables = session_variables.get_json()
        self.assertEqual(original_variables[SessionVariables.AREA], get_session_variables[SessionVariables.AREA])
        self.assertEqual(original_variables[SessionVariables.NAME], get_session_variables[SessionVariables.NAME])
        self.assertEqual(original_variables[SessionVariables.FIRST_TIME],
                         get_session_variables[SessionVariables.FIRST_TIME])
        self.assertEqual(original_variables[SessionVariables.PRACTICE_REPEAT_OR_NEW],
                         get_session_variables[SessionVariables.PRACTICE_REPEAT_OR_NEW])
        self.assertEqual(original_variables[SessionVariables.CURRENT_PRACTICE_PHRASE],
                         get_session_variables[SessionVariables.CURRENT_PRACTICE_PHRASE])
        self.assertEqual(original_variables[SessionVariables.GENDER_PREFERENCE],
                         get_session_variables[SessionVariables.GENDER_PREFERENCE])

    def test_get_initial_returns_default_values(self):
        # TODO: Add test for the get_init function
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
