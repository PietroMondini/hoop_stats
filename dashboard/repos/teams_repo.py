import pandas as pd
import streamlit as st

from dashboard.api.espn import ESPN


@st.cache_resource
def _get_espn_api():
    return ESPN()


class TeamsRepo:
    def __init__(self, api: ESPN = None):
        self.API = api or _get_espn_api()

    def get_teams(self) -> pd.DataFrame:
        data = self.API.get_teams()
        teams = data["sports"][0]["leagues"][0]["teams"]
        rows = []
        for item in teams:
            t = item["team"]
            logo = next(
                (l["href"] for l in t.get("logos", []) if "500" in l["href"]),
                t.get("logos", [{}])[0].get("href", ""),
            )
            rows.append({
                "id":    t["id"],
                "abbr":  t["abbreviation"],
                "name":  t["displayName"],
                "city":  t["location"],
                "color": t.get("color", ""),
                "logo":  logo,
            })
        return pd.DataFrame(rows)