"""
This module holds a function to map servers and regions.
https://developer.riotgames.com/apis

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""


# Get region of server
def map_server_region(server: str) -> str:
    """
    This function helps to find out to which region a given server belongs.

    Args:
        server (str): A server, used to get a summonerDto.

    Returns:
        server (str): The region the given server belongs to.
    """
    # Haven't fully tested the mapping yet xD
    match server:
        case 'br1':  # Valid
            return 'americas'
        case 'eun1':  # Valid
            return 'europe'
        case 'euw1':  # Valid
            return 'europe'
        case 'jp1':
            return 'asia'
        case 'la1':  # Valid
            return 'americas'
        case 'la2':  # Valid
            return 'americas'
        case 'na1':  # Valid
            return 'americas'
        case 'oc1':
            return 'sea'
        case 'ph2':
            return 'asia'
        case 'ru':  # Valid
            return 'europe'
        case 'sg2':
            return 'asia'
        case 'th2':
            return 'asia'
        case 'tr1':
            return 'europe'
        case 'tw2':
            return 'asia'
        case 'vn2':
            return 'asia'
        case _:
            return 'moon'
