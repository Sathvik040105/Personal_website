import streamlit as st
import streamlit.components.v1 as components
from const import *

st.set_page_config(page_title="Sathvik Manthri", layout="wide",initial_sidebar_state="collapsed") 

margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()

    #sidebar --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    with st.sidebar:
        st.success("Select a page above.")

    components.html(
        """
        <style>
        .custom-font {
            font-size: 50px; /* Adjust the font size as needed */
        }
        </style>
        """,
        height=0
    )
        
    #main page --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    st.header("About Me", divider='rainbow')

    # New layout: photo on left, details below photo, brief on right
    col_photo, col_brief = st.columns([1, 2.2])

    with col_photo:
        st.image("me.jpg", width=320)
        st.markdown(f"<h2 style='margin-bottom:0px'>{info['name']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<b>Interest:</b> {info['interest']}", unsafe_allow_html=True)
        st.markdown(
            f'''
            <div style="margin-top: 10px; margin-bottom: 18px;">
                <a href="{linkedin_link}" target="_blank" style="margin-right: 18px; text-decoration: none;">
                    <i class="fa-brands fa-linkedin" style="font-size: 32px; color: #0A66C2;"></i>
                </a>
                <a href="{github_link}" target="_blank" style="margin-right: 18px; text-decoration: none;">
                    <i class="fa-brands fa-github" style="font-size: 32px; color: #fff;"></i>
                </a>
                <a href="mailto:{email}" style="text-decoration: none;">
                    <i class="fa-solid fa-envelope" style="font-size: 32px; color: #EA4335;"></i>
                </a>
            </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            ''', unsafe_allow_html=True)
        with open("Sathvik_Manthri_CV.pdf", "rb") as file:
            pdf_file = file.read()
        st.download_button(
            label="Download my :blue[CV]",
            data=pdf_file,
            file_name="CV",
            mime="application/pdf")

    with col_brief:
        st.write(info['brief'])
        st.subheader("My :blue[skills] ⚒️", divider='rainbow')
        def skill_tab():
            rows, cols = len(info['skills']) // skill_col_size, skill_col_size
            skills = iter(info['skills'])
            if len(info['skills']) % skill_col_size != 0:
                rows += 1
            for x in range(rows):
                columns = st.columns(skill_col_size)
                for index_ in range(skill_col_size):
                    try:
                        columns[index_].button(next(skills))
                    except:
                        break
        with st.spinner(text="Loading section..."):
            skill_tab()
