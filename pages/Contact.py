import streamlit as st
from const import *

# Set page configuration
st.set_page_config(page_title="Contacts", page_icon="🌏", initial_sidebar_state="collapsed", layout="wide")

# Layout for the page
margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

with body:
    # Menu
    menu()

    # Main header
    st.markdown('<h1 style="text-align:center; color: #00AEEF;">📞 Contact Information</h1>', unsafe_allow_html=True)

    # Contact details in colored containers
    with st.container():
        st.markdown('<div class="container">', unsafe_allow_html=True)
        
        # Phone number
        st.markdown(f"""
            <h4 style="color: #FFFFFF;">
                <i class="fa-solid fa-phone"></i> Phone: +91 {phone}
            </h4>
        """, unsafe_allow_html=True)
        
        # Email
        st.markdown(f"""
            <h4 style="color: #FFFFFF;">
                <i class="fa-solid fa-envelope"></i> Email: <a href="mailto:{email}" style="color: #00AEEF;">{email}</a>
            </h4>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Social Profiles Section
    st.markdown('<h3 style="margin-top: 40px; color: #00AEEF;">🌐 Social Profiles</h3>', unsafe_allow_html=True)

    # LinkedIn
    with st.container():
        col1, col2 = st.columns([0.1, 3])
        with col1:
            st.write(linkedin_logo, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <h4>
                    <a href="{linkedin_link}" target="_blank">LinkedIn: {linkedin_link}</a>
                </h4>
            """, unsafe_allow_html=True)

    # GitHub
    with st.container():
        col1, col2 = st.columns([0.1, 3])
        with col1:
            st.write(github_logo, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <h4>
                    <a href="{github_link}" target="_blank">GitHub: {github_link}</a>
                </h4>
            """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown('<p style="text-align:center; color:gray;">Designed by Sathvik Manthri | Powered by Streamlit</p>', unsafe_allow_html=True)
