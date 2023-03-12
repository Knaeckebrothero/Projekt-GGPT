import requests as rq


# Gets the puuid by summoner name
def get_puuid(name: str, api_key: str):
    response = rq.get(
        "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(name),
        headers={"X-Riot-Token": api_key})
    return response.json()["puuid"]


# Gets a match by id
def get_match(match_id: str, api_key: str):
    response = rq.get("https://europe.api.riotgames.com/lol/match/v5/matches/{}".format(match_id),
                      headers={"X-Riot-Token": api_key})
    return response.json()
