import streamlit as st
import pandas as pd
import numpy as np

# Create an empty dataframe
data = pd.DataFrame(columns=["Random"])
if "df" not in st.session_state:
    st.session_state.df = data

st.text("Original dataframe")

# with every interaction, the script runs from top to bottom
# resulting in the empty dataframe
st.dataframe(data) 

# random value to append; could be a num_input widget if you want
random_value = np.random.randn()

if st.button("Append random value"):
    # update dataframe state
    st.session_state.df.loc[len(st.session_state.df.index)] = {'Random': random_value}
    st.text("Updated dataframe")
    st.dataframe(st.session_state.df)

# still empty as state is not persisted
st.text("Original dataframe")
st.dataframe(data)


# # Sidebar
    # st.sidebar.header("Options")
    # if st.sidebar.button("Import CSV"):
    #     print("here")
    #     csv_file = st.file_uploader("Upload CSV", type="csv")
    #     print(csv_file)
    #     if csv_file is not None:
    #         df = pd.read_csv(csv_file)
    #         for _, row in df.iterrows():
    #             game_library.add_game(Game(row['Title'], row ['Console'], row['Media Type'], row['Platform'], row['Number of Players']))

    # if st.sidebar.button("Export CSV"):
    #     df = game_library.to_dataframe()
    #     st.dataframe(df)
    #     st.download_button("Export CSV", df.to_csv(index=False), file_name="game_library.csv", key='export-btn')

    # st.sidebar.header("Query by Attribute")
    # attribute = st.sidebar.selectbox("Select Attribute", ['Title', 'Console', 'Media Type', 'Platform', 'Players'])
    # query_value = st.sidebar.text_input("Enter Value")
    # if st.sidebar.button("Query"):
    #     result = game_library.query_by_attribute(attribute, query_value)
    #     st.table(pd.DataFrame([vars(game) for game in result]))

    # st.sidebar.header("Edit / Delete")
    # edit_title = st.sidebar.text_input("Enter Title for Edit/Delete")
    # if st.sidebar.button("Edit"):
    #     attribute_to_edit = st.sidebar.selectbox("Select Attribute to Edit", ['Title', 'Console', 'Media Type', 'Platform', 'Number of Players'])
    #     new_value = st.sidebar.text_input("Enter New Value")
    #     game_library.edit_game(edit_title, attribute_to_edit, new_value)

    # if st.sidebar.button("Delete"):
    #     game_library.delete_game(edit_title)

    # Main content