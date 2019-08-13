from areas.area import Area
from custom_collections.intents import Intents


class Date(Area):
    speech_text = Area.translator.SpeedDate.fallback

    def question_where:


    def answer_where:

    def wrong_answer:

    intent_dictionary = {
        Intents.QUESTION_WHERE_YOU_FROM: question_where,
        Intents.ANSWER_WHERE_YOU_FROM: answer_where,

    }
