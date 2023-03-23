import json
import yaml
from loldata import api_controller as con
import loldata as lol
from dacite import from_dict


def get_config(key: str):
    with open('development/config.yaml', 'r') as cfg:
        return yaml.safe_load(cfg)[key]
        cfg_file.close()


if __name__ == '__main__':
    api_key = get_config('apikey')

    my_match = from_dict(data_class=lol.MatchDto, data=con.get_match("EUW1_6309535507", api_key))

    print(type(my_match))

    """
    with open('development/example.json') as file:
        my_match = lol.MatchDto(json.load(file))
        print(type(my_match))

        file.close()
    """
