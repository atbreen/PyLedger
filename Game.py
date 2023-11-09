# pylint: skip-file

class Game:
    def __init__(self, title, platform, media_type, num_players):
        self.title = title
        self.platform = platform
        self.media_type = media_type
        self.num_players = num_players

    def create_game_object(self):
