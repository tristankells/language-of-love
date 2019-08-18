import json
from typing import Dict
from custom_collections.intents import Intents
from translators.production_translator import Translator


class Conchita():
    conchita = Translator().Date().Conchita()

    intent_list = [[Intents.QUESTION_WHERE_YOU_FROM, Intents.ANSWER_WHERE_YOU_FROM],
                   [Intents.QUESTION_JOB, Intents.ANSWER_MY_JOB],
                   [Intents.QUESTION_ANIMALS, "AnswerAnimalIntent"],
                   [Intents.QUESTION_FAVOURITE_COLOUR, Intents.ANSWER_FAVOURITE_COLOUR]
                   ]

    response_dict: Dict[str, str] = {Intents.QUESTION_WHERE_YOU_FROM: conchita.question_where_you_from,
                                     Intents.ANSWER_WHERE_YOU_FROM: conchita.answer_where_you_from,
                                     Intents.QUESTION_JOB: conchita.question_job,
                                     Intents.ANSWER_MY_JOB: conchita.answer_job,
                                     Intents.QUESTION_ANIMALS: conchita.question_animals,
                                     "AnswerAnimalIntent": conchita.answer_animals,
                                     Intents.QUESTION_FAVOURITE_COLOUR: conchita.question_favourite_colour,
                                     Intents.ANSWER_FAVOURITE_COLOUR: conchita.answer_favourite_colour
                                     }

    def conversations(self):
        return json.dumps(self.intent_list), json.dumps(self.response_dict)
