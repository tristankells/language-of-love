import json
from audio import Audio

IntentList = [["QuestionWhereYouFromIntent", "AnswerWhereYouFromIntent"],
              ["QuestionJobIntent", "AnswerMyJobIntent"],
              ["QuestionAnimalsIntent", "AnswerAnimalIntent"]
              ]

ResponseDict = {"QuestionWhereYouFromIntent": Audio.Q_tessa_i_am_from_Wellington,
                "AnswerWhereYouFromIntent": "I love that place",
                "QuestionJobIntent": "I am a doctor, what do you do?",
                "AnswerMyJobIntent": "Great",
                }

def conversations():
    return json.dumps(IntentList), json.dumps(ResponseDict)
