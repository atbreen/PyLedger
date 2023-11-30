import streamlit as st
import pandas as pd
from game import Game
from game_library import GameLibrary
from save_changes import save_changes

# TODO: make an export button that exports to CSV
# TODO : (stretch) add charts "this many of this type of game..." piechart?

# Streamlit App


def main():
    if "game_library" not in st.session_state:
        st.session_state.game_library = GameLibrary()
    game_library = st.session_state.game_library

    st.title("PyLedger")

    if len(game_library.games) > 0:
        st.header("Game Library")
        df = game_library.to_dataframe()
        # TODO: finish column_configs
        st.data_editor(df, use_container_width=True, num_rows="dynamic", key="editor", on_change=save_changes, column_config={
            "title": st.column_config.TextColumn("Title", required=True),
            "console": st.column_config.SelectboxColumn("Console", required=True, options=Game.consoles)
        })
        with st.expander("Search Games"):
            with st.form('query'):
                search_title = st.text_input("Title")
                search_console = st.selectbox(
                    "Console", Game.consoles, index=None, placeholder="Console",)
                search_platform = st.selectbox("Platform", ("N/A", "Steam", "Epic Games", "Ubisoft Connect",
                                               "GOG Galaxy", "Electronic Arts",), index=None, placeholder="Platform",)
                search_media_type = st.selectbox(
                    "Media Type", ("Digital", "Disc", "Cartridge"), index=None, placeholder="Media Type",)
                search_players = st.selectbox(
                    "Players", ("Single Player", "MMO", "Split Screen CO-OP", "Online Multiplayer",), index=None, placeholder="Players",)
                submitted = st.form_submit_button("Search")
                if submitted:
                    query = df
                    if search_title:
                        query = query[query["title"].str.contains(
                            search_title, case=False, regex=False)]
                    if search_console:
                        query = query[query["console"] == search_console]
                    if search_platform:
                        query = query[query["platform"] == search_platform]
                    if search_media_type:
                        query = query[query["media_type"] == search_media_type]
                    if search_players:
                        query = query[query["players"] == search_players]
                    st.write(query)
    else:
        with st.form('upload', clear_on_submit=True):
            st.header("Upload CSV")
            csv_file = st.file_uploader("CSV File", type="csv")
            submitted = st.form_submit_button("Upload")

            if submitted and csv_file is not None:
                df = pd.read_csv(csv_file)
                for _, row in df.iterrows():
                    game_library.add_game(Game(
                        row['title'], row['console'], row['media_type'], row['platform'], row['players']))
                st.rerun()
        st.text("--- OR ---")
    with st.expander("Add New Game"):
        with st.form('add', clear_on_submit=True):
            new_title = st.text_input("Title")
            new_console = st.selectbox(
                "Console", Game.consoles, index=None, placeholder="Console",)
            new_platform = st.selectbox("Platform", ("N/A", "Steam", "Epic Games", "Ubisoft Connect",
                                        "GOG Galaxy", "Electronic Arts",), index=None, placeholder="Platform",)
            new_media_type = st.selectbox(
                "Media Type", ("Digital", "Disc", "Cartridge"), index=None, placeholder="Media Type",)
            new_players = st.selectbox("Players", ("Single Player", "MMO", "Split Screen CO-OP",
                                       "Online Multiplayer",), index=None, placeholder="Players",)
            submitted = st.form_submit_button("Add Game")
            if submitted:
                game_library.add_game(
                    Game(new_title, new_console, new_media_type, new_platform, new_players))
                st.rerun()


if __name__ == "__main__":
    main()
