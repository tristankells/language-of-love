import json
from audio import Audio

IntentList = [["QuestionWhereYouFromIntent", "AnswerWhereYouFromIntent"],
              ["QuestionJobIntent", "AnswerMyJobIntent"],
              ["QuestionAnimalsIntent", "AnswerAnimalIntent"]
              ]

ResponseDict = {"QuestionWhereYouFromIntent": Audio.Q_tessa_i_am_from_Wellington + Audio.Q_tessa_where_are_you_from,
                "AnswerWhereYouFromIntent": "I love that place",
                "QuestionJobIntent": Audio.Q_tessa_I_am_lawyer + Audio.Q_tessa_What_is_your_job,
                "AnswerMyJobIntent": "Great",
                "QuestionAnimalsIntent": "My favourite animal is a giraffe, what's yours?",
                "AnswerAnimalIntent": "Cool animal"
                }

def conversations():
    return json.dumps(IntentList), json.dumps(ResponseDict)