import streamlit as st
import matplotlib.pyplot as plt

# Your data
consoles = {
    "PlayStation 4": 6,
    "NES": 12,
    "PC": 20
}

# Create a bar chart


def create_bar_chart(data):
    plt.bar(data.keys(), data.values())
    plt.xlabel('Consoles')
    plt.ylabel('Number of Units')
    plt.title('Sales of Game Consoles')
    st.pyplot()

# Streamlit app


def main():
    st.title("Game Console Sales Bar Chart")

    # Display the data
    st.write("Data:", consoles)

    # Create and display the bar chart
    create_bar_chart(consoles)


if __name__ == "__main__":
    main()
