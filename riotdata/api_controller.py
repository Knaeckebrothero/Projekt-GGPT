"""
This module contains the controller class which handles the communication with the riot games apis.
https://developer.riotgames.com/apis

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

import time
from dacite import from_dict
from development.development_functions import configure_custom_logger
from riotdata import MatchDto, MatchTimelineDto
from riotdata.apis import summoner_v4 as summoner
from riotdata.apis import match_v5 as match


# Primary api controller class
class ApiController:
    """
        Class containing all the attributes and methods used to communicate with the riot games api.
    """
    def __init__(self, api_key: str):
        """
            Args:
                api_key (str): The projects api key.
        """
        self._logger = configure_custom_logger(__name__)
        self.api_key = api_key
        self.rate_limits = {1: 20, 120: 100}
        self.rate_limit_counts = {1: 0, 120: 0}
        self.rate_limit_last_updated = {1: time.time(), 120: time.time()}

    # Resets rate limit counts if the duration has passed.
    def _reset_rate_limit_counts(self):
        current_time = time.time()
        for duration in self.rate_limits:
            if current_time - self.rate_limit_last_updated[duration] > duration:
                self.rate_limit_counts[duration] = 0
                self.rate_limit_last_updated[duration] = current_time

    # Wait before making a request if rate limits have been reached.
    def _wait_if_needed(self):
        for duration in self.rate_limits:
            if self.rate_limit_counts[duration] >= self.rate_limits[duration]:
                # Due to the experience of micro lag i´ve added a 0.1 second buffer.
                time_to_wait = duration - (time.time() - self.rate_limit_last_updated[duration]) + 0.1
                if time_to_wait > 0:
                    self._logger.log(20, f'Waiting {time_to_wait} seconds to stay within api rate limits')
                    time.sleep(time_to_wait)
                self.rate_limit_counts[duration] = 0
                self.rate_limit_last_updated[duration] = time.time()

    # Get puuid
    def get_puuid(self, summoner_name: str, server: str = 'euw1') -> tuple:
        """
            This function gets the puuid of a player from a SummonerDTO.

            Args:
                summoner_name (str): The player's summoner name.
                server (str): Server which the summoner is registered on.

            Returns:
                tuple (int, str): The status code and if the request was successful, the puuid.
        """
        # Call limiter functions to stay within api rate limitations.
        self._reset_rate_limit_counts()
        self._wait_if_needed()

        # Make api call
        response = summoner.get_summoner_by_name(self.api_key, summoner_name, server)

        # Update rate_limit_counts
        for duration in self.rate_limits:
            self.rate_limit_counts[duration] += 1

        # Return results
        if response.status_code == 200:
            return (response.status_code, response.json()["puuid"])
        else:
            self._logger.log(30, f'Failed requesting puuid, summoner name: {summoner_name}, '
                                 f'status: {response.status_code}')
            return (response.status_code, None)

    # Get match ids
    def get_match_ids(
            self, puuid: str, start: int, server: str = 'europe', start_time: float = 1672444800) -> tuple:
        """
                This function gets a list of up to 100 match ids.

                Args:
                    puuid (str): The puuid of the player.
                    start (int): The index where to start.
                    server (str): Server which the matches have been played on.
                    start_time (float): Epoch timestamp used for filtering.

                Returns:
                    tuple (int, list[str]) : The status code and if the request was successful, the match ids.
        """
        # Call limiter functions to stay within api rate limitations.
        self._reset_rate_limit_counts()
        self._wait_if_needed()

        # Make api call
        response = match.get_match_ids_by_puuid(
            api_key=self.api_key, puuid=puuid, start=start, match_type='ranked',
            count=100, server=server, start_time=start_time)

        # Update rate_limit_counts
        for duration in self.rate_limits:
            self.rate_limit_counts[duration] += 1

        # Return results
        if response.status_code == 200:
            return (response.status_code, list(response.json()))
        else:
            self._logger.log(30, f'Failed requesting match ids, puuid: {puuid}, '
                                 f'status: {response.status_code}')
            return (response.status_code, None)

    # Get match
    def get_match(self, match_id: str, server: str = 'europe') -> tuple:
        """
                This function gets a MatchDto.

                Args:
                    match_id (str): Id of the match.
                    server (str): Server which the matches have been played on.

                Returns:
                    tuple (int, MatchDto) : The status code and if the request was successful, the MatchDto.
        """
        # Call limiter functions to stay within api rate limitations.
        self._reset_rate_limit_counts()
        self._wait_if_needed()

        # Make api call
        response = match.get_match(self.api_key, match_id, server)

        # Update rate_limit_counts
        for duration in self.rate_limits:
            self.rate_limit_counts[duration] += 1

        # Return results
        if response.status_code == 200:
            return (response.status_code, from_dict(data_class=MatchDto, data=response.json()))
        else:
            self._logger.log(30, f'Failed requesting match, id: {match_id}, status: {response.status_code}')
            return (response.status_code, None)

    # Get match timeline
    def get_match_timeline(self, match_id: str, server: str = 'europe') -> tuple:
        """
                This function gets a MatchTimelineDto.

                Args:
                    match_id (str): Id of the match.
                    server (str): Server which the matches have been played on.

                Returns:
                    tuple (int, MatchTimelineDto) : The status code and if the request was successful,
                    the MatchTimelineDto.
        """
        # Call limiter functions to stay within api rate limitations.
        self._reset_rate_limit_counts()
        self._wait_if_needed()

        # Make api call
        response = match.get_match(self.api_key, match_id, server)

        # Update rate_limit_counts
        for duration in self.rate_limits:
            self.rate_limit_counts[duration] += 1

        # Return results
        if response.status_code == 200:
            return (response.status_code, from_dict(data_class=MatchTimelineDto, data=response.json()))
        else:
            self._logger.log(30, f'Failed requesting match timeline, id: {match_id}, '
                                 f'status: {response.status_code}')
            return (response.status_code, None)
