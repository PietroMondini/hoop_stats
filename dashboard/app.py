from repos.standings_repo import StandingsRepo
from components.standings import render_standings
import streamlit as st

@st.cache_data(ttl=3600)
def get_standings():
    return StandingsRepo().get_standings()

st.title("NBA Explorer")
render_standings(get_standings())