from dataclasses import dataclass, field


class TournamentException(BaseException):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class InvalidTeamCount(TournamentException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


@dataclass
class Match:
    round: int
    day: int
    visiting_team: str
    homeground_team: str
    label: str = field(init=False, repr=False)

    def generate_label(self):
        self.label = f"{self.day}:{self.visiting_team}->{self.homeground_team}"


class Tournament:
    teams: list[str]
    matches: dict[
        str, dict[str, Match]
    ] = {}  # round top level, nested match.label: match
    violations_count: int = 0

    def __init__(self, team_labels: list[str], rounds_count: int = 2):
        self.teams = team_labels
        self.team_count = len(self.teams)
        self.half_count = int(self.team_count / 2)

        if self.team_count % 2:  # 2N teams required for the tournament
            raise InvalidTeamCount("Team count has to be a multiple of 2")

        self.rounds_count = rounds_count  # each round is day_count days long

        # 2(2N - 1) days total, (2N - 1) days per round
        # each day will have N matches
        self.day_count = self.team_count - 1

        self.__generate_graph()

    def __generate_graph(self):
        for round in range(1, self.rounds_count + 1):
            print(f"ROUND {round}")
            self.matches[str(round)] = {}
            self.__generate_round_schedule(round)

    def __generate_round_schedule(self, round: int):
        team_labels = self.teams
        for day in range(1, self.day_count + 1):
            print(f"DAY {day}")
            team_labels = self.__select_daily_matches(team_labels, round, day)

    def __select_daily_matches(self, team_labels, round, day):
        first_element = team_labels[0]
        remaining_labels = team_labels[1:]

        append_to_first = int((self.team_count - 2) / 2)
        append_list = remaining_labels[:append_to_first]

        first_list = [first_element] + append_list
        second_list = list(reversed(remaining_labels[append_to_first:]))

        if day <= (self.half_count - 1):
            second_element = self.teams[1]
            idx = first_list.index(second_element)
            tmp = second_list[idx]
            second_list[idx] = first_list[idx]
            first_list[idx] = tmp

        if round == 1:
            if day % 2 == 1:
                for idx in range(self.half_count):
                    self.__create_match(round, day, first_list[idx], second_list[idx])
            else:
                for idx in range(self.half_count):
                    self.__create_match(round, day, second_list[idx], first_list[idx])
        else:
            if day % 2 == 1:
                for idx in range(self.half_count):
                    self.__create_match(round, day, second_list[idx], first_list[idx])
            else:
                for idx in range(self.half_count):
                    self.__create_match(round, day, first_list[idx], second_list[idx])

        # prepare next round list
        last_element = remaining_labels[-1]
        remaining_labels.remove(last_element)
        new_labels = [first_element, last_element] + remaining_labels
        return new_labels

    def __create_match(self, round: int, day: int, visiting: str, homeground: str):
        print(f"Creating match {visiting} -> {homeground}")
        match = Match(
            round=round, day=day, visiting_team=visiting, homeground_team=homeground
        )
        match.generate_label()
        self.matches[str(round)][match.label] = match


if __name__ == "__main__":  # Test scenarios
    teams = ["a", "b", "c", "d", "e", "f"]
    tour = Tournament(teams)
    print(tour.teams)
