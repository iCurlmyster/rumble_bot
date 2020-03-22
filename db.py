import os
import logging
from peewee import *

db_name = os.getenv('RUMBLE_DB')
if db_name == None:
    db_name = "testDB.db"

logging.info(f"DB: {db_name}")

db = SqliteDatabase(db_name)

class BaseModel(Model):
    class Meta:
        database = db


