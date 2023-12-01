import pandas as pd
# import matplotlib.pyplot as plt
import streamlit as st


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
        game_data = {'title': [], 'console': [],
                     'media_type': [], 'platform': [], 'players': []}
        for game in self.games:
            game_data['title'].append(game.title)
            game_data['console'].append(game.console)
            game_data['media_type'].append(game.media_type)
            game_data['platform'].append(game.platform)
            game_data['players'].append(game.players)
        return pd.DataFrame(game_data)

    def to_graph(self):
        game_data = {'title': [], 'console': [],
                     'media_type': [], 'platform': [], 'players': []}
        for game in self.games:
            game_data['title'].append(game.title)
            game_data['console'].append(game.console)
            game_data['media_type'].append(game.media_type)
            game_data['platform'].append(game.platform)
            game_data['players'].append(game.players)
        return pd.DataFrame(game_data)
