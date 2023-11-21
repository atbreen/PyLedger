import streamlit as st
import pandas as pd
from game import Game
from game_library import GameLibrary


    # TODO: make an export button that exports to CSV
    # TODO: query the data frame by value attribute
    # TODO: stretch - have the queries return a new dataframe
    # TODO: add charts!

# Streamlit App
def main():
    if "game_library" not in st.session_state:
        st.session_state.game_library = GameLibrary()
    game_library = st.session_state.game_library

    st.title("PyLedger")

    # def show_platform(new_console):
    #     if new_console == "PC":
    #          return st.selectbox("Platform",("Steam", "Epic Games", "Ubisoft Connect", "GOG Galaxy", "Electronic Arts",), index=None, placeholder="Platform",)

    if len(game_library.games) > 0:
        st.header("Game Library")
        df = game_library.to_dataframe()
        st.dataframe(df, use_container_width=True)
    else: 
        with st.form('upload', clear_on_submit=True):
            st.header("Upload CSV")
            csv_file = st.file_uploader("CSV File", type="csv")
            submitted = st.form_submit_button("Upload")

            if submitted and csv_file is not None:
                df = pd.read_csv(csv_file)
                for _, row in df.iterrows():
                    game_library.add_game(Game(row['Title'], row ['Console'], row['Media Type'], row['Platform'], row['Number of Players']))
                st.rerun()
        st.text("--- OR ---")
    with st.form('add', clear_on_submit=True):
        st.header("Add New Game")
        new_title = st.text_input("Title")
        new_console = st.selectbox("Console",("PC", "PlayStation 1", "PlayStation 2", "PlayStation 3", "PlayStation 4", "PlayStation 5", "Nintendo Entertainment System", "Super Nintendo", "Nintendo 64", "Game Cube", "Wii", "GameBoy", "Nintendo DS/3DS", "Switch", "Atari", "Atari 2600",), index=None, placeholder="Console",)
        new_platform = st.selectbox("Platform",("N/A", "Steam", "Epic Games", "Ubisoft Connect", "GOG Galaxy", "Electronic Arts",), index=None, placeholder="Platform",)
        new_media_type = st.selectbox("Media Type",("Digital", "Disc", "Cartridge"), index=None, placeholder="Media Type",)
        new_players = st.selectbox("Players",("Single Player", "MMO", "Split Screen CO-OP", "Online Multiplayer",), index=None, placeholder="Players",)
        submitted = st.form_submit_button("Add Game")
        if submitted:
            game_library.add_game(Game(new_title, new_console, new_media_type, new_platform, new_players))
            st.rerun()

if __name__ == "__main__":
    main()
