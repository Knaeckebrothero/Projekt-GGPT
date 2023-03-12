# Class representing a league game
class Match:

    def __init__(self, match_dto: dict):
        self.participants = match_dto["metadata"]["participants"]


# Modified variant better suited for machine learning, looking at the match from a player perspective.
class MatchLearning(Match):

    def __init__(self, match_dto: dict, puu_id: str):
        super().__init__(match_dto)
        self.won = match_dto["info"]["participants"][match_dto["metadata"]["participants"].index(puu_id)]["win"]
