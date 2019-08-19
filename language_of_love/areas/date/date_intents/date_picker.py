from custom_collections.slots import DateEnum
from areas.date.date_intents.date_conchita import Conchita
from areas.date.date_intents.date_tessa import Tessa
from areas.date.date_intents.date_enrique import Enrique


def date_picker(date):
    if (date == DateEnum.tessa):
        return Tessa().conversations()
    elif (date == DateEnum.enrique):
        return Enrique().conversations()
    elif (date == DateEnum.conchita):
        return Conchita().conversations()
