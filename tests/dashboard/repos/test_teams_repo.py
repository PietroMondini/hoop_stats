import pytest
import pandas as pd
from dashboard.repos.teams_repo import TeamsRepo

MOCK_TEAMS = {
    "sports": [
        {
            "leagues": [
                {
                    "teams": [
                        {
                            "team": {
                                "id": "1",
                                "abbreviation": "ATL",
                                "displayName": "Atlanta Hawks",
                                "location": "Atlanta",
                                "color": "c8102e",
                                "logos": [{"href": "https://a.espncdn.com/i/teamlogos/nba/500/atl.png"}],
                            }
                        },
                        {
                            "team": {
                                "id": "2",
                                "abbreviation": "BOS",
                                "displayName": "Boston Celtics",
                                "location": "Boston",
                                "color": "007a33",
                                "logos": [{"href": "https://a.espncdn.com/i/teamlogos/nba/500/bos.png"}],
                            }
                        },
                    ]
                }
            ]
        }
    ]
}


@pytest.fixture
def repo(mocker):
    mock_api = mocker.Mock()
    mock_api.get_teams.return_value = MOCK_TEAMS
    return TeamsRepo(api=mock_api)


def test_get_teams_returns_dataframe(repo):
    assert isinstance(repo.get_teams(), pd.DataFrame)


def test_get_teams_has_expected_columns(repo):
    df = repo.get_teams()
    for col in ["id", "abbr", "name", "city", "color", "logo"]:
        assert col in df.columns


def test_get_teams_row_count(repo):
    df = repo.get_teams()
    assert len(df) == 2