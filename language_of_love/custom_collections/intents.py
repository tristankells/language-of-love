class Intents:

    # Samples phrases :
    FALLBACK = 'AMAZON.FallbackIntent'

    # Samples phrases :
    CANCEL = 'AMAZON.CancelIntent'

    # Samples phrases : 'help me', 'give me a tip', 'tip', 'prompt me', 'prompt', 'give me a prompt', 'help', 'waiter help', 'I need assistance', 'I need help'
    HELP = 'AMAZON.HelpIntent'

    # Samples phrases : 'bill please', 'quit', 'stop', 'I want to leave', 'end my date', 'cheque please', 'check please', 'I am leaving this date', 'I don't like my date'
    STOP = 'AMAZON.StopIntent'

    # Samples phrases :
    NAVIGATE_HOME = 'AMAZON.NavigateHomeIntent'

    # Samples phrases : 'help find me a date', 'I want to go on a speed date', 'open speed date', 'open language of love', 'i need a date', 'launch language of love', 'start language of love', 'help me find a date', 'Find me a date', 'start speed dating', 'start speed date', 'start date', 'speed dating', 'Let's go on a date', 'I want to go speed dating', 'date'
    START_SPEED_DATE = 'StartSpeedDateIntent'

    # Samples phrases : 'practice first', 'start practice level', 'practice level', 'start practice round', 'practice round', 'Let's practice first', 'Let's practice', 'teach me', 'teach me first', 'i want to practice', 'i would like to practice', 'begin practice', 'start practice', 'practice'
    START_PRACTICE = 'StartPracticeIntent'

    # Samples phrases : 'i want to listen to the audio again', 'can you play that again', 'i want to hear that again', 'please repeat that ', 'repeat'
    REPEAT_PRACTICE_PHRASE = 'RepeatPracticePhraseIntent'

    # Samples phrases : 'give me a new one', 'new word', 'new phrase', 'i would like a new phrase please', 'new phrase please'
    NEW_PRACTICE_PHRASE = 'NewPracticePhraseIntent'

    # Samples phrases : 'exit {Area}', 'finish {Area}', 'leave {Area}'
    LEAVE_AREA = 'LeaveAreaIntent'

    # Samples phrases : 'hi what is your name', 'pleasure to meet you what is your name', 'nice to meet you what is your name', 'what is you name'
    QUESTION_NAME = 'QuestionNameIntent'

    # Samples phrases : 'I am called {Name}', 'I am {Name}', 'Hello i am {Name}', 'Hello my name is {Name}', 'hello love my name is {Name}', 'name is {Name}', 'my name is {Name}', '{Name}'
    ANSWER_NAME = 'AnswerNameIntent'

    # Samples phrases : 'Where is your family from', 'Are you from here', 'Are you a local', 'Are you from around here', 'Where is your hometown', 'Where do you come from', 'where do you live', 'where you from', 'you from around here', 'where did you grow up', 'where are you from'
    QUESTION_WHERE_YOU_FROM = 'QuestionWhereYouFromIntent'

    # Samples phrases : '{city}', '{location}', 'My family is from {city}', 'My family is from {location}', 'I live in {location}', 'I live in {city}', 'My hometown is {location}', 'My hometown is {city}', 'I am from {city}', 'I am from {location}'
    ANSWER_WHERE_YOU_FROM = 'AnswerWhereYouFromIntent'

    # Samples phrases : 'what is your dream job', 'what would you like to work as', 'do you like your work', 'Do you like your job', 'where would you like to work', 'what is your job', 'where do you see yourself in the next five years', 'What job what you want to do', 'which is the one job in the world that you would love to do', 'What are you working as', 'What do you do for work'
    QUESTION_JOB = 'QuestionJobIntent'

    # Samples phrases : 'I am working as a {Job}', 'I work as {Job}', 'I am an {Job}', 'I am a {Job}', 'I works as {Job}', 'My work is {Job}', '{Job}', 'My job is {Job}'
    ANSWER_MY_JOB = 'AnswerMyJobIntent'

    # Samples phrases : 'if you were an animal in the wild what would you be', 'what kind of animal do you wish to be in the next life', 'what animal would you wish to have', 'what animal do you wish to have', 'if you could be an animal what would it be', 'what is your favourite pet animal', 'what is your favourite pet', 'what animal would you like to be', 'What is your favorite animal', 'Do you like animals', 'What animal do you like', 'Do you have any pets', 'How many pets do you have', 'How old is your pet', 'How old are your pets', 'Why don't you like animals'
    QUESTION_ANIMALS = 'QuestionAnimalsIntent'

    # Samples phrases : 'my favourite animal is a dog'
    ANSWER_ANIMALS = 'AnswerAnimalsIntent'

    # Samples phrases : 'what colour do you like', 'what is your favourte color', 'what is your favourite colour '
    QUESTION_COLOUR = 'QuestionColourIntent'

    # Samples phrases : 'I like {Colour}', 'My favourite colour is {Colour}', '{Colour}'
    ANSWER_COLOUR = 'AnswerColourIntent'

    # Samples phrases : 'did you have a good day', 'Having a good day', 'How was your day'
    QUESTION_DAY = 'QuestionDayIntent'

    # Samples phrases : 'my day was shit', 'my day was okay', 'my day was great', 'my day was bad', 'My day was good'
    ANSWER_DAY = 'AnswerDayIntent'

    # Samples phrases : 'what is your age', 'How old are you'
    QUESTION_AGE = 'QuestionAgeIntent'

    # Samples phrases : 'i am  {Age} years old', '{Age}', 'i am {Age}'
    ANSWER_AGE = 'AnswerAgeIntent'

    # Samples phrases : 'what was the name of the last book you read', 'What was the last book you read', 'Do you like to read books', 'What is your favorite book', 'Who is your favorite author', 'Which is the last book you read', 'What is the last book you read', 'Do you have a favorite author'
    QUESTION_BOOK = 'QuestionBookIntent'

    # Samples phrases : 'my favourite book is harry potter'
    ANSWER_BOOK = 'AnswerBookIntent'

    # Samples phrases : 'favourite music instrument to play', 'what music instrument would you like to learn how to play', 'do you like spicy food', 'Do you like sweet food', 'Do you like to go on roadtrips', 'do you like to hike', 'do you like to travel', 'do you like to go to the gym', 'what is your hobby', 'What do you like to do for fun', 'Do you like to cook', 'Do you cook', 'What do you like to cook', 'what do you cook', 'What don't you like to eat', 'What do you like to eat', 'What is your favorite food', 'What is your favorite cuisine', 'What makes you sad', 'What makes you happy', 'What makes you cry', 'What makes you laugh', 'What are you scared of', 'Do you have any fears', 'Do you like hiking', 'What sports do you play', 'Do you go to the gym', 'Do you like travelling ', 'What are your hobbies', 'What do you do for fun'
    QUESTION_HOBBIES = 'QuestionHobbiesIntent'

    # Samples phrases : 'I love playing rugby '
    ANSWER_HOBBIES = 'AnswerHobbiesIntent'
