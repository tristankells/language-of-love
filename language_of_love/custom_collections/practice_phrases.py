from translators.production_translator import Translator


class PracticePhrases():
    WHAT_IS_YOUR_NAME = "what_is_your_name"
    DO_YOU_LIKE_TO_TRAVEL = "do_you_like_to_travel"
    WHAT_IS_YOUR_JOB = "what_is_your_job"
    WHERE_ARE_YOU_FROM = "where_are_you_from"
    WHAT_IS_YOU_FAVOURITE_ANIMAL = 'what_is_you_favourite_animal'
    WHAT_IS_YOUR_FAVOURITE_COLOUR = 'what_is_your_favourite_colour'
    HOW_IS_YOU_DAY = 'how_is_you_day'
    WHAT_IS_YOU_AGE = 'what_is_you_age'
    WHAT_IS_YOU_FAVOURITE_BOOK = 'what_is_you_favourite_book'

    EMPTY = "empty"

    def get_speech_text(phrase_key):
        phrases_dict = {
            PracticePhrases.WHAT_IS_YOUR_NAME: Translator.Practice.what_is_your_name,
            PracticePhrases.DO_YOU_LIKE_TO_TRAVEL: Translator.Practice.do_you_like_to_travel,
            PracticePhrases.WHAT_IS_YOUR_JOB: Translator.Practice.what_is_your_job,

            PracticePhrases.WHERE_ARE_YOU_FROM: Translator.Practice.what_is_your_job,
            PracticePhrases.WHAT_IS_YOU_FAVOURITE_ANIMAL: Translator.Practice.what_is_your_job,
            PracticePhrases.WHAT_IS_YOUR_FAVOURITE_COLOUR: Translator.Practice.what_is_your_job,
            PracticePhrases.HOW_IS_YOU_DAY: Translator.Practice.what_is_your_job,
            PracticePhrases.WHAT_IS_YOU_AGE: Translator.Practice.what_is_your_job,
            PracticePhrases.WHAT_IS_YOU_FAVOURITE_BOOK: Translator.Practice.what_is_your_job,
        }

        return phrases_dict[phrase_key]
