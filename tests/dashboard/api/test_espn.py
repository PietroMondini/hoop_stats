import pytest
from dashboard.api.espn import ClientESPN

@pytest.fixture
def client():
    return ClientESPN()

def test_get_standings(client):
    standings = client.get_standings()
    assert len(standings["children"]) == 2
    assert standings["children"][0]["name"] == "Eastern Conference"
    assert standings["children"][1]["name"] == "Western Conference"

def test_get_teams(client):
    teams = client.get_teams()
    assert len(teams["sports"][0]["leagues"][0]["teams"])


