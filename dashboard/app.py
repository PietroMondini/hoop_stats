import streamlit as st

from components.standings import render_standings
from components.teams_roster import render_teams_roster

# Page configuration
st.set_page_config(
    page_title="Hoop Stats — Premium NBA Analytics",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main content: NBA Explorer tabs
explorer_tab1, explorer_tab2 = st.tabs(["📊 Conference Standings", "👥 Teams & Roster Directory"])

with explorer_tab1:
    render_standings()

with explorer_tab2:
    render_teams_roster()
