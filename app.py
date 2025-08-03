import streamlit as st
import requests
import json
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Set your OpenAI API key
# openai.api_key = 'your_openai_api_key'

# Function to generate a movie plot based on genres, optional plot twist, and a reference movie
def generate_movie_plot(genre1, genre2, plot_twist, movie):
    prompt = f"Create a detailed plot of a movie that would make as much BOX OFFICE revenue as the movie '{movie}'. Generate a catchy rhyming Title. The movie plot should be a mix of the genres '{genre1}' and '{genre2}'. Include a last EXPLANATION section that explains why the plot matches both genres. How is it similar to the movie mentioned in the input."

    if plot_twist and plot_twist != "No Twist" and plot_twist != "":
        prompt = f"Create a detailed plot of a movie that would make as much BOX OFFICE revenue as the movie '{movie}'. Generate a catchy rhyming Title. The movie plot should be a mix of the genres '{genre1}' and '{genre2}'. If provided, include a plot twist: '{plot_twist}'. Include a last section that explains why the plot matches both genres and how the plot twist is incorporated, and how it is similar to the movie mentioned in the input."
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a creative movie plot generator."},
            {"role": "user", "content": prompt}
        ]
    )
    
    plot = response.choices[0].message.content.strip()
    return plot

# Streamlit app
def main():
    st.title("NoirCat Writes Movie Plots")

    # Password input
    password = st.text_input("Enter Password", type="password")

    # Check if the password is correct
    if password == "IamCool4202!" or password == "abir":
        genre1 = st.text_input("Primary Genre:")
        genre2 = st.text_input("Mix with which Genre:")
        plot_twist = st.text_input("Gimme a Plot Twist:", placeholder="No Twist")
        movie = st.text_input("Reference Box Office Hit:")

        if st.button("GO"):
            if not genre1 or not genre2 or not movie:
                st.error("Please provide all the required inputs: Genre 1, Genre 2, and a reference movie.")
            else:
                plot = generate_movie_plot(genre1, genre2, plot_twist, movie)
                plot_html = plot
                st.markdown(f"<div class='plot'>{plot_html}</div>", unsafe_allow_html=True)
    elif password:
        st.error("Incorrect Password. Please try again.")

# Add custom CSS for styling
st.markdown(
    """
    <style>
    /* Set Verdana font and line spacing for input fields */
    div.stTextInput div.stTextInput__input {
        font-family: Verdana;
        line-height: 1.5;
    }

    /* Style the button */
    div.stButton > button:first-child {
        background-color: green;
        color: white;
        font-family: Verdana;
    }

    /* Set Verdana font and line spacing for the plot output */
    .plot {
        font-family: Verdana;
        line-height: 1.5;
    }
    </style>
    """,
    unsafe_allow_html=True
)



if __name__ == '__main__':
    main()
