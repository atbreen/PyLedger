from classes.game import Game


class Atari(Game):
    consoles = ("Atari", "Atari 2600")

    def get_logo(self) -> str:
        return "https://tinypic.host/images/2023/12/03/atari.png"
