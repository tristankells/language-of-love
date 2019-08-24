from translators.production_translator import Translator
from response import Response
from session_variables import SessionVariables


class Area():
    intent_dictionary = None  # Each class Area implementation will need to define a dictionary of intents the implementation has a response too
    player_intent = None  # Store the intent, "StartPracticeIntent" for example, triggered by the player
    session_variables = None  # Store the lambda session attributes
    reprompt = None
    translator = Translator()
    speech_text = translator.General.fallback  # Store the Alexa speech reply for the player. Store the default fallback reply if none of the area intents are triggered

    def __init__(self, player_intent, session_variables, translator=None):
        self.player_intent = player_intent
        self.session_variables = SessionVariables(session_variables)
        if (translator is not None):
            self.translator = translator

    def get_response(self):
        if self.player_intent in self.intent_dictionary:
            self.intent_dictionary[self.player_intent](self)

        return Response(self.speech_text, self.reprompt, self.session_variables)
