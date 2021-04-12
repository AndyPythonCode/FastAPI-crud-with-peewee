from pydantic import BaseModel
from typing import Optional


class SchemasBook(BaseModel):
    title: str
    body: str
    price: float
    is_offer: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "title": "World Api",
                "body": "everything you need to know about api",
                "price": 12.4,
                "is_offer": False,
            }
        }
