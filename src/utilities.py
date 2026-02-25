import os
import sys
import yaml
from sqlalchemy import create_engine 
def engin_creator():
    with open ('/home/korty/Code_House/VS_CODE/INSTAMART/credentials/database.yaml','r') as engine_obj:
        config = yaml.safe_load(engine_obj)
    
    config_database = config['database']

    db_url = f"mysql+mysqlconnector://{config_database['user']}:{config_database['password']}@{config_database['host']}:{config_database['port']}/{config_database['name']}"
    engine = create_engine(db_url)
    return engine
