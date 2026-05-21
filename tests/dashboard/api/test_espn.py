import pytest
from dashboard.api.espn import ClientESPN

@pytest.fixture
def client():
    return ClientESPN()

def test_get_standings(client):
    standings = client.get_standings()
    east_standings = standings["children"][0]
    west_standings = standings["children"][1]

    # Check that there are two conferences
    assert len(standings["children"]) == 2

    # Check that the names of the conferences are correct
    assert east_standings["name"] == "Eastern Conference"
    assert west_standings["name"] == "Western Conference"

    # Check that there are 15 teams in each conference
    assert len(east_standings["standings"]["entries"]) == 15
    assert len(west_standings["standings"]["entries"]) == 15

def test_get_teams(client):
    teams = client.get_teams()
    assert len(teams["sports"][0]["leagues"][0]["teams"]) == 30

def test_get_roster(client):
    roster = client.get_roster(1)
    assert "athletes" in roster.keys()
    assert len(roster["athletes"]) >= 10
    for athlete in roster["athletes"]:
        keys = athlete.keys()
        for field in ["id", "fullName", "displayName", "position"]:
            assert field in keys
