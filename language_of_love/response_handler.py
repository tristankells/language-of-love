from response import Response


def response_handler(intent_name, intent_dictionary, session_variables, fallback):
    if intent_name in intent_dictionary:
        return intent_dictionary[intent_name](session_variables)
    else:
        return fallback(session_variables)
