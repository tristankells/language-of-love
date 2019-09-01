from areas.area import Area
from custom_collections.slots import DateEnum
from response import Response
from areas.date.date_intents.date_helper import date_picker
from custom_collections import slots
from translators.production_translator import Translator

ROUNDS_PER_DATE = 3
BAD_RESPONSE_PER_DATE = 3 # Consider not changing this unless you change the error_response to accommodate


class Date(Area):
    def try_start_conversation(self):
        """
        Handler for when the player in a date will try to ask a question / start a conversation
        """
        for index in range(0, len(self.intent_list)):  # Loop through list of accepted question/answer intents
            if self.intent_list[index][0] == self.player_intent:  # If intent == in list of accepted questions
                self.ask_question(slots.ConversationEnum(index))  # Ask the question
                return

        self.conversation_error()  # If the intent was not in the list of accepted questions, then player has made a mistake

    def try_continue_conversation(self):
        """
        Handler for when the player in a date will try to answer a question / continue a conversation
        """
        if self.intent_list[self.session_variables.conversation.value][1] == self.player_intent:
            self.answer_question()
        else:
            self.conversation_error()
        self.session_variables.date_round += 1

        if self.session_variables.date_round >= ROUNDS_PER_DATE:
            self.finish_date()

    def ask_question(self, question):
        self.session_variables.conversation = slots.ConversationEnum(question)
        self.speech_text = self.response_dict[self.player_intent]

    def answer_question(self):
        self.session_variables.conversation = slots.ConversationEnum.nothing
        self.speech_text = Translator.Date.point + self.response_dict[self.player_intent]
        self.session_variables.date_score += 1

    def conversation_error(self):
        self.session_variables.conversation = slots.ConversationEnum.nothing
        self.session_variables.date_bad_response_count += 1
        self.speech_text = Translator.Date.crickets +  self.error_response(self.session_variables.date_bad_response_count)
        if self.session_variables.date_bad_response_count >= BAD_RESPONSE_PER_DATE:
            self.finish_date()

    def finish_date(self):
        self.speech_text += self.translator.Date.finish.format(self.session_variables.date_score)

        self.session_variables.date_round = self.session_variables.date_bad_response_count = self.session_variables.date_score = 0
        self.session_variables.number_of_dates += 1
        self.session_variables.date = self.get_next_date(self.session_variables.date)


    @staticmethod
    def get_next_date(date):
        if date == DateEnum.conchita:
            date = DateEnum.enrique

        elif date == DateEnum.enrique:
            date = DateEnum.conchita

        return date

    @staticmethod
    def error_response(bad_responses):
        error_audio_dictionary = {
            1: Translator.Date.Error.first_mistake,
            2: Translator.Date.Error.second_mistake,
            3: Translator.Date.Error.third_mistake
        }
        return error_audio_dictionary.get(bad_responses)

    def get_response(self):
        self.intent_list, self.response_dict = date_picker(self.session_variables.date)

        if self.session_variables.conversation == slots.ConversationEnum.nothing:
            self.try_start_conversation()
        else:
            self.try_continue_conversation()

        return Response(self.speech_text, self.reprompt, self.session_variables)
