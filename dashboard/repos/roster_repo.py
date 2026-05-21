import pandas as pd
import streamlit as st

from dashboard.api.espn import ESPN


@st.cache_resource
def _get_espn_api():
    return ESPN()


class RosterRepo:
    """
    Handles the retrieval and processing of sports roster data.

    This class interacts with the ESPN API to fetch and process player roster data
    for a specific team into a structured pandas DataFrame.
    """
    def __init__(self, api: ESPN = None):
        self.API = api or _get_espn_api()

    def get_roster(self, team_id: int) -> pd.DataFrame:
        """
        Fetches roster data for a specific team and structures it into a pandas DataFrame.

        :param team_id: The unique ID of the team whose roster is being requested.
        :type team_id: int
        :return: A DataFrame containing columns: id, name, position, headshot, and status.
        :rtype: pd.DataFrame
        """
        data = self.API.get_roster(team_id)
        athletes = data.get("athletes", [])
        
        rows = []
        for athlete in athletes:
            headshot = athlete.get("headshot")
            headshot_url = headshot.get("href", "") if headshot else ""
            
            position = athlete.get("position")
            position_abbr = position.get("abbreviation", "") if position else ""
            
            status = athlete.get("status")
            status_type = status.get("type", "") if status else ""

            rows.append({
                "id": athlete["id"],
                "name": athlete["displayName"],
                "position": position_abbr,
                "headshot": headshot_url,
                "status": status_type,
            })
        return pd.DataFrame(rows)
