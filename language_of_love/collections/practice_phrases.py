from translators.test_translator import TestTranslator


class PracticePhrases():
    WHAT_IS_YOUR_NAME = "what_is_your_name"
    DO_YOU_LIKE_TO_TRAVEL = "do_you_like_to_travel"
    WHAT_IS_YOUR_JOB = "what_is_your_job"
    EMPTY = "empty"

    def get_speech_text(phrase_key):
        phrases_dict = {
            PracticePhrases.WHAT_IS_YOUR_NAME: TestTranslator.Practice.what_is_your_name,
            PracticePhrases.DO_YOU_LIKE_TO_TRAVEL: TestTranslator.Practice.do_you_like_to_travel,
            PracticePhrases.WHAT_IS_YOUR_JOB: TestTranslator.Practice.what_is_your_job
        }

        return phrases_dict[phrase_key]