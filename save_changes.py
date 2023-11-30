import streamlit as st
from game import Game


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
