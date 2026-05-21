import streamlit as st
import pandas as pd

DISPLAY_COLUMNS = {
    "logo":   "Logo",
    "team":   "Team",
    "seed":   "#",
    "wins":   "W",
    "losses": "L",
    "pct":    "PCT",
    "gb":     "GB",
    "streak": "Streak",
    "home":   "Home",
    "road":   "Road",
    "l10":    "L10",
}

def render_standings(df: pd.DataFrame) -> None:
    east = df[df["conference"] == "East"].sort_values("seed")
    west = df[df["conference"] == "West"].sort_values("seed")

    tab_east, tab_west = st.tabs(["Eastern Conference", "Western Conference"])

    with tab_east:
        _render_table(east)
    with tab_west:
        _render_table(west)


def _render_table(conf_df: pd.DataFrame) -> None:
    display = (
        conf_df[list(DISPLAY_COLUMNS.keys())]
        .rename(columns=DISPLAY_COLUMNS)
        .reset_index(drop=True)
    )
    st.dataframe(
        display,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Logo": st.column_config.ImageColumn("Logo", width="small"),
        },
    )