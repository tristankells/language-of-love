from enums.audio import Audio


class TestTranslator():
    """
    Translator with full game dialog, but spoken by Alexa. Useful for player
    testing before recording lines
    """
    launch = "Game launched. Welcome to language of love, what is your name?"

    class General:
        fallback = "General fallback"

    class Introduction:
        answer_to_your_name = "Intro. Nice name. WHht do you want to do now, practice or speed date"

        answer_to_question_where_are_you_from = """ I am from Columbia. Soy de Columbia. Great job, I think you got the hang of it."""

        fallback = "To finish the tutorial, say what I told you"

    class Testing:
        not_implemented = "Not implemented yet. Come back soon"

        error = "Error logged"

    class Practice:
        begin = Audio.practice_start

        new_or_repeat = "You want to hear that again or practice a new phrase?"

        what_is_your_name = Audio.Q_s_lecturer_what_name + Audio.Q_e_lecturer_what_name + new_or_repeat

        do_you_like_to_travel = Audio.Q_s_lecturer_like_travel + Audio.Q_e_lecturer_like_travel + new_or_repeat

        what_is_your_job = Audio.Q_s_lecturer_what_profession + Audio.Q_e_lecturer_what_profession + new_or_repeat

        end = "Practice over. Good luck out there hope you find love"

        fallback = "Sorry didn't understand that, would you like a new phrase or to repeat a phrase?"

    class SpeedDate:
        begin = "Dates are not quiet up and running yet, come back soon"

    class Error:
        bad_option = "Not an option right now."

    class Reprompt:
        menu = "You decided what you want to do yet?"

    class Menu:
        options = "Would you like to speed date, or practice some more"

        fallback = "Do you want to practice, or start speed dating"
