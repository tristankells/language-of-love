import unittest
from language_of_love.language_of_love import LanguageOfLove
from language_of_love.alexa_talk_translator import Translator
from language_of_love.session_variables import SessionVariables
from language_of_love.slots import AreaEnum


class TestLanguageOfLove(unittest.TestCase):
    def test_launch__first_time(self):
        session_variables = SessionVariables({
            SessionVariables.FIRST_TIME: True
        })
        response = LanguageOfLove.launch(session_variables)
        self.assertEqual(response.speech_text, Translator.launch_first_time)

    def test_launch__not_first_time(self):
        session_variables = SessionVariables({
            SessionVariables.FIRST_TIME: False
        })
        response = LanguageOfLove.launch(session_variables)
        self.assertEqual(response.speech_text, Translator.launch)

    def test_my_name_is__in_tutorial(self):
        session_variables = SessionVariables({
            SessionVariables.AREA: AreaEnum.tutorial
        })
        response = LanguageOfLove.Answers.my_name_is(session_variables)
        self.assertEqual(response.speech_text, Translator.Tutorial.answer_to_your_name)

if __name__ == '__main__':
    unittest.main()
