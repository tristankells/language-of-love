import unittest
from language_of_love.language_of_love import LanguageOfLove
from language_of_love.alexa_talk_translator import Translator
from language_of_love.session_variables import SessionVariables
from language_of_love.slots import AreaEnum


class TestLanguageOfLove(unittest.TestCase):
    def test_launch(self):
        self.assertFalse(False)

    def test_launch_two(self):
        self.assertFalse(False)

    def test_myNameIs_in_tutorial(self):
        session_variables = SessionVariables({
            "area": AreaEnum.tutorial
        })

        response = LanguageOfLove.Answers.my_name_is(session_variables)
        self.assertEqual(response.speech_text, Translator.Tutorial.answer_to_your_name)

if __name__ == '__main__':
    unittest.main()
