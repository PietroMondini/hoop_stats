import pandas as pd
import streamlit as st

from dashboard.repos.teams_repo import TeamsRepo
from dashboard.repos.roster_repo import RosterRepo

@st.cache_data(ttl=3600)
def load_teams_data():
    return TeamsRepo().get_teams()

@st.cache_data(ttl=3600)
def load_roster_data(team_id: int):
    return RosterRepo().get_roster(team_id)

def _player_card(player: dict) -> None:
    with st.container():
        col_img, col_txt = st.columns([1, 4], gap="small")
        with col_img:
            headshot = (
                player.get("headshot")
                or "https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/placeholder.png"
            )
            st.image(headshot, width=80)
        with col_txt:
            st.markdown(f"**{player.get('name', 'Unnamed')}**")
            st.caption(f"Pos: {player.get('position', '').upper()}")

def render_teams_roster() -> None:

    df_teams = load_teams_data()

    # Dropdown selector
    team_names = ["-- Select a Team to View Roster --"] + list(df_teams["name"].sort_values())
    selected_name = st.selectbox("Search / Filter Team Roster:", team_names, label_visibility="collapsed")

    if selected_name != "-- Select a Team to View Roster --":
        # Show selected team banner
        team_row = df_teams[df_teams["name"] == selected_name].iloc[0]
        team_id = int(team_row["id"])

        if st.button("← Back to All Teams"):
            st.rerun()

        col_logo, col_info = st.columns([1, 3])
        with col_logo:
            st.image(team_row["logo"], width=120)
        with col_info:
            st.subheader(team_row["name"])
            st.write(f"{team_row['city']} | {team_row['abbr']}")

        # Load and display roster
        with st.spinner("Fetching active team roster…"):
            df_roster = load_roster_data(team_id)

        if df_roster.empty:
            st.info("No active roster data available for this team at the moment.")
        else:
            st.subheader(f"Active Roster ({len(df_roster)} Players)")
            n_per_row = 4
            rows = (len(df_roster) + n_per_row - 1) // n_per_row
            for r in range(rows):
                cols = st.columns(n_per_row)
                for c, (_, player) in zip(cols, df_roster.iloc[r*n_per_row:(r+1)*n_per_row].iterrows()):
                    with c:
                        _player_card(player.to_dict())
    else:
        # Show all NBA franchises in a grid
        st.subheader("NBA Franchises")
        n_per_row = 5
        rows = (len(df_teams) + n_per_row - 1) // n_per_row
        for r in range(rows):
            cols = st.columns(n_per_row)
            for c, (_, team) in zip(cols, df_teams.iloc[r*n_per_row:(r+1)*n_per_row].iterrows()):
                with c:
                    st.image(team["logo"], width=80)
                    st.caption(team["name"])
