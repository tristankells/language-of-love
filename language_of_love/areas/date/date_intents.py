import json
from custom_collections.audio import Audio
from custom_collections.intents import Intents

IntentList = [[Intents.QUESTION_WHERE_YOU_FROM, Intents.ANSWER_WHERE_YOU_FROM],
              [Intents.QUESTION_JOB, Intents.ANSWER_MY_JOB],
              [Intents.QUESTION_ANIMALS, "AnswerAnimalIntent"],
              [Intents.QUESTION_FAVOURITE_COLOUR, Intents.ANSWER_FAVOURITE_COLOUR]
              ]

ResponseDict = {Intents.QUESTION_WHERE_YOU_FROM: Audio.Q_tessa_i_am_from_Wellington + Audio.Q_tessa_where_are_you_from,
                Intents.ANSWER_WHERE_YOU_FROM: "I love that place",
                Intents.QUESTION_JOB: Audio.Q_tessa_I_am_lawyer + Audio.Q_tessa_What_is_your_job,
                Intents.ANSWER_MY_JOB: "Great",
                Intents.QUESTION_ANIMALS: "My favourite animal is a giraffe, what's yours?",
                "AnswerAnimalIntent": "Cool animal",
                Intents.QUESTION_FAVOURITE_COLOUR: Audio.A_tessa_my_favourite_colour_is_blue + Audio.Q_tessa_whats_your_favourite_colour,
                Intents.ANSWER_FAVOURITE_COLOUR: "Great"
                }

def conversations():
    return json.dumps(IntentList), json.dumps(ResponseDict)