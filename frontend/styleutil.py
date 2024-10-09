import streamlit as st
from pathlib import Path


def cssstyle():
    css_path = Path(__file__).parents[0] / "style.css"

    with open(css_path) as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )

