"""
This module contains the main function.
The project is a machine learning based analysis tool for the video game League of Legends.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

from development.get_credentials import read_config
from loldata.api import match_v5 as con
import loldata as lol
from dacite import from_dict


def my_function(param1: int, param2: str) -> None:
    """
    This is a multi-line docstring that explains the purpose of the function.

    Args:
        param1 (int): This is the first parameter and should be an integer.
        param2 (str): This is the second parameter and should be a string.

    Returns:
        None: This function does not return anything.
    """
    # function body here


# Main function
if __name__ == '__main__':
    api_key = read_config('apikey')
    response = con.get_match("EUW1_6309535507", api_key)

    my_match = from_dict(data_class=lol.MatchDto, data=response)

    print("\n", type(my_match), "\n")

    """
    with open('development/example.json') as file:
        my_match = lol.MatchDto(json.load(file))
        print(type(my_match))

        file.close()
    """
