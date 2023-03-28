"""
This module contains the main function.
The project is a machine learning based analysis tool for the video game League of Legends.

Product -- GetGood.GG
https://github.com/Knaeckebrothero/Projekt-GetGood.GG
App ID -- 616160
https://developer.riotgames.com/
"""

from development.get_credentials import read_config
from loldata import api_controller as con
import loldata as lol
from dacite import from_dict

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
