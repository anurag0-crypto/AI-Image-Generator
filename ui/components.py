import streamlit as st

def apply_css():

    st.markdown("""
    <style>

    .main {
        padding-top: 1rem;
    }

    h1 {
        text-align:center;
    }

    footer {
        visibility:hidden;
    }

    </style>
    """,
    unsafe_allow_html=True)

def header():

    st.title("🎨 AI Image Generator")



