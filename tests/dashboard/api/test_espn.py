import pytest
from dashboard.api.espn import ClientESPN

@pytest.fixture
def client():
    return ClientESPN()

def test_get_standings(client):
    assert len(client.get("standings")["children"]) == 2
    assert client.get("standings")["children"][0]["name"] == "Eastern Conference"
    assert client.get("standings")["children"][1]["name"] == "Western Conference"

