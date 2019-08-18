from custom_collections.slots import Date
from areas.date.date_intents.date_conchita import Conchita
from areas.date.date_intents.date_tessa import Tessa
from areas.date.date_intents.date_enrique import Enrique


def date_picker(date):
    if (date == Date.tessa):
        return Tessa().conversations()
    elif (date == Date.enrique):
        return Enrique().conversations()
    elif (date == Date.conchita):
        return Conchita().conversations()
