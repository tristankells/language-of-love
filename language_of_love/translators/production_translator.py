from custom_collections.audio import Audio

# US english voices voices
SALLI_VOICE = '<voice name="Salli"><lang xml:lang="en-US">{}</lang></voice>'

# Spanish voices
CONCHITA_VOICE = '<voice name="Conchita"><lang xml:lang="es-ES"><prosody rate="85%">{}</prosody></lang></voice>' # Female

ENRIQUE_VOICE = '<voice name="Enrique"><lang xml:lang="es-ES"><prosody rate="85%">{}</prosody></lang></voice>' # Male


class Translator():
    """
    Translator with full game dialog, but spoken by Alexa. Useful for player
    testing before recording lines
    """
    launch = Audio.Carmen_intro_1

    launch_first_time = Audio.welcome + Audio.welcome_2

    class General:
        fallback = "General fallback"

    class Introduction:
        answer_to_your_name = Audio.Carmen_intro_2 + Audio.pracrice_or_date

        fallback = SALLI_VOICE.format("To finish the tutorial, please say your name")

    class Testing:
        not_implemented = SALLI_VOICE.format("Not implemented yet. Come back soon")

        error = SALLI_VOICE.format("Error logged")

    class Practice:
        begin = Audio.practice_start

        new_or_repeat = SALLI_VOICE.format('<break time="2s"/> Would you like to hear that phrase again, or try a new one?')

        what_is_your_name = Audio.Q_s_lecturer_what_name + Audio.Q_e_lecturer_what_name + new_or_repeat

        do_you_like_to_travel = Audio.Q_s_lecturer_like_travel + Audio.Q_e_lecturer_like_travel + new_or_repeat

        what_is_your_job = Audio.Q_s_lecturer_what_profession + Audio.Q_e_lecturer_what_profession + new_or_repeat

        where_are_you_from =  CONCHITA_VOICE.format("de donde eres.") + SALLI_VOICE.format(" means, where are you from. ") + new_or_repeat

        what_is_your_favourite_animal =  CONCHITA_VOICE.format("Cuál es tu animal favorito.") + SALLI_VOICE.format(" this means, what is your favourite animal. ") + new_or_repeat

        what_is_your_favourite_colour =  CONCHITA_VOICE.format("Cuál es tu color favorito.") + SALLI_VOICE.format("means, what is your favourite colour. ") + new_or_repeat

        how_is_your_day =  CONCHITA_VOICE.format("Qué tal tu día.") + SALLI_VOICE.format(" this means, how is your day. ") + new_or_repeat

        how_old_are_you =  CONCHITA_VOICE.format("Cuantos años tienes.") + SALLI_VOICE.format("means, how old are you. ") + new_or_repeat

        what_is_your_favourite_book =  CONCHITA_VOICE.format("cual es tu libro favorito.") + SALLI_VOICE.format("means, what is your favourite book. ") + new_or_repeat

        end = SALLI_VOICE.format("Practice over. Good luck out there hope you find love")

        fallback = SALLI_VOICE.format("Sorry didn't understand that. ") + new_or_repeat

    class Date:
        begin = SALLI_VOICE.format('Your speed date is about to begin. Begin by asking your date a question. Get ready to reply')

        fallback = '<voice name="Nicole"> I do not understand. No entiendo </voice>'

        finish = SALLI_VOICE.format(
            'You finished the date. Your score is {}. Not too bad, you might get another date if your lucky. The another date is about to begin, ask your date a question.')

        help = SALLI_VOICE.format("While on a date, you need to ask questions and reply when you are asked. "
                                  " Doing so correctly will increase your score. If you finish the "
                                  "date, asking and answering enough questions, and your score is high enough, "
                                  "you may score a second date")

        point = Audio.point

        crickets = Audio.cricket_sound

        class Error:
            first_mistake = SALLI_VOICE.format("Your date looks confused, I don't think they understand you. ")
            second_mistake = SALLI_VOICE.format("Your date looks a little frustrated. Be careful they don't leave.")
            third_mistake = SALLI_VOICE.format("Oh no, your date is leaving. You'll get them next time." )

        class Conchita:
            question_name = CONCHITA_VOICE.format(
                "Me llamo Conchita. ¿Cuál es su nombre?")  # "My name is Conchita. What is your name?"
            answer_name = CONCHITA_VOICE.format("Placer conocerte")  # "Pleasure to meet you"

            question_where_you_from = CONCHITA_VOICE.format(
                "Soy de México. ¿De donde eres?")  # CONCHITA_VOICE.format("I'm from Mexico. Where are you from?")
            answer_where_you_from = CONCHITA_VOICE.format(
                "Wow, amo ese lugar")  # CONCHITA_VOICE.format("Wow, i love that place")

            question_job = CONCHITA_VOICE.format(
                "Soy cocinera A qué se dedica")  # CONCHITA_VOICE.format("Im a cook. What do you do for a living")
            answer_job = CONCHITA_VOICE.format(
                "Debe ser un trabajo interesante.")  # CONCHITA_VOICE.format("That must be interesting work")

            question_animals = CONCHITA_VOICE.format(
                "Amo los tigres. Cual es tu animal favorito")  # CONCHITA_VOICE.format("I love tigers. What's your favourite animal")
            answer_animals = CONCHITA_VOICE.format("Que gran animal")  # CONCHITA_VOICE.format("What a great animal")

            question_colour = CONCHITA_VOICE.format(
                "Me encanta el color rojo. Cuál es tu color favorito")  # CONCHITA_VOICE.format("I love the colour red. What's your favourite colour")
            answer_colour = CONCHITA_VOICE.format("Bonito color")  # CONCHITA_VOICE.format("Nice colour")

            question_my_day = CONCHITA_VOICE.format(
                "Mi día fue genial, gracias, incluso mejor ahora")  # "My day was great thanks, even better now"
            answer_my_day = CONCHITA_VOICE.format("Mmmm")  # "Mmmm"

            question_age = CONCHITA_VOICE.format(
                "Tengo veinticuatro años, ¿cuántos años tienes?")  # "I am twenty four years old, how old are you?"
            answer_age = CONCHITA_VOICE.format("Ahhh")  # "Ahhh"

            question_movie = CONCHITA_VOICE.format(
                "Amo Casablanca, definitivamente mi película favorita")  # "I love Casablanca, definitely my favourite film"
            answer_movie = CONCHITA_VOICE.format("Gran película")  # "Great film"

            question_book = CONCHITA_VOICE.format(
                "Me encantan los clásicos, Great Expectations realmente me inspira")  # "I love the classics, Great Expectations really inspires me"
            answer_book = CONCHITA_VOICE.format(
                "Lo he leído y también me encanta.")  # "I've read that, and I also love it"

        class Enrique:
            question_name = ENRIQUE_VOICE.format(
                "Me llamo Enrique. ¿Cuál es su nombre?")  # "My name is Conchita. What is your name?"
            answer_name = ENRIQUE_VOICE.format("Placer conocerte")  # "Pleasure to meet you"

            question_where_you_from = ENRIQUE_VOICE.format(
                "Soy de México. ¿De donde eres?")  # CONCHITA_VOICE.format("I'm from Mexico. Where are you from?")
            answer_where_you_from = ENRIQUE_VOICE.format(
                "Wow, amo ese lugar")  # CONCHITA_VOICE.format("Wow, i love that place")

            question_job = ENRIQUE_VOICE.format(
                "Soy cocinera A qué se dedica")  # CONCHITA_VOICE.format("Im a cook. What do you do for a living")
            answer_job = ENRIQUE_VOICE.format(
                "Debe ser un trabajo interesante.")  # CONCHITA_VOICE.format("That must be interesting work")

            question_animals = ENRIQUE_VOICE.format(
                "Amo los tigres. Cual es tu animal favorito")  # CONCHITA_VOICE.format("I love tigers. What's your favourite animal")
            answer_animals = ENRIQUE_VOICE.format("Que gran animal")  # CONCHITA_VOICE.format("What a great animal")

            question_colour = ENRIQUE_VOICE.format(
                "Me encanta el color rojo. Cuál es tu color favorito")  # CONCHITA_VOICE.format("I love the colour red. What's your favourite colour")
            answer_colour = ENRIQUE_VOICE.format("Bonito color")  # CONCHITA_VOICE.format("Nice colour")

            question_my_day = ENRIQUE_VOICE.format(
                "Mi día fue genial, gracias, incluso mejor ahora")  # "My day was great thanks, even better now"
            answer_my_day = ENRIQUE_VOICE.format("Mmmm")  # "Mmmm"

            question_age = ENRIQUE_VOICE.format(
                "Tengo veinticuatro años, ¿cuántos años tienes?")  # "I am twenty four years old, how old are you?"
            answer_age = ENRIQUE_VOICE.format("Ahhh")  # "Ahhh"

            question_movie = ENRIQUE_VOICE.format(
                "Amo Casablanca, definitivamente mi película favorita")  # "I love Casablanca, definitely my favourite film"
            answer_movie = ENRIQUE_VOICE.format("Gran película")  # "Great film"

            question_book = ENRIQUE_VOICE.format(
                "Me encantan los clásicos, Great Expectations realmente me inspira")  # "I love the classics, Great Expectations really inspires me"
            answer_book = ENRIQUE_VOICE.format(
                "Lo he leído y también me encanta.")  # "I've read that, and I also love it"

    class Error:
        bad_option = SALLI_VOICE.format("Not an option right now.")

    class Reprompt:
        menu = SALLI_VOICE.format("You decided what you want to do yet?")

    class Menu:
        options = SALLI_VOICE.format("Would you like to speed date, or practice some more")

        fallback = SALLI_VOICE.format("Do you want to practice, or start speed dating")
