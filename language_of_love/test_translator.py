class TutorialResponses():
    """
    ErrorResponses - 
    Contains all the possible error messages encountered in Love
    """
    Start = (
        "Tutorial started. What's your name?)"
    )

    AnswerName = (
        "Tutorial. You answered with your name. Trying asking where alexa is "
        "from?"
    )

    QuestionWhereAreYouFrom = (
        "Tutorial. You asked where alexa was from"
    )

    End = (
        "Tutorial over. Would you like to go on a date or practice?"
    )


class GeneralResponses():
    """
    GeneralResponses - 
    Contains all the possible error messages encountered in Love
    """
    Help = (
        "You asked for help "
    )

    FirstTimeLaunch = (
        "Skill launched. First time recognised"
    )

    RepeatLaunch = (
        "Skill launched. Not first time recognised"
    )

    Practice = (
        "You asked to practice"
    )

    Date = (
        "You asked to go on a date"
    )


class DateResponses():
    """
    ErrorResponses - 
    Contains all the possible error messages encountered in Love
    """
    Start = (
        "You started speed dating round"
    )


class PracticeResponses():
    """
    ErrorResponses - 
    Contains all the possible error messages encountered in Love
    """
    Start = (
        "You started practice round"
    )


class ErrorResponses():
    """
    ErrorResponses - 
    Contains all the possible error messages encountered in Love
    """
    Default = (
        "Error. General"
    )

    AnswerName = (
        "Error. You answered with your name, but at the wrong time"
    )

    QuestionWhereAreYouFrom = (
        "Error. You asked where we were from, but at the wrong time "
    )


class Translator():
    """
    The 'Test' translator for the love skill. Shortened responses with state 
    hints for better debugging
    """
    Tutorial = TutorialResponses()
    General = GeneralResponses()
    Error = ErrorResponses()
