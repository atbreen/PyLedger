class Game:
    consoles = ("PC", "PlayStation 1", "PlayStation 2", "PlayStation 3", "PlayStation 4", "PlayStation 5", "Nintendo Entertainment System",
                "Super Nintendo", "Nintendo 64", "Game Cube", "Wii", "GameBoy", "Nintendo DS/3DS", "Switch", "Atari", "Atari 2600",)

    # TODO: media_types = ()
    # TODO: platforms = ()
    # TODO: players = ()

    def __init__(self, title, console, media_type, platform, players):
        self.title = title
        self.console = console
        self.media_type = media_type
        self.platform = platform
        self.players = players
