from fastapi import status
from fastapi.responses import JSONResponse
from peewee import DoesNotExist
from functools import wraps

"""
    functools es un módulo estándar de Python para funciones de orden superior 
    (funciones que actúan sobre otras funciones o las devuelven). wraps()
    es un decorador que se aplica a la función de envoltura de un decorador.
"""


def itemNotFound(func):
    @wraps(func)
    async def wrapper(**kwrags):
        try:
            return await func(**kwrags)
        except DoesNotExist:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={
                "message": "Item doesn't exist"
            })
    return wrapper
