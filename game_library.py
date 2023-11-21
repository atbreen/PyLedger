import pandas as pd

class GameLibrary:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def delete_game(self, title):
        self.games = [g for g in self.games if g.title != title]

    def edit_game(self, title, attribute, value):
        for game in self.games:
            if game.title == title:
                setattr(game, attribute, value)

    def query_by_attribute(self, attribute, value):
        return [game for game in self.games if getattr(game, attribute) == value]

    def to_dataframe(self):
        data = {'Title': [], 'Console': [], 'Media Type': [], 'Platform': [], 'Number of Players': []}
        for game in self.games:
            data['Title'].append(game.title)
            data['Console'].append(game.console)
            data['Media Type'].append(game.media_type)
            data['Platform'].append(game.platform)
            data['Number of Players'].append(game.players)
        return pd.DataFrame(data)
