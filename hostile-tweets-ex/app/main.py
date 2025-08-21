from fastapi import FastAPI
import os
from db.connector import MongoDBAtlasConnection
from db.dal import MongoDAL
from processors.rare_word_processor import RareWordProcessor
from processors.sentiment_processor import SentimentProcessor
from processors.weapon_processor import WeaponProcessor
from manager import Manager

app = FastAPI()

connector = MongoDBAtlasConnection()
dal = MongoDAL()
rare_word_processor = RareWordProcessor()
sentiment_processor = SentimentProcessor()
weapon_list_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'weapon_list.txt'))
weapon_processor = WeaponProcessor(weapon_list_path=weapon_list_path)
manager = Manager(
    connector,
    dal,
    rare_word_processor,
    sentiment_processor,
    weapon_processor
)

@app.get("/records")
def get_processed_records():
    processed = manager.process_records("tweets")
    return {"records": processed}