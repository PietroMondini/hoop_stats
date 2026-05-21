import pytest, pandas as pd
from dashboard.api.standings_repo import StandingsRepo

@pytest.fixture
def repo():
    return StandingsRepo()

def test_get_standings(repo):
    standings = repo.get_standings()
    assert isinstance(standings, pd.DataFrame)
    for col in ['conference', 'id', 'team', 'abbr', 'wins', 'losses', 'pct', 'gb', 'seed', 'streak', 'home', 'road', 'l10']:
        assert col in standings.keys()
