from classes.game import Game


class PC(Game):
    consoles = ("PC")

    def get_logo(self) -> str:
        return "/app/static/pc.png"
