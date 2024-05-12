import streamlit as st
import pyperclip
from Autocompletion import *


def main():
    '''Runs the autocompletion app.'''

    st.title("Python Autocomplete App")

    user_input = st.text_input("Enter text:")

    #Collecting filtered words

    autocomplete_results = prefix_matching(tree, user_input, [])

    #Showing the suggestions

    if autocomplete_results != []:

        selected_suggestion = None
        st.write("Autocomplete Suggestions:")

        for suggestion in autocomplete_results:

            #Selecting word from given suggestions

            if st.button(suggestion):
                selected_suggestion = suggestion
                pyperclip.copy(suggestion)

        if selected_suggestion != None:

            st.write("Selection copied to clipboard!")

        else:

            st.write("No suggestion selected")
    
    #No suggestions

    else:

        st.write("No autocomplete suggestions")

main()
