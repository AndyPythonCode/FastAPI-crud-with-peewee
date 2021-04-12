from typing import List
from peewee import (Model, SqliteDatabase)


class ConfigDatabase:
    db = SqliteDatabase('database/MyDB.db')

    def __init__(self, models: List[str]):
        self.models = models

    def refresh_tables(self):
        self.db.create_tables(self.models)


class BaseModel(Model):
    '''
    Para no tener que estar explificando a cada modelo
    '''
    class Meta:
        database = ConfigDatabase.db
