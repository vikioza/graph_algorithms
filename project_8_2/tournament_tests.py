import pytest
from tournament import Tournament
from tournament import InvalidTeamCount

def TestTournament():
    
    def test_odd_number_of_teams():
        with pytest.raises(InvalidTeamCount):
            tour = Tournament(5)