from database.db import BaseModel
from peewee import (CharField, TextField,
                    BooleanField, FloatField)


class ModelBook(BaseModel):
    title = CharField(max_length=255)
    body = TextField()
    price = FloatField()
    is_offer = BooleanField(null=True)

    class Meta:
        table_name = 'books'
