from areas.area import Area
from custom_collections.intents import Intents


class Date(Area):
    speech_text = Area.translator.SpeedDate.fallback

    intent_dictionary = {
        Intents.NEW_PRACTICE_PHRASE: new_phrase,
        Intents.REPEAT_PRACTICE_PHRASE: repeat_phrase,
        Intents.CANCEL: end_tutorial,
        Intents.LEAVE_AREA: end_tutorial
    }
