import pytest
from tournament import Tournament
from tournament import InvalidTeamCount

class TestTournament:
    
    def test_odd_number_of_teams(self):
        with pytest.raises(InvalidTeamCount):
            tour = Tournament(5)
            
    def test_even_number_of_teams(self):
        tour = Tournament(4)
        assert tour.team_count == 4