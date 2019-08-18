from custom_collections.audio import Audio


class Translator():
    """
    Translator with full game dialog, but spoken by Alexa. Useful for player
    testing before recording lines
    """
    CONCHITA_VOICE = '<voice name="Conchita"><lang xml:lang="es-ES">{}</lang></voice>'

    ENRIQUE_VOICE = '<voice name="Enrique"><lang xml:lang="es-ES">{}</lang></voice>'

    CONCHITA_VOICE.format("lecturer-practice-start")

    launch = Audio.Carmen_intro_1

    launch_first_time = Audio.welcome + Audio.welcome_2

    class General:
        fallback = "General fallback"

    class Introduction:
        answer_to_your_name = Audio.Carmen_intro_2 + Audio.pracrice_or_date

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

    class Date:
        begin = '<voice name="Nicole">Your speed date is about to begin. Begin by asking your date a question. Get ready to reply</voice>'

        fallback = '<voice name="Nicole"> I do not understand. No entiendo </voice>'

        class Conchita:
            CONCHITA_VOICE = '<voice name="Conchita"><lang xml:lang="es-ES">{}</lang></voice>'

            answer_where_you_from = CONCHITA_VOICE.format("Wow, i love that place")
            question_where_you_from = CONCHITA_VOICE.format("I'm from Mexico. Where are you from?")

            answer_job = CONCHITA_VOICE.format("Im a cook")
            question_job = CONCHITA_VOICE.format("What do you do for a living")

            question_animals = CONCHITA_VOICE.format("What's your favourite animal")
            answer_animals = CONCHITA_VOICE.format("I love tigers")

            question_favourite_colour = CONCHITA_VOICE.format("I love the colour red")
            answer_favourite_colour = CONCHITA_VOICE.format("What's your favourite colour")

        class Enrique:
            ENRIQUE_VOICE = '<voice name="Enrique"><lang xml:lang="es-ES">{}</lang></voice>'

            answer_where_you_from = ENRIQUE_VOICE.format("I'm from Mexico")
            question_where_you_from = ENRIQUE_VOICE.format("Where are you from")

            answer_job = ENRIQUE_VOICE.format("Im a cook")
            question_job = ENRIQUE_VOICE.format("What do you do for a living")

            question_animals = ENRIQUE_VOICE.format("What's your favourite animal")
            answer_animals = ENRIQUE_VOICE.format("I love tigers")

            question_favourite_colour = ENRIQUE_VOICE.format("I love the colour red")
            answer_favourite_colour = ENRIQUE_VOICE.format("What's your favourite colour")

    class Error:
        bad_option = "Not an option right now."

    class Reprompt:
        menu = "You decided what you want to do yet?"

    class Menu:
        options = "Would you like to speed date, or practice some more"

        fallback = "Do you want to practice, or start speed dating"
