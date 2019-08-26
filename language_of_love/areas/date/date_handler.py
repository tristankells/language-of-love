"""
Your module description
"""
# -*- coding: utf-8 -*-
# This is a simple Hello World Alexa Skill, built using
# the implementation of handler classes approach in skill builder.
import json
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_intent_name, get_intent_name
from ask_sdk_core.handler_input import HandlerInput
from areas.date.date_intents.date_helper import date_picker

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from session_variables import SessionVariables


def can_handle_date(handler_input):
    # type: (HandlerInput) -> bool

    session_attr = SessionVariables(handler_input.attributes_manager.session_attributes)

    intent_list, response_dict = date_picker(session_attr.date)

    intent_list, response_dict = json.loads(intent_list), json.loads(response_dict)

    intent_name = get_intent_name(handler_input)

    if int(session_attr.conversation) == 1000:
        session_attr = get_variables_not_in_conversation(intent_name, session_attr, intent_list)

    elif int(session_attr.conversation) != 1000:
        session_attr = get_variables_in_conversation(intent_name, session_attr, intent_list)

    z = int(session_attr.conversation)
    y = int(session_attr.place)

    handler_input.attributes_manager.session_attributes = session_attr.get_dict()

    return intent_list[z][y] is intent_name


def get_variables_not_in_conversation(intent_name, session_attr, intent_list):
    # If the intent is in the list left site of the intent list, then make conversation = the index of that intent
    # Make place = 1 indicating a conversation has started, and an answer is expected
    for x in range(0, len(intent_list)):
        if intent_list[x][0] is intent_name:
            session_attr.conversation = x
            session_attr.place = 0
    return session_attr


def get_variables_in_conversation(intent_name, session_attr, intent_list):
    z = session_attr.conversation
    if intent_list[z][1] is intent_name:
        session_attr.place = 1
    return session_attr
