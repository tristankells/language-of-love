class Translator:
    """
    Translator with full game dialog, but spoken by Alexa. Useful for player 
    testing before recording lines
    """
    launch = "Language of Love Launched"

    launch_first_time = ("""Language of Love Launched. Because this is your first time, lets play the 
    tutorial""")

    class Tutorial:
        intro = ("""Let's practice some basic Spanish Greetings. What's 
        your name? como te llamas?""")

        answer_to_your_name = ("""Great start! Alexa likes you. Try asking it 
        where it is from to get Alexa to like you more. """)

        answer_to_question_where_are_you_from = """ I am from Columbia. Soy de 
        Columbia. Great job, I think you got the hang of it. Remember, you might be 
        asked many questions in a real date, and will be expected to show interest 
        in your date. Practice will be important if you want to find love. """

    class Testing:
        not_implemented = "Not implemented yet. Come back soon"

        error = "Error logged"

    class Practice:
        begin = "Practice started. Lets go through some key spanish phrases that you will need to progress through the dates"

        what_is_your_name = "¿Cuál es tu nombre? In english, what is your name"

        where_are_you_from = "de donde eres? In english, where are you from"

        what_is_your_job = "en qué trabajas? In english, what is your job or what do you do for a living"

        end = "Practice over. Good luck out there hope you find love"
