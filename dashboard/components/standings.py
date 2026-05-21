import streamlit as st
import pandas as pd
from dashboard.repos.standings_repo import StandingsRepo

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------
# Mapping of raw dataframe columns to display-friendly names.
# Adjust these keys to match the columns returned by StandingsRepo.
DISPLAY_COLUMNS = {
    "logo": "Logo",
    "team": "Team",
    "wins": "W",
    "losses": "L",
    "pct": "PCT",
    "streak": "Streak",
}

# ---------------------------------------------------------------------
# Data loading (cached for 1 hour)
# ---------------------------------------------------------------------
@st.cache_data(ttl=3600)
def load_standings_data() -> pd.DataFrame:
    """Fetch the latest standings DataFrame from the repository."""
    return StandingsRepo().get_standings()

# ---------------------------------------------------------------------
# Helper: render a single conference block using Streamlit primitives
# ---------------------------------------------------------------------
def _render_conference(conf_df: pd.DataFrame, conference_name: str) -> None:
    """Render a conference table using ``st.dataframe``.

    * The table is displayed in a centered column so it does not span the full
      screen width (approximately 80% of the page).
    * Column headers align correctly because we rely on Streamlit's built‑in
      ``st.dataframe`` widget.
    * The widget is interactive – users can sort by any column by clicking the
      header.
    * The ``logo`` column is rendered as an image via ``st.column_config.ImageColumn``.
    * The ``streak`` column receives a green/red colour based on its value using a
      pandas ``Styler``.
    """
    st.subheader(f"{conference_name} Conference")

    # Select and rename columns for display
    display = (
        conf_df[list(DISPLAY_COLUMNS.keys())]
        .rename(columns=DISPLAY_COLUMNS)
        .reset_index(drop=True)
    )

    # Format percentage column
    if "PCT" in display.columns:
        display["PCT"] = display["PCT"].apply(lambda x: f"{x:.3f}" if pd.notnull(x) else "")

    # Optionally format streak column with emojis for better visual cues
    def _streak_format(val):
        if isinstance(val, str):
            if "W" in val.upper():
                return "✅ " + val
            if "L" in val.upper():
                return "❌ " + val
        return val

    display["Streak"] = display["Streak"].apply(_streak_format)

    # Center the table so it does not take the full width
    left, middle, right = st.columns([1, 3, 1])
    def _streak_style(val):
        if isinstance(val, str) and "W" in val.upper():
            return "color: #34d399; font-weight: bold;"
        if isinstance(val, str) and "L" in val.upper():
            return "color: #f87171; font-weight: bold;"
        return ""

    # Center the table so it does not take the full width
    left, middle, right = st.columns([1, 3, 1])
    with middle:
        st.dataframe(
            display,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Logo": st.column_config.ImageColumn("Logo", width="small"),
                "Team": st.column_config.TextColumn("Team", width="medium"),
            },
            height="content"
        )

# ---------------------------------------------------------------------
# Main entry point – used by dashboard/app.py
# ---------------------------------------------------------------------
def render_standings() -> None:
    """Display Eastern and Western conference standings in two tabs.
    All UI is built with native Streamlit components, so the look follows the
    active Streamlit theme and the table is sortable and centered.
    """
    df = load_standings_data()
    east = df[df["conference"] == "East"].sort_values("seed")
    west = df[df["conference"] == "West"].sort_values("seed")
    tab_east, tab_west = st.tabs(["Eastern Conference", "Western Conference"])
    with tab_east:
        _render_conference(east, "Eastern")
    with tab_west:
        _render_conference(west, "Western")