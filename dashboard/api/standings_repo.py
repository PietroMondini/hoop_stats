import pandas as pd
import streamlit as st

from .espn import ESPN

@st.cache_resource
def _get_espn_api():
    return ESPN()

class StandingsRepo:
    """
    Handles the retrieval and processing of sports standings data.

    This class is designed to interact with an external API to fetch standings
    data for sports teams. It processes the data into a structured format for
    convenient use in data analysis or presentation. The processed data is
    organized into a DataFrame.

    :ivar API: The external API client used to fetch standings data.
    :type API: ESPN
    """
    def __init__(self, api: ESPN = None):
        self.API = api or _get_espn_api()

    def get_standings(self) -> pd.DataFrame:
        """
        Fetches and processes standings data for teams in different conferences.

        This function retrieves standings data from an external client, processes the
        information, and organizes it into a pandas DataFrame. Each row in the DataFrame
        represents a team, including details such as conference, team name, wins, losses,
        winning percentage, games behind, playoff seed, and performance streaks.

        :return: A pandas DataFrame containing the processed standings data.
        :rtype: pd.DataFrame
        """

        data = self.API.get_standings()

        rows = []
        for conference in data["children"]:  # [0]=East, [1]=West
            abbr = conference["abbreviation"]  # "East" / "West"
            for entry in conference["standings"]["entries"]:
                team = entry["team"]
                stats = {s["name"]: s for s in entry["stats"]}  # ← key step

                rows.append({
                    "conference": abbr,
                    "id": team["id"],
                    "team": team["displayName"],
                    "abbr": team["abbreviation"],
                    "wins": int(stats["wins"]["value"]),
                    "losses": int(stats["losses"]["value"]),
                    "pct": float(stats["winPercent"]["value"]),
                    "gb": float(stats["gamesBehind"]["value"]),
                    "seed": int(stats["playoffSeed"]["value"]),
                    "streak": stats["streak"]["displayValue"],
                    "home": stats["Home"]["summary"],
                    "road": stats["Road"]["summary"],
                    "l10": stats["Last Ten Games"]["summary"],
                })
        return pd.DataFrame(rows)
