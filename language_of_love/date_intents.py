import json

IntentList = [["QuestionWhereYouFromIntent", "AnswerWhereYouFromIntent"],
              ["QuestionJobIntent", "AnswerMyJobIntent"]]

IntentDict = {
    "QuestionWhereYouFromIntent": {"QuestionWhereYouFromIntent": "I'm from Columbia",
                                   "AnswerWhereYouFromIntent": "I love that place"},
    "QuestionJobIntent": {"QuestionJobIntent": "I am a doctor, what do you do?",
                          "AnswerMyJobIntent": "Great"}}


def conversations():
    return json.dumps(IntentList), json.dumps(IntentDict)
