from areas.area import Area
from custom_collections.intents import Intents


class Date(Area):
    speech_text = Area.translator.SpeedDate.fallback

    def question_where:

    def answer_where:

    intent_dictionary = {
        Intents.QUESTION_WHERE_YOU_FROM: QUESTION_WHERE_YOU_FROM,
        Intents.ANSWER_WHERE_YOU_FROM: repeat_phrase,
        Intents.CANCEL: end_tutorial,
        Intents.LEAVE_AREA: end_tutorial
    }
