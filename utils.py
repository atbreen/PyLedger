import streamlit as st
import matplotlib.pyplot as plt
from game import Game

st.set_option('deprecation.showPyplotGlobalUse', False)


def create_stats_chart(data, xlabel, ylabel):
    plt.bar(data.keys(), data.values())
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('Game Library Stats')
    st.pyplot()


def save_changes():
    state = st.session_state
    # Edit a game
    edit = state.editor["edited_rows"]
    for idx in edit:
        for attr in edit[idx]:
            state.game_library.edit_game(idx, attr, edit[idx][attr])
    add = state.editor["added_rows"]
    # Add a game
    for game in add:
        state.game_library.add_game(Game(
            game.get("title", ""),
            game.get("console", ""),
            game.get("media_type", ""),
            game.get("platform", "N/A"),
            game.get("players", "")
        ))
    # Delete a game
    delete = state.editor["deleted_rows"]
    for idx in delete[::-1]:  # decending order for safe multiple deletes
        state.game_library.delete_game(idx)
