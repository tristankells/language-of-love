import json
from typing import Dict
from custom_collections.intents import Intents
from translators.production_translator import Translator


class Enrique():
    enrique = Translator().Date().Enrique()

    intent_list = [[Intents.QUESTION_WHERE_YOU_FROM, Intents.ANSWER_WHERE_YOU_FROM],
                   [Intents.QUESTION_JOB, Intents.ANSWER_MY_JOB],
                   [Intents.QUESTION_ANIMALS, "AnswerAnimalIntent"],
                   [Intents.QUESTION_FAVOURITE_COLOUR, Intents.ANSWER_FAVOURITE_COLOUR]
                   ]

    response_dict: Dict[str, str] = {Intents.QUESTION_WHERE_YOU_FROM: enrique.question_where_you_from,
                                     Intents.ANSWER_WHERE_YOU_FROM: enrique.answer_where_you_from,
                                     Intents.QUESTION_JOB: enrique.question_job,
                                     Intents.ANSWER_MY_JOB: enrique.answer_job,
                                     Intents.QUESTION_ANIMALS: enrique.question_animals,
                                     "AnswerAnimalIntent": enrique.answer_animals,
                                     Intents.QUESTION_FAVOURITE_COLOUR: enrique.question_favourite_colour,
                                     Intents.ANSWER_FAVOURITE_COLOUR: enrique.answer_favourite_colour
                                     }

    def conversations(self):
        return json.dumps(self.intent_list), json.dumps(self.response_dict)
