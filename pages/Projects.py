import streamlit as st
import streamlit.components.v1 as components
from const import *

# Page Config ----------------------------------------------------------------
st.set_page_config(page_title="Projects", page_icon="🎨", layout="wide", initial_sidebar_state="collapsed")
margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()

    st.header("🎨 Projects", divider='rainbow')

    # Page Functions ----------------------------------------------------------------
    def Portfolio_component(header, content):
        st.subheader(header, divider='grey')
        st.write(content)
     
    Portfolio_component(":blue[Audio classification using Hierarchical Multi Task Learning] at IIT Indore", "Working with hierarchical multi-task learning models for audio classification")
    # Interplanetary Rover Development ----------------------------------------------------------------
    Portfolio_component(Portfolio[1][0], Portfolio[1][1])
    # Create two columns
    col1, col2, col3 = st.columns(3)

    # Display images in the respective columns
    with col1:
        st.image("1722592429814.jpeg", width=380)
    with col2:
        st.image("1722592748119.jpeg", width=410)
    with col3:
        st.image("1722592715149.jpeg", width=380)
    
    components.iframe("https://iisc303.autodesk360.com/g/shares/SH512d4QTec90decfa6e7bc7a87ed5449f67", width=1000, height=800)

    # Home Service Robot ----------------------------------------------------------------
    Portfolio_component(Portfolio[2][0], Portfolio[2][1])

    # Encrypted Messaging Tool (SaiMan) ----------------------------------------------------------------
    Portfolio_component(Portfolio[3][0], Portfolio[3][1])
    st.link_button("Go to :blue[Project on GitHub]", "https://github.com/Sathvik040105/crypto-SaiMan")
    components.iframe("https://sathvik040105.github.io/crypto-SaiMan/", width=800, height=600,scrolling=True)
    
    # Deep Learning for Genetic Studies ----------------------------------------------------------------
    Portfolio_component(":blue[Deep Learning for Genetic Studies] at IIT Indore", """
    Developed deep learning and attention models to predict gaps in genome sequences as part of the Deep Learning for Genetic Studies project.
    """)

    #Term paper
    Portfolio_component(Portfolio[4][0], Portfolio[4][1])
    st.link_button("Go to :blue[Resources on GitHub]", "https://github.com/Sathvik040105/IISc_UMC-203_AIML_Term_paper")

    # Additional Project (if required) --------------------------------------------------------------
    Portfolio_component("More Coming Soon...", "Stay tuned for updates on upcoming projects and developments!")

    # Additional Interactive Components (optional) --------------------------------------------------------------
    # Add more tabs, buttons, or expander elements if necessary for additional projects or interactive elements.
