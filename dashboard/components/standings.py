import streamlit as st
import pandas as pd

_HEADERS = ["#", "Team", "W", "L", "PCT", "GB", "Streak", "Home", "Road", "L10"]
_COLS    = ["seed", "team", "wins", "losses", "pct", "gb", "streak", "home", "road", "l10"]

_CSS = """
<style>
.standings { width:100%; border-collapse:collapse; font-size:0.9rem; }
.standings th { text-align:left; padding:6px 12px; border-bottom:2px solid #e0e0e0; color:#888; font-weight:600; }
.standings td { padding:6px 12px; border-bottom:1px solid #f0f0f0; white-space:nowrap; }
.standings tr:last-child td { border-bottom:none; }
.standings img { height:28px; vertical-align:middle; margin-right:10px; object-fit:contain; }
</style>
"""

def render_standings(df: pd.DataFrame) -> None:
    east = df[df["conference"] == "East"].sort_values("seed")
    west = df[df["conference"] == "West"].sort_values("seed")

    tab_east, tab_west = st.tabs(["Eastern Conference", "Western Conference"])
    with tab_east:
        _render_table(east)
    with tab_west:
        _render_table(west)


def _render_table(conf_df: pd.DataFrame) -> None:
    header_row = "<tr>" + "".join(f"<th>{h}</th>" for h in _HEADERS) + "</tr>"

    body_rows = []
    for _, row in conf_df.iterrows():
        logo = f'<img src="{row["logo"]}" alt="{row["abbr"]}">'
        cells = [
            f"<td>{row['seed']}</td>",
            f"<td>{logo}{row['team']}</td>",
            f"<td>{row['wins']}</td>",
            f"<td>{row['losses']}</td>",
            f"<td>{row['pct']:.3f}</td>",
            f"<td>{row['gb']}</td>",
            f"<td>{row['streak']}</td>",
            f"<td>{row['home']}</td>",
            f"<td>{row['road']}</td>",
            f"<td>{row['l10']}</td>",
        ]
        body_rows.append("<tr>" + "".join(cells) + "</tr>")

    st.html(f"""
        {_CSS}
        <table class="standings">
            <thead>{header_row}</thead>
            <tbody>{"".join(body_rows)}</tbody>
        </table>
    """)