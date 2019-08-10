from collections.slots import AreaEnum
from collections.intents import Intents
from areas.area import Area


class Introduction(Area):
    speech_text = Area.translator.Introduction.fallback

    def my_name_is(self):
        """
        Handlers when the player responds with there name
        """
        self.speech_text = self.translator.Introduction.answer_to_your_name
        self.session_variables.area = AreaEnum.menu

    intent_dictionary = {
        Intents.ANSWER_NAME: my_name_is
    }
