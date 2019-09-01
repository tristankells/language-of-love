from translators.production_translator import Translator


class PracticePhrases():
    WHAT_IS_YOUR_NAME = "what_is_your_name"
    DO_YOU_LIKE_TO_TRAVEL = "do_you_like_to_travel"
    WHAT_IS_YOUR_JOB = "what_is_your_job"
    WHERE_ARE_YOU_FROM = "where_are_you_from"
    WHAT_IS_YOUR_FAVOURITE_ANIMAL = 'what_is_your_favourite_animal'
    WHAT_IS_YOUR_FAVOURITE_COLOUR = 'what_is_your_favourite_colour'
    HOW_IS_YOUR_DAY = 'how_is_your_day'
    HOW_OLD_ARE_YOU = 'how_old_are_you'
    WHAT_IS_YOUR_FAVOURITE_BOOK = 'what_is_your_favourite_book'

    EMPTY = "empty"

    def get_speech_text(phrase_key):
        phrases_dict = {
            PracticePhrases.WHAT_IS_YOUR_NAME: Translator.Practice.what_is_your_name,
            PracticePhrases.DO_YOU_LIKE_TO_TRAVEL: Translator.Practice.do_you_like_to_travel,
            PracticePhrases.WHAT_IS_YOUR_JOB: Translator.Practice.what_is_your_job,
            PracticePhrases.WHERE_ARE_YOU_FROM: Translator.Practice.where_are_you_from,
            PracticePhrases.WHAT_IS_YOUR_FAVOURITE_ANIMAL: Translator.Practice.what_is_your_favourite_animal,
            PracticePhrases.WHAT_IS_YOUR_FAVOURITE_COLOUR: Translator.Practice.what_is_your_favourite_colour,
            PracticePhrases.HOW_IS_YOUR_DAY: Translator.Practice.how_is_your_day,
            PracticePhrases.HOW_OLD_ARE_YOU: Translator.Practice.how_old_are_you,
            PracticePhrases.WHAT_IS_YOUR_FAVOURITE_BOOK: Translator.Practice.what_is_your_favourite_book,
        }

        return phrases_dict[phrase_key]
