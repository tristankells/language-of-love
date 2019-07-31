from audio import Audio

class Translator:
    """
    Translator with full game dialog, but spoken by Alexa. Useful for player 
    testing before recording lines
    """
    launch = Audio.welcome
    #
    launch_first_time = Audio.welcome + Audio.welcome_2

    class Tutorial:
        answer_to_your_name = Audio.welcome_2

        answer_to_question_where_are_you_from = """ I am from Columbia. Soy de Columbia. Great job, I think you got the hang of it. Remember, you might be asked many questions in a real date, and will be expected to show interest in your date. Practice will be important if you want to find love. """

        error = "To finish the tutorial, say what I told you"

    class Testing:
        not_implemented = "Not implemented yet. Come back soon"

        error = "Error logged"

    class Practice:
        begin = "Practice started. Lets go through some key spanish phrases that you will need to progress through the dates"

        what_is_your_name = "¿Cuál es tu nombre? In english, what is your name. Try saying it yourself"

        where_are_you_from = "de donde eres? In english, where are you from. Try saying it yourself"

        what_is_your_job = "en qué trabajas? In english, what is your job or what do you do for a living. Try saying it yourself"

        new_or_repeat = "You want to hear that again or practice a new phrase?"

        end = "Practice over. Good luck out there hope you find love"

    class SpeedDate:
        begin = "Speed date begun. Have fun and good luck"

    class Error:
        bad_option = "Not an option right now."

    class Reprompt:
        menu = "You decided what you want to do yet?"
