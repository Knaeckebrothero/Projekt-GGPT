import logging
import time
from development.get_credentials import read_config
from riotdata.apis import summoner_v4


# Defines a custom logger, login into a log file.
def configure_custom_logger():
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler = logging.FileHandler("./development/api.log")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(read_config('loggingLevel'))
    return logger


class ApiController:
    def __init__(self, api_key: str):
        self._logger = configure_custom_logger()
        self.api_key = api_key
        self.last_request_time = 0
        self.last_minute_request_time = 0
        self._logger.log(10, 'Class initiated')

    # Extract rate info
    @staticmethod
    def _parse_headers(response_headers):
        """
            This function extracts the rate limit and count from a request headers field.

            Args:
                response_headers: The response headers from a request.

            Returns:
                rate_limits (dict): X-App-Rate-Limit from the apis response headers.
                rate_limit_counts (dict): X-App-Rate-Limit-Count from the apis response headers.
        """
        rate_limit = response_headers["X-App-Rate-Limit"].split(',')
        rate_limit_count = response_headers["X-App-Rate-Limit-Count"].split(',')
        rate_limits = {}
        rate_limit_counts = {}

        for limit in rate_limit:
            count, duration = limit.split(':')
            rate_limits[int(duration)] = int(count)

        for count in rate_limit_count:
            count, duration = count.split(':')
            rate_limit_counts[int(duration)] = int(count)

        return rate_limits, rate_limit_counts

    # Request rate buffer
    def _wait_if_needed(self, rate_limits, rate_limit_counts):
        """
                This function ensures that the apis request rate does stay within limitations.
                Prevents statuscode 429 (Rate limit exceeded) from happening.

                Args:
                    rate_limits (dict): X-App-Rate-Limit from the apis response headers.
                    rate_limit_counts (dict): X-App-Rate-Limit-Count from the apis response headers.
            """
        current_time = time.time()

        for duration in rate_limits.keys():
            if duration not in rate_limit_counts:
                continue

            if rate_limit_counts[duration] >= rate_limits[duration]:
                time_to_wait = max(0, duration - (current_time - self.last_request_time))
                self._logger.log(10, 'Waiting ' + str(time_to_wait) + ' seconds to stay within response limit...')
                time.sleep(time_to_wait)

                if duration == 1:
                    self.last_request_time = time.time()

    # Get puuid by summoner name.
    def get_puuid(self, name: str):
        """
            This function gets the puuid from a SummonerDTO by using the summoner-V4 apis.

            Args:
                name (str): The summoner name

            Returns:
                status_code (int): Api response code
                puuid (str): Puuid as a string if exists.
        """
        self._logger.log(10, 'Getting puuid for ('+name+')')
        response = summoner_v4.get_summoner_by_name(name, self.api_key)

        rate_limits, rate_limit_counts = self._parse_headers(response.headers)
        self._wait_if_needed(rate_limits, rate_limit_counts)

        if response.status_code == 200:
            return response.status_code, response.json()["puuid"]
        else:
            self._logger.log(30, 'Issue during api call response code '+str(response.status_code))
            return response.status_code, None
