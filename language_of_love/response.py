class Response:
    def __init__(self, speech_text, reprompt="repeat yourself"):
        self.speech_text = speech_text if speech_text is not None else "Error logged"
        self.reprompt = reprompt
