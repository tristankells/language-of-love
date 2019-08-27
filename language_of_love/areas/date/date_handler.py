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





