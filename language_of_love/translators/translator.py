from enums.audio import Audio


class Translator:
    """
    Translator with full game dialog, but spoken by Alexa. Useful for player
    testing before recording lines
    """
    launch = Audio.welcome
    #
    launch_first_time = Audio.welcome + Audio.welcome_2

    class General:
        @staticmethod
        def fall_back(): raise NotImplementedError

    class Intro:

        @staticmethod
        def answer_to_your_name(): raise NotImplementedError

        @staticmethod
        def answer_to_question_where_are_you_from(): raise NotImplementedError

        @staticmethod
        def error(): raise NotImplementedError

    class Testing:
        not_implemented = "Not implemented yet. Come back soon"

        error = "Error logged"

    class Practice:
        begin = Audio.practice_start

        what_is_your_name = Audio.Q_e_lecturer_what_name + Audio.Q_s_lecturer_what_name

        do_you_like_to_travel = Audio.Q_e_lecturer_like_travel

        what_is_your_job = Audio.Q_e_lecturer_what_profession

        new_or_repeat = "You want to hear that again or practice a new phrase?"

        end = "Practice over. Good luck out there hope you find love"

    class SpeedDate:
        begin = "Speed date begun. Have fun and good luck"

    class Error:
        bad_option = "Not an option right now."

    class Reprompt:
        menu = "You decided what you want to do yet?"
