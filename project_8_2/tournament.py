class TournamentException(BaseException):
    
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

class InvalidTeamCount(TournamentException):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Tournament:
    
    def __init__(self, team_count):
        if team_count % 2:
            raise InvalidTeamCount("Team count has to be a multiple of 2")
        self.team_count = team_count
        
        


if __name__ == "__main__":  # Test scenarios
    def test_1():
        tour = Tournament(5)
        
    def test_2():
        pass
    
    test_1()
