# -*- coding: utf-8 -*-

# This is a High Low Guess game Alexa Skill.
# The skill serves as a simple sample on how to use the
# persistence attributes and persistence adapter features in the SDK.
import random
import logging

from ask_sdk.standard import StandardSkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name, get_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard
from session_variables import SessionVariables
from custom_collections.slots import AreaEnum, DateEnum
from areas.introduction import Introduction
from areas.menu import Menu
from areas.practice import Practice
from custom_collections.audio import Audio
from custom_collections.intents import Intents

import json
from love import LanguageOfLove
from areas.date.date_intents.date_helper import date_picker
from areas.date.date_handler import can_handle_date

SKILL_NAME = 'Language Of Love'
sb = StandardSkillBuilder(table_name="Language-Of-Love", auto_create_table=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

<< << << < HEAD
DATE_ROUNDS = 3

== == == =
>> >> >> > parent
of
463
ea3b...Removed
the
unused
place
variable
@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """
    Handler for Skill Launch.
    """
    # type: (HandlerInput) -> Response

    state_variables = handler_input.attributes_manager.persistent_attributes

    if not state_variables:
        state_variables = SessionVariables.get_initial_dict()

    handler_input.attributes_manager.session_attributes = state_variables

    response = LanguageOfLove.launch(SessionVariables(state_variables))

    handler_input.response_builder.speak(response.speech_text).ask(response.reprompt)

    return handler_input.response_builder.response

def player_area(handler_input):
    """
    Takes the handler_input and returns an AreaEnum representing what area the play is in
    :param handler_input:
    :return: a AreaEnum representing the players current area
    """
    if SessionVariables.AREA in handler_input.attributes_manager.session_attributes:
        session_variables = handler_input.attributes_manager.session_attributes
        area = session_variables[SessionVariables.AREA]
    else:
        area = 0
    return AreaEnum(area)


@sb.request_handler(
    can_handle_func=lambda input:
    is_intent_name("AMAZON.CancelIntent")(input) or
    is_intent_name("AMAZON.StopIntent")(input))
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "Thanks for playing!!"

    handler_input.response_builder.speak(
        speech_text).ask("Please say again").set_should_end_session(True)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input: player_area(input) is AreaEnum.menu)
def menu_handler(handler_input):
    """
    Menu handlers
    """
    # type: (HandlerInput) -> Response
    intent_name = get_intent_name(handler_input)
    session_variables = handler_input.attributes_manager.session_attributes

    response = Menu(intent_name, session_variables).get_response()

    if response.session_variables is not None:
        handler_input.attributes_manager.session_attributes = response.session_variables.get_dict()
    else:
        handler_input.attributes_manager.session_attributes = session_variables.get_dict()
    handler_input.response_builder.speak(response.speech_text).ask("Say again")

    return handler_input.response_builder.response


# Tutorial intent handlers
@sb.request_handler(can_handle_func=lambda input: player_area(input) is AreaEnum.introduction)
def tutorial_handler(handler_input):
    """
    Tutorial handlers
    """
    # type: (HandlerInput) -> Response
    intent_name = get_intent_name(handler_input)
    session_variables = handler_input.attributes_manager.session_attributes

    response = Introduction(intent_name, session_variables).get_response()

    if response.session_variables is not None:
        handler_input.attributes_manager.session_attributes = response.session_variables.get_dict()

    handler_input.response_builder.speak(response.speech_text).ask("Say again")

    return handler_input.response_builder.response


# Practice intent handlers
@sb.request_handler(can_handle_func=lambda input: player_area(input) is AreaEnum.practice)
def practice_handler(handler_input):
    """
    Practice handlers
    """
    # type: (HandlerInput) -> Response

    intent_name = get_intent_name(handler_input)
    session_variables = handler_input.attributes_manager.session_attributes

    response = Practice(intent_name, session_variables).get_response()

    if response.session_variables is not None:
        handler_input.attributes_manager.session_attributes = response.session_variables.get_dict()

    handler_input.response_builder.speak(response.speech_text).ask("Say again")

    return handler_input.response_builder.response


@sb.request_handler(
    can_handle_func=lambda input: player_area(input) is AreaEnum.speed_date and is_intent_name(Intents.HELP)(input))
def speed_date_help_handler(handler_input):
    session_variables = handler_input.attributes_manager.session_attributes
    handler_input.attributes_manager.session_attributes = session_variables

    handler_input.response_builder.speak("While on a date, you need to ask questions and reply when you are asked. "
                                         " Doing so correctly will increase your score. If you finish the "
                                         "date, asking and answering enough questions, and your score is high enough, "
                                         "you may score a second date").ask("Say again")

    return handler_input.response_builder.response

# Date intent handlers
@sb.request_handler(can_handle_func=lambda input: can_handle_date(input))
def handle_date(handler_input):
    # type: (HandlerInput) -> Response
    session_attr = SessionVariables(handler_input.attributes_manager.session_attributes)
    z = int(session_attr.conversation)
    y = int(session_attr.place)

    # Use date picker to get the correct date audio depending on who you dating
    intent_list, response_dict = date_picker(session_attr.date)
    intent_list, response_dict = json.loads(intent_list), json.loads(response_dict)

    speech_text = response_dict[intent_list[z][y]]

    if y == 1:
        y = 0
        session_attr.place = 0

        # Gain point and put the winning point sound in front of the current speech text
        session_attr.date_round += 1
        session_attr.date_score += 1
        speech_text = Audio.point + speech_text

        session_attr.conversation = 1000

    if y == 0:
        y = 1

    # If date over, add finishing date dialog
    if (session_attr.date_round is DATE_ROUNDS):
        return finish_date(handler_input, session_attr, speech_text)

    handler_input.attributes_manager.session_attributes = session_attr.get_dict()

    handler_input.response_builder.speak(speech_text).ask("Say again")
    return handler_input.response_builder.response
# endregion


@sb.request_handler(can_handle_func=lambda input: not can_handle_date(input))
def handle_date_problems(handler_input):

    session_attr = SessionVariables(handler_input.attributes_manager.session_attributes)

    # Lose point and put the losing point sound in front of the current speech text
    session_attr.date_bad_response_count += 1
    session_attr.date_round += 1

    # Added different bad response audio depending on how many bad responses the player has given so far. If it is
    # their third bad response, takes player back to menu
    if (session_attr.date_bad_response_count is 1):
        speech_text = Audio.Carmen_error_message_1
    elif (session_attr.date_bad_response_count is 2):
        speech_text = Audio.Carmen_error_message_2
    elif (session_attr.date_bad_response_count is 3):
        speech_text = Audio.Carmen_error_message_3
        session_attr.area = AreaEnum.menu
        session_attr.date_round -= 1
    else:
        speech_text = " No Entiedo "

    speech_text = Audio.cricket_sound + speech_text

    session_attr.conversation = 1000
    session_attr.place = 0

    # If date over, add finishing date dialog
    if (session_attr.date_round is 3):
        return finish_date(handler_input, session_attr, speech_text)

    handler_input.attributes_manager.session_attributes = session_attr.get_dict()
    handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("Hello World", speech_text)).set_should_end_session(
        False)
    return handler_input.response_builder.response


def get_next_date(date):
    if date is DateEnum.tessa:
        date = DateEnum.conchita

    elif date is DateEnum.conchita:
        date = DateEnum.enrique

    elif date is DateEnum.enrique:
        date = DateEnum.tessa

    return date


def finish_date(handler_input, session_attr, speech_text):
    speech_text += " You finished the date, your score is " + str(
        session_attr.date_score) + ". Not too bad, you might get another date if your lucky. The second date is about to begin, ask your date a question "

    # After date is over, set number of date rounds, bad response count and date score to zero, ready for a new date to begin
    session_attr.date_round = session_attr.date_bad_response_count = session_attr.date_score = 0

    # Get next date
    session_attr.date = get_next_date(session_attr.date)

    # Increase the number of dates by one, so we can decide how many total dates they have been on and changes things accordingly
    session_attr.number_of_dates += 1

    handler_input.attributes_manager.session_attributes = session_attr.get_dict()
    handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("Hello World", speech_text)).set_should_end_session(
        False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    # type: (HandlerInput) -> Response
    logger.info(
        "Session ended with reason: {}".format(
            handler_input.request_envelope.request.reason))
    return handler_input.response_builder.response


def currently_playing(handler_input):
    """Function that acts as can handle for game state."""
    # type: (HandlerInput) -> bool
    is_currently_playing = False
    session_attr = handler_input.attributes_manager.session_attributes

    if ("game_state" in session_attr
            and session_attr['game_state'] == "STARTED"):
        is_currently_playing = True

    return is_currently_playing


@sb.request_handler(can_handle_func=lambda input:
not currently_playing(input) and
is_intent_name("AMAZON.YesIntent")(input))
def yes_handler(handler_input):
    """Handler for Yes Intent, only if the player said yes for
    a new game.
    """
    # type: (HandlerInput) -> Response

    session_attr = handler_input.attributes_manager.session_attributes
    session_attr['game_state'] = "STARTED"
    session_attr['guess_number'] = random.randint(0, 100)
    session_attr['no_of_guesses'] = 0

    speech_text = "Great! Try saying a number to start the game."
    reprompt = "Try saying a number."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
not currently_playing(input) and
is_intent_name("AMAZON.NoIntent")(input))
def no_handler(handler_input):
    """Handler for No Intent, only if the player said no for
    a new game.
    """
    # type: (HandlerInput) -> Response
    session_attr = handler_input.attributes_manager.session_attributes
    session_attr['game_state'] = "ENDED"
    session_attr['ended_session_count'] += 1

    handler_input.attributes_manager.persistent_attributes = session_attr
    handler_input.attributes_manager.save_persistent_attributes()

    speech_text = "Command Recognised"

    handler_input.response_builder.speak(speech_text)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
is_intent_name("AMAZON.FallbackIntent")(input) or
is_intent_name("AMAZON.YesIntent")(input) or
is_intent_name("AMAZON.NoIntent")(input))
def fallback_handler(handler_input):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    # type: (HandlerInput) -> Response
    game_variables = handler_input.attributes_manager.session_attributes

    if ("game_state" in game_variables and
            game_variables["game_state"] == "STARTED"):
        speech_text = (
            "The {} skill can't help you with that.  "
            "Try guessing a number between 0 and 100. ".format(SKILL_NAME))
        reprompt = "Please guess a number between 0 and 100."
    else:
        speech_text = (
            "The {} skill can't help you with that.  "
            "It will come up with a number between 0 and 100 and "
            "you try to guess it by saying a number in that range. "
            "Would you like to play?".format(SKILL_NAME))
        reprompt = "Say yes to start the game or no to quit."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input: True)
def unhandled_intent_handler(handler_input):
    """Handler for all other unhandled requests."""
    # type: (HandlerInput) -> Response
    speech = "Say yes to continue or no to end the game!!"
    handler_input.response_builder.speak(speech).ask("Say again")
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    # type: (HandlerInput, Exception) -> Response
    logger.error(exception, exc_info=True)
    speech = "Sorry, I can't understand that. Please say again!!"
    handler_input.response_builder.speak(speech).ask("Say again")
    return handler_input.response_builder.response


@sb.global_response_interceptor()
def log_response(handler_input, response):
    """Response logger."""
    # type: (HandlerInput, Response) -> None
    logger.info("Response: {}".format(response))


lambda_handler = sb.lambda_handler()