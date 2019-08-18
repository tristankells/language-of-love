class Audio:

    ROOT_URL = 'https://s3.amazonaws.com/language-of-love/'

    FORMAT_STRING = "<audio src='" + ROOT_URL + "{}.mp3' />"

    # Start audio file for practice
    practice_start = FORMAT_STRING.format("lecturer-practice-start")

    # Questions in english represented by the e. For practice
    Q_e_lecturer_like_chocolate = FORMAT_STRING.format("english-lecturer-do-u-like-chocolate")
    Q_e_lecturer_like_coffee = FORMAT_STRING.format("english-lecturer-do-u-like-coffee")
    Q_e_lecturer_like_flower = FORMAT_STRING.format("english-lecturer-do-u-like-flowers")
    Q_e_lecturer_like_drink = FORMAT_STRING.format("english-lecturer-do-u-like-to-drink")
    Q_e_lecturer_like_travel = FORMAT_STRING.format("english-lecturer-do-u-like-to-travel")
    Q_e_lecturer_what_name = FORMAT_STRING.format("english-lecturer-whats-ur-name")
    Q_e_lecturer_what_profession = FORMAT_STRING.format("english-lecturer-whats-ur-profession")

    # Questions in spanish represented by the s. For practice
    Q_s_lecturer_like_chocolate = FORMAT_STRING.format("spanish-lecturer-do-u-like-chocolate")
    Q_s_lecturer_like_coffee = FORMAT_STRING.format("spanish-lecturer-do-u-like-coffee")
    Q_s_lecturer_like_flower = FORMAT_STRING.format("spanish-lecturer-do-u-like-flowers")
    Q_s_lecturer_like_drink = FORMAT_STRING.format("spanish-lecturer-do-u-like-to-drink")
    Q_s_lecturer_like_travel = FORMAT_STRING.format("spanish-lecturer-do-u-like-to-travel")
    Q_s_lecturer_what_name = FORMAT_STRING.format("spanish-lecturer-whats-ur-name")
    Q_s_lecturer_what_profession = FORMAT_STRING.format("spanish-lecturer-whats-ur-profession")

    # In-game audio
    point = FORMAT_STRING.format("point")

    # TODO Shorten the cricket sound
    cricket_sound = FORMAT_STRING.format("cricket_sound")

    # Intro files
    welcome = FORMAT_STRING.format("tristan-welcome")
    welcome_2 = FORMAT_STRING.format("tristan-welcome-2")
    fantastico = FORMAT_STRING.format("tristan-fantastico")
    mucho_gusto = FORMAT_STRING.format("tristan-mucho_gusto")
    pracrice_or_date = FORMAT_STRING.format("practice_or_speed_date")

    # Tessa audio files
    Q_tessa_how_are_you = FORMAT_STRING.format("tessa_how_are_you")
    Q_tessa_how_old_are_you = FORMAT_STRING.format("tessa_how_old_are_you")
    Q_tessa_how_was_your_day = FORMAT_STRING.format("tessa_how_was_your_day")
    Q_tessa_i_am_from_Wellington = FORMAT_STRING.format("tessa_i_am_from_Wellington")
    Q_tessa_What_is_your_job = FORMAT_STRING.format("tessa_What_is_your_job")
    Q_tessa_what_time_is_it = FORMAT_STRING.format("tessa_what_time_is_it")
    Q_tessa_whats_your_favourite_colour = FORMAT_STRING.format("tessa_whats_your_favourite_colour")
    Q_tessa_whats_your_name = FORMAT_STRING.format("tessa_whats_your_name")
    Q_tessa_where_are_you_from = FORMAT_STRING.format("tessa_where_are_you_from")
    Q_tessa_I_am_lawyer = FORMAT_STRING.format("tessa_I_am_lawyer")
    Q_tessa_i_am_very_tired = FORMAT_STRING.format("tessa_i_am_very_tired")
    A_tessa_im_25_years_old = FORMAT_STRING.format("tessa_im_25_years_old")
    A_tessa_it_is_2_pmn = FORMAT_STRING.format("tessa_i_am_from_Wtessa_it_is_2_pmellington")
    A_tessa_my_favourite_colour_is_blue = FORMAT_STRING.format("tessa_my_favourite_colour_is_blue")
    A_tessa_My_name_is_Tess = FORMAT_STRING.format("tessa_My_name_is_Tess")
    A_tessa_very_good_thanks = FORMAT_STRING.format("tessa_very_good_thanks")

    # Carmen Error Messages
    Carmen_error_message_1 = FORMAT_STRING.format("Carmen_error_messages/Carmen_Error_1")
    Carmen_error_message_2 = FORMAT_STRING.format("Carmen_error_messages/Carmen_Error_2")
    Carmen_error_message_3 = FORMAT_STRING.format("Carmen_error_messages/Carmen_Error_3")

    # Carmen Host
    Carmen_intro_1 = FORMAT_STRING.format("Carmen_host/Carmen_intro_1")
    Carmen_intro_2 = FORMAT_STRING.format("Carmen_host/Carmen_intro_2")

    #
