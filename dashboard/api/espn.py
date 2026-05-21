import requests
from datetime import datetime

class ClientESPN:
    """
    A client for interacting with the ESPN API specific to NBA basketball.

    This class is used to retrieve NBA-related data from the ESPN API, including
    standings and other related resources.
    """

    def __init__(self):
        self.BASE_URL = "https://site.api.espn.com/apis/v2/sports/basketball/nba"

    def get(self, endpoint: str) -> dict:
        """
        Retrieves data from the specified API endpoint using an HTTP GET request.
        The response is returned in JSON format.

        :param endpoint: The specific API endpoint to send the GET request to.
        :type endpoint: str
        :return: The response from the API encoded in JSON format.
        """
        response = requests.get(f"{self.BASE_URL}/{endpoint}", timeout=30)
        response.raise_for_status()
        return response.json()