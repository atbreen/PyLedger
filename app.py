import streamlit as st
import pandas as pd
import utils as u
from game import Game
from game_library import GameLibrary

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
        st.data_editor(df, use_container_width=True, num_rows="dynamic", key="editor", on_change=u.save_changes, column_config={
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
                search_platform = st.selectbox(
                    "Platform", Game.platforms, index=None, placeholder="Platform",)
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

        # Game Library Stats
        # with st.expander("Game Library Stats"):
        #     with st.form('stats'):
        #         game_stat_select = st.selectbox(
        #             "Select a Metric to Compare", Game.stat_metrics)

        #         value_counts_series = df[game_stat_select].value_counts()
        #         result_dict = value_counts_series.to_dict()
        #         # Stats Graph
        #         submitted = st.form_submit_button("Submit")

        #         if submitted:
        #             u.create_stats_chart(result_dict, "", "")
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
            new_platform = st.selectbox(
                "Platform", Game.platforms, index=None, placeholder="Platform",)
            new_media_type = st.selectbox(
                "Media Type", Game.media_types, index=None, placeholder="Media Type",)
            new_players = st.selectbox(
                "Players", Game.player_types, index=None, placeholder="Players",)
            submitted = st.form_submit_button("Add Game")
            if submitted:
                game_library.add_game(
                    Game(new_title, new_console, new_media_type, new_platform, new_players))
                st.rerun()


if __name__ == "__main__":
    main()
