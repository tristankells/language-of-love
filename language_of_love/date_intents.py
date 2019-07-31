import json

IntentList = [["QuestionWhereYouFromIntent", "AnswerWhereYouFromIntent"],
              ["QuestionJobIntent", "AnswerMyJobIntent"],
              ["QuestionAnimalsIntent", "AnswerAnimalIntent"]
              ]

ResponseDict = {"QuestionWhereYouFromIntent": "I'm from Columbia",
                "AnswerWhereYouFromIntent": "I love that place",
                "QuestionJobIntent": "I am a doctor, what do you do?",
                "AnswerMyJobIntent": "Great",
                }

def conversations():
    return json.dumps(IntentList), json.dumps(ResponseDict)
