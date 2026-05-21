import pytest, pandas as pd
from dashboard.repos.standings_repo import StandingsRepo

MOCK_STANDINGS = {
    "uid": "s:40~l:46~g:7",
    "id": "7",
    "name": "National Basketball Association",
    "season": {
        "year": 2026,
        "startDate": "2025-10-01T07:00Z",
        "endDate": "2026-06-27T06:59Z",
        "displayName": "2025-26",
    },
    "children": [
        {
            "uid": "s:40~l:46~g:5",
            "id": "5",
            "name": "Eastern Conference",
            "abbreviation": "East",
            "isConference": True,
            "standings": {
                "season": 2026,
                "seasonType": 2,
                "seasonDisplayName": "2025-26",
                "entries": [
                    {
                        "team": {
                            "id": "8",
                            "uid": "s:40~l:46~t:8",
                            "location": "Detroit",
                            "name": "Pistons",
                            "abbreviation": "DET",
                            "displayName": "Detroit Pistons",
                            "shortDisplayName": "Pistons",
                            "isActive": True,
                        },
                        "stats": [
                            {"name": "wins",             "value": 60.0,       "displayValue": "60"},
                            {"name": "losses",           "value": 22.0,       "displayValue": "22"},
                            {"name": "winPercent",       "value": 0.73170733, "displayValue": ".732"},
                            {"name": "gamesBehind",      "value": 0.0,        "displayValue": "-"},
                            {"name": "playoffSeed",      "value": 1.0,        "displayValue": "1"},
                            {"name": "streak",           "value": 3.0,        "displayValue": "W3"},
                            {"name": "clincher",         "value": 3.0,        "displayValue": "z"},
                            {"name": "avgPointsFor",     "value": 117.77,     "displayValue": "117.8"},
                            {"name": "avgPointsAgainst", "value": 109.61,     "displayValue": "109.6"},
                            {"name": "differential",     "value": 8.2,        "displayValue": "+8.2"},
                            {"id": "0",   "name": "overall",         "summary": "60-22", "displayValue": "60-22"},
                            {"id": "33",  "name": "Home",            "summary": "31-9",  "displayValue": "31-9"},
                            {"id": "34",  "name": "Road",            "summary": "28-13", "displayValue": "28-13"},
                            {"id": "60",  "name": "vs. Div.",        "summary": "12-4",  "displayValue": "12-4"},
                            {"id": "61",  "name": "vs. Conf.",       "summary": "39-13", "displayValue": "39-13"},
                            {"id": "901", "name": "Last Ten Games",  "summary": "8-2",   "displayValue": "8-2"},
                        ],
                    },
                    {
                        "team": {
                            "id": "1",
                            "uid": "s:40~l:46~t:1",
                            "location": "Atlanta",
                            "name": "Hawks",
                            "abbreviation": "ATL",
                            "displayName": "Atlanta Hawks",
                            "shortDisplayName": "Hawks",
                            "isActive": True,
                        },
                        "stats": [
                            {"name": "wins",             "value": 28.0,       "displayValue": "28"},
                            {"name": "losses",           "value": 54.0,       "displayValue": "54"},
                            {"name": "winPercent",       "value": 0.34146341, "displayValue": ".341"},
                            {"name": "gamesBehind",      "value": 32.0,       "displayValue": "32"},
                            {"name": "playoffSeed",      "value": 14.0,       "displayValue": "14"},
                            {"name": "streak",           "value": -2.0,       "displayValue": "L2"},
                            {"name": "clincher",         "value": 0.0,        "displayValue": ""},
                            {"name": "avgPointsFor",     "value": 112.45,     "displayValue": "112.5"},
                            {"name": "avgPointsAgainst", "value": 118.30,     "displayValue": "118.3"},
                            {"name": "differential",     "value": -5.85,      "displayValue": "-5.9"},
                            {"id": "0",   "name": "overall",         "summary": "28-54", "displayValue": "28-54"},
                            {"id": "33",  "name": "Home",            "summary": "16-25", "displayValue": "16-25"},
                            {"id": "34",  "name": "Road",            "summary": "12-29", "displayValue": "12-29"},
                            {"id": "60",  "name": "vs. Div.",        "summary": "7-9",   "displayValue": "7-9"},
                            {"id": "61",  "name": "vs. Conf.",       "summary": "15-37", "displayValue": "15-37"},
                            {"id": "901", "name": "Last Ten Games",  "summary": "4-6",   "displayValue": "4-6"},
                        ],
                    },
                ],
            },
        },
        {
            "uid": "s:40~l:46~g:6",
            "id": "6",
            "name": "Western Conference",
            "abbreviation": "West",
            "isConference": True,
            "standings": {
                "season": 2026,
                "seasonType": 2,
                "seasonDisplayName": "2025-26",
                "entries": [
                    {
                        "team": {
                            "id": "21",
                            "uid": "s:40~l:46~t:21",
                            "location": "Oklahoma City",
                            "name": "Thunder",
                            "abbreviation": "OKC",
                            "displayName": "Oklahoma City Thunder",
                            "shortDisplayName": "Thunder",
                            "isActive": True,
                        },
                        "stats": [
                            {"name": "wins",             "value": 68.0,       "displayValue": "68"},
                            {"name": "losses",           "value": 14.0,       "displayValue": "14"},
                            {"name": "winPercent",       "value": 0.82926829, "displayValue": ".829"},
                            {"name": "gamesBehind",      "value": 0.0,        "displayValue": "-"},
                            {"name": "playoffSeed",      "value": 1.0,        "displayValue": "1"},
                            {"name": "streak",           "value": 5.0,        "displayValue": "W5"},
                            {"name": "clincher",         "value": 3.0,        "displayValue": "z"},
                            {"name": "avgPointsFor",     "value": 122.10,     "displayValue": "122.1"},
                            {"name": "avgPointsAgainst", "value": 107.30,     "displayValue": "107.3"},
                            {"name": "differential",     "value": 14.8,       "displayValue": "+14.8"},
                            {"id": "0",   "name": "overall",         "summary": "68-14", "displayValue": "68-14"},
                            {"id": "33",  "name": "Home",            "summary": "36-5",  "displayValue": "36-5"},
                            {"id": "34",  "name": "Road",            "summary": "32-9",  "displayValue": "32-9"},
                            {"id": "60",  "name": "vs. Div.",        "summary": "14-2",  "displayValue": "14-2"},
                            {"id": "61",  "name": "vs. Conf.",       "summary": "44-8",  "displayValue": "44-8"},
                            {"id": "901", "name": "Last Ten Games",  "summary": "9-1",   "displayValue": "9-1"},
                        ],
                    },
                    {
                        "team": {
                            "id": "7",
                            "uid": "s:40~l:46~t:7",
                            "location": "Denver",
                            "name": "Nuggets",
                            "abbreviation": "DEN",
                            "displayName": "Denver Nuggets",
                            "shortDisplayName": "Nuggets",
                            "isActive": True,
                        },
                        "stats": [
                            {"name": "wins",             "value": 54.0,       "displayValue": "54"},
                            {"name": "losses",           "value": 28.0,       "displayValue": "28"},
                            {"name": "winPercent",       "value": 0.65853658, "displayValue": ".659"},
                            {"name": "gamesBehind",      "value": 14.0,       "displayValue": "14"},
                            {"name": "playoffSeed",      "value": 2.0,        "displayValue": "2"},
                            {"name": "streak",           "value": -1.0,       "displayValue": "L1"},
                            {"name": "clincher",         "value": 1.0,        "displayValue": "x"},
                            {"name": "avgPointsFor",     "value": 115.80,     "displayValue": "115.8"},
                            {"name": "avgPointsAgainst", "value": 111.20,     "displayValue": "111.2"},
                            {"name": "differential",     "value": 4.6,        "displayValue": "+4.6"},
                            {"id": "0",   "name": "overall",         "summary": "54-28", "displayValue": "54-28"},
                            {"id": "33",  "name": "Home",            "summary": "30-11", "displayValue": "30-11"},
                            {"id": "34",  "name": "Road",            "summary": "24-17", "displayValue": "24-17"},
                            {"id": "60",  "name": "vs. Div.",        "summary": "11-5",  "displayValue": "11-5"},
                            {"id": "61",  "name": "vs. Conf.",       "summary": "33-19", "displayValue": "33-19"},
                            {"id": "901", "name": "Last Ten Games",  "summary": "6-4",   "displayValue": "6-4"},
                        ],
                    },
                ],
            },
        },
    ],
}

@pytest.fixture
def mock_api(mocker):
    api = mocker.Mock()
    api.get_standings.return_value = MOCK_STANDINGS
    return api

@pytest.fixture
def repo(mock_api):
    return StandingsRepo(mock_api)

def test_get_standings(repo):
    standings = repo.get_standings()
    assert isinstance(standings, pd.DataFrame)
    for col in ['conference', 'id', 'team', 'abbr', 'wins', 'losses', 'pct', 'gb', 'seed', 'streak', 'home', 'road', 'l10']:
        assert col in standings.keys()
