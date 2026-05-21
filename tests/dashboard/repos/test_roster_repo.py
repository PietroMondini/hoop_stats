import pytest
import pandas as pd
from dashboard.repos.roster_repo import RosterRepo

MOCK_ROSTER = {
    "athletes": [
        {
            "id": "1966",
            "firstName": "Jayson",
            "lastName": "Tatum",
            "fullName": "Jayson Tatum",
            "displayName": "Jayson Tatum",
            "position": {
                "abbreviation": "SF",
                "name": "Small Forward",
                "displayName": "Small Forward",
            },
            "headshot": {"href": "https://a.espncdn.com/i/headshots/nba/players/full/4065648.png"},
            "status": {"name": "Active", "type": "active"},
        },
        {
            "id": "3934672",
            "firstName": "Jaylen",
            "lastName": "Brown",
            "fullName": "Jaylen Brown",
            "displayName": "Jaylen Brown",
            "position": {
                "abbreviation": "SG",
                "name": "Shooting Guard",
                "displayName": "Shooting Guard",
            },
            "headshot": {"href": "https://a.espncdn.com/i/headshots/nba/players/full/3917376.png"},
            "status": {"name": "Active", "type": "active"},
        },
    ]
}


@pytest.fixture
def repo(mocker):
    mock_api = mocker.Mock()
    mock_api.get_roster.return_value = MOCK_ROSTER
    return RosterRepo(api=mock_api)


def test_get_roster_returns_dataframe(repo):
    assert isinstance(repo.get_roster(2), pd.DataFrame)


def test_get_roster_has_expected_columns(repo):
    df = repo.get_roster(2)
    for col in ["id", "name", "position", "headshot", "status"]:
        assert col in df.columns


def test_get_roster_row_count(repo):
    df = repo.get_roster(2)
    assert len(df) == 2


def test_get_roster_passes_team_id(repo, mocker):
    repo.get_roster(13)
    repo.API.get_roster.assert_called_once_with(13)