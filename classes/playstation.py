from classes.game import Game


class Playstation(Game):
    consoles = ("PlayStation 1", "PlayStation 2",
                "PlayStation 3", "PlayStation 4", "PlayStation 5")

    def get_logo(self) -> str:
        return "https://tinypic.host/images/2023/12/03/playstation.png"
