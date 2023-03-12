import json
from loldata import api_controller as con
import loldata as lol

if __name__ == '__main__':
    with open('api_key.txt') as api_key:

        #print(con.get_match("EUW1_6309535507", api_key)["metadata"]["dataVersion"])
        # print(type(con.get_match("EUW1_6309535507", api_key)))

        with open('example.json') as file:
            my_match = lol.MatchLearning(json.load(file), "O5Hjpoknb9hJdKLZ_8zn3aAMa2KFECQSE1HBOVKN_DekLXGu9zniF45BUKzb38dFhi3-u-cSYScNZg")
            print(type(my_match.won))

            file.close()
    file.close()
