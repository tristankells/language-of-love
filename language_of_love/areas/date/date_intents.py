import json
from collections.audio import Audio
from collections.intents import Intents

IntentList = [[Intents.QUESTION_WHERE_YOU_FROM, Intents.ANSWER_WHERE_YOU_FROM],
              [Intents.QUESTION_JOB, Intents.ANSWER_MY_JOB],
              [Intents.QUESTION_ANIMALS, "AnswerAnimalIntent"]
              ]

ResponseDict = {Intents.QUESTION_WHERE_YOU_FROM: Audio.Q_tessa_i_am_from_Wellington + Audio.Q_tessa_where_are_you_from,
                Intents.ANSWER_WHERE_YOU_FROM: "I love that place",
                Intents.QUESTION_JOB: Audio.Q_tessa_I_am_lawyer + Audio.Q_tessa_What_is_your_job,
                Intents.ANSWER_MY_JOB: "Great",
                Intents.QUESTION_ANIMALS: "My favourite animal is a giraffe, what's yours?",
                "AnswerAnimalIntent": "Cool animal",
                }

def conversations():
    return json.dumps(IntentList), json.dumps(ResponseDict)