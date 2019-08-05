from audio import Audio


class Translator():
    """
    Translator with full game dialog, but spoken by Alexa. Useful for player
    testing before recording lines
    """
    launch = Audio.welcome

    launch_first_time = Audio.welcome + Audio.welcome_2

    class General:
        fallback = "General fallback"

    class Introduction:
        answer_to_your_name = Audio.welcome_2 + Audio.pracrice_or_date

        fallback = "To finish the tutorial, please say your name"

    class Testing:
        not_implemented = "Not implemented yet. Come back soon"

        error = "Error logged"

    class Practice:
        begin = Audio.practice_start

        new_or_repeat = "Would you like to hear that phrase again, or try a new one?"

        what_is_your_name = Audio.Q_s_lecturer_what_name + Audio.Q_e_lecturer_what_name + new_or_repeat

        do_you_like_to_travel = Audio.Q_s_lecturer_like_travel + Audio.Q_e_lecturer_like_travel + new_or_repeat

        what_is_your_job = Audio.Q_s_lecturer_what_profession + Audio.Q_e_lecturer_what_profession + new_or_repeat

        end = "Practice over. Good luck out there hope you find love"

        fallback = "Sorry didn't understand that " + new_or_repeat

    class SpeedDate:
        begin = '<voice name="Nicole">Dating has not been implemented, come back soon to practice your spanish skills and see if you can find love</voice>'

    class Error:
        bad_option = "Not an option right now."

    class Reprompt:
        menu = "You decided what you want to do yet?"

    class Menu:
        options = "Would you like to speed date, or practice some more"

        fallback = "Do you want to practice, or start speed dating"
