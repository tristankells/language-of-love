class Audio:
    ROOT_URL = 'https://s3.amazonaws.com/language-of-love/'

    @staticmethod
    def get_audio(audio_name):
        return "<audio src='" + Audio.ROOT_URL + audio_name + ".mp3'/>"

    # Start audio file for practice
    practice_start = get_audio("lecturer-practice-start")

    # Questions in english represented by the e. For practice
    Q_e_lecturer_like_chocolate = get_audio("english-lecturer-do-u-like-chocolate")
    Q_e_lecturer_like_coffee = get_audio("english-lecturer-do-u-like-coffee")
    Q_e_lecturer_like_flower = get_audio("english-lecturer-do-u-like-flowers")
    Q_e_lecturer_like_drink = get_audio("english-lecturer-do-u-like-to-drink")
    Q_e_lecturer_like_travel = get_audio("english-lecturer-do-u-like-to-travel")
    Q_e_lecturer_what_name = get_audio("english-lecturer-whats-ur-name")
    Q_e_lecturer_what_profession = get_audio("english-lecturer-whats-ur-profession")

    # Questions in spanish represented by the s. For practice
    Q_s_lecturer_like_chocolate = get_audio("spanish-lecturer-do-u-like-chocolate")
    Q_s_lecturer_like_coffee = get_audio("spanish-lecturer-do-u-like-coffee")
    Q_s_lecturer_like_flower = get_audio("spanish-lecturer-do-u-like-flowers")
    Q_s_lecturer_like_drink = get_audio("spanish-lecturer-do-u-like-to-drink")
    Q_s_lecturer_like_travel = get_audio("spanish-lecturer-do-u-like-to-travel")
    Q_s_lecturer_what_name = get_audio("spanish-lecturer-whats-ur-name")
    Q_s_lecturer_what_profession = get_audio("spanish-lecturer-whats-ur-profession")

    # In-game audio
    point = get_audio("point")

    # TODO Shorten the cricket sound
    cricket_sound = get_audio("cricket_sound")

    # Intro files
    welcome = get_audio("tristan-welcome")
    welcome_2 = get_audio("tristan-welcome-2")
    fantastico = get_audio("tristan-fantastico")
    mucho_gusto = get_audio("tristan-mucho_gusto")
    pracrice_or_date = get_audio("practice_or_speed_date")

    # Tessa audio files
    Q_tessa_how_are_you = get_audio("tessa_how_are_you")
    Q_tessa_how_old_are_you = get_audio("tessa_how_old_are_you")
    Q_tessa_how_was_your_day = get_audio("tessa_how_was_your_day")
    Q_tessa_i_am_from_Wellington = get_audio("tessa_i_am_from_Wellington")
    Q_tessa_What_is_your_job = get_audio("tessa_What_is_your_job")
    Q_tessa_what_time_is_it = get_audio("tessa_what_time_is_it")
    Q_tessa_whats_your_favourite_colour = get_audio("tessa_whats_your_favourite_colour")
    Q_tessa_whats_your_name = get_audio("tessa_whats_your_name")
    Q_tessa_where_are_you_from = get_audio("tessa_where_are_you_from")
    Q_tessa_I_am_lawyer = get_audio("tessa_I_am_lawyer")
    Q_tessa_i_am_very_tired = get_audio("tessa_i_am_very_tired")
    A_tessa_im_25_years_old = get_audio("tessa_im_25_years_old")
    A_tessa_it_is_2_pmn = get_audio("tessa_i_am_from_Wtessa_it_is_2_pmellington")
    A_tessa_my_favourite_colour_is_blue = get_audio("tessa_my_favourite_colour_is_blue")
    A_tessa_My_name_is_Tess = get_audio("tessa_My_name_is_Tess")
    A_tessa_very_good_thanks = get_audio("tessa_very_good_thanks")

    # Carmen Error Messages
    Carmen_error_message_1 = get_audio("Carmen_error_messages/Carmen_Error_1")
    Carmen_error_message_2 = get_audio("Carmen_error_messages/Carmen_Error_2")
    Carmen_error_message_3 = get_audio("Carmen_error_messages/Carmen_Error_3")

    # Carmen Host
    Carmen_intro_1 = get_audio("Carmen_host/Carmen_intro_1")
    Carmen_intro_2 = get_audio("Carmen_host/Carmen_intro_2")

    #
