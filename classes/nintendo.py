from classes.game import Game


class Nintendo(Game):
    consoles = ("Nintendo Entertainment System",
                "Super Nintendo", "Nintendo 64", "Game Cube", "Wii", "GameBoy", "Nintendo DS/3DS", "Switch")

    def get_logo(self) -> str:
        return "https://tinypic.host/images/2023/12/03/nintendo.png"
