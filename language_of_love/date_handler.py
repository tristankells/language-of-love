"""
Your module description
"""
# -*- coding: utf-8 -*-
# This is a simple Hello World Alexa Skill, built using
# the implementation of handler classes approach in skill builder.
from date_intents import conversations
import json
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

IntentList, ResponseDict = conversations()
IntentList, ResponseDict = json.loads(IntentList), json.loads(ResponseDict)

from session_variables import SessionVariables

def can_handle_date(handler_input):
    # type: (HandlerInput) -> bool

    session_attr = SessionVariables(handler_input.attributes_manager.session_attributes)
    if session_attr.conversation == 'None':
        for x in range(0, len(IntentList)):
            if is_intent_name(IntentList[x][0])(handler_input):
                session_attr.conversation = x
                print(str(x) " - x just before break")
                session_attr.place = 0
                break
        session_attr.conversation = x  # set conversation
        print(str(x) " - x just after break")
    elif session_attr.conversation != 'None':
        z = session_attr.conversation
        if is_intent_name(IntentList[z][1])(handler_input):
            print('continue')
    z = int(session_attr.conversation)
    y = int(session_attr.place)
    print("handler z,y = " + str(z) + " " + str(y))
    handler_input.attributes_manager.session_attributes = session_attr.get()
    print(IntentList[z][y])
    return is_intent_name(IntentList[z][y])(handler_input)