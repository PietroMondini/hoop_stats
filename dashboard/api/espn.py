import requests
from datetime import datetime

class ESPN:
    """
    A client for interacting with the ESPN API specific to NBA basketball.

    This class is used to retrieve NBA-related data from the ESPN API, including
    standings and other related resources.
    """

    def __init__(self):
        self.BASE_URL = "https://site.api.espn.com/apis/v2/sports/basketball/nba"
        self.BASE_SITE_URL = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba"
        self.BASE_ROSTER_URL = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams"

    def get_standings(self) -> dict:
        return self._get(self.BASE_URL, "standings")

    def get_teams(self) -> dict:
        return self._get(self.BASE_SITE_URL, "teams")

    def get_roster(self, team_id: int) -> dict:
        return self._get(self.BASE_ROSTER_URL, f"{team_id}/roster")

    @staticmethod
    def _get(base_url: str, endpoint: str) -> dict:
        """
        Retrieves data from the specified API endpoint using an HTTP GET request.
        The response is returned in JSON format.

        :param endpoint: The specific API endpoint to send the GET request to.
        :type endpoint: str
        :return: The response from the API encoded in JSON format.
        """
        response = requests.get(f"{base_url}/{endpoint}", timeout=30)
        response.raise_for_status()
        return response.json()