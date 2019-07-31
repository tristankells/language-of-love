import unittest
from areas.tutorial import Tutorial
from session_variables import SessionVariables
import slots
from intents import Intents
from alexa_talk_translator import Translator


class TestTutorial(unittest.TestCase):
    # Tutorial -> MyNameIsIntent
    def test_my_name_is_returns_the_correct_speech_text(self):
        session_variables = SessionVariables({
            SessionVariables.AREA: slots.AreaEnum.introduction
        })
        response = Tutorial.request_handler(Intents.ANSWER_NAME, session_variables)
        self.assertTrue(response.speech_text is Translator.Intro.answer_to_your_name)

    # Tutorial -> WhereAreYouFromIntent
    def test_where_are_you_from_returns_the_correct_speech_text(self):
        session_variables = SessionVariables({
            SessionVariables.AREA: slots.AreaEnum.introduction
        })
        response = Tutorial.request_handler(Intents.QUESTION_WHERE_YOU_FROM, session_variables)
        self.assertTrue(response.speech_text is Translator.Intro.answer_to_question_where_are_you_from)

    def test_where_are_you_from_ends_tutorial(self):
        session_variables = SessionVariables({
            SessionVariables.AREA: slots.AreaEnum.introduction
        })
        response = Tutorial.request_handler(Intents.QUESTION_WHERE_YOU_FROM, session_variables)
        self.assertTrue(response.session_variables.area is slots.AreaEnum.menu)

    # Tutorial -> Anything else
    def test_non_tutorial_intent_receives_error_message(self):
        session_variables = SessionVariables({
            SessionVariables.AREA: slots.AreaEnum.introduction
        })
        response = Tutorial.request_handler(Intents.ANIMAL_IS, session_variables)
        self.assertTrue(response.speech_text is Translator.Intro.error)


if __name__ == '__main__':
    unittest.main()
