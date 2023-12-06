from classes.game import Game


class PC(Game):
    consoles = ("PC",)

    def get_logo(self) -> str:
        return "https://tinypic.host/images/2023/12/03/pc.png"
