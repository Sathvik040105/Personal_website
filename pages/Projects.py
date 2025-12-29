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
     
    # Reverse order: show most recent projects first
    for idx in reversed(range(1, 10)):
        Portfolio_component(Portfolio[idx][0], Portfolio[idx][1])
        # Add special content for certain projects
        if idx == 1:
            # Interplanetary Rover images and iframe
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image("1722592429814.jpeg", width=380, use_container_width=True)
            with col2:
                st.image("1722592748119.jpeg", width=410, use_container_width=True)
            with col3:
                st.image("1722592715149.jpeg", width=380, use_container_width=True)
            components.iframe("https://iisc303.autodesk360.com/g/shares/SH512d4QTec90decfa6e7bc7a87ed5449f67", width=1000, height=800)
        elif idx == 3:
            # SaiMan project
            st.link_button("Go to :blue[Project on GitHub]", "https://github.com/Sathvik040105/crypto-SaiMan")
            components.iframe("https://sathvik040105.github.io/crypto-SaiMan/", width=800, height=600,scrolling=True)
        elif idx == 4:
            st.link_button("Go to :blue[Resources on GitHub]", "https://github.com/Sathvik040105/IISc_UMC-203_AIML_Term_paper")
        elif idx == 5:
            st.link_button("Go to :blue[Project on GitHub]", "https://github.com/Sathvik040105/Bird_Scouts_MS")
        elif idx == 6:
            st.link_button("Go to :blue[Project on GitHub]", "https://github.com/Sathvik040105/DA_Financial_networks")
        elif idx == 7:
            st.link_button("Go to :blue[Presentation]", "https://indianinstituteofscience-my.sharepoint.com/:p:/g/personal/sathvikm_iisc_ac_in/ES-57VoFHqJJqO8I3D4qHrEBCrEYF7h8KvElu6j2Ro9XZA?e=Ldh4lV")
        elif idx == 8:
            st.link_button("Go to :blue[Project on GitHub]", "https://github.com/Sathvik040105/Krishi-Mitra")
        elif idx == 9:
            st.link_button("Go to :blue[Project on GitHub]", "https://github.com/Sathvik040105/TachyView")
    # Additional Project (if required)
    Portfolio_component("More Coming Soon...", "Stay tuned for updates on upcoming projects and developments!")
