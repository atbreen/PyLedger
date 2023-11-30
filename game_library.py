import pandas as pd


class GameLibrary:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def delete_game(self, idx):
        self.games.pop(idx)

    def edit_game(self, idx, attribute, value):
        setattr(self.games[idx], attribute, value)

    def to_dataframe(self):
        data = {'title': [], 'console': [],
                'media_type': [], 'platform': [], 'players': []}
        for game in self.games:
            data['title'].append(game.title)
            data['console'].append(game.console)
            data['media_type'].append(game.media_type)
            data['platform'].append(game.platform)
            data['players'].append(game.players)
        return pd.DataFrame(data)
