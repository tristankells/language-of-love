from custom_collections.slots import DateEnum
from translators.production_translator import Translator
from areas.date.date_intents.date import Date

def date_picker(date):
    if date == DateEnum.enrique:
        return Date(Translator.Date.Enrique).conversations()
    elif date == DateEnum.conchita:
        return Date(Translator.Date.Conchita).conversations()
