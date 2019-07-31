from alexa_talk_translator import Translator


class PracticePhrases():
    WHAT_IS_YOUR_NAME = "what_is_your_name"
    DO_YOU_LIKE_TO_TRAVEL = "do_you_like_to_travel"
    WHAT_IS_YOUR_JOB = "what_is_your_job"
    EMPTY = "empty"

    def get_speech_text(phrase_key):
        phrases_dict = {
            PracticePhrases.WHAT_IS_YOUR_NAME: Translator.Practice.what_is_your_name,
            PracticePhrases.DO_YOU_LIKE_TO_TRAVEL: Translator.Practice.do_you_like_to_travel,
            PracticePhrases.WHAT_IS_YOUR_JOB: Translator.Practice.what_is_your_job
        }

        return phrases_dict[phrase_key]
