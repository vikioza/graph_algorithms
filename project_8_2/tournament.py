class TournamentException(BaseException):
    
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

class InvalidTeamCount(TournamentException):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Tournament:
    graph: object
    
    def __init__(self, team_count):
        if team_count % 2:
            raise InvalidTeamCount("Team count has to be a multiple of 2")
        self.team_count = team_count
        self.day_count = 2 * (self.team_count - 1)
        self.__generate_graph()
        
    def __generate_graph(self):
        self.graph = None
        for idx in range(1, self.day_count+1):  # actually move this to graph class
            # TODO some logic for adding edges
            pass
        

if __name__ == "__main__":  # Test scenarios
    pass