import os
import logging
from peewee import *

db_name = os.getenv('RUMBLE_DB')
if db_name == None:
    raise Exception("DB_ERROR", "Must set the RUMBLE_DB environment variable with an appropriate database name")

logging.info(f"DB: {db_name}")

db = SqliteDatabase(db_name)

class BaseModel(Model):
    class Meta:
        database = db


