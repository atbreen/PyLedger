import pandas as pd
from classes.game import Game


class GameLibrary:
    """Manages a list of Game objects, and supports rendering them to a pandas dataframe"""

    def __init__(self):
        self.games: list[Game] = []

    def add_game(self, game: Game):
        """Adds a game to library"""
        self.games.append(game)

    def delete_game(self, idx: int):
        """Deletes a game by index from the library"""
        self.games.pop(idx)

    def edit_game(self, idx: int, attribute: str, value: str):
        """Edits a game by index in the library"""
        setattr(self.games[idx], attribute, value)

    def to_dataframe(self) -> pd.DataFrame:
        """Creates a dataframe of GameLibrary"""
        game_data = {'logo': [], 'title': [], 'console': [],
                     'media_type': [], 'platform': [], 'players': []}
        for game in self.games:
            game_data['logo'].append(game.get_logo())
            game_data['title'].append(game.title)
            game_data['console'].append(game.console)
            game_data['media_type'].append(game.media_type)
            game_data['platform'].append(game.platform)
            game_data['players'].append(game.players)
        return pd.DataFrame(game_data)
