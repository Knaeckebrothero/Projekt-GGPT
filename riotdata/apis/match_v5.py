"""
This module holds riot games apis belonging to the match category.
https://developer.riotgames.com/apis#match-v5

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

import requests
from dacite import from_dict
from riotdata import MatchDto
from riotdata import MatchTimelineDto


# Get a list of match ids by puuid.
def get_match_ids_by_puuid(
        api_key: str,
        puuid: str,
        start: int,
        match_type: str = 'ranked',
        count: int = 100,
        server: str = 'europe',
        start_time: float = 1672444800) -> requests.models.Response:
    return requests.get(
        "https://{}.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?startTime={}&type={}start={}&count={}"
        .format(server, puuid, start_time, match_type, start, count), headers={"X-Riot-Token": api_key})


# Get a match by match id.
def get_match(api_key: str, match_id: str, server: str = 'europe') -> requests.models.Response:
    return requests.get(
        "https://{}.api.riotgames.com/lol/match/v5/matches/{}"
        .format(server, match_id), headers={"X-Riot-Token": api_key})


# Get a match timeline by match id.
def get_match_timeline(
        api_key: str, match_id: str, server: str = 'europe') -> requests.models.Response:
    return requests.get(
        "https://{}.api.riotgames.com/lol/match/v5/matches/{}/timeline"
        .format(server, match_id), headers={"X-Riot-Token": api_key})
