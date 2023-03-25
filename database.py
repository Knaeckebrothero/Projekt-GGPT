import pymongo
import yaml
from pymongo.server_api import ServerApi


def get_config(key: str):
    with open('development/config.yaml', 'r') as cfg:
        return yaml.safe_load(cfg)[key]
        cfg_file.close()


client = pymongo.MongoClient("mongodb+srv://{}:{}@projekt-analysistool.pfdmf3o.mongodb.net/"
                             "?retryWrites=true&w=majority".format('admin', get_config('admin'),
                                                                   server_api=ServerApi('1')))

print(client.test)
print(client.list_database_names())
