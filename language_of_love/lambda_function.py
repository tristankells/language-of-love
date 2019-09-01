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
from session_variables import SessionVariables
from custom_collections.slots import AreaEnum
from areas.introduction import Introduction
from areas.menu import Menu
from areas.practice import Practice
from custom_collections.intents import Intents
from areas.date_file import Date
from love import LanguageOfLove

SKILL_NAME = 'Language Of Love'
sb = StandardSkillBuilder(table_name="Language-Of-Love", auto_create_table=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


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
    is_intent_name("AMAZON.StopIntent")(input) or
    is_intent_name(Intents.EXIT)(input))
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "Thanks for playing!!"

    handler_input.response_builder.speak(
        speech_text).ask("Please say again").set_should_end_session(True)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input: player_area(input) == AreaEnum.menu)
def menu_handler(handler_input):
    """
    Menu handlers
    """
    # type: (HandlerInput) -> Response
    intent_name = get_intent_name(handler_input)
    session_variables = handler_input.attributes_manager.session_attributes

    response = Menu(intent_name, session_variables).get_response()

    if response.session_variables != None:
        handler_input.attributes_manager.session_attributes = response.session_variables.get_dict()
    else:
        handler_input.attributes_manager.session_attributes = session_variables.get_dict()
    handler_input.response_builder.speak(response.speech_text).ask("Say again")

    return handler_input.response_builder.response


# Tutorial intent handlers
@sb.request_handler(can_handle_func=lambda input: player_area(input) == AreaEnum.introduction)
def tutorial_handler(handler_input):
    """
    Tutorial handlers
    """
    # type: (HandlerInput) -> Response
    intent_name = get_intent_name(handler_input)
    session_variables = handler_input.attributes_manager.session_attributes

    response = Introduction(intent_name, session_variables).get_response()

    if response.session_variables != None:
        handler_input.attributes_manager.session_attributes = response.session_variables.get_dict()

    handler_input.response_builder.speak(response.speech_text).ask("Say again")

    return handler_input.response_builder.response


# Practice intent handlers
@sb.request_handler(can_handle_func=lambda input: player_area(input) == AreaEnum.practice)
def practice_handler(handler_input):
    """
    Practice handlers
    """
    # type: (HandlerInput) -> Response

    intent_name = get_intent_name(handler_input)
    session_variables = handler_input.attributes_manager.session_attributes

    response = Practice(intent_name, session_variables).get_response()

    if response.session_variables != None:
        handler_input.attributes_manager.session_attributes = response.session_variables.get_dict()

    handler_input.response_builder.speak(response.speech_text).ask("Say again")

    return handler_input.response_builder.response


@sb.request_handler(
    can_handle_func=lambda input: player_area(input) == AreaEnum.date and is_intent_name(Intents.HELP)(input))
def speed_date_help_handler(handler_input):
    session_variables = handler_input.attributes_manager.session_attributes
    handler_input.attributes_manager.session_attributes = session_variables

    handler_input.response_builder.speak("While on a date, you need to ask questions and reply when you are asked. "
                                         " Doing so correctly will increase your score. If you finish the "
                                         "date, asking and answering enough questions, and your score is high enough, "
                                         "you may score a second date").ask("Say again")

    return handler_input.response_builder.response


@sb.request_handler(
    can_handle_func=lambda input: player_area(input) == AreaEnum.date)
def date_handler(handler_input):
    intent_name = get_intent_name(handler_input)
    session_variables = handler_input.attributes_manager.session_attributes

    response = Date(intent_name, session_variables).get_response()

    handler_input.attributes_manager.session_attributes = response.session_variables.get_dict()

    handler_input.response_builder.speak(response.speech_text).ask("Say again")
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
