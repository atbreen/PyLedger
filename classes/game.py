class Game:
    # Class Variables
    consoles = ("PC", "PlayStation 1", "PlayStation 2", "PlayStation 3", "PlayStation 4", "PlayStation 5", "Nintendo Entertainment System",
                "Super Nintendo", "Nintendo 64", "Game Cube", "Wii", "GameBoy", "Nintendo DS/3DS", "Switch", "Atari", "Atari 2600",)
    platforms = ("N/A", "Steam", "Epic Games", "Ubisoft Connect", "Nintendo Switch Online", "PlayStation Network", "Playstation Plus",
                 "GOG Galaxy", "Electronic Arts",)
    media_types = ("Digital", "Disc", "Cartridge")
    player_types = ("Single Player", "MMO",
                    "Split Screen CO-OP", "Online Multiplayer", "Cooperative", "PVP")
    stat_metrics = ("console", "media_type", "platform", "players")

    def __init__(self, title: str, console: str, media_type: str, platform: str, players: str):
        self.title = title
        self.console = console
        self.media_type = media_type
        self.platform = platform
        self.players = players

    def get_logo(self) -> str:
        # Default Logo
        return "/app/static/default.png"
