import streamlit as st
import altair as alt
import pandas as pd
from classes.playstation import Playstation
from classes.nintendo import Nintendo
from classes.atari import Atari
from classes.pc import PC
from classes.game import Game


def create_stats_chart(df: pd.DataFrame, game_stat_select: str):
    """Creates a chart to show library stats"""
    bars = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            alt.X("count()").title(None),
            alt.Y(game_stat_select).title(None),
            color=game_stat_select
        )
    )
    st.altair_chart(bars, use_container_width=True)


def save_changes():
    """Commits the st.data_editor changes to the game_library"""
    state = st.session_state
    # Edit a game
    edit = state.editor["edited_rows"]
    for idx in edit:
        for attr in edit[idx]:
            state.game_library.edit_game(idx, attr, edit[idx][attr])
    add = state.editor["added_rows"]
    # Add a game
    for game in add:
        state.game_library.add_game(create_game(
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


def create_game(title: str, console: str, media_type: str, platform: str, players: str) -> Game:
    """Creates a Game object"""
    if console in Playstation.consoles:
        return Playstation(title, console, media_type, platform, players)
    if console in Nintendo.consoles:
        return Nintendo(title, console, media_type, platform, players)
    if console in Atari.consoles:
        return Atari(title, console, media_type, platform, players)
    if console in PC.consoles:
        return PC(title, console, media_type, platform, players)
    return Game(title, console, media_type, platform, players)
