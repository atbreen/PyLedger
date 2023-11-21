import streamlit as st
import pandas as pd

class Game:
    def __init__(self, title, console, media_type, platform, players):
        self.title = title
        self.console = console
        self.media_type = media_type
        self.platform = platform
        self.players = players

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

# Streamlit App
def main():
    if "game_library" not in st.session_state:
        st.session_state.game_library = GameLibrary()
    game_library = st.session_state.game_library

    st.title("PyLedger")
    

    # TODO: make an export button that exports to CSV
    # TODO: query the data frame by value attribute
    # TODO: stretch - have the queries return a new dataframe
    # TODO: add charts!

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
        new_console = st.text_input("Console")
        new_media_type = st.text_input("Media Type")
        new_platform = st.text_input("Platform")
        new_players = st.text_input("Number of Players")
        submitted = st.form_submit_button("Add Game")
        if submitted:
            game_library.add_game(Game(new_title, new_console, new_media_type, new_platform, new_players))
            st.rerun()

if __name__ == "__main__":
    main()
