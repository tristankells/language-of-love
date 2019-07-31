import unittest
from love import LanguageOfLove
from alexa_talk_translator import Translator
from session_variables import SessionVariables
from slots import AreaEnum

class TestLanguageOfLove(unittest.TestCase):
    """
    Test class for language of love class
    """

    def setUp(self):
        LanguageOfLove.speech_text = []

    # Answers handler tests

    def test_my_name_is__in_tutorial(self):
        session_variables = SessionVariables({
            SessionVariables.AREA: AreaEnum.tutorial.value
        })

        response = LanguageOfLove.Answers.my_name_is(session_variables)

        self.assertEqual(response.speech_text, Translator.Tutorial.answer_to_your_name)

    # Questions handler tests
    def test_where_are__in_tutorial(self):
        session_variables = SessionVariables({})

        response = LanguageOfLove.Questions.where_are_you_from(session_variables)

        self.assertEqual(response.speech_text, Translator.Tutorial.answer_to_question_where_are_you_from)

    # Test practice handlers
    def test_start_practice(self):
        session_variables = SessionVariables({})

        response = LanguageOfLove.Practice.start(session_variables)

        self.assertEqual(response.speech_text_list[0], Translator.Practice.begin,
                         msg="Assert that the first message is the practice begin message")
        self.assertIsNotNone(response.speech_text_list[1],
                             msg="Assert that a 'Begin Practice' message has been added to the list")
        self.assertTrue(isinstance(response.speech_text, str),
                        msg="Assert that speech text is still a string in the instance that mutiple message are being combined (Consider moving test functionaility to sessions varaibles test)")


if __name__ == '__main__':
    unittest.main()
