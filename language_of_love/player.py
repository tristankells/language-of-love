class Player():
    SCORE = 'score'
    NAME = 'name'

    def __init__(self, player_variables):
        self.score = player_variables[self.SCORE]
        self.name = player_variables[self.NAME]

    def get_play_dictionary(self):
        return {
            self.SCORE: self.score,
            self.NAME: self.name
        }
