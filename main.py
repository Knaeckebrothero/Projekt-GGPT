import json
import yaml
from loldata import api_controller as con
import loldata as lol


def get_config(key: str):
    with open('development/config.yaml', 'r') as cfg:
        return yaml.safe_load(cfg)[key]
        cfg_file.close()


if __name__ == '__main__':
    api_key = get_config('apikey')
    # print(con.get_match("EUW1_6309535507", api_key)["metadata"]["dataVersion"])
    # print(type(con.get_match("EUW1_6309535507", api_key)))
    with open('development/example.json') as file:
        my_match = lol.MatchLearning(json.load(file), "O5Hjpoknb9hJdKLZ_8zn3aAMa2KFECQSE1HBOVKN_DekLXGu9zniF45BUKzb38dFhi3-u-cSYScNZg")
        print(type(my_match.won))

        file.close()
