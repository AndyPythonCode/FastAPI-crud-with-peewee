from fastapi import FastAPI
from database.db import ConfigDatabase
from books.routers import router_book
from config import ALL_MODELS, middlewareAPI

app = FastAPI(
    title='first backend',
    description='This my first time using FastAPI',
    version='0.0.1'
)

# Routers
app.include_router(router_book)

# Middleware
middlewareAPI(app)

# create all my tables
config = ConfigDatabase(ALL_MODELS)


"""
                                **Event**
    Entonces, siempre que se acceda a cualquier punto final de API, 
    creará una conexión y luego la cerrará una vez que se complete la ejecución.
"""


@app.on_event("startup")
async def startup():
    print("\nstarting on: http://127.0.0.1:8000/docs\n")
    if config.db.is_closed():
        config.db.connect()
        config.refresh_tables()


@app.on_event("shutdown")
async def shutdown():
    print("Closing...")
    if not config.db.is_closed():
        config.db.close()
