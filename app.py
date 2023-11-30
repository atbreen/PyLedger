import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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
        # Game Library
        st.header("Game Library")
        df = game_library.to_dataframe()
        st.data_editor(df, use_container_width=True, num_rows="dynamic", key="editor", on_change=save_changes, column_config={
            "title": st.column_config.TextColumn("Title", required=True),
            "console": st.column_config.SelectboxColumn("Console", required=True, options=Game.consoles),
            "platform": st.column_config.SelectboxColumn("Platform", required=False, options=Game.platforms),
            "media_type": st.column_config.SelectboxColumn("Media Type", required=True, options=Game.media_types),
            "players": st.column_config.SelectboxColumn("Players", required=True, options=Game.player_types)
        })
        # Search Games
        with st.expander("Search Games"):
            with st.form('query'):
                search_title = st.text_input("Title")
                search_console = st.selectbox(
                    "Console", Game.consoles, index=None, placeholder="Console",)
                search_platform = st.selectbox("Platform", Game.platforms, index=None, placeholder="Platform",)
                search_media_type = st.selectbox(
                    "Media Type", Game.media_types, index=None, placeholder="Media Type",)
                search_players = st.selectbox(
                    "Players", Game.player_types, index=None, placeholder="Players",)
                submitted = st.form_submit_button("Search")
                # Query Table
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
        # Upload CSV
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
        # Add New Game
    with st.expander("Add New Game"):
        with st.form('add', clear_on_submit=True):
            new_title = st.text_input("Title")
            new_console = st.selectbox(
                "Console", Game.consoles, index=None, placeholder="Console",)
            new_platform = st.selectbox("Platform", Game.platforms, index=None, placeholder="Platform",)
            new_media_type = st.selectbox(
                "Media Type", Game.media_types, index=None, placeholder="Media Type",)
            new_players = st.selectbox("Players", Game.player_types, index=None, placeholder="Players",)
            submitted = st.form_submit_button("Add Game")
            if submitted:
                game_library.add_game(
                    Game(new_title, new_console, new_media_type, new_platform, new_players))
                st.rerun()

    # with st.expander("Game Library Stats"):
    #         with st.form('stats'):
    #             stat = df
    #             game_stat_select = st.selectbox("Select a Metric to Compare", Game.stat_metrics)
                
    #             if game_stat_select == "Title":
    #                 stat_title = st.text_input("Title")
    #                 if stat_title:
    #                     stat = stat[stat["title"].str.contains(
    #                         stat_title, case=False, regex=False)]
                
    #             elif game_stat_select == "Console":
    #                 stat_console = st.selectbox("Console", Game.consoles, index=None, placeholder="Consoles")
    #                 if stat_console:
    #                     stat = stat[stat["console"] == stat_console]

                
    #             elif game_stat_select == "Platform":
    #                 stat_platform = st.selectbox("Platform", Game.platforms, index=None, placeholder="Platforms")
    #                 if stat_platform:
    #                     stat = stat[stat["platform"] == stat_platform]
                
    #             elif game_stat_select == "Media Type":
    #                 stat_media_types = st.selectbox("Media Types", Game.media_types, index=None, placeholder="Media Types")
    #                 if stat_media_types:
    #                     stat = stat[stat["media_types"] == stat_media_types]
                
    #             elif game_stat_select == "Players":
    #                 stat_players = st.selectbox("Platform", Game.player_types, index=None, placeholder="Players")
    #                 if stat_players:
    #                     stat = stat[stat["players"] == stat_players]
                
    #             # Stats Graph
    #             submitted = st.form_submit_button("Submit")
    #             if submitted:
    #                 # Add Dictionary Logic Here
    #                 pass



if __name__ == "__main__":
    main()
