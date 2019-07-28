class Response:
    def __init__(self, speech_input, reprompt="repeat yourself", session_variables=None):
        # if speech_text is not null
        if (speech_input is not None):

            # and if speech_text is an instance of string
            if (isinstance(speech_input, str)):
                self.speech_text = speech_input  # then speech_text is that string

            # or if speech text is an instance of list
            elif (isinstance(speech_input, list)):
                self.speech_text_list = speech_input  # then speech_text_list is populated with list
                self.speech_text = ""
                for text in speech_input:
                    self.speech_text = self.speech_text + text  # and speech text is list items combined

        # else if speech text is null
        elif (speech_input is None):
            self.speech_text = "Error logged"

        self.reprompt = reprompt
        self.session_variables = session_variables
