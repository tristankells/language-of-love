from custom_collections.intents import Intents


class Date:
    def __init__(self, date_translator):
        self.date_translator = date_translator

        self.intent_list = [[Intents.QUESTION_NAME, Intents.ANSWER_NAME],
                            [Intents.QUESTION_WHERE_YOU_FROM, Intents.ANSWER_WHERE_YOU_FROM],
                            [Intents.QUESTION_JOB, Intents.ANSWER_JOB],
                            [Intents.QUESTION_ANIMALS, Intents.ANSWER_ANIMALS],
                            [Intents.QUESTION_COLOUR, Intents.ANSWER_COLOUR],
                            [Intents.QUESTION_DAY, Intents.ANSWER_DAY],
                            [Intents.QUESTION_AGE, Intents.ANSWER_AGE],
                            [Intents.QUESTION_BOOK, Intents.ANSWER_BOOK],
                            ]

        self.response_dict = {Intents.QUESTION_NAME: date_translator.question_name,
                              Intents.ANSWER_NAME: date_translator.answer_name,
                              Intents.QUESTION_WHERE_YOU_FROM: date_translator.question_where_you_from,
                              Intents.ANSWER_WHERE_YOU_FROM: date_translator.answer_where_you_from,
                              Intents.QUESTION_JOB: date_translator.question_job,
                              Intents.ANSWER_JOB: date_translator.answer_job,
                              Intents.QUESTION_ANIMALS: date_translator.question_animals,
                              Intents.ANSWER_ANIMALS: date_translator.answer_animals,
                              Intents.QUESTION_COLOUR: date_translator.question_colour,
                              Intents.ANSWER_COLOUR: date_translator.answer_colour,
                              Intents.QUESTION_DAY: date_translator.question_my_day,
                              Intents.ANSWER_DAY: date_translator.answer_my_day,
                              Intents.QUESTION_AGE: date_translator.question_age,
                              Intents.ANSWER_AGE: date_translator.answer_age,
                              Intents.QUESTION_BOOK: date_translator.question_book,
                              Intents.ANSWER_BOOK: date_translator.answer_book
                              }

    def conversations(self):
        return self.intent_list, self.response_dict
